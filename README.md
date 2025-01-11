# WhatsApp Bulk Message Sender

This project is a Python script that automates the process of sending bulk messages via WhatsApp Web using Selenium WebDriver. The script reads phone numbers from a CSV file, sends a predefined message to each contact, and logs any errors encountered during the process.

## Features
- Reads contacts from a CSV file.
- Automates message sending via WhatsApp Web.
- Logs errors to a dynamically generated log file.
- Estimates and displays the remaining time for the process.

## Prerequisites
- Python 3.x
- Google Chrome
- ChromeDriver
- `selenium` library
- `pandas` library
- `webdriver-manager` library

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install required Python packages**
   ```bash
   pip install selenium pandas webdriver-manager
   ```

3. **Download ChromeDriver**
   ChromeDriver should be compatible with your version of Chrome. The `webdriver-manager` package will handle this automatically.

## Usage

1. **Prepare your CSV file**
   - The CSV file should contain a column named `Phone` with the phone numbers.
   - Example CSV format:
     ```csv
     Name,Phone
     John Doe,+1234567890
     Jane Doe,+0987654321
     ```

2. **Edit the script**
   - Update the `csv_file` variable with the path to your CSV file.
   - Customize the `message` variable with your desired message.

3. **Run the script**
   ```bash
   python <script-name>.py
   ```

4. **Scan the QR code**
   - The script will open WhatsApp Web. Scan the QR code with your mobile device to log in.

5. **Monitor the process**
   - The script will send messages to each contact and display the estimated remaining time.

6. **Check logs**
   - Errors will be logged in a `logs` directory with a timestamped log file.

## Logging

- Logs are saved in the `logs` directory with a filename format like `errorLog_HHMMDDMMYYYY.txt`.
- Logs contain detailed error messages and stack traces.

## Warning

The sole responsibility to abide by WhatsApp's rules and regulations rests with the user. The use of this script should comply with WhatsApp's terms of service and any applicable laws. Misuse of this tool may result in the suspension of your WhatsApp account.

## Troubleshooting

- **ChromeDriver setup failed:** Ensure Chrome is installed and up-to-date.
- **Failed to load contacts:** Ensure the CSV file is correctly formatted with a `Phone` column.
- **Error sending message:** Check if the phone number is valid and if the message format is correct.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- [Selenium](https://www.selenium.dev/) - Browser automation.
- [webdriver-manager](https://github.com/SergeyPirogov/webdriver_manager) - Manages browser drivers.
