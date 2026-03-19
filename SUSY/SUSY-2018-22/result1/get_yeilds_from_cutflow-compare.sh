


for folder in $(ls -d */);
do 
    echo "Processing folder: $folder"
    cd "$folder"
    mkdir -p yields_csv
    #EXAMPLE $ cutflow_compare -f *.root --list-regions
    #Listing region directories (with a 'cutflow' histogram) per file:
    # histoOut-SS_direct_1600_400.root:
    #  SR2j1600
    #  SR2j2200
    #  SR2j2800
    # listing them as space-separated values: to be accepted as SR2j1600 SR2j2200 SR2j2800
    regions=$(cutflow_compare -f *.root --list-regions | grep -oP '(?<=\s{2})\w+')
    echo "Regions found: $regions"
    echo "$regions" > regions.txt
    cutflow_compare -f *.root --regions-from-file regions.txt --labels "CutFlow" --save yields_csv/cutflow_for_reigon --colored
    cd ..
done
    