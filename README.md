# Python-Mini-Projects

## py_qrcode.py

### Description

This Python script (`py_qrcode.py`) generates QR codes using the `qrcode` library. The script prompts the user to input a website or code, generates a QR code for the input, and saves the QR code as an image file. Each generated QR code is uniquely named using a **UUID** to avoid overwriting existing files.

### Usage

1. Run the script.
2. Enter a website URL or code when prompted.
3. The script will generate a QR code and save it as a PNG image with a unique name.
4. Optionally, you can choose to generate another QR code by entering 'Y' when prompted.

### Dependencies

- [qrcode](https://pypi.org/project/qrcode/)
- [uuid](https://docs.python.org/3/library/uuid.html)

### How to Run

```bash
python py_qrcode.py
```

## py_weather.py

### Description

This script uses the **requests** library to fetch current weather information from the **wttr.in API**. It prompts to input a location, and then retrieves and displays the weather details using the "F2" view option.

### Information Displayed

-Current condition (e.g., Overcast)
-Temperature (e.g., -2°C)
-Wind speed and direction (e.g., 6 km/h ←)
-Visibility (e.g., 10 km)
-Precipitation (e.g., 0.0 mm)

### Requirements

1. Python 3.x
2. requests library (install it using pip install requests)
