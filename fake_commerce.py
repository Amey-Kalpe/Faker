from faker import Faker
import faker_commerce
import random

fake = Faker()

fake.add_provider(faker_commerce.Provider)


def ecommerce_price(as_int: bool = True):
    n = random.randint(100, 100000)
    return round(n, 2) if as_int else n / 100


def generate_product_info():
    return {
        "name": fake.ecommerce_name(),
        "category": fake.ecommerce_category(),
        "price": ecommerce_price(),
    }


print(generate_product_info())
