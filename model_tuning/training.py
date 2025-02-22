import pandas as pd
from datasets import Dataset, DatasetDict
from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments

# load the csv file into a pandas dataframe
df = pd.read_csv("model_tuning/datasets/generated_descriptions.csv")

# Convert the dataframe into a Dataset object for Hugging Face
dataset = Dataset.from_pandas(df)

print(dataset.column_names)

# Split into train and test datasets
train_dataset = dataset.train_test_split(test_size=0.1)["train"]
val_dataset = dataset.train_test_split(test_size=0.1)["test"]

# Load pre-trained GPT-2 model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

tokenizer.pad_token = tokenizer.eos_token

# Tokenize the datasets
def tokenize_function(examples):
    inputs = tokenizer(examples["input"], padding="max_length", truncation=True, max_length=50)
    inputs["labels"] = tokenizer(examples["output"], padding="max_length", truncation=True, max_length=50)["input_ids"]
    return inputs

train_dataset = train_dataset.map(tokenize_function, batched=True)
val_dataset = val_dataset.map(tokenize_function, batched=True)

# Define training arguments
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=5,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    evaluation_strategy="epoch",
    save_total_limit=2,
    logging_dir="./logs",
    logging_steps=10,
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
)

# Start training
trainer.train()

# Step 7: Save the trained model
model.save_pretrained("trained_model_v2")
tokenizer.save_pretrained("trained_tokenizer_v2")
