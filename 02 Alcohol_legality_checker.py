"""This project is a checker for alcohol legality based on age and country
"""

name = input("What is your name? ")
age = int(input("What is your age? "))

legal_drinking_ages = {
    "usa": 21,
    "uk": 18,
    "germany": 16,
    "philippines": 18,
    "india": 25,
    "japan": 20,
    "canada": 19,
    "south korea": 19,
    "france": 18,
    "brazil": 18,
    "saudi arabia": None,  # Alcohol is illegal
    "russia": 18,
    "china": 18,
    "thailand": 20,
    "australia": 18
}
country = input("Which country are you in? ").lower()


def legal_age(country):
    if country in legal_drinking_ages:
        return legal_drinking_ages[country]


country_legal_age = legal_age(country)


def alcohol_legality(age, country_legal_age):
    if country_legal_age == None:
        print("invalid input. Country might not be on the list or alcohol is not legal in the country.")
    elif age < country_legal_age:
        print("I'm sorry, you are not yet legal to consume any alcohol in this country.")
    elif age >= country_legal_age:
        print("You are in the right age to consume alcohol in this country.")
    else:
        return ("country")


alcohol_legality(age, country_legal_age)
