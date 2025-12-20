# regions list: 

regions="2J 4J 6J"

for region in $regions; do
    cd "$region"
    if [ "$1" = "save" ];  then
        cutflow_compare --files ../../../results_6/$region/histoOut-*.root  ../../../ahmetcan/yeni_14_10_2025/$region*.root --regions-from-file regions.txt --save $region_ibeulerVSahmetcan --colored --labels ibeuler ahmetcan --separate-selections
    else 
        cutflow_compare --files ../../../results_6/$region/histoOut-*.root  ../../../ahmetcan/yeni_14_10_2025/$region*.root --regions-from-file regions.txt --colored --labels ibeuler ahmetcan --separate-selections
    fi
    cd ..
done
       