from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import shutil
import os
import argparse
import cv2
import glob

# F̶u̶n̶c̶t̶i̶o̶n̶ ̶f̶o̶r̶ ̶c̶o̶n̶v̶e̶r̶t̶i̶n̶g̶ ̶t̶e̶x̶t̶ ̶f̶r̶o̶m̶ ̶t̶e̶r̶m̶i̶n̶a̶l̶ ̶t̶o̶ ̶l̶i̶s̶t̶ ̶o̶f̶ ̶w̶o̶r̶d̶s̶,̶ ̶c̶o̶m̶m̶a̶s̶ ̶a̶n̶d̶ ̶d̶o̶t̶s̶ ̶g̶o̶ ̶t̶o̶ ̶t̶h̶e̶ ̶p̶r̶e̶v̶i̶o̶u̶s̶ ̶w̶o̶r̶d̶.̶  Completed
# F̶u̶n̶c̶t̶i̶o̶n̶ ̶f̶o̶r̶ ̶c̶o̶n̶v̶e̶r̶t̶i̶n̶g̶ ̶t̶e̶x̶t̶ ̶f̶r̶o̶m̶ ̶a̶ ̶f̶i̶l̶e̶ ̶t̶o̶ ̶a̶ ̶l̶i̶s̶t̶ ̶o̶f̶ ̶w̶o̶r̶d̶s̶,̶ ̶c̶o̶m̶m̶a̶s̶ ̶a̶n̶d̶ ̶d̶o̶t̶s̶ ̶g̶o̶ ̶t̶o̶ ̶t̶h̶e̶ ̶p̶r̶e̶v̶i̶o̶u̶s̶ ̶w̶o̶r̶d̶.  Completed
# F̶u̶n̶c̶t̶i̶o̶n̶ ̶f̶o̶r̶ ̶c̶r̶e̶a̶t̶i̶n̶g̶ ̶i̶m̶a̶g̶e̶s̶ ̶w̶i̶t̶h̶ ̶t̶h̶e̶ ̶w̶o̶r̶d̶s̶ ̶f̶r̶o̶m̶ ̶t̶h̶e̶ ̶l̶i̶s̶t̶.̶  Completed
# F̶u̶n̶c̶t̶i̶o̶n̶ ̶f̶o̶r̶ ̶c̶r̶e̶a̶t̶i̶n̶g̶ ̶v̶i̶d̶e̶o̶ ̶f̶r̶o̶m̶ ̶t̶h̶e̶ ̶i̶m̶a̶g̶e̶s̶.̶  Completed
# F̶u̶n̶c̶t̶i̶o̶n̶ ̶f̶o̶r̶ ̶d̶e̶l̶e̶t̶i̶n̶g̶ ̶t̶h̶e̶ ̶u̶s̶e̶d̶ ̶i̶m̶a̶g̶e̶s̶.̶  Completed
# N̶e̶e̶d̶ ̶t̶o̶ ̶a̶d̶d̶ ̶o̶p̶t̶i̶o̶n̶s̶ ̶f̶o̶r̶ ̶c̶u̶s̶t̶o̶m̶ ̶F̶P̶S̶,̶ ̶R̶e̶s̶o̶l̶u̶t̶i̶o̶n̶,̶ ̶C̶o̶l̶o̶r̶s̶.  Completed


# test_list = ["Here", "is", "a", "new", "image", "example", "using"]


def arg_check():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-f", "--file", required=False, default='', help="Specify the file you want to read from. If left blank, it will ask you to enter the text (Not recommended for large projects).")
    argParser.add_argument("-fps", "--FramesPerSecond", required=False, type=float,  default=6,  help="Specify how many images per second you want to read. The number is (float) between [1..30]. Default [10]. ")
    argParser.add_argument("-c", "--color", required=False,  default='black-white', help="Specify color scheme. By default is black-white [BG-Text].")
    argParser.add_argument("-i", "--invert", required=False, choices=['off','on'], default='off', help="Creates a reverse frame every second frame. Default [off].")
    argParser.add_argument("-res", "--resolution", required=False, default='1920,1080', help="Image and video resolution. This must be provided as a comma-separated string. Default [1920,1080]")
    argParser.add_argument("-font",required=False, default='arial.ttf', help="The font of the characters. You will have to put the extension of the font as well. Default [arial.ttf]")
    argParser.add_argument("-tz", "--text_size", required=False, type=int, default=192, help="The size of the characters. Default [192]")
    args = vars(argParser.parse_args())
    return args


def terminal_text_to_list():
    print("Enter your text: ")
    # text_list = input().split(' ')
    text_list = input().replace('\n', ' ').split(' ')
    return text_list


def text_file_to_list(opt):
    with open(opt['file'], mode='rt') as f:
        text_list = f.read().replace('\n', ' ').split(' ')
    return text_list


def text_list_to_images(test_list, opt=None):
    backGroundColor, textColor = '', ''
    if opt and opt['color']:
        backGroundColor = opt['color'].split('-')[0]
        textColor = opt['color'].split('-')[1]

    # font = ImageFont.truetype("arial.ttf", 192)
    font = ImageFont.truetype(opt['font'], opt['text_size'])
    frame = 0
    # x, y = (200, 150)
    x, y = map(int, opt['resolution'].split(','))

    if not os.path.exists("Images"):
        os.makedirs("Images")

    for text in test_list:
        img_normal = Image.new(mode="RGBA", size=(x, y), color=f'{backGroundColor}')
        draw_normal = ImageDraw.Draw(img_normal)
        draw_normal.text((x // 2, y // 2), text, font=font, fill=f'{textColor}', anchor="mm")
        # img_normal.save(f"Images\{frame}_normal.png")
        img_normal.save(os.path.join("Images", f"{frame}_normal.png"))
        frame += 1

        if opt and opt.get('invert') == 'on':
            img_inverted = Image.new(mode="RGBA", size=(x, y), color=f'{textColor}')
            draw_inverted = ImageDraw.Draw(img_inverted)
            draw_inverted.text((x // 2, y // 2), text, font=font, fill=f'{backGroundColor}', anchor="mm")
            # img_inverted.save(f"Images\{frame}_inverted.png")
            img_inverted.save(os.path.join("Images", f"{frame}_inverted.png"))
            frame += 1


def images_to_video(opt=None):
    fps = 0.0
    if opt:
        fps = opt['FramesPerSecond']

    img_array = []
    width, height = 0, 0
    image_list = glob.glob('Images\*.png')
    image_list.sort(key=os.path.getmtime)
    for filename in image_list:
        img = cv2.imread(filename)
        height, width, layers = img.shape
        img_array.append(img)

    size = (width, height)
    fourcc = cv2.VideoWriter.fourcc(*'mp4v')
    out = cv2.VideoWriter('video.mp4', fourcc=fourcc, fps=fps, frameSize=size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()


def image_cleaner():
    if os.path.exists("Images"):
        try:
            shutil.rmtree("Images")
        except Exception as e:
            print(f"Error deleting folder: {e}")


def main():
    options = arg_check()
    if options['file'] != '':
        textt_list = text_file_to_list(options)
    else:
        textt_list = terminal_text_to_list()

    text_list_to_images(textt_list, options)
    images_to_video(options)
    image_cleaner()


if __name__ == '__main__':
    main()
