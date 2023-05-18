from coarsen import coarsen
from dataVis import visualize_schi
from impute import impute
import sys

# 181218_21yr_2_A12_AD004_OPC_10kb_contacts.cool
# 181218_21yr_2_A12_AD006_MP_10kb_contacts.cool
inputfile = sys.argv[1] 

file_name = inputfile.split(".")[0].replace("_10kb_", "_100kb_")

inpath = "~/scHi-C_link/Lee2019/Human_single_cell_10kb_cool/"+inputfile
orig_img_outpath = "~/CompBioRA2023/Hi-C_Visualizations/"+ file_name +"/"+file_name+"_original.png"
coarse_img_outpath = "~/CompBioRA2023/Hi-C_Visualizations/"+ file_name +"/"+file_name+"_coarse.png"
imputed_img_outpath = "~/CompBioRA2023/Hi-C_Visualizations/"+ file_name +"/"+file_name+"_imputed.png"
coarse_outpath = "~/100kb_imputed_cool/"+file_name+"/"+file_name+"_coarse.cool"
imputed_outpath = "~/100kb_imputed_cool/"+file_name+"/"+file_name+"_imputed.cool"

visualize_hic(inpath, orig_img_outpath)
coarsen(inpath, coarse_outpath)
visualize_hic(coarse_outpath, coarse_img_outpath)
impute(coarse_outpath, imputed_outpath)
visualize_hic(imputed_outpath, imputed_img_outpath)

