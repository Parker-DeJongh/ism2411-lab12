
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

print("--- Exercise 4: Compute Totals ---")

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        line_total = price * quantity
        total_revenue += line_total

        print(f"{product}: {quantity} units * ${price:.2f} = ${line_total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")

print("--- Exercise 5: Filter and Write ---")

original_count = 0
written_count = 0

with open("data/sales.csv", "r") as infile:
    reader = csv.reader(infile)
    next(reader)

    with open("data/cleaned.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)

        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_count += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])

            line_total = price * quantity

            if line_total > 100:
                writer.writerow([product, price, quantity, line_total])
                written_count += 1

print(f"Original rows: {original_count}")
print(f"Rows written: {written_count}")

print("--- Exercise 6: DictReader ---")

dict_total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        line_total = price * quantity
        dict_total_revenue += line_total

print(f"Total revenue using DictReader: ${dict_total_revenue:.2f}")

# csv.reader uses column position to access data, while csv.DictReader uses column names. This makes DictReader more readable and less error-prone.

print("--- Exercise 7: Sales Summary by Product ---")

sales_summary = {}

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        line_total = price * quantity

        if product in sales_summary:
            sales_summary[product] += line_total
        else:
            sales_summary[product] = line_total

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")
