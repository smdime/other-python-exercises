grocery = [
    {"name": "penne", "price": 16.68},
    {"name": "sauce", "price": 6.98},
    {"name": "garlic", "price": 16.78},
    {"name": "seasoning", "price": 15.26},
    {"name": "bread", "price": 3.00},
    {"name": "meatballs", "price": 4.39}
]
# Sum the prices
print(round(sum(item["price"] for item in grocery),2))