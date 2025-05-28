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

def Number_of_Wins(driver_name_query):
    # This function counts the number of wins for a given driver
    filepath = 'GP_winners.txt'
    data = read_csv_file(filepath)
    if data is None or len(data) <= 1: # Check for no data or only header
        # print("No data or only header found to count wins.") # Optional: more specific message
        return 0

    # The first row is the header, skip it for data processing.
    actual_data = data[1:]
    search_name_lower = driver_name_query.strip().lower()
    total_wins = 0

    for row in actual_data:
        if len(row) > 2: # Ensure 'Winner' column (index 2) exists
            winner_in_row = row[2].strip().lower()
            if search_name_lower in winner_in_row: # Check if the queried driver is part of the winner's name
                total_wins += 1
        # else:
            # print(f"Warning: Row with insufficient columns in Number_of_Wins: {row}") # Optional
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

    if not data or len(data) <= 1: # No data or only header
        print("No race data available from GP_winners.txt.")
        return

    car_query_input = input("Enter a Constructor: ").strip()
    if not car_query_input:
        print("No constructor name entered.")
        return

    car_query_lower = car_query_input.lower()
    
    # Using a dictionary to store drivers and their total wins to avoid redundant calls
    # and to easily sort/present later.
    # Key: driver name (original casing), Value: their total career wins
    drivers_for_constructor = {}
    constructor_total_wins = 0
    
    actual_data = data[1:] # Skip header row

    for row in actual_data:
        if len(row) > 3: # Need at least Grand Prix, Date, Winner, Car
            car_in_row = row[3].strip().lower()
            driver_name_from_file = row[2].strip()

            if car_query_lower in car_in_row:
                constructor_total_wins += 1
                if driver_name_from_file not in drivers_for_constructor:
                    drivers_for_constructor[driver_name_from_file] = Number_of_Wins(driver_name_from_file)

    print(f"\nTotal wins for constructor '{car_query_input.title()}': {constructor_total_wins}")
    if drivers_for_constructor:
        print(f"\nDrivers who won for '{car_query_input.title()}' (and their total career F1 wins):")
        print("---------------------------------------------------------------------")
        # Sort drivers alphabetically for consistent output
        for driver_name in sorted(drivers_for_constructor.keys()):
            print(f"Driver: {driver_name}, Total Career Wins: {drivers_for_constructor[driver_name]}")
        print("---------------------------------------------------------------------")
    else:
        print(f"No drivers found who won for constructor '{car_query_input.title()}'.")

def __main__():
    find_car_driver()
    #find_driver_car()
    #find_race()
    print("Done")


if __name__ == "__main__":
    __main__()
