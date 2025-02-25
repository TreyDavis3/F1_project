import csv, os

def read_csv_file(filepath):
    data = []
    try:
        with open(filepath, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found in {os.getcwd()}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    return data

def __main__():
    filepath = 'GP_winners.txt'
    data = read_csv_file(filepath)
    if data:
        country = input("Enter the country name: ")
        for row in data:
            if (country.lower() in row[0].lower()):
                print(f"{row[0]}: {row[1]} - {row[2]}")
        print("Done")


if __name__ == "__main__":
    __main__()
