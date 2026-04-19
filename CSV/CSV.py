import csv

try:
    with open("sample.csv","r") as file:
        reader=csv.reader(file)

        count=0

        for row in reader:
            count+=1

        print(f"Total number of rows is {count}")

except FileNotFoundError:
    print("File not found")