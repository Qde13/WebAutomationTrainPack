import random

from data.data import Person
from faker import Faker

faker_en = Faker('en')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_en.first_name() + " " + faker_en.last_name(),
        firstname=faker_en.first_name(),
        lastname=faker_en.last_name(),
        age=random.randint(10, 80),
        department=faker_en.sentence(nb_words=1),
        salary=random.randint(200, 12000),
        email=faker_en.email(),
        current_address=faker_en.address(),
        permanent_address=faker_en.address(),
        phone_number=faker_en.msisdn()[0:10],
    )


def generated_file():
    filepath = rf"D:\PythonProjects\WebAutomationTrainPack\testfile{random.randint(0,999)}.txt"
    file = open(filepath, "w+")
    file.write("some text")
    file.close()
    return filepath
