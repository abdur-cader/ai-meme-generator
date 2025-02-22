import google.generativeai as genai
from google.generativeai.types import GenerationConfig #configure model output settings
import time, os

# Use your API key here
genai.configure(api_key="AIzaSyAZQOELgFxmhqaonFel5j4BWbvsCgh2Kwo")
models = list(genai.list_tuned_models())
config = GenerationConfig(max_output_tokens = 10)

model = genai.GenerativeModel(model_name="tunedModels/memecaptionerv1-am02zm7iaov6")

def gemini_generate(intext):
    result = model.generate_content(f"generate meme caption: {intext}", generation_config=config)
    print(result.text)
    return result.text

for model in models:
    print(model.name)

# gemini_generate("hey gemini, im not feeling well today, be serious, how can i be better")