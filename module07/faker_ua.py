# pip install faker
from faker import Faker

# "uk_UA" - Ukrainian locale: names, cities, phones, addresses in Ukrainian
fake = Faker("uk_UA")

# seed makes results reproducible (same data on every run)
Faker.seed(42)

print("--- person ---")
print(fake.name())
print(fake.first_name_male(), fake.last_name_male())
print(fake.first_name_female(), fake.last_name_female())
print(fake.middle_name())  # по батькові

print("--- contacts ---")
print(fake.phone_number())
print(fake.email())
print(fake.user_name())

print("--- address ---")
print(fake.city_name())
print(fake.region())
print(fake.street_address())
print(fake.postcode())
print(fake.address())

print("--- other ---")
print(fake.company())
print(fake.job())
print(fake.date_of_birth(minimum_age=18, maximum_age=60))
print(fake.text(max_nb_chars=80))

# several locales at once: fake["uk_UA"], fake["en_US"]
multi = Faker(["uk_UA", "en_US"])
print("--- multiple locales ---")
print(multi["uk_UA"].name(), "|", multi["en_US"].name())

# a list of Ukrainian users as dicts
users = [
    {
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "city": fake.city_name(),
        "age": fake.random_int(min=18, max=60),
    }
    for _ in range(3)
]
print("--- users ---")
for user in users:
    print(user)
