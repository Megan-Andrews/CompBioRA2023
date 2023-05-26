import matplotlib.pyplot as plt
import sys
import numpy as np
import pandas as pd
import cooler

# Set the precision to display all decimal places
np.set_printoptions(precision=16)

# inputfile = sys.argv[1] 
# outputfile = sys.argv[2] 

def visualize_hic(inputfile, outputfile): 
    filepath = inputfile
    c = cooler.Cooler(filepath)

    # Get the contact matrix (e.g., for chromosome 1)
    chrom = "chr22"
    matrix = c.matrix(balance=False).fetch(f"{chrom}")
    #print(np.float32(np.min(matrix)), np.float32(np.min(np.log1p(matrix))))

    # log(M + 1) scale the matrix
    matrix_log = np.log1p(matrix)
    mean_value = np.mean(matrix_log)
    std_dev = np.std(matrix_log)

    min_value = 0#0.0000001#np.finfo(np.float32).tiny * 2 #mean_value - 4 * std_dev# #smallest positive numpy.float64  #np.min(matrix_log)
    max_value = np.max(matrix_log)/64

    #print(min_value, mean_value + 3 * std_dev, np.max(matrix_log)/64)

    # Clear the plot
    plt.clf()

    # Create a discrete colormap with 10 colors
    cmap = plt.get_cmap('tab20', 20)
    
    # Set the color for the exact zero values
    #cmap.set_under("gray")  # Replace with your desired color for zero values

    # Create a heatmap plot
    plt.imshow(matrix_log, cmap=cmap, origin="lower", vmin=min_value, vmax=max_value)

    # Set the plot title and labels
    plt.title("Contact Matrix")
    plt.xlabel("Genomic Position")
    plt.ylabel("Genomic Position")

    # Generate logarithmically spaced ticks for the colorbar
    num_ticks = 20
    log_ticks = np.logspace(min_value, max_value, num=num_ticks)

    # Show the colorbar with logarithmic scale
    cbar = plt.colorbar(ticks=log_ticks)
    #cbar.set_label('Intensity')
    cbar.ax.set_yticklabels(["{:.2e}".format(tick) for tick in log_ticks])


    # Show the heatmap
    plt.savefig(outputfile)
