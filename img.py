import sys
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img_file = sys.argv[1]

i = Image.open(img_file)

iar = np.asarray(i)


plt.imshow(iar)
print(iar)
plt.show()	
