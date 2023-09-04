import csv
import random


def generate_csv_file(filename, num_rows):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Value 1', 'Value 2', 'Value 3'])

        for _ in range(num_rows):
            random_values = [random.randint(1, 1000) for _ in range(3)]
            csv_writer.writerow(random_values)
