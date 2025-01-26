import qrcode
import os

def generate_qr_code(data, file_path):
    """
    Generate a QR code and save it to the specified file path.

    Args:
        data (str): The data to encode in the QR code.
        file_path (str): The path to save the QR code image.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)


def main():
    """Main function to generate multiple QR codes."""
    inventory_items = {
        "item001": "Product A details",
        "item002": "Product B details",
        "item003": "Product C details",
    }

    output_directory = "qr_codes"
    os.makedirs(output_directory, exist_ok=True)

    for item_id, details in inventory_items.items():
        file_name = f"{item_id}.png"
        file_path = os.path.join(output_directory, file_name)
        generate_qr_code(details, file_path)
        print(f"QR code for {item_id} saved at {file_path}")

if __name__ == "__main__":
    main()