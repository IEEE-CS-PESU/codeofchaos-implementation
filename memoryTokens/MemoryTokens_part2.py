import cv2
from cv2 import GaussianBlur
import numpy as np
import math
from pylab import array, plot, show, axis, arange, figure, uint8
from scipy.interpolate import interp1d, UnivariateSpline
  
image = cv2.imread('')
 
rows, cols = image.shape[:2]

windowName = 'image'
 
 
# def AA (image):
#     img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)      #BGR TO RGB
#     return img


# def BB (image):
#     img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)      #GREYSCALE
#     return img


# def CC(image):
#     img_output = np.zeros(image.shape, dtype=image.dtype) 
#     for i in range(rows): 
#         for j in range(cols): 
#             offset_x = int(25.0 * math.sin(2 * 3.14 * i / 180)) 
#             offset_y = 0 
#             if j+offset_x < rows: 
#                 img_output[i,j] = image[i,(j+offset_x)%cols] 
#             else: 
#                 img_output[i,j] = 0 
#     return img_output


# def DD(image):
#     kernel = np.array([[0.272, 0.534, 0.131],
#                        [0.349, 0.686, 0.168],
#                        [0.393, 0.769, 0.189]])
#     return cv2.filter2D(image, -1, kernel)


# def EE(image):
#     return cv2.GaussianBlur(image, (35, 35), 0)


# def FF(image):
#     kernel = np.array([[0,-1,-1],
#                             [1,0,-1],

#                             [1,1,0]])
#     return cv2.filter2D(image, -1, kernel)


# def GG(image):
#     kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
#     return cv2.filter2D(image, -1, kernel)


# def HH(image, level):
#     return cv2.convertScaleAbs(image, beta=level)


# def II(image):
#     num_rows, num_cols = image.shape[:2]
#     translation_matrix = np.float32([ [1,0,70], [0,1,110] ])
#     return cv2.warpAffine(image, translation_matrix, (num_cols, num_rows), cv2.INTER_LINEAR)


# def JJ (image):
#     num_rows, num_cols = image.shape[:2]
#     return cv2.warpAffine(image, cv2.getRotationMatrix2D((num_cols/2, num_rows/2), 30, 0.6), (num_cols, num_rows))

# def KK (image):
#     num_rows, num_cols = image.shape[:2]
#     src_points = np.float32([[0,0], [num_cols-1,0], [0,num_rows-1]])
#     dst_points = np.float32([[0,0], [int(0.6*(num_cols-1)),0], [int(0.4*(num_cols-1)),num_rows-1]])
#     matrix = cv2.getAffineTransform(src_points, dst_points)
#     return cv2.warpAffine(image, matrix, (num_cols,num_rows))



# def LL (image):
#     num_rows, num_cols = image.shape[:2]
#     src_points = np.float32([[0,0], [num_cols-1,0], [0,num_rows-1], [num_cols-1,num_rows-1]])
#     dst_points = np.float32([[0,0], [num_cols-1,0], [int(0.33*num_cols),num_rows-1], [int(0.66*num_cols),num_rows-1]])
#     projective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
#     return cv2.warpPerspective(image, projective_matrix, (num_cols,num_rows))


# def spreadLookupTable(x, y):
#   spline = UnivariateSpline(x, y)
#   return spline(range(256))

# def MM(image):
#     increaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 80, 160, 256])
#     decreaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 50, 100, 256])
#     red_channel, green_channel, blue_channel = cv2.split(image)
#     red_channel = cv2.LUT(red_channel, increaseLookupTable).astype(np.uint8)
#     blue_channel = cv2.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)
#     return cv2.merge((red_channel, green_channel, blue_channel))

# def NN(image):
#     increaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 80, 160, 256])
#     decreaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 50, 100, 256])
#     red_channel, green_channel, blue_channel = cv2.split(image)
#     red_channel = cv2.LUT(red_channel, decreaseLookupTable).astype(np.uint8)
#     blue_channel = cv2.LUT(blue_channel, increaseLookupTable).astype(np.uint8)
#     return cv2.merge((red_channel, green_channel, blue_channel))


cv2.waitKey(0)
cv2.destroyAllWindows()