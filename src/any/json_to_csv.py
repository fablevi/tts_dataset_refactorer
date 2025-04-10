import json
import csv
import os

# Input and output paths
input_json = "../../data/hungarian-single-speaker-tts/pure/metadata.json"
output_dir = "../../data/hungarian-single-speaker-tts/pure"
output_csv = os.path.join(output_dir, "metadata.csv")

# Read JSON data
with open(input_json, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Write to CSV with pipe delimiter
with open(output_csv, 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='|')

    # Write header
    writer.writerow(['path', 'text'])

    # Write data rows
    for item in data:
        writer.writerow([item['path'], item['text']])

print(f"CSV fájl elkészült: {output_csv}")