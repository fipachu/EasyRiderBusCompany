# TODO: put all the stages in easyrider.py at once
#       prolly will need to redo the whole thing using functional or OOP
import json
# import logging
# import sys

# logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


data = json.loads(input())
errors = []

previous_id = data[0]["bus_id"]  # why preprocess if can not preprocess
previous_time = -1
for stop in data:
    if stop["bus_id"] in [error[0] for error in errors]:  # if stop in bad line go to next stop
        continue
    if stop["bus_id"] != previous_id:  # if new line reset previous_time
        previous_id = stop["bus_id"]
        previous_time = -1
    if int(stop['a_time'].replace(':', '')) <= previous_time:  # if time bad, save error
        errors.append((stop["bus_id"], stop["stop_name"]))
        # you could print the error here already, for worse readability!
        # print(f'bus_id line {stop["bus_id"]}: wrong time on station {stop["stop_name"]}')
        continue
    previous_time = int(stop['a_time'].replace(':', ''))

print('Arrival time test:')
if not errors:
    print('OK')
else:
    for line, station in errors:
        print(f'bus_id line {line}: wrong time on station {station}')
