import os # to check for path
from PIL import Image, ImageDraw, ImageFont
import imageToText
from gpt2_tuned.gpt2_main import gpt2_generate
from gemini_tuned.gemini_main import gemini_generate



"""def generate_template(choice):

    # retrieving user's choice
    if choice == "1":
        in_file = "images/templates/spongebob_book.jpg"
    elif choice == "2":
        in_file = "images/templates/mr_incredible.jpg"
    elif choice == "3":
        in_file = "images/templates/isteppedinshit.jpg"
    else:
        print("Choose between 1 or 2.")
        return 2 # wrong template choice

    if os.path.exists(in_file):
        img = Image.open(in_file)
    else:
        print("Sorry! we can't seem to find the file. Please check if you've spelt it correctly/have the right extension, or if it's in the right folder.")
        return
    
    draw = ImageDraw.Draw(img)

    width, height = img.size
    imgArea = (width * height)
    
    # adjust font based on image size
    

    # font paths & fonts
    impact_path = "fonts/impact.ttf"
    arial_path = "fonts/ARIAL.TTF"
    
    # draw
    if choice == "1": # spongebob
        textSize = max(10, min(imgArea / 10000, 40))
        captionSize = max(15, min(imgArea / 5000, 70))
        arial_font = ImageFont.truetype(arial_path, textSize)
        impact_font = ImageFont.truetype(impact_path, captionSize)


        captionText = input("Caption: ")
        leftText = input("Left text: ")
        rightText = input("Right text: ")

        caption_length = draw.textlength(captionText, font=impact_font)
        left_length = draw.textlength(leftText, font= arial_font)
        right_length = draw.textlength(rightText, font= arial_font)

        x_caption, y_caption = ((width // 2)-(caption_length // 2)), 145
        x_left, y_left = 280 - (left_length // 2), 920
        x_right, y_right = 825 - (right_length) // 2, 920
        
        draw.text((x_caption, y_caption), captionText, (255, 255, 255), impact_font)

        # draw left and right text
        draw.text((x_left, y_left), leftText, (255, 255, 255), arial_font)
        draw.text((x_right, y_right), rightText, (255, 255, 255), arial_font)
    
    elif choice == "2":
        textSize = max(200, min(imgArea / 1000, 100))
        arial_font = ImageFont.truetype(arial_path, textSize)

        calmText = input("Calm text: ")
        painText = input("pain text: ")
        
        calm_length = draw.textlength(calmText, font = arial_font)
        pain_length = draw.textlength(painText, font = arial_font)
        
        x_calm, y_calm = (width // 4) - (calm_length // 2), height // 4
        x_pain, y_pain = (width // 4) - (pain_length // 2), height - (height // 4)

        draw.text((x_calm, y_calm), calmText, (0, 0, 0), arial_font)
        draw.text((x_pain, y_pain), painText, (0, 0, 0), arial_font)

    img.show()
    return"""


def generate_two(captionText, leftText, rightText):
    in_file = "images/templates/spongebob_book.jpg"

    if os.path.exists(in_file):
        img = Image.open(in_file)
    else:
        print("Sorry! we can't seem to find the file. Please check if you've spelt it correctly/have the right extension, or if it's in the right folder.")
        return
    
    draw = ImageDraw.Draw(img)

    width, height = img.size
    imgArea = (width * height)

    # font paths & fonts
    impact_path = "fonts/impact.ttf"
    arial_path = "fonts/ARIAL.TTF"
    

    textSize = max(10, min(imgArea / 10000, 40))
    captionSize = max(15, min(imgArea / 5000, 70))
    arial_font = ImageFont.truetype(arial_path, textSize)
    impact_font = ImageFont.truetype(impact_path, captionSize)

    caption_length = draw.textlength(captionText, font=impact_font)
    left_length = draw.textlength(leftText, font= arial_font)
    right_length = draw.textlength(rightText, font= arial_font)

    x_caption, y_caption = ((width // 2)-(caption_length // 2)), 145
    x_left, y_left = 280 - (left_length // 2), 920
    x_right, y_right = 825 - (right_length) // 2, 920
        
    draw.text((x_caption, y_caption), captionText, (255, 255, 255), impact_font)

    # draw left and right text
    draw.text((x_left, y_left), leftText, (255, 255, 255), arial_font)
    draw.text((x_right, y_right), rightText, (255, 255, 255), arial_font)

    img.show()

def generate_one(calmText, painText):
    in_file = "images/templates/mr_incredible.jpg"

    if os.path.exists(in_file):
        img = Image.open(in_file)
    else:
        print("Sorry! we can't seem to find the file. Please check if you've spelt it correctly/have the right extension, or if it's in the right folder.")
        return
    
    draw = ImageDraw.Draw(img)

    width, height = img.size
    imgArea = (width * height)

    # font paths & fonts
    arial_path = "fonts/ARIAL.TTF"

    textSize = max(200, min(imgArea / 1000, 100))
    arial_font = ImageFont.truetype(arial_path, textSize)

            
    calm_length = draw.textlength(calmText, font = arial_font)
    pain_length = draw.textlength(painText, font = arial_font)
            
    x_calm, y_calm = (width // 4) - (calm_length // 2), height // 4
    x_pain, y_pain = (width // 4) - (pain_length // 2), height - (height // 4)

    draw.text((x_calm, y_calm), calmText, (0, 0, 0), arial_font)
    draw.text((x_pain, y_pain), painText, (0, 0, 0), arial_font)

    img.show()
    return


