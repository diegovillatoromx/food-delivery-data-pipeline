import random
import json
import hashlib  
from generate_customer_comment import generate_customer_comment
from generate_delivery_address import generate_delivery_addresses
from generate_delivery_method import generate_delivery_method
from generate_delivery_time import calculate_delivery_time
from generate_payment_method import choose_payment_method
from generate_price_costs import generate_product_order
from generate_restaurant_address import load_restaurant_data, get_random_restaurant

def generate_purchase():
    # Generate delivery address
    delivery_address = generate_delivery_addresses()
    # Generate delivery method
    delivery_method = generate_delivery_method()
    # Calculate delivery time
    delivery_time_data = calculate_delivery_time()
    # Load restaurant data
    restaurants = load_restaurant_data('restaurant_data.json')
    # Get random restaurant
    restaurant = get_random_restaurant(restaurants)
    # Generate product order
    product_order = generate_product_order(restaurant['Category'], restaurant['Name'])
    # Generate customer comment
    customer_comment = generate_customer_comment()
    # Choose payment method
    payment_method = choose_payment_method()
    # Generate Purchase ID
    purchase_ID = hashlib.sha256(f"{delivery_time_data['Delivery time']} {delivery_method}".encode('utf-8')).hexdigest()[:10]
    # Construct purchase data
    purchase_data = {
        "Purchase_ID": purchase_ID,
        "Delivery Address": delivery_address,
        "Delivery Method": delivery_method,
        **delivery_time_data,
        "Restaurant Category": restaurant["Category"],
        "Restaurant Name": restaurant["Name"],
        "Product Order": product_order,
        "Customer Comment": customer_comment,
        "Payment Method": payment_method
    }

    return purchase_data
