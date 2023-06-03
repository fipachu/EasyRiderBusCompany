age = int(input())

print("Lion King" if age <= 16 else
      "Trainspotting" if age <= 25 else
      "Matrix" if age <= 40 else
      "Pulp Fiction" if age <= 60 else
      "Breakfast at Tiffany's")
