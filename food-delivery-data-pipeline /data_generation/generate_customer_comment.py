import random   

# List of customer comments 
customer_comments = [
    "No onions",
    "Gluten-free",
    "Dairy-free",
    "Extra spicy",
    "Rare",
    "Well done",
    "Extra cheese",
    "Extra sauce",
    "With lemon",
    "Sugar-free",
    "With sweetener",
    "With almond milk",
    "With soy milk",
    "No allergens",
    "With allergens",
    "No condiments",
    "With condiments",
    "No spices",
    "With spices",
    "No salt",
    "With salt",
    "With ice",
    "No ice",
    "With lid",
    "No lid",
    "With straw",
    "No straw",
    "With bag",
    "No bag"
]

def generate_customer_comment():
    return random.choice(customer_comments)
