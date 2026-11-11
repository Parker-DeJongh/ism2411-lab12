
import csv
from datetime import datetime

print("--- Exercise 2: Raw CSV Rows ---")

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

print("--- Exercise 3: Skip Header ---")

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)
