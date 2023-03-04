from PIL import Image, ImageFont, ImageDraw
import csv
import textwrap
import os


CARD_TYPE_TO_CARD_INFO = {
    "gray": ("Обычный", (0, 0, 0)),
    "blue": ("Необычный", (0, 0, 0)),
    "purple": ("Мифический", (0, 0, 0)),
    "red": ("Удачный шанс", (0, 0, 0)),
    "gold": ("Легендарный", (0, 0, 0)),
    "ulred": ("Загадывает именинник", (255, 255, 255)),
}


os.makedirs("results", exist_ok=True)


for line_number, line in enumerate(csv.reader(open("cards.csv", encoding="utf-8-sig"), delimiter=";"), start=1):
    card_type, card_text = line
    font = ImageFont.truetype("font/JetBrainsMono-Bold.ttf", 20)
    image = Image.open(f"frames/{card_type}.png")
    draw = ImageDraw.Draw(image)
    card_title, text_color = CARD_TYPE_TO_CARD_INFO[card_type]
    draw.text((40, 40), f"Тип сложности:\n{card_title}", fill=text_color, font=font)
    draw.text((40, 120), "\n".join(textwrap.wrap(card_text, 42)), fill=text_color, font=font)
    image.save(f"results/{line_number}_{card_type}.png")
