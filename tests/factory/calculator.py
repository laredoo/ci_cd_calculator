from faker import Faker
from app.calculator import Calculadora

fake = Faker()

def create_fake_calculator(digits) -> Calculadora:
    num_1 = fake.random_number(digits)
    num_2 = fake.random_number(digits)
    return Calculadora(num_1, num_2)