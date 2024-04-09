from faker import Faker
from random import randint

fake = Faker()


class Payloads:

    create_user = {
        "userName": fake.user_name(),
        "password": fake.password(length=randint(10, 20))
    }
    with open("../../.env", "w") as file:
        for key, value in create_user.items():
            file.write(f"{key.upper()}={value}\n")
