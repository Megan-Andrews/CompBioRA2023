import matplotlib.pyplot as plt
import sys
import numpy as np
import pandas as pd
import cooler


# inputfile = sys.argv[1] 
# outputfile = sys.argv[2] 

def visualize_hic(inputfile, outputfile): 
# Load Hi-C data from a text or CSV file using NumPy or Pandas
# 'hic_data' should be a 2D numpy array or a pandas DataFrame
#filepath = "/project/compbio-lab/scHi-C/Lee2019/Human_single_cell_10kb_cool/181218_21yr_2_A10_AD001_L23_10kb_contacts.cool"

    filepath = inputfile #"/home/maa160/CompBioRA2023/tempData/imputed.cool"
    c = cooler.Cooler(filepath)

    #c.coarsen_cooler()

    # Get the contact matrix (e.g., for chromosome 1)
    chrom = "chr22"
    # start = 0
    # end = 2000000
    matrix = c.matrix(balance=False).fetch(f"{chrom}")

    # log(M + 1) scale the image
    matrix_log = np.log1p(matrix)
    min_value = np.min(matrix_log)
    max_value = np.max(matrix_log)

    # # Define the desired downsampling factor
    # downsample_factor = 1

    # # Downsample the matrix
    # downsampled_matrix = matrix_log[::downsample_factor, ::downsample_factor]

    # Clear the plot
    plt.clf()

    # Create a heatmap plot
    plt.imshow(matrix_log, cmap="hot", origin="lower", vmin=min_value, vmax=max_value)

    # Set the plot title and labels
    plt.title("Contact Matrix")
    plt.xlabel("Genomic Position")
    plt.ylabel("Genomic Position")

    # Show the colorbar
    plt.colorbar()

    # Show the heatmap
    plt.savefig(outputfile)
