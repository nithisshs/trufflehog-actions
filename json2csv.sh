#!/bin/bash

# Define input JSON file
input_json="results.json"

# Define output CSV file
output_csv="secret-scan-results.csv"

# Define headers
headers="repo_name,link,commit,filename,Lines,Detector_type,verified_status,raw"

# Extract relevant data using jq and save it to temporary JSON file
jq -r '[
    .SourceMetadata.Data.Github.repository,
    .SourceMetadata.Data.Github.link,
    .SourceMetadata.Data.Github.commit,
    .SourceMetadata.Data.Github.file,
    .SourceMetadata.Data.Github.line,
    .DetectorName,
    .Verified,
    .Raw
] | @csv' "$input_json" > temp.csv

# Add headers to the output CSV file
echo "$headers" > "$output_csv"
cat temp.csv >> "$output_csv"

# Remove temporary CSV file
rm temp.csv

echo "Conversion complete. Output saved to $output_csv"
