# Mother Teresa starts with these items
ledger = {
    'bandages': 50,
    'aspirin': 100,
    'clean water': 20
}

ledger['blankets'] = 5

ledger['bandages'] -= 10
#doesn't go negative | get prevents from "error" and gives 2nd answer (0) | min chooses between what we have and 10 
#ledger['bandages'] = ledger.get('bandages', 0) - min(ledger.get('bandages', 0),10)

del ledger['aspirin']

print("Do we still have aspirin?")
#if ledger['antibiotics'] > 0 => eine Fehler (es gibt kein antibiotics)
if "antibiotics" in ledger.keys() and ledger['antibiotics'] > 0:
    print("Yes, we have")
else: 
    print("No, we have not")

if ledger['clean water'] < 30:
    print("\nI shall organize water")
