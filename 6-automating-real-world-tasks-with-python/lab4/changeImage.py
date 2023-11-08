#!/usr/bin/env python3

import os
from PIL import Image

home_path = os.path.expanduser("~")
image_path = os.path.join(home_path, "supplier-data/images")
image_size = 600, 400


def open_image(path: str):
    try:
        image = Image.open(path)
        return image
    except:
        return None


def save_image_as_jpeg(image: Image, path: str):
    image.save(path, "JPEG")
    image.close()


def resize_image(image: Image):
    return image.resize(image_size)


def convert_image(image: Image):
    return image.convert("RGB")


def main():
    for file in os.scandir(image_path):
        if file.is_dir():
            continue
        src_path = file.path

        image = open_image(src_path)
        if image is None:
            continue

        image = convert_image(image)
        image = resize_image(image)
        dest_path = src_path.replace("tiff", "jpeg")
        save_image_as_jpeg(image, dest_path)


main()
