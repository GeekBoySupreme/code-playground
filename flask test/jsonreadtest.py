import json

def writefile(data,name,website,place):
    data['people'].append({
    'name': name,
    'website': website,
    'from': place
    })

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

def loadfile(name1,website1,place1):
    with open('data.json') as json_file:
        data = json.load(json_file)
        name=name1
        website=website1
        place=place1

        writefile(data,name,website,place)

        for p in data['people']:
            print('Name: ' + p['name'])
            print('Website: ' + p['website'])
            print('From: ' + p['from'])
            print('')

