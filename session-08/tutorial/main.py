import press_office as pm

release = pm.create_press_release("A Historic Day for Justice", "I am happy to join with you today", "Nineteen sixty-three is not an end",
                        "I have a dream", 
                        attendance=250000, 
                        location="Lincoln Memorial", 
                        organizer="Bayard Rustin")

print(f"HEADLINE: {release['headline']}")
print(f"TRANSCRIPT: {release['transcript']}")
print(f"EVENT DATA:", end = "")
for key, value in release['data'].items():
    print(f"{key.title()}: {value},", end = " ") #by default end = "\n"

# print(f"HEADLINE: {release['headline']}")
# print(f"TRANSCRIPT: {release['transcript']}")
# print(f"EVENT DATA: {release['data']}")


##by print(release)would show all \n without making space 