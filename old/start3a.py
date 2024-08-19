import csv

def find_unique_rows(file1, file2):
    """
    Find rows from file1 that do not exist in file2 by comparing columns 1, 2, and 3.

    Args:
        file1 (str): Path to the first CSV file.
        file2 (str): Path to the second CSV file.

    Returns:
        A list of rows that exist only in file1.
    """
    with open(file1, 'r', encoding='latin-1') as f1, open(file2, 'r', encoding='latin-1') as f2:
        reader1 = csv.reader(f1)
        reader2 = csv.reader(f2)
        rows1 = [row for row in reader1]
        rows2 = [row for row in reader2]

    # Create a set of tuples from file2, containing columns 1, 2, and 3
    file2_set = set()
    for row in rows2:
        if len(row) >= 4:  # Check if row has at least 4 columns
            file2_set.add((row[1], row[2], row[3]))

    # Find unique rows in file1
    unique_rows = []
    for row in rows1:
        if len(row) >= 4:  # Check if row has at least 4 columns
            if (row[1], row[2], row[3]) not in file2_set:
                unique_rows.append(row)

    return unique_rows

def main():
    file1 = 'file2.csv'
    file2 = 'file1.csv'
    unique_rows = find_unique_rows(file1, file2)
    count = 0
    if unique_rows:
        print("The following rows exist only in file1:")
        for row in unique_rows:
            #print(row)
            count +=1
        print(count)
    else:
        print("No unique rows found in file1.")

if __name__ == '__main__':
    main()