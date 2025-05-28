import csv, os
from datetime import datetime

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

def Number_of_Wins(driver):
    # This function counts the number of wins for a given driver
    filepath = 'GP_winners.txt'
    data = read_csv_file(filepath)
    if data is None:
        print("No data found to count wins.")
        return 0
    driver = driver.lower() in row[2].lower() # This will be used to check if the driver name matches in the data
    total_wins = 0
    for row in data:
        if(driver.lower() in row[2].lower()):
            total_wins += 1
    return total_wins
    # This function returns the total number of wins for a given driver

def find_race():
    filepath = 'GP_winners.txt'
    data = read_csv_file(filepath)
    if data:
        country = input("Enter the country name: ")
        for row in data:
            if (country.lower() in row[0].lower()):
                print(f"{row[0]}: {row[1]} - {row[2]} - {row[3]}")

def find_driver_car():
    #TODO Possibly add a check to see if the driver has won in multiple cars and print each instance

    # Define the expected date format in your GP_winners.txt file.
    # Example: '%Y-%m-%d' for dates like '2023-03-05'.
    # Adjust this format string if your dates are different (e.g., '%d/%m/%Y' for '05/03/2023').
    DATE_FORMAT = '%Y-%m-%d'

    filepath = 'GP_winners.txt'
    data = read_csv_file(filepath)

    if not data:
        print("No data available from GP_winners.txt.")
        return

    driver_name_query = input("Enter driver name: ").strip().lower()
    if not driver_name_query:
        print("No driver name entered.")
        return

    driver_wins_list = []

    for row_index, row in enumerate(data):
        # Expecting at least 4 columns: Country/Event, Date, Driver, Car
        if len(row) < 4:
            # print(f"Warning: Row {row_index + 1} is malformed or has too few columns: {row}")
            continue

        race_date_str = row[1]
        driver_in_row = row[2].lower()
        car_in_row = row[3]
        original_driver_name_from_file = row[2] # Keep original casing for display

        if driver_name_query in driver_in_row:
            parsed_date_obj = None
            try:
                parsed_date_obj = datetime.strptime(race_date_str, DATE_FORMAT)
            except ValueError:
                print(f"Warning: Date '{race_date_str}' for driver '{original_driver_name_from_file}' (Car: {car_in_row}) "
                      f"could not be parsed with format '{DATE_FORMAT}'. This win may not be sorted chronologically.")
            
            driver_wins_list.append({
                'parsed_date_obj': parsed_date_obj, # This will be None if parsing failed
                'date_str': race_date_str,          # Original date string for display
                'car': car_in_row,
                'driver_name_from_file': original_driver_name_from_file
            })

    if not driver_wins_list:
        print(f"No wins found for a driver matching '{driver_name_query.title()}'.")
        return

    # Sort the list: wins with parseable dates first (oldest to newest), then unparseable dates (sorted by their string representation).
    driver_wins_list.sort(key=lambda win: (win['parsed_date_obj'] is None, win['parsed_date_obj'] if win['parsed_date_obj'] else win['date_str']))

    print(f"\nTotal wins for drivers matching '{driver_name_query.title()}': {len(driver_wins_list)}")
    if driver_wins_list:
        print("Wins are listed from oldest to newest (unparseable dates, if any, are listed after chronological wins):")
        print("----------------------------------------------------")
        for win in driver_wins_list:
            print(f"Driver: {win['driver_name_from_file']}, Car: {win['car']}, Date of Win: {win['date_str']}")
        print("----------------------------------------------------")

def find_car_driver():
    filepath = 'GP_winners.txt'
    data = read_csv_file(filepath)
    if data:
        car = input("Enter a Constructor: ")
        constructor = set()
        print(car)
        for row in data:
            if(car.lower() in row[3].lower()):
                car_info = f"Driver: {row[2]}, Total Wins: {Number_of_Wins}" #TODO add total number of wins for each driver
                constructor.add(car_info)
        car_wins = 0
        for row in data:
            if(car.lower() in row[3].lower()):
                car_wins += 1
        print(f"Total wins for {car}: {car_wins}")
        for car_drivers in constructor:
            print(car_drivers)

def __main__():
    #find_car_driver()
    find_driver_car()
    #find_race()
    print("Done")


if __name__ == "__main__":
    __main__()
