F1 Grand Prix Winners Analysis Tool
This Python script allows you to explore historical Formula 1 Grand Prix winner data from a CSV file. You can search for races by country, find a driver's wins sorted by date, or list drivers who have won with a specific car constructor.

Features
Search Races by Country/Grand Prix: Find all races associated with a given country or Grand Prix name.

Driver Wins by Date: Get a list of a specific driver's wins, including the car and date, sorted chronologically.

Drivers by Constructor: List all drivers who have won races with a particular car constructor, along with their total career F1 wins.

Getting Started
Prerequisites
You'll need Python 3 installed on your system.

Installation
Clone the repository (or download the script):

Bash

git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
(Replace YOUR_USERNAME and YOUR_REPO_NAME with your actual GitHub details if this is a real repository.)

Ensure you have your data file:
This script expects a CSV file named GP_winners.txt (or .csv) in the same directory as the script. The CSV must have the following headers (case-insensitive, whitespace will be trimmed):

Grand Prix

Date (format must match YYYY-MM-DD, e.g., 2023-03-05)

Winner

Car

Example GP_winners.txt content:

Grand Prix,Date,Winner,Car
Bahrain Grand Prix,2023-03-05,Max Verstappen,Red Bull
Saudi Arabian Grand Prix,2023-03-19,Sergio Pérez,Red Bull
Australian Grand Prix,2023-04-02,Max Verstappen,Red Bull
Azerbaijan Grand Prix,2023-04-30,Sergio Pérez,Red Bull
Monaco Grand Prix,2023-05-28,Max Verstappen,Red Bull
Spanish Grand Prix,2023-06-04,Lewis Hamilton,Mercedes
Canadian Grand Prix,2023-06-18,Max Verstappen,Red Bull
British Grand Prix,2023-07-09,Lewis Hamilton,Mercedes
Usage
Run the script from your terminal:

Bash

python F1_project.py

Follow the prompts in the terminal to enter driver names, country names, or constructor names.

Code Structure
read_csv_file(filepath): A utility function to read the CSV data into a list of dictionaries, cleaning header names for easier access.

Number_of_Wins(driver_name_query, data): Counts total career wins for a given driver within the dataset.

find_race(data): Prompts for a country/Grand Prix and lists matching races.

find_driver_car(data): Prompts for a driver name and lists their wins, sorted by date.

find_car_driver(data): Prompts for a car constructor and lists drivers who won with it, along with their career win counts.

__main__(): The entry point of the script, responsible for loading data and calling the desired analysis function.
