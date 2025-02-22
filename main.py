try:
    with open("GP_winners.txt", "r") as file:  # Open the file in read mode ('r')
        file_content = file.read()  # Read the entire file content
        print(file_content)
except FileNotFoundError:
    print("Error: File 'GP_winners.txt' not found.")
