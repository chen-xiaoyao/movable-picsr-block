from PIL import ImageGrab
import os


def get_pic():
    img = ImageGrab.grabclipboard()
    img.save('picture.png')


def del_pic():
    os.remove('picture.png')  # 及时清理文件


if __name__ == '__main__':
    get_pic()
