import json
from pprint import pprint
import scheduling

def read_input_file(filename):
    return json.load(open(filename, 'r'))

schedulers = {}

j = read_input_file('victor/input_unsorted.json')


s = scheduling.Scheduler()
t = s.allocate_bus_schedule(j)

pprint(t)