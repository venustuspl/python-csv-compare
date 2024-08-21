import pandas as pd
import datetime

try:
    # Define the list of car brands
    car_brands = ['KIA', 'Jaguar', 'Land Rover', 'Ford', 'Hyundai', 'MG']

    # Read file1.csv with encoding latin-1, delimiter ';', and no header
    file1 = pd.read_csv('rv_config_IE_new.csv', encoding='latin-1', delimiter=';', header=None, dtype=str)

    # Filter file1 to only include rows where column 2 is in car_brands
    table1 = file1[(file1.iloc[:, 0].isin(car_brands))][[0, 1, 2, 3]]

    print("Table 1:")
    print(table1)

    # Read file2.csv with encoding latin-1, delimiter ';', and no header
    file2 = pd.read_csv('pojazdy.csv', encoding='latin-1', delimiter=';', header=None, dtype=str)

    # Filter file2 to only include rows where column 0 is in car_brands
    table2 = file2[(file2.iloc[:, 2].isin(car_brands))][[2, 3, 4, 7]]

    print("Table 2:")
    print(table2)

    # Find rows in table2 that are not in table1
    tableDiff = table2[~table2.apply(tuple, 1).isin(table1.apply(tuple, 1))]

    print("Table Diff:")
    print(tableDiff)

    # Export tableDiff to a CSV file with the current date and time, separated by ';'
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    tableDiff.to_csv(f"tableDiff_{current_datetime}.csv", index=False, header=False, sep=';')

except FileNotFoundError as e:
    print(f"Error: File not found - {e.filename}")
except pd.errors.EmptyDataError as e:
    print(f"Error: Empty data - {e}")
except pd.errors.ParserError as e:
    print(f"Error: Parser error - {e}")
except Exception as e:
    print(f"Error: {e}")