import json

filename = 'data.json'
with open(filename) as f:
    pop_data = json.load(f)

    for value in pop_data:
        # if (pop_data['day'] == "1.26"):
        area = value['area']
        country = value['country']
        confirm = value['confirm']
        if area: print(area + ": " + str(confirm) + " confirm cases.")
        else: print(country + ": " + str(confirm) + " confirm cases.")