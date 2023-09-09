import itertools
import json
import logging
import sys

# this one's quick and dirty


good_data = [
    {"bus_id": 128, "stop_id": 1, "stop_name": "ProspektAvenue", "next_stop": 3, "stop_type": "S", "a_time": "08:12"},
    {"bus_id": 128, "stop_id": 3, "stop_name": "ElmStreet", "next_stop": 5, "stop_type": "", "a_time": "08:19"},
    {"bus_id": 128, "stop_id": 5, "stop_name": "FifthAvenue", "next_stop": 7, "stop_type": "O", "a_time": "08:25"},
    {"bus_id": 128, "stop_id": 7, "stop_name": "SesameStreet", "next_stop": 0, "stop_type": "F", "a_time": "08:37"},
    {"bus_id": 256, "stop_id": 2, "stop_name": "PilotowStreet", "next_stop": 3, "stop_type": "S", "a_time": "09:20"},
    {"bus_id": 256, "stop_id": 3, "stop_name": "ElmStreet", "next_stop": 6, "stop_type": "", "a_time": "09:45"},
    {"bus_id": 256, "stop_id": 6, "stop_name": "SunsetBoulevard", "next_stop": 7, "stop_type": "", "a_time": "09:59"},
    {"bus_id": 256, "stop_id": 7, "stop_name": "SesameStreet", "next_stop": 0, "stop_type": "F", "a_time": "10:12"},
    {"bus_id": 512, "stop_id": 4, "stop_name": "BourbonStreet", "next_stop": 6, "stop_type": "S", "a_time": "08:13"},
    {"bus_id": 512, "stop_id": 6, "stop_name": "SunsetBoulevard", "next_stop": 0, "stop_type": "F", "a_time": "08:16"}]

bad_data = [
    {"bus_id": 128, "stop_id": 1, "stop_name": "ProspektAvenue", "next_stop": 3, "stop_type": "S", "a_time": "08:12"},
    {"bus_id": 128, "stop_id": 3, "stop_name": "ElmStreet", "next_stop": 5, "stop_type": "", "a_time": "08:19"},
    {"bus_id": 128, "stop_id": 5, "stop_name": "FifthAvenue", "next_stop": 7, "stop_type": "O", "a_time": "08:25"},
    {"bus_id": 128, "stop_id": 7, "stop_name": "SesameStreet", "next_stop": 0, "stop_type": "F", "a_time": "08:37"},
    {"bus_id": 512, "stop_id": 4, "stop_name": "BourbonStreet", "next_stop": 6, "stop_type": "", "a_time": "08:13"},
    {"bus_id": 512, "stop_id": 6, "stop_name": "SunsetBoulevard", "next_stop": 0, "stop_type": "F", "a_time": "08:16"}]

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

data = json.loads(input())

# lines = {line_1:
#                  {'start_stops': []
#                   'transfer_stops': []
#                   'finish_stops': []
#                  }
#          line_2:
#                  {'start_stops': []
#                   'transfer_stops': []
#                   'finish_stops': []
#                  }...
#         }
# todo: think of something better
# maybe get to counting special stops in the same loop
# that scans for bus lines?
# but then what if input data alternates bus lines?

start_stops = set()
transfer_stops = set()
finish_stops = set()

# scans for bus lines and puts their stops in a dictionary

lines = {}
for stop in data:
    # logging.debug(f" current stop: {stop}")

    line = stop['bus_id']
    # logging.debug(f"current line: {line}")
    if line not in lines:
        lines[line] = {'all_stops': set(),
                       'start_stops': set(),
                       'transfer_stops': set(),
                       'finish_stops': set()
                       }

    stop_name = stop['stop_name']

    lines[line]['all_stops'].add(stop_name)

    stop_type = stop['stop_type']
    if stop_type == 'S':
        lines[line]['start_stops'].add(stop_name)
        start_stops.add(stop_name)
    elif stop_type == 'F':
        lines[line]['finish_stops'].add(stop_name)
        finish_stops.add(stop_name)

for line, stops in lines.items():
    logging.debug(f'{line=}')
    logging.debug(f'{stops=}')
    if len(stops['start_stops']) != 1 or len(stops['finish_stops']) != 1:
        # print(f'There is no start or end stop for the line: {line}.')
        print(f'Wrong number of start or end stops for the line: {line}.')

        exit()

combos = list(itertools.combinations(lines, 2))
for line1, line2 in combos:
    transfer_stops.update(lines[line1]['all_stops'] & lines[line2]['all_stops'])

print(f'Start stops: {len(start_stops)} {sorted(start_stops)}')
print(f'Transfer stops: {len(transfer_stops)} {sorted(transfer_stops)}')
print(f'Finish stops: {len(finish_stops)} {sorted(finish_stops)}')

# logging.debug(" found lines: ")
# for line, stops in lines.items():
#     logging.debug(f' {line}')

# ugly idea:
# for line, stops in lines.items():
#     for stop in stops:
#         if stop['stop_type'] == 's':
#             pass

# print("Line names and number of stops:")
# for line, stops in lines.items():
#     # logging.debug(line)
#     print(f"bus_id: {line}, stops: {stops}")
