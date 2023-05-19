from coarsen import coarsen
from dataVis import visualize_hic
from impute import impute
import sys
import os

# 181218_21yr_2_A12_AD004_OPC_10kb_contacts.cool
# 181218_21yr_2_A12_AD006_MP_10kb_contacts.cool

inputfile = sys.argv[1] 

# get stem of file name
file_name = inputfile.split(".")[0]
new_file_name = inputfile.split(".")[0].replace("_10kb_", "_100kb_")

# the input cool file
inpath = "/project/compbio-lab/scHi-C/Lee2019/Human_single_cell_10kb_cool/"+inputfile

# create image directory
image_directory_path = "/home/maa160/CompBioRA2023/Hi-C_Visualizations/"+ new_file_name 
# Check if the directory exists
if not os.path.exists(image_directory_path):
    os.mkdir(image_directory_path)

# create cool directory
cool_directory_path = "/project/compbio-lab/100kb_imputed_cool/"+new_file_name
# Check if the directory exists
if not os.path.exists(cool_directory_path):
    os.mkdir(cool_directory_path)

# image out paths
orig_img_outpath = image_directory_path+"/"+file_name+"_original.png"
coarse_img_outpath = image_directory_path +"/"+new_file_name+"_coarse.png"
imputed_img_outpath = image_directory_path  +"/"+new_file_name+"_imputed.png"

# cool file out paths
coarse_outpath = cool_directory_path+"/"+new_file_name+"_coarse.cool"
imputed_outpath = cool_directory_path+"/"+new_file_name+"_imputed.cool"

# visualize coarsen impute
visualize_hic(inpath, orig_img_outpath)
coarsen(inpath, coarse_outpath)
visualize_hic(coarse_outpath, coarse_img_outpath)
impute(coarse_outpath, imputed_outpath)
visualize_hic(imputed_outpath, imputed_img_outpath)

