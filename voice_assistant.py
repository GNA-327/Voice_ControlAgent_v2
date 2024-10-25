import speech_recognition as sr
import pyttsx3
import time
import subprocess
import psutil
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
import re  # To improve URL detection

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to capture voice input
def listen_to_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to User's Command:")
        audio = recognizer.listen(source, timeout=5)
    return audio

# Convert speech to text
def speech_to_text(audio):
    recognizer = sr.Recognizer()
    try:
        command_text = recognizer.recognize_google(audio)
        print(f"You Said: {command_text}")
        return command_text
    except sr.UnknownValueError:
        print("Couldn't understand the audio")
    except sr.RequestError:
        print("Speech recognition service is not available")

# Command parser
def parse_command(command_text):
    command_text = command_text.lower().strip()  # Normalize to lowercase
    if "open" in command_text:
        target = command_text.split("open", 1)[1].strip()
        return {"action": "open", "target": target}
    elif "close" in command_text:
        target = command_text.split("close", 1)[1].strip()
        return {"action": "close", "target": target}
    elif "search" in command_text:
        target = command_text.split("search", 1)[1].strip()
        return {"action": "search", "target": target}
    else:
        return {"action": "unknown"}

# Open a URL in Chrome
def open_url(url):
    os.system(f"open -a 'Google Chrome' {url}")
    provide_feedback(f"Opening {url} in Google Chrome.")

# Improved function to handle URL validation
def is_valid_url(query):
    pattern = re.compile(r"https?://[^\s/$.?#].[^\s]*")
    return pattern.match(query)

# Function to handle dynamic search and URL formation
def search_web(query):
    # Try forming the website URL dynamically
    base_url = f"https://{query}.com"
    
    if is_valid_url(base_url):
        open_url(base_url)
    else:
        # If the URL is invalid, fall back to Google search
        print(f"Failed to open {base_url}, performing a Google search instead.")
        search_google(query)

# Function to search on Google
def search_google(query):
    driver_path = ChromeDriverManager().install()
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Go to Google and search for the query
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    print(f"Searched for {query} on Google.")

    time.sleep(2)  # Wait for results to load
    
    driver.quit()

# Open an application
def open_application(app_name):
    try:
        if app_name == 'chrome':
            subprocess.run(['open', '-a', 'Google Chrome'])
        else:
            subprocess.run(['open', '-a', app_name])
        provide_feedback(f"Opening {app_name}.")
    except Exception as e:
        provide_feedback(f"Failed to open {app_name}. Error: {str(e)}")

# Close an application if it's open
def close_application(app_name):
    try:
        for proc in psutil.process_iter():
            if app_name.lower() in proc.name().lower():
                proc.terminate()
                provide_feedback(f"Closed {app_name}.")
                return
        provide_feedback(f"{app_name} is not running.")
    except Exception as e:
        provide_feedback(f"Failed to close {app_name}. Error: {str(e)}")

# Provide feedback via speech
def provide_feedback(message):
    engine.say(message)
    engine.runAndWait()

# Main loop
def main():
    no_input_counter = 0
    max_no_input_turns = 3  # Number of turns with no voice input before ending

    while True:
        audio = listen_to_voice()
        command_text = speech_to_text(audio)

        if command_text:
            command = parse_command(command_text)

            if command['action'] == 'open':
                open_application(command['target'])  # Open application
            elif command['action'] == 'close':
                close_application(command['target'])  # Close application
            elif command['action'] == 'search':
                search_web(command['target'])  # Handle search commands
            else:
                provide_feedback("Unknown command.")

            no_input_counter = 0  # Reset counter on valid input
        else:
            no_input_counter += 1
            print(f"Turn without input: {no_input_counter}")

        # Check if no input received for consecutive turns
        if no_input_counter >= max_no_input_turns:
            provide_feedback("Hope everything worked out! Goodbye!")
            break

        time.sleep(1)

# Run the main loop
main()
