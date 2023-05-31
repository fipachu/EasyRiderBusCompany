import json
import logging
import sys

# this one's quick and dirty

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

data = json.loads(input())

lines = {}

for stop in data:
    line = stop['bus_id']
    # logging.debug(f"current line: {line}")
    if line not in lines:
        lines[line] = 1
    else:
        lines[line] += 1

# logging.debug(f"found lines: {lines}")
print("Line names and number of stops:")
for line in lines.items():
    print(f"bus_id: {line[0]}, stops: {line[1]}")
