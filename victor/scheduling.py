
class Scheduler:

    def __init__(self):
        self.bus_type_sizes = {
            "GROOT": 4,
            "NORMAAL": 2,
            "MINI": 1
        }

        self.stelplaatsen = {}

        self.stelplaatsen["De Lijn Arsenaal"] = Stelplaats("De Lijn Arsenaal")


    def allocate_bus_schedule(self, j):
        stelplaats_name = j["stelplaats"]
        stelplaats = self.stelplaatsen[stelplaats_name]
        parking = j["parking"]

        garage_allocations = {k: [] for k in stelplaats.garage_spots.keys()}

        # Sort buses by size, to optimize garage allocation
        parking.sort(key=lambda x: self.bus_type_sizes[x["type"]], reverse=True)

        for bus in parking:
            allocated = False
            for garage_spot_name, garage_spot_definition in stelplaats.garage_spots.items():
                garage_spot_size, _ = garage_spot_definition
                # Check that bus could fit in garage spot
                if self.bus_type_sizes[bus["type"]] <= garage_spot_size:
                    # Check if there are still garage spots available
                    if stelplaats.remaining_garage_slots[garage_spot_name] > 0:
                        garage_allocations[garage_spot_name].append(bus)
                        stelplaats.remaining_garage_slots[garage_spot_name] -= self.bus_type_sizes[bus["type"]]
                        allocated = True
                        break
            if not allocated:
                raise ValueError("No garage spot available for bus: {}".format(bus))

        return garage_allocations

class Stelplaats:

    def __init__(self, name):
        self.name = name
        self.garage_spots = { # (size, count)
            "groot": (4, 4),
            "medium": (2, 6),
            "klein": (1, 10)
        }

        self.remaining_garage_slots = {
            k: v[0] * v[1] for k, v in self.garage_spots.items()
        }

    def get_bus_type_sizes(self):
        return self.bus_type_sizes
    
    def get_garage_spots(self):
        return self.garage_spots

    def get_bus_type_size(self, bus_type):
        return self.bus_type_sizes[bus_type]
    
    def get_garage_spot(self, garage_spot_name):
        return self.garage_spots[garage_spot_name]
