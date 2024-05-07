import random
import hashlib
from datetime import datetime, timedelta

def generate_purchase_id():
    return str(hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest())[:10]

def generate_delivery_time():
    # Definition of trip durations 
    trip_durations = [f"{i} minutes" for i in range(20, 95, 5)]
    
    # Definition of waiting times
    waiting_times = [i for i in range(5, 30, 5)]  # Assuming waiting time can vary from 5 to 25 minutes in 5-minute increments

    # Definition of preparation times
    preparation_times = [i for i in range(10, 40, 5)]  # Assuming preparation time can vary from 10 to 35 minutes in 5-minute increments

    # Definition of distances to the restaurant
    distances_to_restaurant = [i for i in range(1, 11)]  # Assuming distances to the restaurant can vary from 1 to 10 kilometers

    # Generate a random creation time one week ago
    current_time = datetime.now()
    creation_time = current_time - timedelta(days=random.randint(1, 7))

    # Select random values for the parameters
    selected_trip_duration = random.choice(trip_durations)
    selected_waiting_time = random.choice(waiting_times)
    selected_preparation_time = random.choice(preparation_times)
    selected_distance_to_restaurant = random.choice(distances_to_restaurant)

    # Calculate the delivery time
    delivery_time = creation_time + \
        timedelta(minutes=selected_preparation_time) + \
        timedelta(minutes=selected_waiting_time)

    # Add the distance to the delivery time
    delivery_time += timedelta(minutes=selected_distance_to_restaurant)

    # Add the trip duration to the delivery time
    delivery_time += timedelta(minutes=int(selected_trip_duration.split()[0]))

    return {
        "Creation time": creation_time.strftime("%Y-%m-%d %H:%M:%S"),
        "Waiting times": f"{selected_waiting_time} minutes",
        "Preparation times": f"{selected_preparation_time} minutes",
        "Distances to restaurant": f"{selected_distance_to_restaurant} minutes",
        "Trip durations": selected_trip_duration,
        "Delivery time": delivery_time.strftime("%Y-%m-%d %H:%M:%S")
    }

def generate_order():
    purchase_id = generate_purchase_id()
    delivery_address = "Calle Juárez #695, Col. San Marcos, Tuxtla Gutiérrez, Chiapas"
    delivery_method = "Meeting point delivery"
    delivery_time = generate_delivery_time()
    product_category = "Mexican"
    product_name = "Burritos El Chilango"
    product_order = {
        "Product Quantity": 8,
        "Price Per Item": 8.5,
        "Total Price": 68.0,
        "User Credits": 50,
        "Applied Promotion": "Buy one get one free",
        "Final Cost": 0.0
    }
    customer_comment = "Sugar-free"
    payment_method = "Cash on delivery"

    return {
        "Purchase_ID": purchase_id,
        "Delivery Address": delivery_address,
        "Delivery Method": delivery_method,
        **delivery_time,
        "Restaurant Category": product_category,
        "Restaurant Name": product_name,
        "Product Order": product_order,
        "Customer Comment": customer_comment,
        "Payment Method": payment_method
    }
