import random
from data.data import Person
from faker import Faker

faker_us = Faker(locale='en_US')
Faker.seed()


def generated_person():
    """Generate data"""
    yield Person(
        full_name=faker_us.first_name() + " " + faker_us.last_name(),
        firstname=faker_us.first_name(),
        lastname=faker_us.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(10000, 100000),
        department=faker_us.job(),
        email=faker_us.email(),
        current_address=faker_us.address(),
        permanent_address=faker_us.address()
    )
