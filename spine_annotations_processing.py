# -*- coding: utf-8 -*-
import pandas as pd
import os
import pdb
import numpy as np



path = (r"C:\Users\")  # Annotations file directory
save_path = path


col_names = ['I' + str(x).zfill(2) for x in range(1,16)]
f_list = []
n_spines_df = pd.DataFrame(columns=col_names)


par_list = ['n_spines',

            'n_stable',

            'n_lost',

            'n_gained',
            
            'n_dynamic',

            'spine_density',
            
            'dynamic_spines_density',
            
            'perc_stable',

            'perc_lost',

            'perc_gained',

            'perc_transient',

            'n_new_persistent_by_all_gained',
            
            'survival_im3_gained_norm',
            
            'survival_im4_gained_norm',
            
            'survival_im5_gained_norm',
            
            'survival_im6_gained_norm',
            
            'survival_im7_gained_norm',
            
            'survival_im8_gained_norm',
            
            'survival_im9_gained_norm',
            
            'survival_im10_gained_norm',

            'survival_im11_gained_norm',

            'survival_im12_gained_norm',
            
            'survival_im13_gained_norm',
            
            'survival_im14_gained_norm',

            'survival_im3_present_norm',
            'survival_im4_present_norm',
            'survival_im5_present_norm',
            'survival_im6_present_norm',
            'survival_im7_present_norm',
            'survival_im8_present_norm',
            'survival_im9_present_norm',
            'survival_im10_present_norm',
            'survival_im11_present_norm',
            'survival_im12_present_norm',
            'survival_im13_present_norm',
            
            'survival_superstable_norm',

            'n_protrusions_2_density',

            'n_protrusions_3_density',

            'n_protrusions_2',

            'n_protrusions_3',
            
            'gain_by_loss',
            
            'turnover',

            'gain_density',
            
            'survival_stable']



result_dict = {par: pd.DataFrame() for par in par_list}

total_dend_len_dict = {}
total_dend_len_list = []



for root, dirs, files in os.walk(path):
    for f in files:
        if not '.csv' in f:

            continue

        f_list.append(f)

        data = pd.read_csv(root + '\\' +f,

                           header=3,

                           delimiter=';',

                           skip_blank_lines=True,

                           skipfooter=4,

                           usecols=range(1,16),

                           names = col_names,

                           dtype=float,

                           skipinitialspace=True)



        data_bool = data > 10

        data_bool.any(axis=1)

        dends = data[data_bool.any(axis=1)]

        total_dend_len = dends.mean(axis=1, skipna=True).sum()

        total_dend_len_dict[f] = total_dend_len

        total_dend_len_list.append(total_dend_len)



        spines_size = data[~data_bool.any(axis=1)]

        n_protrusions_2_density = (spines_size > 2).sum(axis=0) / total_dend_len

        n_protrusions_3_density = (spines_size > 3).sum(axis=0) / total_dend_len

        n_protrusions_2 = (spines_size > 2).sum(axis=0)

        n_protrusions_3 = (spines_size > 3).sum(axis=0)



        spines_bin = spines_size > 0

        spines_bin_shifted = spines_bin.shift(1,axis='columns')

        spines_added = spines_bin + spines_bin_shifted

        spines_diff = spines_bin - spines_bin_shifted

        spines_stable = spines_added == 2

        spines_lost = (spines_diff == -1)

        spines_gained = (spines_diff == 1)

        im3_gained = spines_bin[spines_gained[spines_gained.columns[2]]]
        survival_im3_gained = im3_gained[spines_gained.columns[2:]].sum(axis=0)
        survival_im3_gained_norm = (survival_im3_gained / survival_im3_gained [0]) * 100
        
        im4_gained = spines_bin[spines_gained[spines_gained.columns[3]]]
        survival_im4_gained = im4_gained[spines_gained.columns[3:]].sum(axis=0)
        survival_im4_gained_norm = (survival_im4_gained / survival_im4_gained [0]) * 100
        
        im5_gained = spines_bin[spines_gained[spines_gained.columns[4]]]
        survival_im5_gained = im5_gained[spines_gained.columns[4:]].sum(axis=0)
        survival_im5_gained_norm = (survival_im5_gained / survival_im5_gained[0])*100
        
        im6_gained = spines_bin[spines_gained[spines_gained.columns[5]]]
        survival_im6_gained = im6_gained[spines_gained.columns[5:]].sum(axis=0)
        survival_im6_gained_norm = (survival_im6_gained / survival_im6_gained[0])*100
        
        im7_gained = spines_bin[spines_gained[spines_gained.columns[6]]]
        survival_im7_gained = im6_gained[spines_gained.columns[6:]].sum(axis=0)
        survival_im7_gained_norm = (survival_im7_gained / survival_im7_gained[0])*100
        
        im8_gained = spines_bin[spines_gained[spines_gained.columns[7]]]
        survival_im8_gained = im8_gained[spines_gained.columns[7:]].sum(axis=0)
        survival_im8_gained_norm = (survival_im8_gained / survival_im8_gained [0]) * 100
        
        im9_gained = spines_bin[spines_gained[spines_gained.columns[8]]]
        survival_im9_gained = im9_gained[spines_gained.columns[8:]].sum(axis=0)
        survival_im9_gained_norm = (survival_im9_gained / survival_im9_gained[0])*100
        
        im10_gained = spines_bin[spines_gained[spines_gained.columns[9]]]
        survival_im10_gained = im10_gained[spines_gained.columns[9:]].sum(axis=0)
        survival_im10_gained_norm = (survival_im10_gained / survival_im10_gained [0]) * 100
        
        im11_gained = spines_bin[spines_gained[spines_gained.columns[10]]]
        survival_im11_gained = im11_gained[spines_gained.columns[10:]].sum(axis=0)
        survival_im11_gained_norm = (survival_im11_gained / survival_im11_gained [0]) * 100

        im12_gained = spines_bin[spines_gained[spines_gained.columns[11]]]
        survival_im12_gained = im12_gained[spines_gained.columns[11:]].sum(axis=0)
        survival_im12_gained_norm = (survival_im12_gained / survival_im12_gained [0] ) * 100
    
        im13_gained = spines_bin[spines_gained[spines_gained.columns[12]]]
        survival_im13_gained = im13_gained[spines_gained.columns[12:]].sum(axis=0)
        survival_im13_gained_norm = (survival_im13_gained / survival_im13_gained [0]) * 100
        
        im14_gained = spines_bin[spines_gained[spines_gained.columns[13]]]
        survival_im14_gained = im14_gained[spines_gained.columns[13:]].sum(axis=0)
        survival_im14_gained_norm = (survival_im14_gained / survival_im14_gained [0]) * 100
        
        
        
        im3_present = spines_bin[spines_bin[spines_gained.columns[2]]]
        survival_im3_present = im3_present[spines_gained.columns[2:]].sum(axis=0)
        survival_im3_present_norm = (survival_im3_present / survival_im3_present [0]) * 100
        
        im4_present = spines_bin[spines_bin[spines_gained.columns[3]]]
        survival_im4_present = im4_present[spines_gained.columns[3:]].sum(axis=0)
        survival_im4_present_norm = (survival_im4_present / survival_im4_present [0]) * 100
        
        im5_present = spines_bin[spines_bin[spines_gained.columns[4]]]
        survival_im5_present = im5_present[spines_gained.columns[4:]].sum(axis=0)
        survival_im5_present_norm = (survival_im5_present / survival_im5_present [0]) * 100
        
        im6_present = spines_bin[spines_bin[spines_gained.columns[5]]]
        survival_im6_present = im6_present[spines_gained.columns[5:]].sum(axis=0)
        survival_im6_present_norm = (survival_im6_present / survival_im6_present [0]) * 100
                
        im7_present = spines_bin[spines_bin[spines_gained.columns[6]]]
        survival_im7_present = im7_present[spines_gained.columns[6:]].sum(axis=0)
        survival_im7_present_norm = (survival_im7_present / survival_im7_present [0]) * 100
        
        im8_present = spines_bin[spines_bin[spines_gained.columns[7]]]
        survival_im8_present = im8_present[spines_gained.columns[7:]].sum(axis=0)
        survival_im8_present_norm = (survival_im8_present / survival_im8_present [0]) * 100
                
        im9_present = spines_bin[spines_bin[spines_gained.columns[8]]]
        survival_im9_present = im9_present[spines_gained.columns[8:]].sum(axis=0)
        survival_im9_present_norm = (survival_im9_present / survival_im9_present [0]) * 100
        
        im10_present = spines_bin[spines_bin[spines_gained.columns[9]]]
        survival_im10_present = im10_present[spines_gained.columns[9:]].sum(axis=0)
        survival_im10_present_norm = (survival_im10_present / survival_im10_present [0]) * 100
        
        im11_present = spines_bin[spines_bin[spines_gained.columns[10]]]
        survival_im11_present = im11_present[spines_gained.columns[10:]].sum(axis=0)
        survival_im11_present_norm = (survival_im11_present / survival_im11_present [0]) * 100
        
        im12_present = spines_bin[spines_bin[spines_gained.columns[11]]]
        survival_im12_present = im12_present[spines_gained.columns[11:]].sum(axis=0)
        survival_im12_present_norm = (survival_im12_present / survival_im12_present [0]) * 100
        
        im13_present = spines_bin[spines_bin[spines_gained.columns[12]]]
        survival_im13_present = im13_present[spines_gained.columns[12:]].sum(axis=0)
        survival_im13_present_norm = (survival_im13_present / survival_im13_present [0]) * 100
        
        
        superstable = spines_bin[spines_bin[spines_gained.columns[0:3]].sum(axis=1) == 3]
        survival_superstable = superstable[spines_gained.columns[2:]].sum(axis=0)     
        survival_superstable_norm = (survival_superstable / survival_superstable [0]) * 100



        stable = spines_bin[spines_bin[spines_gained.columns[1:3]].sum(axis=1) == 2]
        survival_stable = stable[spines_gained.columns[2:]].sum(axis=0)

        transient_temp = (spines_gained + spines_bin.shift(-1, axis='columns')) == 1

        transient = transient_temp & spines_gained

        n_transient = transient.sum(axis=0)





        new_persistent = (spines_gained + spines_bin.shift(-1, axis='columns')) == 2

        n_new_persistent = new_persistent.sum(axis=0)



        total_spines = spines_bin.any(axis=1).sum()

        n_stable = spines_stable.sum()

        n_spines = spines_bin.sum(axis=0)

        n_lost = spines_lost.sum(axis=0)

        n_gained = spines_gained.sum(axis=0)
        
        n_dynamic = n_lost + n_gained

        perc_stable = (n_stable / n_spines.shift(1)) * 100

        spine_density = n_spines / total_dend_len

        perc_lost = (n_lost / n_spines.shift(1)) * 100

        perc_gained = (n_gained / n_spines) * 100

        gain_by_loss = (perc_gained / perc_lost)

        turnover = (n_lost + n_gained) / (n_spines + n_spines.shift(1))

        gain_density = n_gained / total_dend_len

        perc_transient = (n_transient / n_spines) * 100

        n_new_persistent_by_all_gained = n_new_persistent / n_gained
        
        dynamic_spines_density = (n_lost+n_gained) / total_dend_len


        n_spines_df = n_spines_df.append(n_spines, ignore_index=True)



        for k in result_dict.keys():

            result_dict[k] = result_dict[k].append(eval(k), ignore_index=True)



index_dict = {}

for idx, x in enumerate(f_list):

    index_dict[idx] = x



xl_writer = pd.ExcelWriter(save_path + '\\' + 'results_young_090921.xlsx')

for k in result_dict.keys():

    result_dict[k].rename(index=index_dict, inplace=True)

    result_dict[k].to_excel(xl_writer, sheet_name = k)

xl_writer.close()