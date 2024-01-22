# Python-Mini-Projects

## QR Code Generator py_qrcode.py [Link](https://github.com/cfunkz/Python-Mini-Projects/blob/main/py_qrcode.py)

### Description

This Python script generates QR codes using the `qrcode` library. The script prompts the user to input a website or code, generates a QR code for the input, and saves the QR code as an image file. Each generated QR code is uniquely named using a **UUID** to avoid overwriting existing files.

### Usage

1. Run the script.
2. Enter a website URL or code when prompted.
3. The script will generate a QR code and save it as a PNG image with a unique name.
4. Optionally, you can choose to generate another QR code by entering 'Y' when prompted.

### Dependencies

- Python 3.x
- [qrcode](https://pypi.org/project/qrcode/)
- [uuid](https://docs.python.org/3/library/uuid.html)

Or install using ```pip install qrcode, uuid```

## Weather API Call py_weather.py [Link](https://github.com/cfunkz/Python-Mini-Projects/blob/main/py_weather.py)

### Description

This script uses the **requests** library to fetch current weather information from the **wttr.in API**. It prompts to input a location, and then retrieves and displays the weather details using the "F2" view option.

### Information Displayed

- Current condition (e.g., Overcast)
- Temperature (e.g., -2°C)
- Wind speed and direction (e.g., 6 km/h ←)
- Visibility (e.g., 10 km)
- Precipitation (e.g., 0.0 mm)

### Dependencies

- Python 3.x
- [requests](https://pypi.org/project/requests/)

Or install using ```pip install requests```

## Inventory Management inventory_management.py [Link](https://github.com/cfunkz/Python-Mini-Projects/blob/main/inventory_management.py)

### Description

A basic inventory management system coded in Python. The script allows users to add, update, remove, and find items in the inventory.

### Features

- **Add Item:** Add a new item to the inventory by providing the name, barcode, and quantity `add_item("name", "barcode", quantity)`.
- **Update Item:** Update the quantity of an existing item in the inventory. `update_item("barcode or name", quantity)`.
- **Remove Item:** Remove an item from the inventory or decrease its quantity. `remove_item("barcode or name", quantity)`.
- **Find Item:** Search for an item in the inventory using its name or barcode. `find_item("item name or barcode")`.

### Usage

1. Create inventory.json file
2. Run the script.
3. Select an option from the displayed options.

### Dependencies

- Python 3.x
- [uuid](https://docs.python.org/3/library/uuid.html)

Or install using ```pip install uuid```
