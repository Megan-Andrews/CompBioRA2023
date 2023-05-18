import cooler

base_uri = "/project/compbio-lab/scHi-C/Lee2019/Human_single_cell_10kb_cool/181218_21yr_2_A10_AD001_L23_10kb_contacts.cool"
output_uri = "/home/maa160/CompBioRA2023/tempData/coarse.cool"
factor = 10
chunksize = 10000
cooler.coarsen_cooler(base_uri, output_uri, factor, chunksize)