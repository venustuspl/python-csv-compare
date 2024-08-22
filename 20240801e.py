import pandas as pd
import datetime

try:
    print(f"Program started at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Get current year and last year
    current_year = datetime.date.today().year
    print(f"Current year value: {current_year}")
    last_year = current_year - 1
    print(f"Last year value: {last_year}")

    # Define the list of car brands
    car_brands = ['KIA', 'Jaguar', 'Land Rover', 'Ford', 'Hyundai', 'MG']
    print(f"Selected car brands: {', '.join(car_brands)}")

    # Read rv_config_IE_new.csv with encoding latin-1, delimiter ';', and no header
    file1 = pd.read_csv('rv_config_IE_new.csv', encoding='latin-1', delimiter=';', header=None, dtype=str)

    # Filter file1 to only include rows where column 0 is in car_brands
    table1 = file1[(file1.iloc[:, 0].isin(car_brands))][[0, 1, 2, 3]]

    print(f"Program selected: {len(table1)} rows from file rv_config_IE_new.csv")

    # Read pojazdy.csv with encoding latin-1, delimiter ';', and no header
    file2 = pd.read_csv('pojazdy.csv', encoding='latin-1', delimiter=';', header=None, dtype=str)

    # Filter file2 to only include rows where column 2 is in car_brands and column 11 is empty or equal to last_year or equal to current_year
    table2 = file2[(file2.iloc[:, 2].isin(car_brands)) & ((file2.iloc[:, 11].isna()) | (file2.iloc[:, 11] == str(last_year)) | (file2.iloc[:, 11] == str(current_year)))][[2, 3, 4, 7]]

    print(f"Program selected: {len(table2)} rows from file pojazdy.csv")

    # Find rows in table2 that are not in table1
    filesDiff = table2[~table2.apply(tuple, 1).isin(table1.apply(tuple, 1))]

    # Export filesDiff to a CSV file with the current date and time, separated by ';'
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filesDiff.to_csv(f"filesDiff_{current_datetime}.csv", index=False, header=False, sep=';')

    # Check for duplicates in file1 and export to a CSV file
    table3 = file1[file1.duplicated()]
    print(f"Program found: {len(table3)} duplicates in file rv_config_IE_new.csv")
    table3.to_csv(f"rvDuplicates_{current_datetime}.csv", index=False, header=False, sep=';')

except FileNotFoundError as e:
    print(f"Error: File not found - {e.filename}")
except pd.errors.EmptyDataError as e:
    print(f"Error: Empty data - {e}")
except pd.errors.ParserError as e:
    print(f"Error: Parser error - {e}")
except Exception as e:
    print(f"Error: {e}")

print(f"Program ended at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")