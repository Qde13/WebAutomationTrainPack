import random

from faker import Faker

from data.data import Person, Color, Date

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
    filepath = rf"D:\PythonProjects\WebAutomationTrainPack\testfile{random.randint(0, 999)}.txt"
    file = open(filepath, "w+")
    file.write("some text")
    file.close()
    return filepath


def generated_color():
    yield Color(
        color_name=["Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )


def generated_date():

    def gen_time():
        h = random.randint(0, 24)
        m = random.randrange(0, 60, 15)
        if h < 10:
            h = f"0{h}"
        if m == 0:
            m = '00'
        time = f"{h}:{m}"
        return time

    yield Date(
        year=str(random.randint(2018, 2028)),
        month=faker_en.month_name(),
        time=gen_time(),
        day=str(random.randint(1, 29))
    )
