import json
import logging
import sys
import re

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


data = json.loads(input())
# logging.debug(data)

data_types = {'bus_id': int,
              'stop_id': int,
              'stop_name': str,
              'next_stop': int,
              'stop_type': str,
              'a_time': str}
all_fields = list(data_types.keys())
formatted_fields = [all_fields[i] for i in [2, 4, 5]]
logging.debug(repr(formatted_fields))


# initialize errors with a zero for every field
errors = {field: 0 for field in formatted_fields}
logging.debug(errors)
# logging.debug(type(data[1]['stop_type']))

STOP_NAME = re.compile("^([A-Z][a-z]+ )+(Road|Avenue|Boulevard|Street)$")
STOP_TYPE = re.compile("^[SOF]?$")
A_TIME = re.compile("^([0-1][0-9]|2[0-3]):([0-5][0-9])$")

formats = dict(zip(formatted_fields, [STOP_NAME, STOP_TYPE, A_TIME]))
logging.debug(formats)

for item in data:
    for field in formatted_fields:
        if not re.match(formats[field], item[field]):
            errors[field] += 1
            logging.debug(f'error in {field}: {item[field]}')

errors_total = sum(errors.values())

print(f'Format validation: {errors_total} errors')
for field, value in errors.items():
    print(f"{field}: {value}")
