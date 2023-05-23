import cooler
import pandas as pd
import scipy.sparse as sp

def cool_to_coo(cool_path, resolution):
    # Read the .cool file
    c = cooler.Cooler(cool_path)
    # Get the chromosome names
    chrom_names = c.chromnames

    # Create an empty list to store the resulting data
    data = []

    # Loop over each chromosome
    for chromosome in chrom_names:
        # Extract the contact matrix for the current chromosome
        matrix = c.matrix(balance=False).fetch(chromosome)
        df = pd.DataFrame(matrix)
        coo = sp.coo_matrix(df)

        # Create a DataFrame for the current chromosome
        df_chromosome = pd.DataFrame()
        df_chromosome["chrnum"] = [int(chromosome[3:])] * coo.size
        df_chromosome["from"] = coo.row * resolution
        df_chromosome["from.1"] = df_chromosome["from"] + resolution
        df_chromosome["chrnum.1"] = [int(chromosome[3:])] * coo.size
        df_chromosome["to"] = coo.col * resolution
        df_chromosome["to.1"] = df_chromosome["to"] + resolution
        df_chromosome["value"] = coo.data

        # Append the DataFrame for the current chromosome to the data list
        data.append(df_chromosome)

    # Concatenate all the chromosome DataFrames into a single DataFrame
    result_df = pd.concat(data, ignore_index=True)
    # Reset the index and remove the index column
    result_df = result_df.reset_index(drop=True)
    #print(result_df)
    
    return result_df