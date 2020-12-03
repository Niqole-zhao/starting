from PIL import Image
import os

input_dir = 'E:\PycharmFiles\huidu/'
out_dir = 'E:\PycharmFiles\pythonProject\picture/'
a = os.listdir(input_dir)

for i in a:
    print(i)
    I = Image.open(input_dir + i)
    L = I.convert('L')
    L.save(out_dir + i)