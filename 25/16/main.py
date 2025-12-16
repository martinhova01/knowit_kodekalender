from PIL import Image
import re

data = open("input.txt").read().rstrip()

img = Image.new("RGB", (1024, 1024), 255)
img_pixels = img.load()
for point in data.split(" "):
    nums = re.findall(r"\d+", point)
    x = int(nums[0])
    y = int(nums[1])
    hex = re.findall(r"\(([^()]*)\)", point)[0]
    img_pixels[x, y] = int(hex, 16)

img.show()
