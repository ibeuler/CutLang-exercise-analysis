import pandas as pd
import os

regions = ["2J", "4J", "6J"]

# dirs:
input_dir = "results_8"
add_ahmetcan_dir = "compare_with_ahmetcan/04_11_2025_v2"

output_dir = "ibo_ahmetcan_paper_3"

for i in regions:
    target = f"{input_dir}/{i}/"
    # list the .csv files in the target
    list_of_csv = [f for f in os.listdir(target) if f.endswith('.csv')]
    for csv_file in list_of_csv:
        df_main = pd.read_csv(os.path.join(target, csv_file))
        a_path = f"{add_ahmetcan_dir}/{i}/"
        df_ia = pd.read_csv(os.path.join(a_path, csv_file))
        
        # align lengths by padding with nan if mismatched
        max_len = max(len(df_main), len(df_ia))
        df_main = df_main.reindex(range(max_len))
        df_ia = df_ia.reindex(range(max_len))
        
        # ahmetcan_Selection, ahmetcan_Cutflow
        df_main["ahmetcan_Selection"] = df_ia["ahmetcan_Selection"]
        df_main["ahmetcan_Cutflow"] = df_ia["ahmetcan_Cutflow"]
        df_main.to_excel(f"{output_dir}/exel/{csv_file.replace('.csv', '.xlsx')}", index=False)
        df_main.to_csv(f"{output_dir}/csv/{csv_file}",index=False)