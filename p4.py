import csv
import os


SPECIES_FILE = 'species.csv'
SIGHTINGS_FILE = 'sightings.csv'


def initialize_files():
    if not os.path.exists(SPECIES_FILE):
        with open(SPECIES_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Conservation Status", "Habitat"])
    
    if not os.path.exists(SIGHTINGS_FILE):
        with open(SIGHTINGS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Species Name", "Location", "Date", "Count"])


def add_species(name,status, habitat):
    with open(SPECIES_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, status, habitat])
    print(f"Species '{name}' added successfully!")


def remove_species(name):
    rows = []
    found = False
    with open(SPECIES_FILE, 'r') as file:
        reader = csv.reader(file)
        rows = [row for row in reader if row and row[0].lower() != name.lower()]
        found = any(row[0].lower() == name.lower() for row in reader)
    
    with open(SPECIES_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    if found:
        print(f"Species '{name}' not found!")
    else:
        print(f"Species '{name}' removed successfully!")


def update_species(name, new_status=None, new_habitat=None):
    rows = []
    updated = False
    with open(SPECIES_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0].lower() == name.lower():
                if new_status:
                    row[1] = new_status
                if new_habitat:
                    row[2] = new_habitat
                updated = True
            rows.append(row)
    
    with open(SPECIES_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    if updated:
        print(f"Species '{name}' updated successfully!")
    else:
        print(f"Species '{name}' not found!")


def add_sighting(species_name, location, date, count):
    with open(SIGHTINGS_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([species_name, location, date, count])
    print(f"Sighting of '{species_name}' added successfully!")


def view_species():
    with open(SPECIES_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def view_sightings():
    with open(SIGHTINGS_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def search_species(name):
    with open(SPECIES_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0].lower() == name.lower():
                print(f"Found: {row}")
                return
    print(f"Species '{name}' not found!")


def species_report(name):
    with open(SIGHTINGS_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0].lower() == name.lower():
                print(row)


def count_sightings(name):
    total = 0
    with open(SIGHTINGS_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0].lower() == name.lower():
                total += int(row[3])
    print(f"Total sightings of '{name}': {total}")


def delete_sighting(index):
    rows = []
    with open(SIGHTINGS_FILE, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    if 1 <= index < len(rows):
        print(f"Deleted sighting: {rows.pop(index)}")
    else:
        print("Invalid index!")
    
    with open(SIGHTINGS_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def main():
    initialize_files()
    while True:
        print("\n--- Wildlife Management System ---")
        print("1. Add Species")
        print("2. Remove Species")
        print("3. Update Species")
        print("4. Add Sighting")
        print("5. View Species")
        print("6. View Sightings")
        print("7. Search Species")
        print("8. Generate Species Report")
        print("9. Count Total Sightings")
        print("10. Delete Sighting")
        print("11. Exit")
        
        choice = input("Enter choice: ")
        if choice == '1':
            add_species(input("Name: "), input("Status: "), input("Habitat: "))
        elif choice == '2':
            remove_species(input("Name: "))
        elif choice == '3':
            update_species(input("Name: "), input("New Status (Leave blank to keep same): "), input("New Habitat (Leave blank to keep same): "))
        elif choice == '4':
            add_sighting(input("Species: "), input("Location: "), input("Date: "), input("Count: "))
        elif choice == '5':
            view_species()
        elif choice == '6':
            view_sightings()
        elif choice == '7':
            search_species(input("Name: "))
        elif choice == '8':
            species_report(input("Species: "))
        elif choice == '9':
            count_sightings(input("Species: "))
        elif choice == '10':
            delete_sighting(int(input("Index: ")))
        elif choice == '11':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
