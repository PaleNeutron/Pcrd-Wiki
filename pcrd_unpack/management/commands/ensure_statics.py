from django.core.management.base import BaseCommand, CommandError
import os
import shutil
import distutils
from PIL import Image
import logging
import re
logger = logging.getLogger('django')

class Command(BaseCommand):
    target_static_dir = "pcrd_unpack/static/pcrd_unpack"
    asset_folder = "../unpacked_asset"

    def handle(self, *args, **options):
        self.get_img([
            "Texture2D/assets/_elementsresources/resources/icon/equipment/",
            "Texture2D/assets/_elementsresources/resources/icon/item/",
            "Texture2D/assets/_elementsresources/resources/icon/skill/",
            "Texture2D/assets/_elementsresources/resources/icon/unitplate/",
            "Texture2D/assets/_elementsresources/resources/unit/icon/",
        ])
        self.get_img([r"Texture2D\assets\_elementsresources\resources\unit\profile/"], force43=True)
        self.get_img([r"Texture2D\assets\_elementsresources\resources\unit\actualprofile/"], force43=True)

    def get_img(self, img_dirs, force43=False, fill_color="#fff", force=False):
        for d_rel in img_dirs:
            d = os.path.join(self.asset_folder, d_rel)
            new_dir = os.path.join(self.target_static_dir, d_rel)
            os.makedirs(os.path.join(new_dir, ""), exist_ok=True)
            # distutils.dir_util.copy_tree(d, new_dir)
            for f in os.listdir(d):
                outfile = os.path.join(new_dir, f.replace("png", "jpg"))
                if os.path.exists(outfile) and not force:
                    continue
                im = Image.open(os.path.join(d,f))
                im.convert("RGB")

                if im.mode in ('RGBA', 'LA'):
                    background = Image.new(im.mode[:-1], im.size, fill_color)
                    background.paste(im, im.split()[-1])
                    im = background

                if force43:
                    x, y = im.size
                    y = x // 4 * 3
                    im = im.resize((x, y), Image.ANTIALIAS)
                logger.debug("saved {}".format(outfile))
                im.save(outfile, "JPEG", quality=85)








