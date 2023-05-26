from cool_to_coo import cool_to_coo
import pandas as pd

df1 = cool_to_coo("/project/compbio-lab/100kb_imputed_cool/181218_21yr_2_A12_AD004_OPC_100kb_contacts/181218_21yr_2_A12_AD004_OPC_100kb_contacts_imputed.cool", 100000)
df1.to_csv('/project/compbio-lab/100kb_imputed_cool/181218_21yr_2_A12_AD004_OPC_100kb_contacts/181218_21yr_2_A12_AD004_OPC_100kb_contacts_imputed.csv', sep='\t', index=False)

df2 = cool_to_coo("/project/compbio-lab/100kb_imputed_cool/181218_21yr_2_A12_AD006_MP_100kb_contacts/181218_21yr_2_A12_AD006_MP_100kb_contacts_imputed.cool",100000)
df2.to_csv('/project/compbio-lab/100kb_imputed_cool/181218_21yr_2_A12_AD006_MP_100kb_contacts/181218_21yr_2_A12_AD006_MP_100kb_contacts_imputed.csv', sep='\t', index=False)