# coding: utf-8
from PIL import Image, ImageFont, ImageDraw
import sys
import math

# 画像に文字を入れる関数
def img_add_msg(img, message, fontcolor = "#FF5555", fontsize = 30):
    font_path = './Noto.otf'
    fontcustom = ImageFont.truetype(font_path, fontsize, 0, encoding='utf-8')
    img = Image.open(img).convert("RGBA")
    bg = Image.new("RGBA", (320,320), (0,0,0,0))
    draw = ImageDraw.Draw(bg)
    w , h = draw.textsize(message, font=fontcustom)
    while(w > 320):
        font_size -= 1
        fontcustom = ImageFont.truetype(font_path, font_size, 0, encoding='utf-8')
        w , h = draw.textsize(message, font=fontcustom)
    x = (320 - w)/2
    y = 250
    centery = 0
    centerx = 0
    bg.paste(img,(centerx,centery),img)
    draw.text((x, y), message, font=fontcustom, fill=fontcolor)
    # textch = np.array(textch) # PIL型の画像をcv2(NumPy)型に変換
    return bg # 文字入りの画像をリターン
