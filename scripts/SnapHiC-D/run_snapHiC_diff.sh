#!/bin/bash

############################################################################
###                            User Variables                            ###
############################################################################

SnapHiC_D_dir="/home/maa160/CompBioRA2023/scripts/SnapHiC-D"
group_A_dir="/project/compbio-lab/100kb_imputed_cool/181218_21yr_2_A12_AD004_OPC_100kb_contacts/"
group_B_dir="/project/compbio-lab/100kb_imputed_cool/181218_21yr_2_A12_AD006_MP_100kb_contacts/"
file_list_dir="/project/compbio-lab/100kb_imputed_cool/181218_21yr_2_A12_AD006_MP_AD004_OPC_100kb_contacts_snap/test_file_list.txt"
out_dir="/project/compbio-lab/100kb_imputed_cool/181218_21yr_2_A12_AD006_MP_AD004_OPC_100kb_contacts_snap"
chr="chr22"
genome="hg19"
num_CPUs=24
bin_size=100000
fdr_threshold=0.1
max_gap=101
min_gap=2

############################################################################
if [ ! -d "$out_dir" ]; then
  mkdir $out_dir
fi

if [ ! -d "${out_dir}/tempfile" ]; then
  mkdir ${out_dir}/tempfile
fi

python ${SnapHiC_D_dir}/snapHiC_diff.py -s $SnapHiC_D_dir -i $group_A_dir -j $group_B_dir -a $file_list_dir -o $out_dir -c $chr -g $genome -n $num_CPUs --binsize $bin_size --fdr_threshold $fdr_threshold --maxi_gap $max_gap --mini_gap $min_gap


if [ "$(ls -A ${out_dir}/tempfile)" ]; then
     cd ${out_dir}/tempfile; awk 'FNR==1 && NR!=1{next;}{print}' DI_FDR10_T2_Test_${chr}_GAP*.txt > ../DI_FDR10_T2_Test_all${chr}.txt; awk 'FNR==1 && NR!=1{next;}{print}' all_results_${chr}_GAP*.txt > ../combined_all${chr}_results.txt
 
else
    echo Program did not run successfully
fi