import cooler

def coarsen(inputfile, outputfile):
    base_uri = inputfile
    output_uri = outputfile
    factor = 10
    chunksize = 10000
    cooler.coarsen_cooler(base_uri, output_uri, factor, chunksize)