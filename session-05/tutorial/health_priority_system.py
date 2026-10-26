# Test case 1: High fever with coughing
patient_temp = 39.2
is_coughing = True

# Symbols to copy: 🔴🟡🟢

# {} creates a set, which always will be True unless it's emrty, DIFFRENT with f-String

if patient_temp < 38 and is_coughing == False:
    message = "🟢 HOME - low fever"
    recommendation = "Rest and hydrate."
elif patient_temp < 38 and is_coughing == True:
    message = "🟡 STANDARD - cough"
    recommendation = "Hand-over dragees."
elif 38 <= patient_temp < 39 and is_coughing == False:
    message = "🟡 STANDARD - moderate fever"
    recommendation = "Book appointment."
elif 38 <= patient_temp < 39 and is_coughing == True:
    message = "🔴 URGENT - possible pneumonia"
    recommendation = "See doctor immediately for respiratory check."
else:
    message = "🔴 URGENT - high fever"
    recommendation = "See doctor immediately."


print(f"Temperature: {patient_temp}°C, Coughing: {is_coughing}")
print(f"{message}")
print(f"Recommendation: {recommendation}")
