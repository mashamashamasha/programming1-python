# The available buses
bus_schedule = [
    {"bus_id": "A", "time": "10:00 AM"},
    {"bus_id": "B", "time": "10:30 AM"}
]

def generate_tickets(names):
    """Generate tickets for the Freedom Riders."""
    all_tickets = []
    for index, name in enumerate(names):
        passenger_num = index + 1  # Humans count from 1, not 0! index for the first one is 0
        if passenger_num > 20:
            ticket = {
            "name": name,
            "departure": bus_schedule[1]['time'],
        "ticket_id": f"FREEDOM-{100 + passenger_num}"}
        else:
            ticket = {
            "name": name,
            "departure": bus_schedule[0]['time'],
            "ticket_id": f"FREEDOM-{100 + passenger_num}"
            
}       
        all_tickets.append(ticket)
        
    return all_tickets

# --- Test your software ---
volunteers = ["John Lewis", "Diane Nash", "Jim Zwerg", "Bernard Lafayette"] 
# (In a real test, try a list with 25 names!)
tickets = generate_tickets(volunteers) #return VALUE to a VARIABLE tickets
print(tickets)
# t is a dict from list tickets (returned value is a list named "all_ticket")
for t in tickets:
    print(f"Passenger: {t['name']} | Time: {t['departure']} | ID: {t['ticket_id']}")