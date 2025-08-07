# Chotu - Advanced Voice Assistant 🤖

Chotu is an intelligent voice assistant built in Python that can perform various tasks through voice commands. It can search YouTube for songs, control applications, send messages, and much more! This project demonstrates advanced speech recognition, natural language processing, and system automation capabilities.

## 🎯 Project Overview

Chotu is designed to be your personal digital assistant that understands both Hindi and English commands. With its advanced contextual understanding and smart automation features, it can help you navigate your computer, control applications, play music, send messages, and perform various system operations - all through simple voice commands.

## ✨ Key Features

### 🎤 **Advanced Voice Recognition**
- Real-time speech-to-text conversion using Google Speech Recognition
- Support for both Hindi and English commands
- Noise cancellation and ambient sound adjustment
- Custom voice response with adjustable speed and volume

### 🎵 **Smart Music & Entertainment**
- YouTube integration with contextual search
- YouTube Music support
- Play, pause, resume, and skip songs with voice commands
- Smart song search using artist names and song titles
- Volume control through voice commands

### 💬 **Communication Features**
- WhatsApp desktop integration for sending messages
- Telegram desktop integration for chat management
- Voice-to-text message composition
- Contact search and chat opening

### 🖥️ **System Control & Automation**
- Open any installed application through voice commands
- System information retrieval
- File management operations (select all, delete, etc.)
- Recycle bin management
- Desktop navigation and window management
- Internet connectivity checking

### 🌐 **Web Integration**
- Google search with voice queries
- Website opening and navigation
- Context-aware search functionality
- URL handling and web automation

### 🧠 **Intelligent Context Management**
- Remembers current application context
- Contextual command processing
- Smart query interpretation
- Multi-step task execution

## 🎵 Example Usage Scenarios

```
User: "Open YouTube"
Chotu: Opens YouTube in browser

User: "Usme Arijit Singh ka gana chalao"
Chotu: Searches and plays Arijit Singh songs on YouTube

User: "WhatsApp kholo"
Chotu: Opens WhatsApp desktop application

User: "Mom ko message bhejo"
Chotu: Opens Mom's chat and asks for message content

User: "Volume badhao"
Chotu: Increases system volume

User: "Time kya hai?"
Chotu: Tells current time in Hindi/English
```

## 🏗️ System Architecture

```
📊 Insert Architecture Diagram Here 📊
(A detailed system architecture diagram showing the flow from 
voice input to command execution through various processing layers)
```

### Architecture Components:
1. **Voice Interface Layer** - Handles speech recognition and text-to-speech
2. **Natural Language Processing** - Parses commands and extracts intent
3. **Context Management** - Maintains application state and context
4. **Command Processing** - Routes commands to appropriate handlers
5. **Integration Layer** - Interfaces with external applications and APIs
6. **System Control** - Manages system-level operations and automation

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7 or higher
- Microphone for voice input
- Speakers/headphones for voice output
- Internet connection for web features

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/chotu-voice-assistant.git
   cd chotu-voice-assistant
   ```

2. **Create virtual environment (recommended)**
   ```bash
   python -m venv chotu_env
   source chotu_env/bin/activate  # On Windows: chotu_env\Scripts\activate
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Required Dependencies**
   ```bash
   pip install pyttsx3 speechrecognition webbrowser pyautogui pywhatkit youtubesearchpython
   ```

### Additional Setup for Windows
- Ensure microphone permissions are enabled
- Install Microsoft Visual C++ Redistributable if needed
- Configure default microphone in system settings

## 🚀 How to Run

### Basic Usage
```bash
python chotu.py
```

### Advanced Usage with Custom Settings
```bash
# Run with debug mode
python chotu.py --debug

# Run with custom voice settings
python chotu.py --voice-rate 180 --volume 0.8
```

### Voice Commands Guide

#### **Application Control**
- "Open [app name]" - Opens any installed application
- "Start WhatsApp" - Launches WhatsApp desktop
- "Chrome kholo" - Opens Google Chrome browser

#### **Music & Entertainment**
- "YouTube chalao" - Opens YouTube
- "Arijit Singh ka gana bajao" - Plays Arijit Singh songs
- "Next song" / "Gana badlo" - Changes to next song
- "Pause" / "Resume" - Controls playback

#### **Communication**
- "WhatsApp message bhejo [contact]" - Sends WhatsApp message
- "Telegram kholo" - Opens Telegram

#### **System Operations**
- "Volume up/down" - Controls system volume
- "Time batao" - Tells current time
- "System info" - Shows system information
- "Internet check karo" - Checks connectivity

## 📋 Detailed Feature Documentation

### 🎤 Voice Recognition Engine
The voice recognition system uses Google's Speech Recognition API with the following features:
- **Language Support**: English (en-IN) with Hindi word recognition
- **Timeout Handling**: 4-second listening timeout with 5-second phrase limit
- **Error Recovery**: Automatic retry on recognition failures
- **Noise Adjustment**: Dynamic ambient noise calibration

### 🎵 Music Integration
- **YouTube Search**: Uses `youtubesearchpython` for accurate results
- **Playlist Management**: Maintains search results for song navigation
- **Context Awareness**: Remembers current music platform
- **Multi-platform Support**: YouTube and YouTube Music integration

### 💬 Messaging System
- **WhatsApp Integration**: Direct desktop app control using `pywhatkit`
- **Contact Management**: Voice-based contact search and selection
- **Message Composition**: Voice-to-text message creation
- **Auto-sending**: Instant message delivery with confirmation

### 🖥️ System Automation
- **Application Launcher**: Universal app opening using Windows search
- **File Operations**: Bulk file selection, deletion, and management
- **System Controls**: Volume, screen navigation, window management
- **Process Automation**: Multi-step task execution with GUI automation

## ⚠️ Important Notes & Warnings

### 🔐 Security Considerations
- **GUI Control**: Uses `pyautogui` which can control mouse & keyboard
- **Sensitive Operations**: Avoid running during password entry or financial transactions
- **Permission Requirements**: Requires microphone and system control permissions
- **Network Access**: Makes internet requests for speech recognition and searches

### 📱 Application Requirements
- **WhatsApp**: Requires WhatsApp Desktop to be installed and logged in
- **Telegram**: Requires Telegram Desktop for full functionality
- **Web Browser**: Default browser should be configured for web operations
- **Audio System**: Requires working microphone and audio output

## 🔧 Configuration & Customization

### Voice Settings
```python
# Customize voice properties
engine.setProperty('rate', 150)  # Speech rate (words per minute)
engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)
engine.setProperty('voice', voices[0].id)  # Voice selection
```

### Recognition Settings
```python
# Adjust recognition parameters
r.pause_threshold = 1  # Pause detection sensitivity
timeout=4  # Maximum listening time
phrase_time_limit=5  # Maximum phrase duration
```

### Adding Custom Commands
```python
# Add new voice commands in main() function
elif "your custom command" in query:
    your_custom_function()
    speak("Custom action performed")
```

## 🚀 Future Improvements & Roadmap

### 🎯 Planned Features
- **GUI Interface**: Modern desktop application using Tkinter/PyQt
- **Email Integration**: Voice-controlled email composition and sending
- **Weather API**: Real-time weather information and forecasts
- **News Integration**: Voice-activated news updates and reading
- **Smart Home Control**: IoT device integration and control
- **Calendar Management**: Schedule management and reminders

### 🤖 AI Enhancements
- **Wake Word Detection**: "Hey Chotu" activation phrase
- **Conversation Memory**: Context retention across sessions
- **Learning Capabilities**: Personalized response improvement
- **Multilingual Expansion**: Support for more Indian languages
- **Emotion Recognition**: Voice tone analysis and appropriate responses

### 🔧 Technical Improvements
- **Cloud Integration**: Google Drive, OneDrive file management
- **Database Support**: SQLite for storing user preferences and history
- **Plugin System**: Extensible architecture for third-party additions
- **Mobile App**: Companion mobile application for remote control
- **API Development**: REST API for external integrations

## 👨‍💻 Author & Development Team

**Faizal Rahman**
- 🎓 Cybersecurity Student & AI Enthusiast
- 💻 Python & Flask Developer
- 🌐 Full-Stack Web Developer
- 📍 Based in India
- 🚀 Passionate about Voice AI and Automation

### Connect with the Developer
- GitHub: [FaizalRahman01]([https://github.com/faizalrahman](https://github.com/FaizalRahman01))
- LinkedIn: [Faizal Rahman]([https://linkedin.com/in/faizalrahman](https://www.linkedin.com/in/faizal-rahman-68275a260/))
- Email: [faizalrahman7834@gmail.co](mailto:faizalrahman7834@gmail.com)

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### 🐛 Bug Reports
- Report bugs through GitHub Issues
- Provide detailed reproduction steps
- Include system information and error logs

### ✨ Feature Requests
- Suggest new voice commands
- Propose integration ideas
- Share use case scenarios

### 💻 Code Contributions
1. Fork the repository
2. Create a feature branch
3. Make your changes with proper documentation
4. Submit a pull request with detailed description

## 📜 License & Legal

This project is intended for **educational and personal use** only.

### 📋 Terms of Use
- ✅ Personal and educational use allowed
- ✅ Modification and customization permitted
- ✅ Non-commercial distribution allowed
- ❌ Commercial use requires explicit permission
- ❌ Warranty and liability disclaimers apply

### 🔒 Privacy Notice
- Voice data is processed locally when possible
- Internet-based recognition uses Google's API
- No personal data is stored or transmitted unnecessarily
- Users are responsible for their own data security

## 🎉 Acknowledgments

Special thanks to the open-source community and the following libraries:
- **pyttsx3** - Text-to-Speech conversion
- **SpeechRecognition** - Voice recognition capabilities
- **PyAutoGUI** - GUI automation and control
- **pywhatkit** - WhatsApp integration
- **youtubesearchpython** - YouTube search functionality

---

### 🚀 Ready to Get Started?

```bash
git clone https://github.com/yourusername/chotu-voice-assistant.git
cd chotu-voice-assistant
pip install -r requirements.txt
python chotu.py
```

**Say "Hello Chotu" and start your voice-controlled computing experience!** 🎤✨
