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
