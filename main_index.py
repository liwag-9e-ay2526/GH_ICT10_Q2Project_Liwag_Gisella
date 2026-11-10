# Coding Club Checker

from pyscript import display, document

def verify_candidate(e):
    document.getElementById('output').innerHTML = ''
    
    first_input = document.getElementById('firstName').value.strip()
    last_input = document.getElementById('lastName').value.strip() 
    full_name = f"{first_input} {last_input}".lower()
    club_members = ["josh ortiz", "maria santos", "juan dela cruz", "anna reyes"]
    is_member = full_name in club_members

    display_message = (
        f"Sorry {first_input} {last_input}, your name is not on the list.", 
        f"Congratulations {first_input} {last_input}! You are now part of the Coding Club."
    )
    
    display(display_message[is_member], target='output')