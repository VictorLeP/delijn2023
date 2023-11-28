class Bus:
    def __init__(self, bus: str, type: str):
        self.bus = bus
        self.type = type
        assert self.type in ["GROOT", "NORMAAL", "MINI"], "Invalid type!"

    def __repr__(self):
        return f"Bus(bus={self.bus}, type={self.type})"


bus_type_sizes = {
    "GROOT": 4,
    "NORMAAL": 2,
    "MINI": 1
}


class Garage:
    def __init__(self, groot: list[Bus], medium: list[Bus], klein: list[Bus]):
        self.groot = groot
        self.medium = medium
        self.klein = klein


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

class Stelplaats:
    def __init__(self, naam: str, parking: list, garage: Garage):
        self.naam = naam
        self.parking = parking
        self.garage = garage

        self.unallocated_buses = []


    def __repr__(self):
        return f"Stelplaats(naam={self.naam}, parking={self.parking}, garage={self.garage})"

    def get_bus_type_sizes(self):
        return bus_type_sizes

    def get_garage_spots(self):
        return self.garage.garage_spots

    def get_bus_type_size(self, bus_type):
        return bus_type_sizes[bus_type]

    def get_garage_spot(self, garage_spot_name):
        return self.garage.garage_spots[garage_spot_name]
