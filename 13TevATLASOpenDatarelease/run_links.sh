#!/bin/bash




# Check if an ADL file is provided as an argument
if [ $# -lt 1 ]; then
    echo "Usage: $0 <ADL_FILE>"
    exit 1
fi

# Get the ADL file from the input argument
ADL_FILE="$1"

# Extract the ADL filename without the extension
ADL_NAME=$(basename "$ADL_FILE" .adl)

# Get the current date and hour
current_time=$(date "+%d.%m.%Y_%Hh")

# Define the working directory including ADL name and hourly timestamp
WORKDIR="HZZ-ResultsCL-${ADL_NAME}-$current_time"

# Create the working directory if it doesn't exist
mkdir -p "$WORKDIR"

# Read the file line by line
while IFS= read -r link; do
    # Extract filename from the link (removing directory path and extension)
    filename=$(basename "$link" .root)
    
    # Run the command with each link
    CLA "$link" ATLASODR2 -i "$ADL_FILE"

    # Check if CLA ran successfully
    if [ $? -eq 0 ]; then
        # Rename and move the output file to the working directory
        mv histoOut-${ADL_NAME}.root "$WORKDIR/histoOut-${filename}.root"
    fi
done < data_links.txt
