from pyscript import display, document

# 1. List containing ICT club members
club_members = [
    "Mateo Salacup",
    "Mandy Cajanding",
    "Maggie Chiong",
    "Cianna Del Prado",
    "Julia Bermudez",
    "Jacque Tian",
    "Myka Dela Rosa"
]

def check_membership(event=None):
    # Retrieve values directly using pyscript's document object
    first_name = document.querySelector("#first-name").value.strip()
    last_name = document.querySelector("#last-name").value.strip()
    
    # 3. Combine into one full name with title case formatting
    full_name = f"{first_name} {last_name}".title()
    
    # 4. Check whether full name is in club members list (returns True/False)
    is_member = full_name in club_members
    
    # 5. Message options (No conditional statements or loops used)
    # Tuple indexing: 0 = False, 1 = True
    messages = (
        f"Sorry {full_name}, your name is not on the list.",
        f"Congratulations {full_name}! You are now part of the ICT club."
    )
    
    # Select message using boolean indexing
    result_text = messages[is_member]
    
    # Render result cleanly inside the target container using display()
    display(result_text, target="result", append=False)

# Attach click event listener to the button
document.querySelector("#check-btn").onclick = check_membership