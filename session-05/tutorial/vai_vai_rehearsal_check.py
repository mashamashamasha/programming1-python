names = ["Maria", "João", "Ana", "Carlos", "Fatima", "Pedro"]
ages = [24, 16, 17, 17, 31, 15]
positions = ["front", "back", "front", "back", "front", "back"]
has_costume = [True, True, False, True, True, True]

print("=" * 70)
print("VAI-VAI REHEARSAL CHECK")
print("=" * 70)

# Task 1: Validate front dancers
print("\n📋 FRONT DANCER VALIDATION (Age >= 18 required):")
print("-" * 70)

approved_front_dancers = 0

# TODO: Add your code here
for i in range(len(names)):                  # i connects position of name with age/position
    if positions[i] == "front":
        if ages[i] >= 18:
            approved_front_dancers = approved_front_dancers + 1
            print(f"{names[i]} - approved for front")
        else:
            print(f"{names[i]} - disapproved")


# Task 2: Check costume status
print("\n👗 COSTUME INVENTORY CHECK:")
print("-" * 70)

missing_costume = 0
missing_costume_names = []
dancers_with_costume = 0

# TODO: Add your code here
for i in range(len(has_costume)):
    if has_costume[i] == False:
        missing_costume_names.append(names[i])
        missing_costume +=1
    else: 
        dancers_with_costume += 1

print(f"Dancers with complete costume: {dancers_with_costume}/{len(names)}")
if len(missing_costume_names) > 0:
    print(f"⚠️  Missing costumes: {','.join(missing_costume_names)}")

# Task 3: Count dancers by position
print("\n🎭 POSITION BREAKDOWN:")
print("-" * 70)

front_count = 0
backup_count = 0

# TODO: Add your code here
for position in positions:
    if position == "front":
        front_count +=1
    else:
        backup_count +=1
print(f"Front dancers: {front_count}")
print(f"Backup dancers: {backup_count}")

# Task 4: Generate summary report
print("\n" + "=" * 70)
print("FINAL SUMMARY REPORT")
print("=" * 70)

total_dancers = 0
all_have_costume = False

total_dancers = len(names)
all_have_costume = dancers_with_costume == total_dancers

print(f"Total registered dancers: {total_dancers}")
print(f"Approved front dancers: {approved_front_dancers}/{front_count}")
print(f"Dancers with complete costume: {dancers_with_costume}/{total_dancers}")
print(f"Position breakdown: {front_count} front | {backup_count} backup")

# TODO: Add your code here
# Display this messages, depending on the status:
# - \n✨✨✨ READY FOR CARNIVAL! All dancers approved and costumed! ✨✨✨
# - \n⚠️  ISSUES TO RESOLVE before Carnival performance
# - \n⚠️  ACTION NEEDED: 2 dancer(s) need costume!


print("=" * 70)
if dancers_with_costume == total_dancers:
    print("\n✨✨✨ READY FOR CARNIVAL! All dancers approved and costumed! ✨✨✨")
else:
    print("\n⚠️  ISSUES TO RESOLVE before Carnival performance")
    print(f"\n⚠️  ACTION NEEDED: {missing_costume} dancer(s) need costume!")

