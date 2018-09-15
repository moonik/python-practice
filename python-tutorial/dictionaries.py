super_villains = {"Fiddler": "Isaac Bowin",
                  "Captain Cold": "Leonard Snart"}

print(super_villains["Fiddler"])
del super_villains["Fiddler"]

super_villains["Captain Cold"] = "Cortney Kox"

print(super_villains.get("Captain Cold"))

super_villains.keys()
super_villains.values()
