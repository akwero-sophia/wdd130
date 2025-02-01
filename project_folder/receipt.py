import csv

def read_dictionary(filename, key_column_index):
    """
    Reads the contents of a CSV file into a dictionary and returns the dictionary.

    Parameters:
        filename (str): The name of the CSV file to read.
        key_column_index (int): The index of the column to use as the keys in the dictionary.

    Returns:
        dict: A dictionary where the keys are values from the key_column_index and the values are lists of row data.
    """
    dictionary = {}
    try:
        with open(filename, "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip the header row
            for row in reader:
                if len(row) > key_column_index:
                    key = row[key_column_index]
                    dictionary[key] = row
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except PermissionError:
        print(f"Error: Permission denied to access {filename}.")
    except Exception as ex:
        print(f"Error: {ex}")
    return dictionary

def main():
    """
    The main function of the program. It reads the product catalog and customer request,
    processes the order, and prints a receipt.
    """
    # Read the product catalog into a dictionary
    products_dict = read_dictionary("products.csv", 0)

    # Read the customer request into a list
    request_list = []
    try:
        with open("request.csv", "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip the header row
            for row in reader:
                request_list.append(row)
    except FileNotFoundError:
        print("Error: The file request.csv was not found.")
        return
    except PermissionError:
        print("Error: Permission denied to access request.csv.")
        return
    except Exception as ex:
        print(f"Error: {ex}")
        return

    # Process the customer request and print the receipt
    print("\nReceipt:")
    print("----------------------------------------")
    total_items = 0
    total_price = 0.0

    for item in request_list:
        product_number = item[0]
        quantity = int(item[1])

        if product_number in products_dict:
            product = products_dict[product_number]
            product_name = product[1]
            product_price = float(product[2])
            total_items += quantity
            total_price += quantity * product_price
            print(f"{product_name}: {quantity} @ ${product_price:.2f}")
        else:
            print(f"Error: Product {product_number} not found in catalog.")

    print("----------------------------------------")
    print(f"Total Items: {total_items}")
    print(f"Total Price: ${total_price:.2f}")
    print("----------------------------------------")

if __name__ == "__main__":
    main()
    