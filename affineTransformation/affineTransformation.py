# Description: Algorithm will prompt user to pick 3 points on 2 of the same images
#              to calculate the affine transformation matrix. From the generated matrix,
#              the similarity image is carried out by calculating the rotation, translation and scale
#              of the image.

import cv2
import numpy

def click(event, x, y, flags, param):
    global i, pos
    if event == cv2.EVENT_LBUTTONDOWN: # left button pressed
        pos[i, 0] = x # save position-x
        pos[i, 1] = y # save position-y
        i = i + 1
i = 0
pos = numpy.zeros((3,2), dtype=int)

if __name__ == '__main__':
    img = cv2.imread('hutao.png')
    while(1):
        cv2.imshow('Image_1', img) # show the image
        cv2.setMouseCallback('Image_1', click) # read status for mouse
        cv2.waitKey(1)
        if i == 3: # point counter
            pts1_I1 = pos
            break
    cv2.destroyAllWindows()
    
    i = 0
    pos = numpy.zeros((3,2), dtype=int)
    while(1):
        cv2.imshow('Image_2', img) # show the image
        cv2.setMouseCallback('Image_2', click) # read status for mouse
        cv2.waitKey(1)
        if i == 3: # point counter
            pts2_I1 = pos
            break
    cv2.destroyAllWindows()

    pts1 = numpy.float32(pts1_I1) # first dot matrix
    pts2 = numpy.float32(pts2_I1) # second dot matrix
    M_affine = cv2.getAffineTransform(pts1, pts2) # matrix H for affine transformation
    img_affine = cv2.warpAffine(img, M_affine, img.shape[:2]) # image transformation

    # scaling
    sx = numpy.sqrt(M_affine[0, 0] ** 2 + M_affine[1, 0] ** 2)
    sy = numpy.sqrt(M_affine[0, 1] ** 2 + M_affine[1, 1] ** 2)
    
    # rotation
    theta = -numpy.arctan(numpy.divide(M_affine[1, 0], M_affine[0, 0]))
    theta_rad = theta * numpy.pi / 180

    # translation
    tx = numpy.divide( ((M_affine[0, 2] * numpy.cos(theta_rad)) - (M_affine[1, 2] * numpy.sin(theta_rad))), sx)
    ty = numpy.divide( ((M_affine[0, 2] * numpy.sin(theta_rad)) + (M_affine[1, 2] * numpy.cos(theta_rad))), sy)
    
    # similarity
    M_similar = numpy.float32([
        [sx * numpy.cos(theta_rad), -numpy.sin(theta_rad), tx],
        [numpy.sin(theta_rad), sy * numpy.cos(theta_rad), ty]
    ])
    img_similarity = cv2.warpAffine(img, M_similar, img.shape[:2]) # image similarity

    # display original and results
    # start by clicking 3 points anywhere in the image
    cv2.imshow("Original", img)
    cv2.imshow("Affine", img_affine)
    cv2.imshow("Similarity", img_similarity)
    cv2.imwrite("img_affined.png", img_affine)
    cv2.imwrite("img_similarity.png", img_similarity)
    cv2.waitKey(0)
    cv2.destroyAllWindows()