import random
  
# List of delivery methods
delivery_methods = [
    "Home delivery", 
    "Pickup at restaurant",
    "Meeting point delivery", 
    "Express delivery",
    "Scheduled delivery",
    "Courier delivery",
    "Office delivery",
    "Workplace delivery",
    "Customer's address delivery",
    "Neighbor's address delivery",
    "Mailbox delivery",
    "Locker delivery"
]

def generate_delivery_method():
    return random.choice(delivery_methods)
