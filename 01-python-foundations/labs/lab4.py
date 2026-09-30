"""
Model a Customer with id: int, email: str, age: int. Add validators:
age must be 0–120; email must contain "@". Feed it three good and
three bad records; count how many validate.
"""


class Customer:
    def __init__(self, id: int, email: str, age: int):
        # Bouncer 1: Check the age
        if age < 0 or age > 120:
            raise ValueError(f"Age {age} is impossible. Must be 0-120.")

        # Bouncer 2: Check the email
        if "@" not in email:
            raise ValueError(f"Email '{email}' is missing an '@' sign.")

        # If we make it past the bouncers, we stamp the clipboard
        self.id = id
        self.email = email
        self.age = age


# OUr raw data (using tuples so it's easy to unpack)
test_records = [
    (1, "a@b.com", 25),
    (2, "x@y.org", 0),
    (3, "test@test.co", 120),
    (4, "bad_email.com", 30),
    (5, "good@good.com", -5),
    (6, "old@old.com", 150),
]

valid_count = 0

for record in test_records:
    id_val, email_val, age_val = record  # Unpack the tuple

    try:
        # Attempt to build the customer
        customer = Customer(id_val, email_val, age_val)
        # If no error was raised, the line below will run:
        valid_count += 1

    except ValueError as e:
        # If a ValueError was raised, it gets caught here.
        # 'e' holds the error message we wrote in the raise statement.
        print(f"Failed to create Customer {id_val}: {e}")

print(f"\nTotal valid customers created: {valid_count}")
