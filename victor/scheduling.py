from victor.classes import Stelplaats, Garage


class Scheduler:

    def __init__(self):
        self.stelplaatsen = {}

        self.stelplaatsen["De Lijn Arsenaal"] = Stelplaats("De Lijn Arsenaal",
                                                            parking=[],
                                                           garage=Garage(groot=4, medium=2, klein=1)
                                                           )


    def allocate_bus_schedule(self, j):
        stelplaats_name = j["stelplaats"]
        stelplaats = self.stelplaatsen[stelplaats_name]
        parking = j["parking"]

        garage_allocations = stelplaats.garage.garage_allocations

        # Sort buses by size, to optimize garage allocation
        parking.sort(key=lambda x: stelplaats.get_bus_type_sizes()[x["type"]], reverse=True)

        unallocated_buses = stelplaats.unallocated_buses

        for bus in parking:
            allocated = False
            for garage_spot_name, garage_spot_definition in stelplaats.get_garage_spots().items():
                garage_spot_size, _ = garage_spot_definition
                # Check that bus could fit in garage spot
                if stelplaats.get_bus_type_sizes()[bus["type"]] <= garage_spot_size:
                    # Check if there are still garage spots available
                    if stelplaats.garage.remaining_garage_slots[garage_spot_name] > 0:
                        garage_allocations[garage_spot_name].append(bus)
                        stelplaats.garage.remaining_garage_slots[garage_spot_name] -= stelplaats.get_bus_type_sizes()[bus["type"]]
                        allocated = True
                        break
            if not allocated:
                unallocated_buses.append(bus)

        # return garage_allocations
