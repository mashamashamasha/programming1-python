import random

year = 1790
supporters = 1

campaign_active = True

while campaign_active:
    # time passes
    pass
    year += 1
    # you can win support over time
    supporters += random.randint(5, 20)

    # war in France distracts Parliament
    pass
    if 1793<=year<=1802:
        #would be better to put it here
        #if year == 1801:
                #mps_present += 100
                #supporters +=90
        continue
        
    # Randomly simulate how many MPs actually showed up to work that day
    mps_present = random.randint(300, 600)
    needed_to_win = (mps_present // 2) + 1                                # two // gives non float result
    print(f"Year {year}: {mps_present} MPs present. We need {needed_to_win} votes.")

    # A big boost in support due to the Act of Union
    pass
    if year == 1801:
        #mps_present += 100
        supporters +=90

    # Now let's cast our votes!
    if supporters >= needed_to_win:
        print(f"SUCCESS! We got {supporters} votes. The Act is passed!")
        campaign_active = False # This acts like a 'break'
    else:
        print(f"Defeat. We only had {supporters} votes. The struggle continues...")
    
    if year > 1810: # Safety value for the loop
        break