from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Function for converting text from terminal to list of words, commas and dots go to the previous word.
# Function for converting text from a file to a list of words, commas and dots go to the previous word.
# Function for creating images with the words from the list.
# Function for creating video from the images.
# Function for deleting the used images.

test_list = ["Here","is","a","new","image","example","using"]


def terminal_text_to_list():
    pass


def text_file_to_list():
    pass


def text_list_to_images():
    font = ImageFont.truetype("arial.ttf", 24)

    for text in test_list:
        x, y = (200, 150)
        img_black = Image.new(mode="RGBA", size=(x, y), color='black')
        img_white = Image.new(mode="RGBA", size=(x, y), color='white')
        draw_black = ImageDraw.Draw(img_black)
        draw_white = ImageDraw.Draw(img_white)
        # w, h = draw_white.textsize(text)
        draw_black.text((x//2, y//2), text, font=font, fill='white', anchor="mm")
        draw_white.text((x//2, y//2), text, font=font, fill='black', anchor="mm")
        # img.show()
        img_black.save(f"Images\{text}_black.png")
        img_white.save(f"Images\{text}_white.png")


def images_to_video():
    pass


def image_cleaner():
    pass


def main():
    text_list_to_images()


if __name__ == '__main__':
    main()
