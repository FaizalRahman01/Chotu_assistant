import pyttsx3
import speech_recognition as sr
import webbrowser
import urllib.parse
import datetime
import os
import pyautogui
import time
import platform
import socket
import pywhatkit
from youtubesearchpython import VideosSearch

# Initialize engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Set specific voice manually for consistency
engine.setProperty('voice', voices[0].id)  # 0 = David (Male), 1 = Zira (Female)
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

# Speak function (fast, no threading)
def speak(text):
    print("Chotu: " + text)
    engine.say(text)
    engine.runAndWait()

# Listen from mic
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙 Sun raha hoon...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=4, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            speak("Kuch suna nahi... phir se boliye.")
            return ""

    try:
        query = r.recognize_google(audio, language='en-IN')
        print(f"🗣 Aapne kaha: {query}")
        return query.lower()
    except Exception as e:
        print(f"Error: {e}")
        speak("Samajh nahi paya. Thoda clearly boliye.")
        return ""

def send_whatsapp_message(contact_number, message):
    try:
        speak(f"{contact_number} ko WhatsApp par message bhej raha hoon.")
        pywhatkit.sendwhatmsg_instantly(contact_number, message, 15, True)
    except Exception as e:
        speak("WhatsApp message nahi bhej paya. Error aaya hai.")
        print(f"Error: {e}")

# Open known websites
def open_website(name):
    urls = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "github": "https://github.com",
        "facebook": "https://www.facebook.com",
        "linkedin": "https://www.linkedin.com"
    }
    if name in urls:
        webbrowser.open(urls[name])
        speak(f"{name} khol raha hoon")
    else:
        speak("Website nahi mili.")

# System info
def system_info():
    speak("System information yeh rahi:")
    info = f"""
    System: {platform.system()}
    Node Name: {platform.node()}
    Release: {platform.release()}
    Version: {platform.version()}
    Machine: {platform.machine()}
    Processor: {platform.processor()}
    """
    print(info.strip())
    speak("System details screen par dikha diye hain.")

# Check internet
def check_internet():
    try:
        socket.create_connection(("www.google.com", 80))
        speak("Internet connected hai.")
    except:
        speak("Internet disconnected hai.")

# Handle YouTube/Google search
def handle_contextual_search(query, context):
    global search_results, current_song_index
    for word in ["usme", "dikhawo", "dikhaye", "chalao", "khol", "search", "bajao", "play", "lagao", "sunao", "ka gana"]:
        query = query.replace(word, "")
    search_terms = query.strip()

    if context == "youtube":
        try:
            videosSearch = VideosSearch(search_terms, limit=5)
            result = videosSearch.result()
            search_results = result['result']
            current_song_index = 0
            webbrowser.open(search_results[0]['link'])
            speak(f"YouTube par {search_terms} play kar raha hoon.")
        except Exception as e:
            print(f"Error: {e}")
            speak("YouTube result nahi mila.")
    elif context == "google":
        url = f"https://www.google.com/search?q={urllib.parse.quote_plus(search_terms)}"
        webbrowser.open(url)
        speak(f"Google par {search_terms} dhoondh raha hoon.")
    else:
        speak("Bataye kis platform par search karna hai?")

# Delete Recycle Bin content
def delete_files_in_recycle_bin():
    try:
        os.system('start shell:RecycleBinFolder')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(1)
        pyautogui.press('delete')
        time.sleep(1)
        pyautogui.press('enter')
        speak("Recycle Bin clean kar diya gaya hai.")
    except Exception as e:
        speak("Recycle Bin clean nahi kar paya.")
        print(f"Error: {e}")

def open_app_with_search(app_name):
    try:
        pyautogui.hotkey('win', 's')
        time.sleep(1)
        pyautogui.typewrite(app_name)
        time.sleep(1)
        pyautogui.press('enter')
        speak(f"{app_name} khol raha hoon.")
    except Exception as e:
        speak("App nahi khol paya.")
        print(f"Error: {e}")

def open_whatsapp_chat(contact_name):
    try:
        # WhatsApp open karo
        pyautogui.hotkey('win', 's')
        time.sleep(1)
        pyautogui.typewrite('WhatsApp')
        time.sleep(1)
        pyautogui.press('enter')
        speak("WhatsApp khol raha hoon...")
        
        # App load hone ke liye wait
        time.sleep(8)

        # Search bar open
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)

        # Contact name type and select
        pyautogui.typewrite(contact_name)
        time.sleep(2)
        pyautogui.press('enter')
        speak(f"{contact_name} ka chat khol diya gaya hai.")
    except Exception as e:
        speak("WhatsApp chat nahi khol paya.")
        print(f"Error: {e}")

def send_message_in_whatsapp(message):
    try:
        time.sleep(2)
        pyautogui.typewrite(message)
        pyautogui.press('enter')
        speak("Message bhej diya gaya hai.")
    except Exception as e:
        speak("Message nahi bhej paya.")
        print(f"Error: {e}")

def open_telegram_chat(contact_name):
    try:
        # Telegram open
        pyautogui.hotkey('win', 's')
        time.sleep(1)
        pyautogui.typewrite('Telegram')
        time.sleep(1)
        pyautogui.press('enter')
        speak("Telegram khol raha hoon...")
        
        # App load hone ka wait
        time.sleep(8)

        # Search bar open (Ctrl + K works in Telegram desktop)
        pyautogui.hotkey('ctrl', 'k')
        time.sleep(1)

        # Contact name search and open
        pyautogui.typewrite(contact_name)
        time.sleep(2)
        pyautogui.press('enter')
        speak(f"{contact_name} ka chat khol diya gaya hai.")
    except Exception as e:
        speak("Telegram chat nahi khol paya.")
        print(f"Error: {e}")

# Main loop
def main():
    global search_results, current_song_index, current_context
    current_context = None
    search_results = []
    current_song_index = 0
    
    speak("Namaste! Mai aapka virtual assistant Chotu. Kaise madad kar sakta hoon?")
    
    while True:
        query = take_command().strip()

        if not query:
            continue
            
        elif "exit" in query or "band kar" in query or "bye" in query:
            speak("Chalo bhai, alvida!")
            break
            
        elif "youtube" in query:
            webbrowser.open("https://www.youtube.com")
            current_context = "youtube"
            time.sleep(2)  # Wait for YouTube to load
        elif "youtube music" in query or "music youtube" in query or "yt music" in query:
            webbrowser.open("https://music.youtube.com")
            current_context = "ytmusic"
            speak("YouTube Music khol diya gaya hai.")

            
        elif any(word in query for word in ["change song", "next song", "gana badlo", "dusra gana", "agli video", "song change"]):
            if current_context == "youtube" and search_results:
                current_song_index += 1
                if current_song_index < len(search_results):
                    # Switch to YouTube tab and stop current song
                    pyautogui.hotkey('ctrl', '1')  # Switch to first tab
                    time.sleep(1)
                    pyautogui.press('k')  # Space to pause current video
                    time.sleep(0.5)
                    # Refresh to stop completely and load new URL
                    pyautogui.hotkey('ctrl', 'r')
                    time.sleep(2)
                    # Focus address bar and paste new URL
                    pyautogui.hotkey('ctrl', 'l')
                    pyautogui.hotkey('ctrl', 'a')
                    pyautogui.press('delete')
                    pyautogui.typewrite(search_results[current_song_index]['link'])
                    pyautogui.press('enter')
                    speak("Naya gana play kar raha hoon: " + search_results[current_song_index]['title'])
                else:
                    speak("Aur gana nahi hai playlist mein")
            else:
                speak("Pehle koi gana play kijiye")
                
        elif "volume up" in query or "volume badhao" in query or "awaz jyada karo" in query:
            # Increase system volume
            pyautogui.press('volumeup')
            # Also increase speech volume
            vol = min(1.0, engine.getProperty('volume') + 0.1)
            engine.setProperty('volume', vol)
            speak("Volume badha diya gaya hai")
            
        elif "volume down" in query or "volume kam" in query or "awaz kam karo" in query:
            # Decrease system volume
            pyautogui.press('volumedown')
            # Also decrease speech volume
            vol = max(0.0, engine.getProperty('volume') - 0.1)
            engine.setProperty('volume', vol)
            speak("Volume kam kar diya gaya hai")
            
        elif "main screen" in query or "home screen" in query or "desktop dikhao" in query or "screen pe le jao" in query:
            pyautogui.hotkey('win', 'd')
            speak("Main screen dikh rahi hai.")

        elif "select all" in query or "sabhi chune" in query or "sab select" in query:
            pyautogui.hotkey('ctrl', 'a')
            speak("Sabhi files select kar li gayi hain.")
            
        elif "delete all" in query or "delete selected" in query or "sab delete" in query:
            pyautogui.press('delete')
            time.sleep(1)
            pyautogui.press('enter')
            speak("Selected files delete kar diya gaya hai.")

        elif "open" in query or "start" in query or "chalu karo" in query:
            app_list = {
                "vs code": "Visual Studio Code",
                "whatsapp": "WhatsApp",
                "telegram": "Telegram",
                "notepad": "Notepad",
                "calculator": "Calculator",
                "chrome": "Google Chrome",
                "file explorer": "File Explorer",
                "pycharm": "PyCharm",
                "intellij": "IntelliJ IDEA",
                "android studio": "Android Studio",
                "sublime": "Sublime Text",
                "notepad plus": "Notepad++",
                "firefox": "Mozilla Firefox",
                "edge": "Microsoft Edge",
                "opera": "Opera",
                "brave": "Brave",
                "this pc": "This PC",
                "cmd": "Command Prompt",
                "powershell": "Windows PowerShell",
                "terminal": "Windows Terminal",
                "control panel": "Control Panel",
                "paint": "Paint",
                "word": "Microsoft Word",
                "excel": "Microsoft Excel",
                "powerpoint": "Microsoft PowerPoint",
                "onenote": "Microsoft OneNote",
                "teams": "Microsoft Teams",
                "skype": "Skype",
                "zoom": "Zoom",
                "vlc": "VLC media player",
                "spotify": "Spotify",
                "itunes": "iTunes",
                "photoshop": "Adobe Photoshop",
                "illustrator": "Adobe Illustrator",
                "premiere": "Adobe Premiere Pro",
                "after effects": "Adobe After Effects",
                "lightroom": "Adobe Lightroom",
                "xd": "Adobe XD",
                "acrobat": "Adobe Acrobat Reader",
                "git": "Git Bash",
                "docker": "Docker Desktop",
                "virtualbox": "Oracle VM VirtualBox",
                "vmware": "VMware Workstation",
                "obs": "OBS Studio",
                "discord": "Discord",
                "slack": "Slack",
                "postman": "Postman",
                "mysql": "MySQL Workbench",
                "mongodb": "MongoDB Compass",
                "anaconda": "Anaconda Navigator",
                "jupyter": "Jupyter Notebook",
                "pyqt designer": "Qt Designer",
                "task manager": "Task Manager"
            }
            found = False
            for key, value in app_list.items():
                if key in query:
                    open_app_with_search(value)
                    found = True
                    break
            if not found:
                speak("Kaunsa application kholna hai?")

        elif "whatsapp" in query and ("message" in query or "bhejo" in query):
            speak("Kisko message bhejna hai?")
            name = take_command()
            if name:
                open_whatsapp_chat(name)
                speak("Kya message bhejna hai?")
                msg = take_command()
                if msg:
                    send_message_in_whatsapp(msg)

        elif "whatsapp" in query and any(word in query for word in ["open", "khol", "start"]):
            open_app_with_search("WhatsApp")
            current_context = "whatsapp"
            speak("WhatsApp khul gaya hai. Kisko message bhejna hai?")

        elif "telegram" in query and any(word in query for word in ["open", "khol", "start"]):
            open_app_with_search("Telegram")
            current_context = "telegram"
            speak("Telegram khul gaya hai. Kisko message bhejna hai?")

        elif current_context == "whatsapp" and ("message" in query or "bhejo" in query or "ko" in query):
            name = query.replace("message", "").replace("bhejo", "").replace("ko", "").strip()
            if not name:
                speak("Kisko message bhejna hai?")
                name = take_command()
            if name:
                open_whatsapp_chat(name)
                speak("Kya message bhejna hai?")
                msg = take_command()
                if msg:
                    send_message_in_whatsapp(msg)

        elif "kya haal hai" in query or "kaise ho" in query:
            speak("Main bilkul badiya hoon bhai, aap kaise ho?")
            
        elif "kya kar rahe ho" in query:
            speak("Main aapka intezar kar raha tha, kuch command do bhai.")
            
        elif "thank you" in query or "dhanyawad" in query or "shukriya" in query:
            speak("Aapka swagat hai bhai.")
            
        elif "hello" in query or "hi chotu" in query or "namaste" in query:
            speak("Hello bhai, kaise ho?")
            
        elif "good morning" in query:
            speak("Good morning bhai, aapka din shubh ho.")
            
        elif "good night" in query:
            speak("Good night bhai, acche se sona.")
            
        elif "how are you" in query:
            speak("I'm doing great bhai, thank you for asking!")
            
        elif "i love you" in query:
            speak("Main bhi aapko pasand karta hoon bhai, par main sirf ek program hoon.")

        elif "google" in query:
            open_website("google")
            current_context = "google"
            
        elif "github" in query:
            open_website("github")
            current_context = "github"
            
        elif "system info" in query or "system information" in query:
            system_info()
            
        elif "time" in query or "samay" in query:
            speak("Time hai " + datetime.datetime.now().strftime("%I:%M %p"))
            
        elif "date" in query or "tareekh" in query:
            speak("Aaj hai " + datetime.date.today().strftime("%d %B, %Y"))

        elif "pause song" in query or "pause video" in query or "gana pause" in query:
            pyautogui.press('k')
            speak("Gana pause kar diya gaya hai.")
        
        elif "resume song" in query or "resume video" in query or "gana chalu" in query or "gana resume" in query or "play song" in query:
            pyautogui.press('k')
            speak("Gana phir se chalu kar diya gaya hai.")
   
        elif "internet" in query or "connection" in query:
            check_internet()
                
        elif any(word in query for word in ["search", "dikh", "chalao", "khol", "play", "bajao", "lagao", "sunao", "ka gana"]):
            handle_contextual_search(query, current_context)
            
        elif "recycle bin delete" in query or "recycle bin clean" in query or "recycle bin saaf" in query:
            delete_files_in_recycle_bin()
            
        elif current_context == "ytmusic":
            search_terms = query.replace("play", "").replace("song", "").strip()
            url = f"https://music.youtube.com/search?q={urllib.parse.quote_plus(search_terms)}"
            webbrowser.open(url)
            speak(f"YouTube Music par {search_terms} search kar raha hoon.")
    
        else:
            speak("Yeh command mujhe samajh nahi aayi. Phir se try kijiye.")

if __name__ == "__main__":
    main()
