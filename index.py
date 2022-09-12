import csv
filename = 'sales.csv'
with open('sales.csv','r') as csv_file:
    csvReader=csv.reader(csv_file)
    for row in csvReader:
        print(row)

sales = [6226, 1521,  1842, 2051, 1728, 2138, 7479, 4434, 3615, 5472, 7224, 1812]
total = sum(sales)
print("The total of all sales is: £",sum(sales))
with open('sales.csv','r') as csv_file:
    csvReader=csv.reader(csv_file)

    next(csvReader)

    for line in csvReader:
        sales.append

    print(sales)
    print(type(sales))
