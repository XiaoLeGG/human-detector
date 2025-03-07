#提取图片hog特征
import skimage.feature as feature
import skimage.io as io
import joblib
import glob
import os
from config import *

    
def extract_features():
    des_type = 'HOG'

    # If feature directories don't exist, create them
    if not os.path.isdir(pos_feat_ph):
        os.makedirs(pos_feat_ph)

    # If feature directories don't exist, create them
    if not os.path.isdir(neg_feat_ph):
        os.makedirs(neg_feat_ph)

    print ("Calculating the descriptors for the positive samples and saving them")
    for im_path in glob.glob(os.path.join(pos_im_path, "*")):
        #print im_path
        
        im = io.imread(im_path, as_gray=True)
        if des_type == "HOG":
            fd = feature.hog(im, orientations=orientations, pixels_per_cell=pixels_per_cell, cells_per_block=cells_per_block, visualize=visualize, block_norm=block_norm)
        fd_name = os.path.split(im_path)[1].split(".")[0] + ".feat"
        fd_path = os.path.join(pos_feat_ph, fd_name)
        joblib.dump(fd, fd_path)
    print ("Positive features saved in {}".format(pos_feat_ph))

    print ("Calculating the descriptors for the negative samples and saving them")
    for im_path in glob.glob(os.path.join(neg_im_path, "*")):
        im = io.imread(im_path, as_gray=True)
        if des_type == "HOG":
            fd = feature.hog(im, orientations=orientations, pixels_per_cell=pixels_per_cell, cells_per_block=cells_per_block, visualize=visualize, block_norm=block_norm)
        fd_name = os.path.split(im_path)[1].split(".")[0] + ".feat"
        fd_path = os.path.join(neg_feat_ph, fd_name)
    
        joblib.dump(fd, fd_path)
    print ("Negative features saved in {}".format(neg_feat_ph))

    print ("Completed calculating features from training images")

if __name__=='__main__':
    extract_features()
