#!/usr/bin/env python3

import os
from PIL import Image

src_path = "./images"
dest_path = "/opt/icons"
size = 128, 128


def open_image(path: str):
    try:
        image = Image.open(path)
        return image
    except:
        return None


def save_image_as_jpeg(image: Image, path: str):
    image.convert("RGB").save(path, "JPEG")
    image.close()


def rotate_image(image: Image):
    return image.rotate(90)


def resize_image(image: Image):
    image.thumbnail(size)


def main():
    if not os.path.exists(src_path):
        print(f"{src_path} does not exist")
        return

    for file in os.listdir(src_path):
        src_file = os.path.join(src_path, file)
        dest_file = os.path.join(dest_path, file)

        if not os.path.isfile(src_file):
            continue

        image = open_image(src_file)
        if image is None:
            print(f"failed to open file {file}")
            continue

        image = rotate_image(image)
        resize_image(image)
        save_image_as_jpeg(image, dest_file)


main()
