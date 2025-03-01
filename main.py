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

def find_race():
    filepath = 'GP_winners.txt'
    data = read_csv_file(filepath)
    if data:
        country = input("Enter the country name: ")
        for row in data:
            if (country.lower() in row[0].lower()):
                print(f"{row[0]}: {row[1]} - {row[2]} - {row[3]}")

def find_driver_car():
    filepath = 'GP_winners.txt'
    data = read_csv_file(filepath)
    if data:
        driver = input("Enter driver name: ")
        single_driver = set()
        for row in data:
            if (driver.lower () in row[2].lower()):
                driver_info = f"Car: {row[3]}, Date of Win: {row[1]}"
                single_driver.add(driver_info)
        for driver_results in single_driver:
            print(driver)
            print(driver_results)

def __main__():
    find_driver_car()
    #find_race()
    print("Done")


if __name__ == "__main__":
    __main__()
