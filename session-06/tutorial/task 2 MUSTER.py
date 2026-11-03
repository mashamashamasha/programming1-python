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
for donor, intention in donations.items():
    print(f"{donor}: {intention}")



# 2. Check for misuse - compare intended vs actual
print("\n" + "=" * 60)
print("MISUSE DETECTION:")
print("=" * 60)
for donor, intention in donations.items():
    actual = actual_use[donor]
    if intention != actual:
        print(f"⚠️  MISUSE DETECTED - {donor}")
        print(f"   Intended: {intention}")
        print(f"   Actual:   {actual}")
    else:
        print(f"✓ OK - {donor}")

# 3. Find ALL purposes that were misused (using set())
print("\n" + "=" * 60)
print("PURPOSES WITH MISUSE:")
print("=" * 60)

# Get all purposes that were misused (intended but not matched actual)
misused_purposes = []
for key in donations.keys():
    if donations[key] != actual_use[key]:
        misused_purposes.append(donations[key])



# Show unique misused purposes
print("Purposes that were misused:")
for purpose in set(misused_purposes):
    #how many purposes in the list
    count = misused_purposes.count(purpose)
    print(f"  • {purpose} (misused {count} time(s))")

# 4. Show unique purposes intended vs actual
print("\n" + "=" * 60)
print("SUMMARY - UNIQUE PURPOSES:")
print("=" * 60)

print("\nIntended uses:")
for purpose in sorted(set(donations.values())):
    print(f"  • {purpose}")

print("\nActual uses:")
for purpose in sorted(set(actual_use.values())):
    print(f"  • {purpose}")

# Additional analysis: How many donors were affected by misuse?
print("\n" + "=" * 60)
print("IMPACT SUMMARY:")
print("=" * 60)
misused_donors = []
for donor in donations.keys():
    if donations[donor] != actual_use[donor]:
        misused_donors.append(donor)

print(f"Total donors: {len(donations)}")
print(f"Donors affected by misuse: {len(misused_donors)}")
print(f"Misuse percentage: {(len(misused_donors) / len(donations)) * 100:.1f}%")

print("\nAffected donors:")
for donor in misused_donors:
    print(f"  • {donor}")