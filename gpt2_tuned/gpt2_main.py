""" 
        This program takes in description generated from imageToText, and is taken as 
        input to generate a meme-y output
"""

from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "gpt2_tuned/trained_model_v2"
tokenizer_name = "gpt2"

# Load model and tokenizer
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(tokenizer_name)


def gpt2_generate(input_text):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Generate text with desired parameters
    generated_ids = model.generate(
        input_ids=input_ids,
        max_length=15,           # Maximum length of the generated sequence
        do_sample=True,          # Enable sampling
        temperature=0.7,         # Control randomness
        top_k=50,                # Top-k filtering
        top_p=0.95,              # Nucleus sampling
        num_return_sequences=3,  # Number of generated sequences
        repetition_penalty=1.2,  # Penalty for repetition
        length_penalty=1.0,      # Length penalty
        no_repeat_ngram_size=2,  # Prevent repeating n-grams
    )

    # Decode the generated text
    generated_text = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    return generated_text


# print("Generated text:", generated_text)
