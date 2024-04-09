import random  
payment_methods = [ 
    "Cash",
    "Credit card",
    "Debit card", 
    "Bank transfer",
    "PayPal",
    "Mercado Pago",
    "Oxxo Pay",
    "SPEI (Interbank Electronic Payment System)",
    "Saldazo (Oxxo debit card)",
    "Payment at 7-Eleven",
    "Payment at Extra",
    "Payment at Farmacias Guadalajara",
    "Payment at Farmacias del Ahorro",
    "Payment at Walmart",
    "Payment at Soriana",
    "Payment at Oxxo",
    "Online banking payment",
    "Cash on delivery"
]

def choose_payment_method():
    return random.choice(payment_methods)
