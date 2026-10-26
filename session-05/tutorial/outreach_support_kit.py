name = "Camila"
age = 15
willingness_score = 7
requested_support = 'samba_workshop'

# List of available support types
available_support = ['meal', 'shelter_referral', 'medical_check', 'samba_workshop', 'counseling']

# List of people currently barred from the program
barred_people = ['carlos_silva', 'joao_santos', 'ana_pereira']

if {(age >= 12) and (willingness_score >= 5)}:
    print("Camila is eligible for the outreach program.")
else: 
    print("Camila is not eligible for the outreach program.")

#for every item from requested_support (works cause we have only 1 )
if requested_support in available_support:
    print("Samba_Workshop is available in our system.")
else: 
    print("Samba_Workshop is not available in our system.")

# would work but only if we make a list in requested_support
# for support in requested_support:
#     if support in available_support:
#         print("is available")
#     else:print("not")


if name.lower() not in barred_people:
    print(f"{name} is not barred from receiving assistance.")

# ANOTHER EXAMPLE
# # List of ingredients Dona Rita CAN use tonight
# available_ingredients = ['black beans', 'bacon', 'paio sausage', 'ribs', 'onion', 'garlic']

# # List of ingredients she needs to check for tonight's feijoada
# requested_ingredients = ['black beans', 'linguiça', 'ribs']

# # OPTION 1 it takes all of the items from requested_ingredients at once 
# if requested_ingredients in available_ingredients:
#     print(f"✓ {available_ingredients} is available...")
# else: print(f"✗ I should ask Humberto to get {available_ingredients}.")

# #OPTION 2 for every single one item from requested_ingridients
# for ingredient in requested_ingredients:
#     if ingredient in available_ingredients:
#         print(f"✓ {ingredient} is available...")
#     else:
#         print(f"✗ I should ask Humberto to get {ingredient}.")
