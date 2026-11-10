# ICT Drill 2: Working With Sets and Set Operators

from pyscript import document, display

grade7 = {'Aubrey Graham', 'Rakim Mayers', 'Jahron Brathwaite'}
grade8 = {'Abel Tesfaye', 'Jacques Webster', 'Dominic Fike'}
grade9 = {'Solána Rowe', 'Shayaa Joseph', 'Tyler Okonma', 'Belcalis Almánzar'}
grade10 = {'Onika Maraj', 'Marshall Mathers', 'Stefani Germanotta', 'Belén Aguilera'}

def add_member(event):
    first_name = document.getElementById('fname').value
    last_name = document.getElementById('lname').value
    
    full_name = first_name + " " + last_name
    new_member_set = {full_name}
    
    master_set = grade7 | grade8 | grade9 | grade10 | new_member_set
    total_members = len(master_set)
    
    document.getElementById('output').innerHTML = f"""
        <h3>All members:</h3>
        <p>{master_set}</p>
        <h3>Total members: {total_members}</h3>
    """