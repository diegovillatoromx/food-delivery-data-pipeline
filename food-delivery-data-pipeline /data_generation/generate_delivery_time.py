import random 
from datetime import datetime, timedelta   
 
# Definition of trip durations 
trip_durations = [f"{i} minutes" for i in range(20, 95, 5)]
  
# Definition of waiting times
waiting_times = [i for i in range(5, 30, 5)]  # Assuming waiting time can vary from 5 to 25 minutes in 5-minute increments

# Definition of preparation times
preparation_times = [i for i in range(10, 40, 5)]  # Assuming preparation time can vary from 10 to 35 minutes in 5-minute increments

# Definition of distances to the restaurant
distances_to_restaurant = [i for i in range(1, 11)]  # Assuming distances to the restaurant can vary from 1 to 10 kilometers

def calculate_delivery_time():
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

    # Create a dictionary with the values
    delivery_data = {
        "Creation time": creation_time.strftime("%Y-%m-%d %H:%M:%S"),
        "Waiting times": f"{selected_waiting_time} minutes",
        "Preparation times": f"{selected_preparation_time} minutes",
        "Distances to restaurant": f"{selected_distance_to_restaurant} minutes",
        "Trip durations": selected_trip_duration,
        "Delivery time": delivery_time.strftime("%Y-%m-%d %H:%M:%S")
    }

    return delivery_data
