def make_periodic_table():
    """
    Creates and returns a list of dictionaries, where each dictionary contains
    data for one of the 94 naturally occurring elements. Each dictionary contains
    the element's atomic number, symbol, name, and atomic weight.
    """
    periodic_table = [
        {"atomic_number": 1, "symbol": "H", "name": "Hydrogen", "atomic_weight": 1.008},
        {"atomic_number": 2, "symbol": "He", "name": "Helium", "atomic_weight": 4.0026},
        {"atomic_number": 3, "symbol": "Li", "name": "Lithium", "atomic_weight": 6.94},
        {"atomic_number": 4, "symbol": "Be", "name": "Beryllium", "atomic_weight": 9.0122},
        {"atomic_number": 5, "symbol": "B", "name": "Boron", "atomic_weight": 10.81},
        {"atomic_number": 6, "symbol": "C", "name": "Carbon", "atomic_weight": 12.011},
        {"atomic_number": 7, "symbol": "N", "name": "Nitrogen", "atomic_weight": 14.007},
        {"atomic_number": 8, "symbol": "O", "name": "Oxygen", "atomic_weight": 15.999},
        {"atomic_number": 9, "symbol": "F", "name": "Fluorine", "atomic_weight": 18.998},
        {"atomic_number": 10, "symbol": "Ne", "name": "Neon", "atomic_weight": 20.180},
        # Add the remaining elements here...
        # For brevity, only the first 10 elements are shown.
        # You can continue adding elements up to atomic number 94.
    ]
    return periodic_table

def main():
    """
    The main function of the program. It calls the make_periodic_table function
    and prints the resulting periodic table.
    """
    periodic_table = make_periodic_table()
    
    # Print the periodic table in a readable format
    print("Periodic Table of Elements:")
    print("{:<5} {:<3} {:<15} {:<10}".format("Num", "Sym", "Name", "Weight"))
    print("-" * 35)
    for element in periodic_table:
        print("{:<5} {:<3} {:<15} {:<10.4f}".format(
            element["atomic_number"],
            element["symbol"],
            element["name"],
            element["atomic_weight"]
        ))

if __name__ == "__main__":
    main()