# regions list: 

regions="2JB 2JBveto 4JLowxB 4JLowxBveto 4JHighxB 4JHighxBveto 6JB 6JBveto"

for i in ./*/; do
    echo "Processing directory: $i"
    # take the first character of $i
    first_char=$(basename "$i" | cut -c 1)
    echo "First character: $first_char"
    # if first character is the same as the first character of a region in regions, then process the directory
    for region in $regions; do
        if [ "$first_char" == "${region:0:1}" ]; then
            echo "Matching region found: $region"
            cd "$i" 
            if [ "$1" = "save" ];  then
                cutflow_compare --files histoOut-*.root -r $region --colored --counts PAPER_CUTFLOW --relative-error --save
            else 
                cutflow_compare --files histoOut-*.root -r $region --colored --counts PAPER_CUTFLOW --relative-error
            fi
            cd ..
        fi
    done
done
