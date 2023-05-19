import cooler
import pandas as pd
import scipy.sparse as sp

def cool_to_coo(cool_path, chromosome, resolition):
    # cool_path = "/project/compbio-lab/100kb_imputed_cool/181218_21yr_2_A12_AD004_OPC_100kb_contacts/181218_21yr_2_A12_AD004_OPC_100kb_contacts_imputed.cool"
    # chromosome = "chr22"  # Replace with the desired chromosome
    # resolution = 100000
    # Read the .cool file
    c = cooler.Cooler(cool_path)

    # Extract the desired chromosome's contact matrix
    matrix = c.matrix(balance=False).fetch(chromosome)

    # Convert the matrix to a DataFrame
    df = pd.DataFrame(matrix)
    coo = sp.coo_matrix(df)

    #  ["chrnum", "from", "from.1", "chrnum.1", "to", "to.1", "value"]

    # Create the DataFrame
    df = pd.DataFrame()
    df["chrnum"] = [int(chromosome[3:])] * coo.size
    df["from"] = coo.row*resolution
    df["from.1"] = coo.col*resolution
    df["chrnum.1"] = [int(chromosome[3:])] * coo.size
    df["to"] = df["from"] + resolution
    df["to.1"] = df["from.1"] + resolution
    df["value"] = coo.data

    # Print the resulting DataFrame
    return(df)
