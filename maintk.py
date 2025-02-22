import customtkinter as ctk
from generate_image import generate_custom
from templates import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class MemeApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Meme Generator")
        self.geometry("500x400")
        self.configure(bg="#2E2E2E")
        self.main_menu()

    def main_menu(self):
        self.clear_widgets()
        
        self.option_label = ctk.CTkLabel(self, text="Choose an option:", font=("Arial", 16))
        self.option_label.pack(pady=10)

        self.meme_button = ctk.CTkButton(self, text="Meme Template", command=self.choose_template)
        self.meme_button.pack(pady=10)

        self.custom_button = ctk.CTkButton(self, text="Custom Image", command=self.custom_image)
        self.custom_button.pack(pady=10)

    def choose_template(self):
        self.clear_widgets()
        
        self.template_label = ctk.CTkLabel(self, text="Choose a template:")
        self.template_label.pack(pady=10)

        self.template_var = ctk.StringVar()
        self.template_dropdown = ctk.CTkOptionMenu(self, variable=self.template_var, values=["Mr Incredible", "Spongebob"])
        self.template_dropdown.pack(pady=10)

        self.confirm_button = ctk.CTkButton(self, text="Next", command=self.get_template_captions)
        self.confirm_button.pack(pady=10)

        self.back_button = ctk.CTkButton(self, text="Back", command=self.main_menu)
        self.back_button.pack(pady=10)

    def get_template_captions(self):
        template_choice = self.template_var.get()
        self.clear_widgets()
        
        if template_choice == "Mr Incredible":
            self.calm_label = ctk.CTkLabel(self, text="Calm text:")
            self.calm_label.pack(pady=5)
            self.calm_entry = ctk.CTkEntry(self)
            self.calm_entry.pack(pady=5)

            self.pain_label = ctk.CTkLabel(self, text="Pain text:")
            self.pain_label.pack(pady=5)
            self.pain_entry = ctk.CTkEntry(self)
            self.pain_entry.pack(pady=5)

            self.generate_button = ctk.CTkButton(self, text="Generate", command=lambda: generate_one(self.calm_entry.get(), self.pain_entry.get()))
            self.generate_button.pack(pady=10)
        else:
            self.caption_label = ctk.CTkLabel(self, text="Caption:")
            self.caption_label.pack(pady=5)
            self.caption_entry = ctk.CTkEntry(self)
            self.caption_entry.pack(pady=5)

            self.left_label = ctk.CTkLabel(self, text="Left text:")
            self.left_label.pack(pady=5)
            self.left_entry = ctk.CTkEntry(self)
            self.left_entry.pack(pady=5)

            self.right_label = ctk.CTkLabel(self, text="Right text:")
            self.right_label.pack(pady=5)
            self.right_entry = ctk.CTkEntry(self)
            self.right_entry.pack(pady=5)

            self.generate_button = ctk.CTkButton(self, text="Generate", command=lambda: generate_two(self.caption_entry.get(), self.left_entry.get(), self.right_entry.get()))
            self.generate_button.pack(pady=10)

        self.back_button = ctk.CTkButton(self, text="Back", command=self.choose_template)
        self.back_button.pack(pady=10)

    def custom_image(self):
        self.clear_widgets()

        self.file_label = ctk.CTkLabel(self, text="Enter image full path:")    
        self.file_label.pack(pady=5)
        self.file_entry = ctk.CTkEntry(self)
        self.file_entry.pack(pady=5)

        self.model_label = ctk.CTkLabel(self, text="Choose a model:")
        self.model_label.pack(pady=5)

        self.model_var = ctk.StringVar()
        self.model_dropdown = ctk.CTkOptionMenu(self, variable=self.model_var, values=["GPT2 (Tuned - EXPERIMENTAL)", "Gemini (Tuned)", "Custom Caption"])
        self.model_dropdown.pack(pady=5)

        self.caption_entry = ctk.CTkEntry(self, placeholder_text="Enter caption (if custom)")
        self.caption_entry.pack(pady=5)

        self.generate_button = ctk.CTkButton(self, text="Generate", command=self.generate_custom_image)
        self.generate_button.pack(pady=10)

        self.back_button = ctk.CTkButton(self, text="Back", command=self.main_menu)
        self.back_button.pack(pady=10)

    def generate_custom_image(self):
        in_file = self.file_entry.get()
        generation_choice = self.model_dropdown.get()
        caption = self.caption_entry.get() if generation_choice == "Custom Caption" else ""
        generate_custom(in_file, generation_choice, caption)

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = MemeApp()
    app.mainloop()
