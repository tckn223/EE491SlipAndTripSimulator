import numpy as np
import csv
import shutil

# Read csv file and format into dictionary structure

# Custom Simulation dictionary struture:
#   Key: Name of simulation
#   Value: Dictionary that stores the distance, duration, speed, and acceleration
#   of the simulation
custom_simulation_path = 'Data/Custom Simulation.csv'
custom_simulation_copy = 'Backup/Custom Simulation.csv'
custom_simulation = {}
custom_simulation_headers = []

def load_database():
    # Load custom simulations
    with open(custom_simulation_path, encoding = 'utf-8-sig') as custom_simulation_file:
        csv_reader = csv.reader(custom_simulation_file, delimiter = ',')
        # Extract headers
        global custom_simulation_headers
        custom_simulation_headers = next(csv_reader)
        for row in csv_reader:
            # First column of .csv will always be the simulation name
            name = ''
            for header, datum in zip(custom_simulation_headers, row):
                if (header == 'Name'):
                    # Create subdictionary
                    name = datum
                    custom_simulation[name] = {}
                else:
                    # Populate subdictionary
                    custom_simulation[name][header] = datum

def write_to_database():
    # Create backup file
    shutil.copyfile(custom_simulation_path, custom_simulation_copy)
    # Write to custom simulations
    with open(custom_simulation_path, mode = 'w', newline = '') as output_custom_simulation:
        csv_writer = csv.writer(output_custom_simulation, delimiter = ',')
        # Write headers
        csv_writer.writerow(custom_simulation_headers)
        for simulation in list(custom_simulation.keys()):
            # First column of .csv will always be the simulation name
            name = ''
            # Create a list for each row of the output .csv file
            row = []
            for header in custom_simulation_headers:
                if (header == 'Name'):
                    name = simulation
                    row.append(name)
                else:
                    row.append(custom_simulation[name][header])
            csv_writer.writerow(row)
