import qrcode
import uuid


def generate_random_name():
    # Generate a UUID
    unique_id = uuid.uuid4()
    # Convert the UUID to a string and remove hyphens
    name = str(unique_id).replace('-', '')
    return name


def generate_qr(data: str):
    loop = True
    while loop:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        name = generate_random_name()
        img.save(f"{name}.png")
        print(f"Successfully printed {name}.png")
        question = input("Print another one? (Enter Y/N): ")
        if question.upper() == "N":
            loop = False


try:
    data = input("Enter a website or code: ")
    generate_qr(data)
except Exception as e:
    print(f"An error occurred: {e}")
