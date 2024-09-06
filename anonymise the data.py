import csv
import hashlib


def anonymize_data(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()



def process_csv(input_file, output_file, chunk_size=10000):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Write header
        header = next(reader)
        writer.writerow(header)
        
        # Process each chunk of data
        for i, row in enumerate(reader):
            row[0] = anonymize_data(row[0])  # First name
            row[1] = anonymize_data(row[1])  # Last name
            row[2] = anonymize_data(row[2])  # Address
            
            writer.writerow(row)
            if i % chunk_size == 0:
                print(f"Processed {i} rows")



# Call the process_csv function with the appropriate file paths

input_file = r'C:\Users\rajes\Downloads\google_data\DE challenge\csv_anonymise\large_data.csv'
output_file = r'C:\Users\rajes\Downloads\google_data\DE challenge\csv_anonymise\anonymise_data.csv'

process_csv(input_file, output_file)
