Voice Control Assistant
This Python-based voice control assistant allows you to interact with your computer through voice commands. It supports opening and closing applications, searching websites, and provides feedback via text-to-speech. The assistant can open URLs directly, search Google when needed, and even handle applications on the user's system.

Features
Voice recognition: Converts spoken commands into text.
Web Search: Dynamically searches the web or directly opens websites.
Application Control: Opens and closes applications on your local machine.
Text-to-Speech Feedback: Provides verbal feedback to the user.
Auto Exit on Silence: Automatically exits after three consecutive turns without valid voice input.
Prerequisites
To run the voice assistant on your local computer, you'll need:

Python 3.x: Download and install the latest version of Python from here.
Google Chrome: Install Google Chrome for web searching.
Selenium WebDriver: Install the Chrome WebDriver to automate Google Chrome actions.
Packages: The required Python packages are listed below.
Setup Instructions
1. Install Python
Make sure you have Python installed by running the following command:

bash
Copy code
python --version
If Python is not installed, download and install it from the Python official website.

2. Install Required Packages
You need to install the following Python libraries:

speech_recognition: For voice input
pyttsx3: For text-to-speech feedback
selenium: For web automation
psutil: For managing system processes
webdriver-manager: For managing WebDriver installations
To install these, run:

bash
Copy code
pip install speechrecognition pyttsx3 selenium psutil webdriver-manager
3. Install Google Chrome and ChromeDriver
Make sure you have Google Chrome installed on your system. To install ChromeDriver (which is needed for Selenium), run:

bash
Copy code
pip install webdriver-manager
webdriver-manager will automatically manage the correct version of ChromeDriver needed for your system.

4. Code Configuration
Ensure that you have the following script saved as voice_assistant.py or a name of your choice. Make sure you have the necessary permissions to run it.

5. Running the Assistant
Once you've set up everything, you can run the assistant using the command:

bash
Copy code
python voice_assistant.py
6. Usage
Once the program starts running, it will listen for your voice commands. The following commands are supported:

Open an application: Say, for example, "Open Chrome".
Close an application: Say, for example, "Close Chrome".
Search the web: Say, for example, "Search Facebook" to either open Facebook directly or perform a Google search.
Auto-exit: If the assistant doesn't receive a valid command after three consecutive tries, it will exit automatically and provide a farewell message.
7. Customizing the Project
Add more applications: You can modify the open_application() and close_application() functions to handle more apps on your system.
Change exit threshold: The number of turns for which no input is received before exiting can be changed by adjusting the max_no_input_turns variable in the code.
8. Known Issues
The program relies on Google Chrome for web searches, so it requires an active Chrome installation.
The open_url() function uses the os.system() command to open applications, which may not work universally across operating systems (it's designed for macOS in the current version).
Future Improvements
Add support for Windows and Linux for opening/closing applications.
Improve error handling for invalid voice inputs.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
Developed by Abhinav Swaminathan

