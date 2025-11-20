CURRENT_YEAR = 2025

def generate_profile(age : int) -> str:
    """Return life stage based on age"""
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"

print("Hello!")

user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = CURRENT_YEAR - birth_year

hobbies = []
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == "stop":
        break
    hobbies.append(hobby)

life_stage = generate_profile(current_age)

user_profile = {'name': user_name,
                'age': current_age,
                'stage': life_stage,
                'hobbies': hobbies}

print(f"Profile Summary:\n"
          f"Name: {user_profile["name"].title()}\n"
          f"Age: {user_profile["age"]}\n"
          f"Life Stage: {user_profile["stage"]}")

if len(user_profile["hobbies"]):
        print(f"Favorite Hobbies ({len(user_profile['hobbies'])}):")
        for hobby in user_profile["hobbies"]:
            print(f"- {hobby}")
else:
    print("You didn't mention any hobbies.")