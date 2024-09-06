import csv
import random
from faker import Faker

fake = Faker()

def generate_csv(file_name, num_rows):
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['first_name', 'last_name', 'address', 'date_of_birth']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for _ in range(num_rows):
            writer.writerow({
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'address': fake.address().replace("\n", ", "),  # Clean up address format
                'date_of_birth': fake.date_of_birth()
            })

# Example: Generate a CSV file with 1 million rows (~2GB depending on data)
file_path = r'c:\Users\rajes\Downloads\google_data\DE challenge\csv_anonymise\large_data.csv'
generate_csv(file_path, 100000)
