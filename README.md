# Real-Time Data Simulator Function

The Real-Time Data Simulator Function provides a Python function that generates simulated data for orders, customers, products, payments, and deliveries. This function can be used to create realistic datasets that mimic the behavior of real-time data streams, allowing data engineers to test and validate their data pipelines effectively. 
  
 
## Table of Contents

1. [Introduction](#introduction)
2. [Purpose](#purpose)
3. [Key Features](#key-features)
4. [Data Simulation](#data-simulation)
   - [Data Generation](#data-generation)
   - [Data Structure](#data-structure)
   - [Simulated Events](#simulated-events)
5. [Usage](#usage)
6. [Installation](#installation)
7. [Requirements](#requirements)
8. [Example](#example)
9. [Detailed Script Overview](#detailed-script-overview)
   - [generate_order_data.py](#generate_order_data.py)
   - [generate_customer_data.py](#generate_customer_data.py)
   - [generate_product_data.py](#generate_product_data.py)
   - [generate_payment_data.py](#generate_payment_data.py)
   - [generate_delivery_data.py](#generate_delivery_data.py)
10. [Integration with Data Pipeline](#integration-with-data-pipeline)
11. [Future Enhancements](#future-enhancements)
12. [Contributing](#contributing)
13. [Contact](#contact)
14. [License](#license)

## Introduction

The Real-Time Data Simulator Function for Food Delivery Service provides a Python function that generates simulated data for orders, customers, products, payments, and deliveries. This function can be used to create realistic datasets that mimic the behavior of real-time data streams, allowing data engineers to test and validate their data pipelines effectively.

## Purpose

The purpose of this project is to facilitate the creation of realistic datasets for data engineering purposes. Many data engineers often need to practice and simulate information or test their data pipelines but lack the necessary data for streaming. This function aims to bridge that gap by providing a tool to generate simulated data that closely resembles real-world scenarios.

## Key Features

- Simulated Data Generation: The function generates synthetic data for various aspects of a food delivery service, including orders, customers, products, payments, and deliveries. This simulated data closely resembles real-world scenarios, enabling realistic testing of data pipelines.
- Configurable Parameters: Users can configure various parameters of the data generation process, such as the number of orders, the frequency of orders, the range of product types, and the distribution of customer locations. This flexibility allows for the generation of diverse datasets to suit different testing scenarios.
- Realistic Data Distribution: The function uses probabilistic distributions to simulate realistic patterns in data, such as the distribution of order values, the frequency of customer orders, and the geographical distribution of customers. This approach ensures that the generated data closely resembles actual data distributions.
- Easy Integration: The function can be easily integrated into existing Python scripts and data pipelines. Users can call the function to generate data on-demand or incorporate it into automated testing processes.
- Scalability: The function is designed to scale with the needs of the user. Whether generating data for a small-scale test or a large-scale simulation, the function can handle varying data generation requirements efficiently.


## Data Simulation

The data simulation process involves generating realistic data for orders in a food delivery service. This process includes three main parts:

1. **Data Generation**: In this step, various aspects of the order are generated, such as delivery address, delivery method, delivery time, restaurant details, product order, customer comment, and payment method. This step uses a combination of predefined data and random generation to simulate realistic orders.

2. **Data Structure**: The generated data follows a structured format to ensure consistency and usability. Each order includes specific fields such as purchase ID, delivery address, delivery method, delivery time, restaurant category and name, product order details, customer comment, and payment method.

3. **Simulated Events**: These events represent different stages of the order process and include placing the order, preparing the order, delivering the order, and completing the order. Each event is simulated based on the generated data and provides a comprehensive view of the order lifecycle.

### Data Generation

The `generate_order_data.py` script is the primary script responsible for generating order data. It imports various functions for generating different aspects of the order, such as delivery address, delivery method, delivery time, restaurant details, product order, customer comment, and payment method. These functions use random generation and predefined data to create realistic orders.

### Data Structure

The data structure of the generated orders includes the following fields:

- **Purchase_ID**: A unique identifier for each purchase, generated using a combination of delivery time and delivery method.
- **Delivery Address**: The address to which the order will be delivered.
- **Delivery Method**: The method of delivery chosen by the customer.
- **Delivery Time**: The estimated time for delivery, calculated based on various factors.
- **Restaurant Category**: The category of the restaurant from which the order is placed.
- **Restaurant Name**: The name of the restaurant from which the order is placed.
- **Product Order**: Details of the products ordered, including category, name, and quantity.
- **Customer Comment**: Any additional comments or instructions provided by the customer.
- **Payment Method**: The method of payment chosen by the customer.

### Simulated Events

The simulated events for each order include the following stages:

1. **Placing the Order**: The customer places an order on the food delivery platform.
2. **Preparing the Order**: The restaurant receives the order and begins preparing it.
3. **Delivering the Order**: The delivery service picks up the order from the restaurant and delivers it to the customer.
4. **Completing the Order**: The customer receives the order and completes the transaction.

Each event is simulated based on the generated data and provides a realistic representation of the order process.


```python
{
    "Purchase_ID": "01a29e2b0e",
    "Delivery Address": "Calle Juárez #695, Col. San Marcos, Tuxtla Gutiérrez, Chiapas",
    "Delivery Method": "Meeting point delivery",
    "Creation time": "2024-03-12 15:42:00",
    "Waiting times": "15 minutes",
    "Preparation times": "20 minutes",
    "Distances to restaurant": "3 minutes",
    "Trip durations": "40 minutes",
    "Delivery time": "2024-03-12 16:40:00",
    "Restaurant Category": "Mexican",
    "Restaurant Name": "Burritos El Chilango",
    "Product Quantity": 8,
    "Price Per Item": 8.5,
    "Total Price": 68.0,
    "User Credits": 50,
    "Applied Promotion": "Buy one get one free",
    "Final Cost": 0.0,
    "Customer Comment": "Sugar-free",
    "Payment Method": "Cash on delivery"
}
```
