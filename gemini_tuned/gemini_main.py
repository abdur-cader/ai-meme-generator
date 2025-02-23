import google.generativeai as genai
from google.generativeai.types import GenerationConfig #configure model output settings
import time, os

# Use your API key here
genai.configure(api_key="ENTER_YOUR_KEY_HERE")
models = list(genai.list_tuned_models())
config = GenerationConfig(max_output_tokens = 10)

model = genai.GenerativeModel(model_name="tunedModels/PASTE-MODEL-NAME-HERE")

def gemini_generate(intext):
    result = model.generate_content(f"generate meme caption: {intext}", generation_config=config)
    print(result.text)
    return result.text





# View tuned models
for model in models:
    print(model.name)
