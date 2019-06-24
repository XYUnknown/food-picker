import requests
import json
import random

def get_location():
    postcode = input("please provide your UK postcode meow: ")
    url = 'https://api.postcodes.io/postcodes/' + postcode.strip()
    response = requests.get(url)
    data = json.loads(response.content)
    if (data['status'] != 200):
        print("meow... no location information for postcode " + postcode.strip())
        exit(1)
    else:
        result = data['result']
        long = result['longitude']
        lat = result['latitude']
        return long, lat

# Zomato api request headers
headers = {'Accept': 'application/json', 'user-key': 'd59eb41c133145c5eb9252e1b831eb89'}
# user location base on uk postcode
long, lat = get_location()
print('your location meow: ')
print('longitude: ' + str(long) + ' latitude: ' + str(lat))

def parse_response(url):
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        exit(1)
    else:
        data = json.loads(response.content)
        return data

def get_cuisines():
    url = 'https://developers.zomato.com/api/v2.1/cuisines?lat=' + str(lat) + '&lon=' + str(long)
    data = parse_response(url)
    for cuisine in data['cuisines']:
        print(cuisine['cuisine']['cuisine_name'] + ': ' + str(cuisine['cuisine']['cuisine_id']))

def get_restaurants(cuisine_id):
    url = 'https://developers.zomato.com/api/v2.1/search?count=10&lat=55.865674&lon=-4.288961&cuisines='+ str(cuisine_id) + '&sort=real_distance'
    data = parse_response(url)
    list = []
    for r in data['restaurants']:
        restaurant = {'name': r['restaurant']['name'], 'address': r['restaurant']['location']['address'], 'rating': r['restaurant']['user_rating']['aggregate_rating']}
        list.append(restaurant)
    if len(list) == 0:
        print('meow.. no restaurant found...')
        return
    index = random.randint(0, len(list)-1)
    choice = list[index]
    print('the chosen restaurant for you meow: ')
    print(choice)
    print('enjoy meow QwQ')
    print('all the options for you: ')
    for r in list:
        print(r)
    # unsued return value
    return list

def run():
    cmd = ''
    while(cmd != 'q'):
        cmd = input("meow~ please specify your options: \
        \n[list]: list cuisine IDs \
        \n[jap]: choosing a japanese restaurant \
        \n[korean]: choosing a korean restaurant \
        \n[burger]: find a burger place \
        \n[pizza]: get a pizza \
        \n[it]: get an italian restaurant \
        \n[spanish]: get a spanish restaurant \
        \n[o]: customise input with a cuisine id \
        \n[q]: quit\
        \nyour option meow: ")
        cmd = cmd.lower().strip()
        if cmd == 'list':
            get_cuisines()
        elif cmd == 'jap':
            get_restaurants(60)
        elif cmd == 'korean':
            get_restaurants(67)
        elif cmd == 'burger':
            get_restaurants(168)
        elif cmd == 'it':
            get_restaurants(55)
        elif cmd == 'pizza':
            get_restaurants(82)
        elif cmd == 'spanish':
            get_restaurants(89)
        elif cmd == 'o':
            try:
                id = int(input('please specify cuisine id: '))
                get_restaurants(id)
            except:
                print('meow... unrecognised id..')
        elif cmd == 'q':
            print('thanks for playing with me meow, bye QwQ')
        else:
            print('meow... unrecognised command.. please try again meow')

# run program
run()
