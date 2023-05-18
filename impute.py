from rwr import impute_chromosome
import sys

inputfile = sys.argv[1] 
outputfile = sys.argv[2] 
# /project/compbio-lab/scHi-C/Lee2019/Human_single_cell_10kb_cool/181218_21yr_2_A10_AD001_L23_10kb_contacts.cool"

# Provide the necessary parameters
scool_url = inputfile
chrom = "chr22"
resolution = 100000
output_path = outputfile#"tempData/imputed.cool"

# Call the impute_chromosome function
impute_chromosome(
    scool_url=scool_url,
    chrom=chrom,
    resolution=resolution,
    output_path=output_path,
    logscale=False,
    pad=1,
    std=1,
    rp=0.5,
    tol=0.01,
    window_size=500000000,
    step_size=10000000,
    output_dist=500000000,
    min_cutoff=0
)