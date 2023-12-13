#receives values of key pairs, where each key is associated with a value
capitals = {
    'USA': "Washington DC", 'India': "New Dehli", 'China': "Beijing", 'Russia': "Moscow"
}
#print(capitals.get("Germany"))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())
capitals.update({"Rwanda": "Kigali", "Burundi": 'Bujumbura', "uganda": 'Kampala'})
#You can update your dictionary by adding new elements
capitals.update({"India": 'Indianna'})
#You can also update your dictionary by altering the value of a key
capitals.pop("Rwanda")
#capitals.clear()
for key, value in capitals.items():
    print(key, value)