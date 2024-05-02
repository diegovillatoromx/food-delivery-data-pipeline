import json 
import random   
  
def generate_delivery_addresses():
    with open('address_data.json') as f:
        data = json.load(f)
    
    street_names = data['street_names']
    neighborhoods = data['neighborhoods']
    city = data['city']
    state = data['state']

    street_numbers = [random.randint(100, 999) for _ in range(len(street_names))]
    
    delivery_addresses = []
    for i in range(len(street_names)):
        address = f"{street_names[i]} #{street_numbers[i]}, {neighborhoods[i]}, {city}, {state}"
        delivery_addresses.append(address)

    return random.choice(delivery_addresses)
