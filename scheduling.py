
import json
from pprint import pprint


def read_input_file(filename):
    return json.load(open(filename, 'r'))

j = read_input_file('input.json')
stelplaats = j["stelplaats"]
parking = j["parking"]
garage = j["garage"]

# Map incompatibiliteit 
bus_type_to_garage_spot_mapping = {
    "GROOT": "groot",
    "NORMAAL": "medium",
    "MINI": "klein"
}

bus_type_sizes = {
    "GROOT": 4,
    "NORMAAL": 2,
    "MINI": 1
}

garage_spot_sizes = {
    "groot": {"GROOT": 1, "NORMAAL": 1/2, "MINI": 1/4},
    "medium": {"NORMAAL": 1, "MINI": 1/2},
    "klein": {"MINI": 1}
}

garage_nb_spots = {
    "groot": 4,
    "medium": 6,
    "klein": 10
}



garage_allocations = {k: [] for k in garage_nb_spots.keys()}

bus_type_counts = {k: 0 for k in bus_type_sizes.keys()}

for bus in parking:
    bus_type_counts[bus["type"]] += 1 
    for garage_spot_size, compatibility_mapping in garage_spot_sizes.items():
        # Bus can fit in garage spot 
        if compatibility_mapping.get(bus["type"], 0) > 0:
            # there are still garage spots available
            if len(garage_allocations[garage_spot_size]) < garage_nb_spots[garage_spot_size]:
                garage_allocations[garage_spot_size].append(bus)

pprint(garage_allocations)

    # bus_type_sizes[


# todo class BUS