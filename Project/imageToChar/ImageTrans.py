# -*- coding: utf-8 -*-
from PIL import Image

IMG='dage.jpg'
IMG2='paonan.jpg'
IMG3='IMG3.jpg'
Height = 60
WIDTH = 100
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
# 将256灰度映射到70个字符上
def get_char(r,b,g,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0+1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    im = Image.open(IMG)
    # im = im.resize((80,80)Image.NEAREST)
    im = im.resize((WIDTH, Height), Image.NEAREST)

    txt = ''

    for i in range(Height):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    print txt
    with open('output.txt','w') as f:
        f.write(txt)