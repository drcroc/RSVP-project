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
    frame = 0
    for text in test_list:

        x, y = (200, 150)
        img_black = Image.new(mode="RGBA", size=(x, y), color='black')
        img_grey = Image.new(mode="RGBA", size=(x, y), color='grey')

        draw_black = ImageDraw.Draw(img_black)
        draw_grey = ImageDraw.Draw(img_grey)

        draw_black.text((x//2, y//2), text, font=font, fill='grey', anchor="mm")
        draw_grey.text((x//2, y//2), text, font=font, fill='black', anchor="mm")

        img_black.save(f"Images\{frame}_black.png")
        frame += 1
        img_grey.save(f"Images\{frame}_white.png")
        frame += 1


def images_to_video():
    pass


def image_cleaner():
    pass


def main():
    text_list_to_images()


if __name__ == '__main__':
    main()
