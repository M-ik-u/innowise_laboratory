def generate_profile(age: int) -> str:
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"

def profile_summary(user_profile: dict) -> None:
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

def valid_birth_year() -> int:
    while True:
        birth_year_str = input("Enter your birth year: ")

        if not birth_year_str.isdigit():
            print("Please enter a valid numeric year.")
            continue

        birth_year = int(birth_year_str)

        if birth_year < 1900 or birth_year > 2025:
            print("Birth year must be between 1900 and 2025.")
        else:
            return birth_year

def valid_hobbies(hobbies: list) -> None:
    while True:
        hobby = input("Enter a favourite hobby or type 'stop' to finish: ").strip()

        if hobby.lower() == "stop":
            break

        if not hobby:
            print("Hobby cannot be empty.")
            continue

        if hobby in hobbies:
            print("You already added this hobby.")
            continue

        hobbies.append(hobby)

def valid_user_name() -> str:
    while True:
        user_name = input("Enter your full name: ")

        if not user_name:
            print("Username cannot be empty.")
            continue
        user_name_temp = user_name.split()

        if len(user_name_temp) < 2:
            print("Please enter your full name.")

        elif user_name_temp[0].isalpha() and user_name_temp[1].isalpha():
            return user_name

        else:
            print("Please enter a valid username.")

if __name__ == "__main__":

    print("Hello!")
    user_profile = {}

    user_name = valid_user_name()
    user_profile["name"] = user_name

    birth_year = valid_birth_year()
    current_age = 2025 - birth_year
    user_profile["age"] = current_age

    life_stage = generate_profile(current_age)
    user_profile["stage"] = life_stage

    hobbies = []
    valid_hobbies(hobbies)
    user_profile["hobbies"] = hobbies

    profile_summary(user_profile)