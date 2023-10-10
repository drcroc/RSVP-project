from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import cv2
import glob

# F̶u̶n̶c̶t̶i̶o̶n̶ ̶f̶o̶r̶ ̶c̶o̶n̶v̶e̶r̶t̶i̶n̶g̶ ̶t̶e̶x̶t̶ ̶f̶r̶o̶m̶ ̶t̶e̶r̶m̶i̶n̶a̶l̶ ̶t̶o̶ ̶l̶i̶s̶t̶ ̶o̶f̶ ̶w̶o̶r̶d̶s̶,̶ ̶c̶o̶m̶m̶a̶s̶ ̶a̶n̶d̶ ̶d̶o̶t̶s̶ ̶g̶o̶ ̶t̶o̶ ̶t̶h̶e̶ ̶p̶r̶e̶v̶i̶o̶u̶s̶ ̶w̶o̶r̶d̶.̶  Completed
# Function for converting text from a file to a list of words, commas and dots go to the previous word.
# F̶u̶n̶c̶t̶i̶o̶n̶ ̶f̶o̶r̶ ̶c̶r̶e̶a̶t̶i̶n̶g̶ ̶i̶m̶a̶g̶e̶s̶ ̶w̶i̶t̶h̶ ̶t̶h̶e̶ ̶w̶o̶r̶d̶s̶ ̶f̶r̶o̶m̶ ̶t̶h̶e̶ ̶l̶i̶s̶t̶.̶ Completed
# F̶u̶n̶c̶t̶i̶o̶n̶ ̶f̶o̶r̶ ̶c̶r̶e̶a̶t̶i̶n̶g̶ ̶v̶i̶d̶e̶o̶ ̶f̶r̶o̶m̶ ̶t̶h̶e̶ ̶i̶m̶a̶g̶e̶s̶.̶ Completed
# Function for deleting the used images.
# Need to add options for custom FPS, Resolution, Colors


# test_list = ["Here", "is", "a", "new", "image", "example", "using"]
# textt_list = []


def terminal_text_to_list():
    print("Enter your text: ")
    text_list = input().split(' ')
    return text_list


def text_file_to_list():
    pass


def text_list_to_images(test_list):
    font = ImageFont.truetype("arial.ttf", 192)
    frame = 0
    for text in test_list:
        # x, y = (200, 150)
        x, y = (1920, 1080)
        img_black = Image.new(mode="RGBA", size=(x, y), color='black')
        img_grey = Image.new(mode="RGBA", size=(x, y), color='grey')

        draw_black = ImageDraw.Draw(img_black)
        draw_grey = ImageDraw.Draw(img_grey)

        draw_black.text((x // 2, y // 2), text, font=font, fill='grey', anchor="mm")
        draw_grey.text((x // 2, y // 2), text, font=font, fill='black', anchor="mm")

        img_black.save(f"Images\{frame}_black.png")
        frame += 1
        img_grey.save(f"Images\{frame}_white.png")
        frame += 1


def images_to_video():
    img_array = []
    width, height = 0, 0
    for filename in glob.glob('Images\*.png'):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        img_array.append(img)

    size = (width, height)
    fourcc = cv2.VideoWriter.fourcc(*'mp4v')
    out = cv2.VideoWriter('video.mp4', fourcc=fourcc, fps=12, frameSize=size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()


def image_cleaner():
    pass


def main():
    textt_list = terminal_text_to_list()
    text_list_to_images(textt_list)
    images_to_video()


if __name__ == '__main__':
    main()
