import json
import scheduling

def read_input_file(filename):
    return json.load(open(filename, 'r'))

j = read_input_file('input_unsorted.json')

scheduling.allocate_bus_schedule(j)