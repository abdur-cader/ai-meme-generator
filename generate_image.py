import os # to check for path
from PIL import Image, ImageDraw, ImageFont
import imageToText
from gpt2_tuned.gpt2_main import gpt2_generate
from gemini_tuned.gemini_main import gemini_generate


def generate_custom(in_file, model_choice, caption=""):
    if os.path.exists(in_file):
        img = Image.open(in_file)
    else:
        print("Sorry! we can't seem to find the file. Please check if you've spelt it correctly/have the right extension, or if it's in the right folder.")
        return

    width, height = img.size
    img_area = width * height
    increment = round(height * 0.4)

    new_image = Image.new("RGB", (width, height + increment), "white")
    new_image.paste(img, (0, increment))

    draw = ImageDraw.Draw(new_image)
    font_path = "impact.ttf"
    base_font_size = img_area * 0.0002
    textresults = imageToText.get_description(in_file) # generate image desc


    #User menu / model choice
    if model_choice == "1":
        caption = gpt2_generate(textresults[0])
    elif model_choice == "2":
        caption = gemini_generate(textresults[0])
    elif model_choice == "3":
        pass
    else:
        return 70 # unknown error
    
    font_size = int(base_font_size)
    font = ImageFont.truetype(font_path, font_size)
    
    # automatically adjust size
    while True:
        bounding = draw.textbbox((0, 0), caption, font=font)
        twidth = bounding[2] - bounding[0]
        
        if twidth <= width * 0.9:  # padding
            break
        font_size -= 2 
        font = ImageFont.truetype(font_path, font_size)

    theight = bounding[3] - bounding[1]
    x = (width - twidth) // 2
    y = (increment - theight) // 2

    draw.text((x, y), caption, fill="black", font=font)
    new_image.show()
    print(textresults)


# generate_image("images/cat.png") # test code if you want to run this file directly