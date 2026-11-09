# Questions and the "Key" we use to store the objection in a dictionary
questions = [
    ("Is the slave trade morally indefensible?", "morality"),
    ("Should the British Empire prioritize human rights over sugar profits?", "profits"),
    ("Do you support the boycott of slave-produced sugar?", "boycott"),
    ("Would you vote for immediate abolition?", "immediate"),
    ("Is it true that the trade is 'contrary to the laws of God'?", "religion"),
    ("Do you believe the middle passage is unnecessarily cruel?", "cruelty"),
    ("Will you sign the petition for the 1792 session?", "petition")
]

for_answers = 0
against_answers = {'topics to discuss' : []}
name = input("Please enter your name: ")
for question, theme in questions:
    answer = input(f"{question} \nPlease answer with yes or no: ")
    if answer == "yes":
        for_answers += 1
    else:
        against_answers['topics to discuss'].append(question)

print(f"{name} is")
if for_answers <= 3:
    print("...the opponent")
if  3 < for_answers <= 5:
    print("...the persuadable one")
    print(f"We need to talk about following topics: \n{'\n'.join(against_answers['topics to discuss'])}")
if 5 < for_answers <= 7:
    print("...the supporter")




 