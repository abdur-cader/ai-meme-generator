from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer, GPT2Tokenizer
import torch
from PIL import Image
import gpt2_tuned.gpt2_main

model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning", ignore_mismatched_sizes=True)
feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

max_tokens = 16
num_beams = 4

# store values into kwargs to pass it to generation
gen_kwargs = {"max_length": max_tokens, "num_beams": num_beams} 

# use cuda if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def get_description(in_path):
    img = Image.open(in_path)
    if img.mode != "RGB": # check if image is RGB (supported image mode)
        img = img.convert(mode="RGB") # convert to support mode 

    # convert image to tensors
    pixel_values = feature_extractor(images=[img], return_tensors="pt").pixel_values.to(device)

    # generate tokens
    output_ids = model.generate(pixel_values, **gen_kwargs)

    # decode tokens
    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    
    # clean up text
    preds = [pred.strip() for pred in preds]

    return preds

