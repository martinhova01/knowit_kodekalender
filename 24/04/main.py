from PIL import Image
import numpy as np

Image.fromarray((np.array(Image.open("santa.png")) & 1) * 255).save("solution.png")