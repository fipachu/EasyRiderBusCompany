# TODO: put all the stages in easyrider.py at once
# def will need to redo the whole thing using functional or OOP
# stage 6 even uses code from stage 4!
import itertools
import json
import logging
import sys


logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

data = json.loads(input())
lines = {}
# lines = {line_1:
#                  {'all_stops': set(),
#                   'start_stops': set(),
#                   # 'transfer_stops': set(),
#                   'finish_stops': set()
#                  },
#          line_2:
#                  {'all_stops': set(),
#                   'start_stops': set(),
#                   # 'transfer_stops': set(),
#                   'finish_stops': set()
#                  }...
#          }
# maybe get to counting special stops in the same loop
# that scans for bus lines?
# but then what if input data alternates bus lines?
start_stops = set()
transfer_stops = set()
finish_stops = set()
demand_stops = set()

# scan for bus lines and put their stops names in dict lines
for stop in data:
    # logging.debug(f" current stop: {stop}")
    line = stop['bus_id']
    # logging.debug(f"current line: {line}")
    if line not in lines:
        lines[line] = {'all_stops': set(),
                       # 'start_stops': set(),
                       # 'transfer_stops': set(),
                       # 'finish_stops': set()
                       }

    stop_name = stop['stop_name']

    lines[line]['all_stops'].add(stop_name)

    stop_type = stop['stop_type']
    # find all start, end, and on demand stops
    if stop_type == 'S':
        # lines[line]['start_stops'].add(stop_name)
        start_stops.add(stop_name)
    elif stop_type == 'F':
        # lines[line]['finish_stops'].add(stop_name)
        finish_stops.add(stop_name)
    elif stop_type == 'O':
        demand_stops.add(stop_name)

# for line, stops in lines.items():
#     # logging.debug(f'{line=}')
#     # logging.debug(f'{stops=}')
#     if len(stops['start_stops']) != 1 or len(stops['finish_stops']) != 1:
#         # print(f'There is no start or end stop for the line: {line}.')
#         print(f'Invalid number of start or end stops for the line: {line}.')
#         break
# else:

# find all transfer stops:
combos = list(itertools.combinations(lines, 2))
for line1, line2 in combos:
    transfer_stops.update(lines[line1]['all_stops'] & lines[line2]['all_stops'])

# find overlaps:
overlaps = (demand_stops & start_stops) |\
           (demand_stops & finish_stops) |\
           (demand_stops & transfer_stops)
overlaps = list(sorted(overlaps))
# logging.debug(f"{overlaps=}")


# hurray!
print('On demand stops test:')
if overlaps:
    print(f'Wrong stop type: {overlaps}')
else:
    print('OK')
