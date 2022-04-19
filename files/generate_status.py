import sys
from PIL import Image, ImageFilter, ImageDraw, ImageFont


def blur_image(image, radius=30):
    return image.filter(
        ImageFilter.GaussianBlur(radius=radius)
    )


def write_text(image, text, font, size=150, color=(0, 143, 33)):
    text = text.upper()
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font, size)
    img_w, img_h = image.size
    font_w, font_h = font.getsize(text)
    draw.text(
        ((img_w - font_w) // 2, (img_h - font_h) // 2),
        text, color, font=font
    )


def generate(img_path, text, font):
    with Image.open(img_path) as image:
        blurred_image = blur_image(image)
        write_text(blurred_image, text, font)
        blurred_image.save("/tmp/status.jpg")


def main():
    font_path = sys.argv[1]
    wallpaper_path = "roles/personalize/files/wallpapers/" + sys.argv[2]
    status = " ".join(sys.argv[3:])
    generate(img_path=wallpaper_path, text=status, font=font_path)


main()
