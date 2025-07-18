import csv
import os
from datetime import datetime

def read_csv_file(filepath):
    """Reads a CSV file and returns its content as a list of dictionaries."""
    data = []
    try:
        with open(filepath, 'r', newline='', encoding='utf-8') as file:
            # Use DictReader to treat each row as a dictionary.
            # This automatically uses the first row as keys.
            reader = csv.DictReader(file)
            # Clean up header names (e.g., "  Car " -> "car") for easy access
            reader.fieldnames = [name.strip().lower() for name in reader.fieldnames]
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found in {os.getcwd()}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    return data

def Number_of_Wins(driver_name_query, data):
    """
    Counts the number of wins for a given driver.
    Assumes 'data' is a list of dictionaries from read_csv_file.
    """
    if not data:
        return 0

    actual_data = data[1:]
    search_name_lower = driver_name_query.strip().lower()
    total_wins = 0

    for row in data:
        winner_in_row = row.get('winner', '').strip().lower()
        if search_name_lower in winner_in_row:
            total_wins += 1
    return total_wins

def find_race(data):
    """Finds race details by country/event name and prints the total count."""
    if not data:
        print("No race data available.")
        return

    country_query = input("Enter the country name: ").strip()
    if not country_query:
        print("No country name entered.")
        return

    matching_races = [
        row for row in data if country_query.lower() in row.get('grand prix', '').lower()
    ]

    display_name = country_query.title()
    if matching_races:
        display_name = matching_races[0].get('grand prix', display_name)

        print(f"\nFound {len(matching_races)} race(s) for '{display_name}':")
        print("----------------------------------------------------")
        for row in matching_races:
            print(f"{row.get('grand prix', 'N/A')}: {row.get('date', 'N/A')} - Winner: {row.get('winner', 'N/A')} - Car: {row.get('car', 'N/A')}")
        print("----------------------------------------------------")
    else:
        print(f"No race found for '{display_name}'.")

    print(f"Total races found for {display_name}: {len(matching_races)}")

def find_driver_car(data):
    # Define the expected date format in your GP_winners.txt file.
    # Example: '%Y-%m-%d' for dates like '2023-03-05'.
    # Adjust this format string if your dates are different (e.g., '%d/%m/%Y' for '05/03/2023').
    DATE_FORMAT = '%Y-%m-%d'

    if not data:
        print("No data available from GP_winners.txt.")
        return

    driver_name_query = input("Enter driver name: ").strip().lower()
    if not driver_name_query:
        print("No driver name entered.")
        return

    driver_wins_list = []

    for row in data:
        race_date_str = row.get('date', '')
        driver_in_row = row.get('winner', '').lower()
        car_in_row = row.get('car', '')
        original_driver_name_from_file = row.get('winner', '') # Keep original casing for display

        if driver_name_query in driver_in_row:
            parsed_date_obj = None
            try:
                parsed_date_obj = datetime.strptime(race_date_str, DATE_FORMAT)
            except ValueError:
                print(f"Warning: Date '{race_date_str}' for driver '{original_driver_name_from_file}' (Car: {car_in_row}) "
                      f"could not be parsed with format '{DATE_FORMAT}'. This win may not be sorted chronologically.")
            
            driver_wins_list.append({
                'parsed_date_obj': parsed_date_obj,
                'date_str': race_date_str,
                'car': car_in_row,
                'driver_name_from_file': original_driver_name_from_file
            })

    if not driver_wins_list:
        print(f"No wins found for a driver matching '{driver_name_query.title()}'.")
        return

    driver_wins_list.sort(key=lambda win: (win['parsed_date_obj'] is None, win['parsed_date_obj'] if win['parsed_date_obj'] else win['date_str']))


    if driver_wins_list:
        print("Wins are listed from oldest to newest (unparseable dates, if any, are listed after chronological wins):")
        print("----------------------------------------------------")
        for win in driver_wins_list:
            print(f"Driver: {win['driver_name_from_file']}, Car: {win['car']}, Date of Win: {win['date_str']}")
        print("----------------------------------------------------")

    print(f"Total wins for {win['driver_name_from_file']}: {len(driver_wins_list)}")

def find_car_driver(data):

    if not data:
        print("No race data available from GP_winners.txt.")
        return

    print("Ensure you enter the constructor name exactly as it appears in the GP_winners.txt file, not case senstive.")

    car_query_input = input("Enter a Constructor: ").strip()
    if not car_query_input:
        print("No constructor name entered.")
        return

    car_query_lower = car_query_input.lower()
    
    drivers_for_constructor = {}
    constructor_total_wins = 0
    
    for row in data:
        car_in_row = row.get('car', '').strip().lower()
        driver_name_from_file = row.get('winner', '').strip()

        if car_query_lower in car_in_row:
            constructor_total_wins += 1
            if driver_name_from_file and driver_name_from_file not in drivers_for_constructor:
                drivers_for_constructor[driver_name_from_file] = Number_of_Wins(driver_name_from_file, data)

   
    if drivers_for_constructor:
        print(f"\nDrivers who won for '{car_query_input.title()}' (and their total career F1 wins):")
        print("---------------------------------------------------------------------")
        for driver_name in sorted(drivers_for_constructor.keys()):
            print(f"Driver: {driver_name}, Total Career Wins: {drivers_for_constructor[driver_name]}")
        print("---------------------------------------------------------------------")
    else:
        print(f"No drivers found who won for constructor '{car_query_input.title()}'.")

    print(f"\nTotal wins for constructor '{car_query_input.title()}': {constructor_total_wins}")

def __main__():
    filepath = 'GP_winners.txt'
    race_data = read_csv_file(filepath)
    if not race_data:
        print("Exiting program because data could not be loaded.")
        return 
    #find_car_driver(race_data)
    #find_driver_car(race_data)
    find_race(race_data)
    print("Done")


if __name__ == "__main__":
    __main__()