import json
import csv

# Load the JSON data
with open("results.json", "r") as f:
    data = json.load(f)

# Extract relevant data
repo_name = data["SourceMetadata"]["Data"]["Github"]["repository"].split("/")[-1]
link = data["SourceMetadata"]["Data"]["Github"]["link"]
commit = data["SourceMetadata"]["Data"]["Github"]["commit"]
filename = data["SourceMetadata"]["Data"]["Github"]["file"]
lines = data["SourceMetadata"]["Data"]["Github"]["line"]
detector_type = data["DetectorType"]
verified_status = data["Verified"]
raw = data["Raw"]

# Create a list of data for the CSV row
data_row = [repo_name, link, commit, filename, lines, detector_type, verified_status, raw]

# Write the data to a CSV file
with open("secret-scan-results.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["repo_name", "link", "commit", "filename", "Lines", "Detector type", "verified status", "raw"])
    writer.writerow(data_row)

print("Converted JSON data to CSV file: secret-scan-results.csv")
