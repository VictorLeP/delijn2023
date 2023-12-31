class Bus:
    def __init__(self, bus: str, type: str):
        self.bus = bus
        self.type = type
        assert self.type in bus_type_sizes, "Invalid type!"

    def __repr__(self):
        return f"Bus(bus={self.bus}, type={self.type})"


bus_type_sizes = {
    "GROOT": 4,
    "NORMAAL": 2,
    "MINI": 1
}


class Garage:
    def __init__(self):

        self.garage_spots = {  # (size, count)
            "groot": (4, 4),
            "medium": (2, 6),
            "klein": (1, 10)
        }

        self.remaining_garage_slots = {
            k: v[0] * v[1] for k, v in self.garage_spots.items()
        }

        self.garage_allocations = {k: [] for k in self.garage_spots.keys()}


    def __repr__(self):
        return f"Garage(groot={self.groot}, medium={self.medium}, klein={self.klein})"

    def retrieve_garage_spots(self):
        return {k: {"size": v[0], "count": v[1]} for k, v in self.garage_spots.items()}

class Stelplaats:
    def __init__(self, naam: str, garage: Garage):
        self.naam = naam
        self.garage = garage

        self.unallocated_buses = []


    def __repr__(self):
        return f"Stelplaats(naam={self.naam},  garage={self.garage})"

    def get_bus_type_sizes(self):
        return bus_type_sizes

    def get_garage_spots(self):
        return self.garage.garage_spots

    def get_bus_type_size(self, bus_type):
        return bus_type_sizes[bus_type]

    def get_garage_spot(self, garage_spot_name):
        return self.garage.garage_spots[garage_spot_name]
