import json
import sys
total_born_overseas = 0
total_population = 0
file_name = sys.argv[1]
with open(file_name,"r") as f:
    data = json.load(f)

    for row in data["features"]:
        total_born_overseas += row["properties"]["total_migration"]
        total_population += row["properties"]["mig_pop_total"]

print("TBO",total_born_overseas)
print("TP", total_population)
