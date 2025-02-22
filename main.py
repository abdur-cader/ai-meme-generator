from generate_image import generate_custom
from templates import *



def get_template_captions(choice):
    if choice == "1":
        calmText = input("Calm text: ")
        painText = input("pain text: ")

        generate_one(calmText, painText)
        
    elif choice == "2":
        captionText = input("Caption: ")
        leftText = input("Left text: ")
        rightText = input("Right text: ")

        generate_two(captionText, leftText, rightText)




def main():
    firstChoice = input("\n1. Meme Template\n2. Custom image\nChoose an option: ")

    if firstChoice == "1":
        template_choice = input("1. Mr Incredible\n2. Spongebob\nChoose a template: ")

        if template_choice not in ["1", "2"]:
            return 4 # template choice error
        else:
            get_template_captions(template_choice)

    elif firstChoice == "2":
        in_file = input("Type your image name and its format: ")
        generationChoice = input("1. GPT2 (Tuned - EXPERIMENTAL)\n2. Gemini (Tuned)\n3. Custom Caption\nWhich model would you like to use for your caption? ")

        if generationChoice not in ["1", "2", "3"]:
            print("wrong choice")
            return 5 # generation choice error
        
        caption = ""
        if generationChoice == "3":
            caption = input("(main) Enter your caption here: ")
        
        generate_custom(in_file, generationChoice, caption)

if __name__ == "__main__":
    main()