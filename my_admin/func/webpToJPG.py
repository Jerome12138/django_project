from io import BytesIO
from PIL import Image
import requests
from django.conf import settings


def webp_to_jpg(url):  # 图片转换
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    byte_stream = BytesIO(resp.content)
    im = Image.open(byte_stream)
    if im.mode == "RGBA":
        im.load()  # required for png.split()
        background = Image.new("RGB", im.size, (255, 255, 255))
        background.paste(im, mask=im.split()[3])
    save_name = url.split('/')[-1].replace('webp', 'jpg')
    save_path = 'static/app_video/img/carousel/%s' % (save_name)
    im.save("%s/collected_%s" % (settings.BASE_DIR, save_path), 'JPEG')
    im.save("%s/%s" % (settings.BASE_DIR, save_path), 'JPEG')
    return '/'+save_path
