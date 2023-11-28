
import json
from pprint import pprint

def allocate_bus_schedule(j):
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

    garage_spots = { # (size, count)
        "groot": (4, 4),
        "medium": (2, 6),
        "klein": (1, 10)
    }

    garage_allocations = {k: [] for k in garage_spots.keys()}

    bus_type_counts = {k: 0 for k in bus_type_sizes.keys()}

    # Sort buses by size, to optimize garage allocation
    parking.sort(key=lambda x: bus_type_sizes[x["type"]], reverse=True)

    for bus in parking:
        bus_type_counts[bus["type"]] += 1 
        for garage_spot_name, garage_spot_definition in garage_spots.items():
            garage_spot_size, garage_spot_count = garage_spot_definition
            # Check that bus could fit in garage spot
            if bus_type_sizes[bus["type"]] <= garage_spot_size:
                # Check if there are still garage spots available
                if sum(
                    [bus_type_sizes[bus["type"]] for bus in garage_allocations[garage_spot_name]]
                    ) < (garage_spot_size * garage_spot_count):
                    garage_allocations[garage_spot_name].append(bus)
                    break
        raise ValueError("No garage spot available for bus: {}".format(bus))

    pprint(garage_allocations)

        # bus_type_sizes[


    # todo class BUS