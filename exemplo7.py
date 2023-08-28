from PIL import Image
import numpy as np
im = Image.open("quadro.jpg")
a = np.asarray(im)
print(a)

