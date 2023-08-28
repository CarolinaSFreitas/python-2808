from PIL import Image
import numpy as np
a = np.zeros((5, 5))
a[0] = [720, 725, 720, 725, 725]
print(a)

im = Image.fromarray(a)
im.show()

