#实现单个图片灰度化和二值化

from PIL import Image

# load a color image
im = Image.open('E:\PycharmFiles\pupian\\b1f42a79ed2892bdb5f2087a2c618a18.jpg')  # 当前目录创建picture文件夹，即图片所在文件夹

# convert to grey level image
Lim = im.convert('L')
Lim.save('E:\PycharmFiles\pupian\\b1.jpg')

#二值化
# setup a converting table with constant threshold
# threshold = 185
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
#
# # convert to binary image by the table
# bim = Lim.point(table, '1')
#
# bim.save('picf3.jpg')