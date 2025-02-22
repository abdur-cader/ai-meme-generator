import google.generativeai as genai
from gemini_training_data import training_data
import time, os

genai.configure(api_key="AIzaSyAZQOELgFxmhqaonFel5j4BWbvsCgh2Kwo")

base_model = "models/gemini-1.5-flash-001-tuning"

operation = genai.create_tuned_model(
    display_name="meme-captioner-v1",   # choose a display name
    source_model=base_model,
    epoch_count=10,
    batch_size=4,
    learning_rate=0.001,
    training_data=training_data,        # gemini_training_data.py
    temperature=0.3,
    id = "gemini-tuned-model",    # set your own id
)

for status in operation.wait_bar():
    time.sleep(10)

result = operation.result()
print(result)

model = genai.GenerativeModel(model_name=result.name)
# result = model.generate_content("A person riding a bike")   # test run
print(result.text)