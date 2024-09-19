import csv
import json
import os

CSV_FILE_PATH = 'zones/zones.csv'

def read_zones():
    if not os.path.exists(CSV_FILE_PATH):
        return []
    with open(CSV_FILE_PATH, 'r') as file:
        zones = []
        reader = csv.DictReader(file)
        # Convert points from string to list
        for row in reader:
            row['points'] = json.loads(row['points'])  
            zones.append(row)
        return zones

def write_zones(zones):
    with open(CSV_FILE_PATH, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'name', 'points'])
        writer.writeheader()
        writer.writerows(zones)

def delete_zone(zone_id):
    zones = read_zones()
    zones = [zone for zone in zones if zone['id'] != str(zone_id)]
    write_zones(zones)

def create_zone(name, points):
    zones = read_zones()
    zone_id = str(max([int(zone['id']) for zone in zones], default=0) + 1)
    new_zone = {'id': zone_id, 'name': name, 'points': points}
    zones.append(new_zone)
    write_zones(zones)
    return new_zone
