import pandas as pd
import json

# Load JSON files
with open('all-keys.json') as f:
    all_keys_data = json.load(f)

with open('verified-keys.json') as f:
    verified_keys_data = json.load(f)

# Convert to DataFrames
all_keys_df = pd.json_normalize(all_keys_data)
verified_keys_df = pd.json_normalize(verified_keys_data)

# Save to Excel
with pd.ExcelWriter('trufflehog-results.xlsx', engine='openpyxl') as writer:
    all_keys_df.to_excel(writer, sheet_name='All_Keys', index=False)
    verified_keys_df.to_excel(writer, sheet_name='Verified_Keys', index=False)
