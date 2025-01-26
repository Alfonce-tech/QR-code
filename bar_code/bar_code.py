import barcode
from barcode.writer import ImageWriter
import os

def generate_barcode(serial_number, file_path):
    """
    Generate a barcode for the given serial number and save it to the specified file path.

    Args:
        serial_number (str): The serial number to encode in the barcode.
        file_path (str): The path to save the barcode image.
    """
    CODE128 = barcode.get_barcode_class('code128')
    barcode_obj = CODE128(serial_number, writer=ImageWriter())
    barcode_obj.save(file_path)


def main():
    """Main function to generate and track inventory with barcodes."""
    inventory = {
        "item001": {"serial_number": "SN123456", "status": "available"},
        "item002": {"serial_number": "SN789012", "status": "available"},
        "item003": {"serial_number": "SN345678", "status": "available"},
    }

    output_directory = "barcodes"
    os.makedirs(output_directory, exist_ok=True)

    for item_id, item_details in inventory.items():
        serial_number = item_details["serial_number"]
        file_name = f"{item_id}.png"
        file_path = os.path.join(output_directory, file_name)
        generate_barcode(serial_number, file_path)
        print(f"Barcode for {item_id} with serial number {serial_number} saved at {file_path}")

    # Simulating a sale
    sold_item = "item001"
    if sold_item in inventory:
        inventory[sold_item]["status"] = "sold"
        print(f"{sold_item} has been sold. Status updated.")

if __name__ == "__main__":
    main()
