from django.core.management.base import BaseCommand, CommandError
import os
import shutil
import distutils
from PIL import Image
import logging
import re

class Command(BaseCommand):
    target_static_dir = "pcrd_unpack/static/pcrd_unpack"

    def handle(self, *args, **options):
        self.get_img([
            "unpacked_asset/Texture2D/assets/_elementsresources/resources/icon/equipment/",
            "unpacked_asset/Texture2D/assets/_elementsresources/resources/icon/item/",
            "unpacked_asset/Texture2D/assets/_elementsresources/resources/icon/unitplate/",
            "unpacked_asset/Texture2D/assets/_elementsresources/resources/unit/icon/",
        ])
        self.get_img([r"unpacked_asset\Texture2D\assets\_elementsresources\resources\unit\profile/"], force43=True)
        self.get_img([r"unpacked_asset\Texture2D\assets\_elementsresources\resources\unit\actualprofile/"], force43=True)

    def get_img(self, img_dirs, force43=False, fill_color="#fff"):
        for d in img_dirs:
            new_dir = os.path.join(self.target_static_dir, re.split(r"/|\\", d, 1)[1])
            os.makedirs(os.path.join(new_dir, ""), exist_ok=True)
            # distutils.dir_util.copy_tree(d, new_dir)
            for f in os.listdir(d):
                "ad".split()
                im = Image.open(os.path.join(d,f))
                im.convert("RGB")
                outfile = os.path.join(new_dir, f.replace("png", "jpg"))

                if im.mode in ('RGBA', 'LA'):
                    background = Image.new(im.mode[:-1], im.size, fill_color)
                    background.paste(im, im.split()[-1])
                    im = background

                if force43:
                    x, y = im.size
                    y = x // 4 * 3
                    im = im.resize((x, y), Image.ANTIALIAS)
                logging.debug("saved {}".format(outfile))
                im.save(outfile, "JPEG", quality=85)








