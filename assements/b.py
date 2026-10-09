Advanced Python Solo Assessment (4 Hours)
ebutechristopher6@gmail.com Switch account
 
* Indicates required question
PART B — One-hour technical assessment (30 marks)
Start after your 3-hour coding period. Six questions, 5 marks each. Give explanations and code where requested.
B1. Trace the code and explain the output *
What exactly is printed, and why?

items = [2, 4, 6]
result = []
for item in items:
    if item % 4 == 0:
        continue
    result.append(item * 2)
print(result)
B2. Diagnose and repair a borrowing bug *
Identify the problem, explain its consequences and rewrite the function correctly.

def borrow(resource, quantity):
    resource["available"] -= quantity
    if resource["available"] < 0:
        return "Not enough stock"
    return "Success"
B3. Aggregate transaction data *
Write a function that returns a dictionary of the total quantity per fellow, without hardcoding results.

transactions = [
    {"fellow": "Ada", "quantity": 2},
    {"fellow": "John", "quantity": 4},
    {"fellow": "Ada", "quantity": 3},
    {"fellow": "Grace", "quantity": 1},
    {"fellow": "John", "quantity": 2}
]

Expected totals: Ada 5; John 6; Grace 1.
B4. Mutating a list during iteration *
Will the code always remove every unavailable resource? Explain and provide a reliable correction.

resources = [
    {"name": "Laptop", "available": 0},
    {"name": "Mouse", "available": 0},
    {"name": "Keyboard", "available": 3}
]
for resource in resources:
    if resource["available"] == 0:
        resources.remove(resource)
print(resources)
B5. Reason about simultaneous requests *
Inventory has five available laptops. Two fellows request four each at nearly the same time. Why can a separate stock check and stock update be unsafe if requests execute concurrently? Describe a method to ensure no more laptops are issued than available. No code required.
B6. Defend your own implementation *
Answer all three: (a) What was the most challenging project feature and how did you solve it? (b) Describe a bug you encountered, how you found it and how you fixed it. (c) What would you improve first if 500 fellows used the system, and why?

S