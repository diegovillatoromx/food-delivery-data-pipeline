import random
 
# Average prices of products in each type of restaurant
average_prices = { 
    "Mexican": 8.5,
    "Italian": 12.0, 
    "Japanese": 15.0,
    "Chinese": 10.0, 
    "American": 9.0,
    "Indian": 10.5,
    "Thai": 13.0,
    "Vegetarian": 11.0
}

# User Credits in numerical values
user_credits = [0, 10, 20, 50, 100]

# Applied Promotion
applied_promotion = [
    "No promotion applied",
    "Discount on total order",
    "Free delivery promotion",
    "Buy one get one free",
    "Percentage discount on specific menu items"
]

# List of product quantities
product_quantity = list(range(1, 11))  # From 1 to 10

def generate_product_order(category, name=None):
    if name is None:
        name = random.choice(restaurant_names.get(category, []))
    
    # Randomly select the quantity of products
    quantity = random.choice(product_quantity)
    
    # Calculate the price of the product based on the restaurant type and average price
    price_per_item = average_prices.get(category, 0)
    total_price = quantity * price_per_item
    
    # Randomly select user credits and applied promotion
    user_credit = random.choice(user_credits)
    applied_promo = random.choice(applied_promotion)
    
    # Calculate the final cost after applying credits and promotions
    final_cost = max(total_price - user_credit, 0)
    
    return {
        "Product Quantity": quantity,
        "Price Per Item": price_per_item,
        "Total Price": total_price,
        "User Credits": user_credit,
        "Applied Promotion": applied_promo,
        "Final Cost": final_cost
    }
