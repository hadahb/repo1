full_name = input("Enter your full name: ").title()
age = int(input("Enter your age: "))
height_meters = float(input("Enter your height (in meters): "))
favorite_language = input("Enter your favorite programming language: ").title()
hobbies = input("Enter your hobbies [separate with comma (,)]: ").split(", ")

hobbies = [hobby.title() for hobby in hobbies]
date_of_birth = 2025 - age
height_centimeters = height_meters * 100


# Store data in a dictionary
user_profile = {
    "Full Name": full_name,
    "age" : age,
    "Date Of Birth": date_of_birth,
    "Height in meters": height_meters,
    "Height in centimeters": height_centimeters,
    "Favorite Programming Language": favorite_language,
    "Hobbies": hobbies
}

# Print the stored data
print("User Profile Summary:")
print("-Name: " , user_profile["Full Name"])
print("-Age: " , user_profile["age"], "(Born in" , user_profile["Date Of Birth"], ")")
print("-Height: " , user_profile["Height in meters"], "meters",  "(", user_profile["Height in centimeters"], "centimeters)")
print("-Favorite Programming Language: " , user_profile["Favorite Programming Language"], "(Yes, it's ", user_profile["Favorite Programming Language"], "!)")
print("-Hobbies: " , len(hobbies) , "hobbies- ", ", ".join(user_profile["Hobbies"]))

