import json
import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


data = json.loads(input())
# logging.debug(data)

STOP_TYPE = 'stop_type'
# logging.debug(all_keys)

data_types = {'bus_id': int,
              'stop_id': int,
              'stop_name': str,
              'next_stop': int,
              'stop_type': str,
              'a_time': str}
all_keys = list(data_types.keys())
required_keys = [all_keys[i] for i in [0, 1, 2, 3, 5]]

# logging.debug(repr(data_types))

errors = {key: 0 for key in all_keys}
# logging.debug(errors)

# logging.debug(type(data[1]['stop_type']))

for data_item in data:
    for key in all_keys:
        if type(data_item[key]) != data_types[key] \
                or key in required_keys and data_item[key] == "" \
                or key not in required_keys and len(data_item[STOP_TYPE]) > 1:
            errors[key] += 1

errors_total = sum(errors.values())

print(f'Type and required field validation: {errors_total} errors')
for error, value in errors.items():
    print(f"{error}: {value}")
