# AI-Meme-Generator 💥

## ‼️Before you begin...
how's your day going 🦔

## 1️⃣ Overview
This program automatically generates AI-Based captions for any image you choose and turns them into memes. This also includes a *custom* captioning feature if you'd rather input your own caption.
Captions are generated (with PyTorch) using Hugging Face's [nlpconnect/vit-gpt2-image-captioning](https://huggingface.co/nlpconnect/vit-gpt2-image-captioning) and a tuned (but experimental) version of [gpt2](https://huggingface.co/gpt2), and the Google Gemini 1.5-Flash-Tuned API.
Note, if you want to use Gemini's model, you'll have to tune it yourself - don't worry, all the nessecary code and datasets are prepped in this repo (further instructions can be found below.)

## 2️⃣ Features
- AI-Generated Captions: Generate captions based on the image using AI.
- Custom captions: You may also enter your own preferred caption instead of using an AI-generated one; total control for ya 🤙
- Templates, for fun: You have the option to add your own captions on two different premade meme templates

## 3️⃣ Before you actually begin
### **A** - Installing Packages:
- in your terminal, run `pip install -r requirements.txt` to install the required dependencies.

### **B** - Getting Started:
- If you prefer to use Gemini's model, you'll need to train your own model. To do so, you need your own API key. You can get it [here.](https://aistudio.google.com/app/apikey)
- After you sign-in, Select "Get API Key". From there, create an API key and copy its key.
- In `gemini_tuned\gemini_main.py`, replace `ENTER_YOUR_KEY_HERE` (line 6) with the API key you just generated - save changes. You can also set up an environment variable (further docs for Gemini are found [here](https://ai.google.dev/gemini-api/docs)).

### **C** - Tuning Your Gemini Model
- Head to `gemini_training.py` and insert your API key there. Run the code to tune your model; this might take some time- You'll just have to do this once.
- After it's trained, go back to `gemini_main.py`, comment lines 8-15 (highlight lines 8-15, then `ctrl`+`/`), then run lines 22-24.
- When you're done, you can uncomment line 8 to 15 again, and save the file. That's it!

## 🏁 Start-up
To start using the program, run `maintk.py`. Just note- if you're asked to enter the image path, you'll need to copy the full path to the image, otherwise it may not work. Or, you can save your image in the `\images` folder and enter the relative path
