# Multi-line prompt for the supporter's name
prompt = "Welcome to the Abolitionist Movement Registry.\n"
prompt += "Please enter your full name: "

#Task 1: Collect the supporter's name using the `input()` function and store it in a variable called `name`.
name = None
#TODO: YOUR CODE GOES HERE
name = input(prompt)

# Task 2: Collect the supporter's year of birth and store it in a variable called `birth_year` and convert it to an integer.
birth_year = None
prompt += "Please enter the year of your birth: "
#TODO: YOUR CODE GOES HERE
birth_year = int(input(prompt))

# Task 3: Collect the supporter's home county and store it in a variable called `county`.
county = None
#TODO: YOUR CODE GOES HERE
county = input("Please enter your home county: ")
# Task 4: Calculate age at the time of the Slave Trade Act (1807)
age_in_1807 = None
#TODO: YOUR CODE GOES HERE
age_in_1807 = 1807 - birth_year
# Print the membership card
print("\n--- Abolitionist Movement Membership Card ---")
print(f"Name:         {name}")
print(f"Home County:  {county}")
print(f"Age in 1807:  {age_in_1807}")
print(f"Status:       Registered Supporter")
print("---------------------------------------------")
print(f"Welcome, {name}! Your commitment to justice is recorded for history.")
