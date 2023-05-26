import cooler
import pandas as pd
import numpy as np
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

        # df = pd.DataFrame()
        # for r in range(len(matrix)):
        #     for c in range(len(matrix)):
        #         # New row to append
        #         new_row = pd.Series({'chrnum':int(chromosome[3:]),
        #                              'from': r*resolution,
        #                              'from.1': (r+1)*resolution,
        #                              'chrnum.1':int(chromosome[3:]),
        #                              'to': c*resolution,
        #                              'to.1': (c+1)*resolution,
        #                              'value': matrix[r][c]
        #                              })

        #         # Append the new row to the DataFrame
        #         df = pd.concat([df, new_row.to_frame().T], ignore_index=True)
        # print(df)

        blank_df = pd.DataFrame()
        blank_df["chrnum"] = [int(chromosome[3:])] * matrix.shape[0] **2
        blank_df["from"] = np.tile(np.arange(0, matrix.shape[0] * resolution, resolution), matrix.shape[0])
        blank_df["from.1"] = blank_df["from"] + resolution
        blank_df["chrnum.1"] = [int(chromosome[3:])] * matrix.shape[0] **2
        blank_df["to"] = np.repeat(np.arange(0, matrix.shape[0] * resolution, resolution), matrix.shape[0])
        blank_df["to.1"] = blank_df["to"] + resolution
        blank_df["value"] = 0
        
        df = pd.DataFrame(matrix)
        coo = sp.coo_matrix(df)
        #print(coo)

        # Create a DataFrame for the current chromosome
        df_chromosome = pd.DataFrame()
        df_chromosome["chrnum"] = [int(chromosome[3:])] * coo.size
        df_chromosome["from"] = coo.row * resolution
        df_chromosome["from.1"] = df_chromosome["from"] + resolution
        df_chromosome["chrnum.1"] = [int(chromosome[3:])] * coo.size
        df_chromosome["to"] = coo.col * resolution
        df_chromosome["to.1"] = df_chromosome["to"] + resolution
        df_chromosome["value"] = coo.data

        total_df = pd.concat([blank_df, df_chromosome], ignore_index=True)
        #print(df_chromosome)
        #print(blank_df)
        #print(total_df)
        grouped = total_df.groupby(['chrnum','from','from.1','chrnum.1','to','to.1'])
        blank_df['value'] = grouped['value'].transform('sum')

        # print(blank_df)
        # Append the DataFrame for the current chromosome to the data list
        data.append(blank_df)

    # Concatenate all the chromosome DataFrames into a single DataFrame
    result_df = pd.concat(data, ignore_index=True)
    # Reset the index and remove the index column
    result_df = result_df.reset_index(drop=True)
    #print(result_df)
    
    return result_df