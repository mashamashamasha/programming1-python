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

# Setup
print("--- Slave Trade Abolition Sentiment Tracker (1791) ---")
MP_name = input("Enter the MP's name: ")

objections = {}
score = 0
question_number = 1

# Using a While Loop to process the 7 questions
while question_number <= 7:
    current_q, category = questions[question_number - 1]
    
    answer = input(f"Q{question_number}: {current_q} (yes/no): ").lower().strip()
    
    if answer == 'yes':
        score += 1
    else:
        # If they say 'no', we document their objection category
        objections[category] = "Negative/Unconvinced"
        
    question_number += 1

# --- The Results Logic ---
print(f"\n--- Final Report for MP {MP_name} ---")
print(f"Supporter Score: {score}/7")

if score >= 6:
    print("ACTION: Invite this MP to the secret planning meeting at the Clapham Sect immediately!")

elif 3 <= score < 6:
    print(f"ACTION: Sending report to William Wilberforce...")
    print(f"Subject: Campaign Strategy for {MP_name}")
    print(f"Note: William, you still need to convince them on: {list(objections.keys())}")

else:
    print("RESULT: This person is a villain of history. Do not waste our limited pamphlets on them.")