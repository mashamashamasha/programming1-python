# Donation records - what donors intended their money to be used for
donations = {
    'American Red Cross': 'Medical supplies for the clinic',
    'UNICEF': 'Food for children',
    'World Health Org': 'Medical supplies for the clinic',
    'Catholic Charities': 'Food for children',
    'Oxfam': 'Educational programs',
    'Save the Children': 'Educational programs',
    'Global Fund': 'Medical supplies for the clinic',
}

# Actual use - where the money really went
actual_use = {
    'American Red Cross': 'Medical supplies for the clinic',
    'UNICEF': 'Administrative overhead',
    'World Health Org': 'Medical supplies for the clinic',
    'Catholic Charities': 'Food for children',
    'Oxfam': 'Administrative overhead',
    'Save the Children': 'Educational programs',
    'Global Fund': 'Building renovation project',
}

# 1. Loop through donors and print their intended donations
print("=" * 60)
print("DONATION INTENTIONS:")
print("=" * 60)

#TODO: 
for key, value in donations.items():
    print(f"{key}: {value}")


# 2. Check for misuse - compare intended vs actual
print("\n" + "=" * 60)
print("MISUSE DETECTION:")
print("=" * 60)

# TODO: Add your code here
for key, value in donations.items(): 
    #"not in" needs ()
    if (key, value) not in actual_use.items():
        print(f"\n{key}: MISUSE DETECTED")
        print(f"   Intended: {actual_use[key]}")
        print(f"   Actual:   {value}")
    else:
        print(f"\n✓ OK - {key}")
        

# 3. Find ALL purposes that were misused (using set())
print("\n" + "=" * 60)
print("PURPOSES WITH MISUSE:")
print("=" * 60)
# Get all purposes that were misused (intended but not matched actual)

# TODO: Add your code here
misused_purposes = []
for key, value in donations.items():
    if value != actual_use[key]:
        misused_purposes.append(value)

# Show unique misused purposes
print("Purposes that were misused:")
# TODO: Add your code here
for purpose in set(misused_purposes):
    number = misused_purposes.count(purpose)                #where we count and then what we count 
    print(f"{purpose.title()}: was missed {number} times")

# 4. Show unique purposes intended vs actual
print("\n" + "=" * 60)
print("SUMMARY - UNIQUE PURPOSES:")
print("=" * 60)

# TODO: Add your code here
intended = "\n".join(set(donations.values()))
print(f"Intended uses: \n{intended}" )

print("\nActual uses:")
for value in set(actual_use.values()):
    print(value)

# Additional analysis: How many donors were affected by misuse?
print("\n" + "=" * 60)
print("IMPACT SUMMARY:")
print("=" * 60)

number_total = len(donations.keys())
print(f"Total donors: {number_total}")

affected_donors = []
for key, value in donations.items():
    if value != actual_use[key]:
        affected_donors.append(key)
aff_donors_list = "\n".join(affected_donors)
number_affected = len(affected_donors)

print(f"Misuse percentage:{number_affected/number_total:.2f}%")
print(f"\nNumber of affected donors: {number_affected} \nNames of affected donors: \n{aff_donors_list}")





# TODO: Add your code here