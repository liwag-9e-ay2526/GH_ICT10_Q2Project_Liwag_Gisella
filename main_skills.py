# Periodic Table Information Finder

from pyscript import document

non_metals = {
    "H": ("Hydrogen", 1, 1.008),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "I": ("Iodine", 53, 126.90),
    "He": ("Helium", 2, 4.0026),
    "Ne": ("Neon", 10, 20.180),
    "Ar": ("Argon", 18, 39.948),
    "Kr": ("Krypton", 36, 83.798),
    "Xe": ("Xenon", 54, 131.29),
    "Rn": ("Radon", 86, 222)
}

def search_element(event):
    user_input = document.querySelector("#symbolInput").value.strip()
    symbol = user_input.capitalize() if len(user_input) == 2 else user_input.upper()
    output_div = document.querySelector("#output")

    try:
        name, atomic_num, atomic_mass = non_metals[symbol]
        output_div.innerHTML = f"""
            <strong>Symbol:</strong> {symbol} <br>
            <strong>Element Name:</strong> {name} <br>
            <strong>Atomic Number:</strong> {atomic_num} <br>
            <strong>Atomic Mass:</strong> {atomic_mass}
        """
    except KeyError:
        output_div.innerHTML = "<em>Element does not exist in the non-metals list.</em>"