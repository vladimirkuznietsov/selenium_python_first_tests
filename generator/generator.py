from data.data import Person
from faker import Faker

faker_en = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_en.first_name() + ' ' + faker_en.middle_name() + ' ' + faker_en.last_name(),
        email=faker_en.email(),
        current_address=faker_en.address(),
        permanent_address=faker_en.address()
    )
