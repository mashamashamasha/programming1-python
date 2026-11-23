resources = {}
speakers = []

# --- Add function definition for add_to_march_plan ---
def add_to_march_plan(*name, **logistics):
    for key, value in logistics.items():
        if key in resources.keys():
            resources[key] += value
        else: 
            resources[key] = value
    speakers.extend(name)

# --- function definition for the output ---
def build_march_plan(speakers, resources):
    print("--- 📢 OFFICIAL MARCH ON WASHINGTON PROGRAM 📢 ---")
       
    print("\nOrder of Events:")
    for speaker in speakers:
        print(f"  - Speech by: {speaker}")
    
    print("\nLogistics Checklist:")
    for item, quantity in resources.items():
        print(f"  - {item.replace('_', ' ').title()}: {quantity}")


# --- Add speakers and logistics ---
add_to_march_plan('Martin Luther King', sound_system="High Power", water_bottles=500)
add_to_march_plan('John Lewis', first_aid_kits=5, portable_toilets=10)
add_to_march_plan('Diane Nash', 'Ella Baker', security_personnel=15, banners=20, food_trucks=3, volunteers=50, water_bottles=300)

# --- Call the function ---
build_march_plan(speakers, resources)

"""     MUSTER      MUSTER      MUSTER      """

resources = {}
speakers = []

def add_to_march_plan(*activists, **logistics):
    """Add a speaker and logistics to the march plan."""
    # 1. Process arbitrary speakers (*args)
    for activist in activists:
        speakers.append(activist)
    # 2. Process arbitrary logistics (**kwargs)
    for key, value in logistics.items():
        if key in resources.keys():
            resources[key] += value
        else: 
            resources[key] = value

def build_march_plan(speakers, resources):
    print("--- 📢 OFFICIAL MARCH ON WASHINGTON PROGRAM 📢 ---")
       
    print("\nOrder of Events:")
    for speaker in speakers:
        print(f"  - Speech by: {speaker}")
    
    print("\nLogistics Checklist:")
    for item, quantity in resources.items():
        print(f"  - {item.replace('_', ' ').title()}: {quantity}")


# --- Add speakers and logistics ---
add_to_march_plan(
    'Martin Luther King', 
    sound_system="High Power", water_bottles=500
    )
add_to_march_plan('John Lewis', first_aid_kits=5, portable_toilets=10)
add_to_march_plan(
    'Diane Nash', 'Ella Baker', 
    security_personnel=15, banners=20, food_trucks=3, 
    volunteers=50, water_bottles=200
    )

# --- Call the function ---
build_march_plan(speakers, resources)