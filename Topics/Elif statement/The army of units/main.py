army = int(input())
label = None

if army < 1:
    label = "no army"
elif army < 10:
    label = "few"
elif army < 50:
    label = "pack"
elif army < 500:
    label = "horde"
elif army < 1000:
    label = "swarm"
else:
    label = "legion"

print(label)
