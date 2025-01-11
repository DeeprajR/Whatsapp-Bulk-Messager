import os
import time
import logging
import pandas as pd
import traceback
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Get current working directory
working_directory = os.getcwd()

# Create a 'logs' directory if it doesn't exist
log_directory = os.path.join(working_directory, "logs")
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Generate a dynamic log file name (e.g., errorLog_154517052025.txt)
current_time = datetime.now()
log_file_name = current_time.strftime("errorLog_%H%M%d%m%Y.txt")

# Define the full path for the log file
log_file_path = os.path.join(log_directory, log_file_name)

# Configure logging with the generated log file name
logging.basicConfig(
    filename=log_file_path,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print(f"Log file will be saved at: {log_file_path}")

def load_contacts(csv_file):
    """
    Load contacts from a CSV file.
    Logs an error if the file is not found or improperly formatted.
    """
    try:
        data = pd.read_csv(csv_file)
        if 'Phone' not in data.columns:
            raise ValueError("CSV file must contain a 'Phone' column.")
        return data['Phone'].tolist()
    except Exception as e:
        error_message = f"Failed to load contacts: {e}"
        logging.error(f"{error_message}\n{traceback.format_exc()}")
        raise Exception(error_message)

def send_message_via_web(driver, number, message):
    """
    Sends a message via WhatsApp Web.
    Logs an error if the operation fails for any contact.
    """
    try:
        # Open WhatsApp chat for the number
        url = f"https://web.whatsapp.com/send?phone={number}&text={message}"
        driver.get(url)
        
        # Wait for the page to load
        time.sleep(10)
        
        # Find and click the send button
        send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
        send_button.click()
        
        # Wait a bit to ensure the message is sent
        time.sleep(5)
    except Exception as e:
        error_message = f"Failed to send message to {number}: {e}"
        logging.error(f"{error_message}\n{traceback.format_exc()}")
        print(f"Error for {number}: {error_message}. Check {log_file_path} for details.")

def display_estimated_time(start_time, total_contacts, processed_contacts):
    """
    Displays the estimated remaining time for the entire process.
    """
    elapsed_time = time.time() - start_time  # Time elapsed in seconds
    average_time_per_contact = elapsed_time / processed_contacts if processed_contacts else 0
    remaining_contacts = total_contacts - processed_contacts
    
    # Calculate the remaining time
    remaining_time = average_time_per_contact * remaining_contacts
    remaining_minutes = int(remaining_time // 60)
    remaining_seconds = int(remaining_time % 60)

    print(f"Estimated Time Remaining: {remaining_minutes} minutes {remaining_seconds} seconds")

if __name__ == "__main__":
    # Path to your CSV file
    csv_file = "C:\\Users\\"  # Replace with your CSV file path. If Windows OS, use \\ for file directory.
    
    # Message to be sent, use %A%A for line breaker. /n is not parsing in message being send (prolly selenium issue).
    message = (
    "TEXT!%0A%0A"
    "TEXT. "
    "TEXT.%0A%0A"
    "TEXT.:%0A%0A"
    "1. TEXT."
    "2. TEXT.%0A"
    "3. TEXT.%0A%0A"
    "TEXT!%0A%0A"
    "TEXT.%0A%0A"
    "TEXT,%0A"
    "TEXT"
)
    
    # Load contacts from CSV
    try:
        contacts = load_contacts(csv_file)
    except Exception as e:
        print(f"Critical error loading contacts: {e}. Check {log_file_path} for details.")
        exit()

    # Initialize WebDriver
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    except Exception as e:
        error_message = f"ChromeDriver setup failed: {e}"
        logging.error(f"{error_message}\n{traceback.format_exc()}")
        print(f"Critical error: {error_message}. Check {log_file_path} for details.")
        exit()
    
    # Open WhatsApp Web
    try:
        print("Please scan the QR code on WhatsApp Web.")
        driver.get("https://web.whatsapp.com")
        time.sleep(15)  # Wait for the user to scan the QR code
    except Exception as e:
        error_message = f"Error loading WhatsApp Web: {e}"
        logging.error(f"{error_message}\n{traceback.format_exc()}")
        print(f"Critical error: {error_message}. Check {log_file_path} for details.")
        driver.quit()
        exit()

    # Track the start time
    start_time = time.time()
    total_contacts = len(contacts)

    # Send messages to each contact
    for idx, number in enumerate(contacts, start=1):
        try:
            print(f"Sending message to {number} ({idx}/{total_contacts})...")
            send_message_via_web(driver, number, message)

            # Display estimated time for the entire process
            display_estimated_time(start_time, total_contacts, idx)
        
        except Exception as e:
            error_message = f"Error while processing {number}: {e}"
            logging.error(f"{error_message}\n{traceback.format_exc()}")
            print(f"Error with {number}. Check {log_file_path} for details.")
    
    print(f"All messages processed. Check '{log_file_path}' for any errors.")
    driver.quit()
