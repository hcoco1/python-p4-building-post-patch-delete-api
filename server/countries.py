import json
from faker import Faker
import random

fake = Faker()

def generate_country_data(num_countries=50):
    countries_data = {"countries": []}
    for _ in range(num_countries):
        country_code = fake.country_code().lower()
        country_name = fake.country()
        random_message = fake.sentence()  # Generate a random sentence
        country = {
            "id": random.randint(1, 200),
            "country": country_name,
            "area_in_Square_Kilometers": random.randint(100000, 2000000),
            "population": random.randint(5000000, 300000000),
            "flagUrl": f"https://www.worldometers.info/img/flags/{country_code}-flag.gif",
            "message": [random_message]  # Add the random sentence to the message list
        }
        countries_data["countries"].append(country)
    return countries_data

data = generate_country_data()
json_str = json.dumps(data, indent=2)  # Convert data to JSON string with indentation for readability
print(json_str)


