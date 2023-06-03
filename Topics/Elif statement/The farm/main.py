# import sys

prices = {'sheep': 6769, 'cow': 3848, 'pig': 1296, 'goat': 678, 'chicken': 23}
budget = int(input())
# print(prices, file=sys.stderr)

# for item in prices:
#     print(item, file=sys.stderr)

# for animal, price in reversed(prices.items()):
#     print(animal, price, file=sys.stderr)

# solution = None
# for animal, price in prices.items():
#     count = budget // price
#     if count > 0:
#         solution = {'animal': animal, 'count': count}
#         break
#
# if not solution:
#     print(None)
# elif solution['count'] == 1:
#     print(f"1 {solution['animal']}")
# elif solution['count'] > 1:
#     if solution['animal'] == 'sheep':
#         print(f"{solution['count']} sheep")
#     else:
#         print(f"{solution['count']} {solution['animal']}s")

# output = None
if budget < prices['chicken']:
    print(None)
else:
    for animal, cost in prices.items():
        if budget >= cost:
            count = budget // cost
            # formatted_animal = animal + 's' * (count > 1) and (animal != 'sheep')
            suffix = 's' if count > 1 and animal != 'sheep' else ''
            # output = f"{count} {animal}{suffix}"
            print(f"{count} {animal}{suffix}")
            break
# else:
#     print(None)

