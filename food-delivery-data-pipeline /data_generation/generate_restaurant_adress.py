import json 
 
def load_restaurant_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file) 
    return data

def get_random_restaurant(restaurants):
    # Choose a random restaurant category
    category = random.choice(list(restaurants.keys()))
    
    # Choose a random restaurant from the selected category
    restaurant = random.choice(restaurants[category])
    
    return {
        "Category": category,
        "Name": restaurant["Name"],
        "Address": restaurant["Address"]
    }
