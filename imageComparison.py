import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage import measure

def compare(primary, secondary, show_figure=True):
    similarity = measure.compare_ssim(primary, secondary, multichannel=True)

    if(show_figure):
        fig = plt.figure("Similarity")
        plt.suptitle("SSIM : "+str(similarity))
        ax = fig.add_subplot(1,2,1)
        plt.imshow(primary)
        plt.axis("off")
        ax = fig.add_subplot(1,2,2)
        plt.imshow(secondary)
        plt.axis("off")
        plt.show()
    else:
        return similarity

if(__name__=="__main__"):
    image_list = ["pic1.jpg","pic2.jpg","pic3.jpg","pic4.jpg"]
    mat = [[] for i in image_list]
    for i in range(len(image_list)):
        for j in range(len(image_list)):
            primary = cv2.imread(image_list[i])
            secondary = cv2.imread(image_list[j])
            mat[i].append(compare(primary,secondary,show_figure=False))
    print(np.array(mat))
