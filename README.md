# Bantu AI

This repository contains the code for Bantu AI, a personal assistant developed using Python. Bantu AI is capable of performing various tasks such as playing songs, opening websites, providing translations, and engaging in conversational interactions.

## Modules Used

- `datetime`: Used to retrieve the current time.
- `speech_recognition`: Used for speech recognition.
- `win32com.client`: Used for text-to-speech synthesis.
- `webbrowser`: Used to open websites.
- `os`: Used for file operations.
- `googletrans`: Used for text translation.
- `openai`: Used for AI-powered responses and completion.

## Functionality

### Speaker

The `speaker` module is responsible for text-to-speech synthesis and utilizes the `win32com.client` library.

### Play Song

The `playsong()` function plays a random song from a specified playlist.

### Play YouTube Song

The `play_youtube_song(song_name)` function searches and plays a song on YouTube based on the provided `song_name`.

### Translate Text

The `translate_text(text, source, destination)` function translates the given `text` from the source language to the destination language using the `googletrans` library.

### AI

The `ai(prompt)` function uses OpenAI's GPT-3 model to generate a response based on the provided `prompt`.

### Chat

The `chat(prompt, name, enortel)` function engages in a conversational interaction with the user, generating responses using OpenAI's GPT-3 model.

### Take Command

The `takeCommand(enortel)` function uses speech recognition to convert user's speech to text. It supports both English and Telugu languages based on the `enortel` parameter.

## Usage

1. Run the script.
2. Enter your name when prompted.
3. Select the language preference by entering 0 for Telugu or 1 for English.
4. Communicate with Bantu AI using voice commands or by typing.

Bantu AI supports various commands such as opening websites, playing songs, providing the current time, utilizing artificial intelligence for generating responses, and engaging in conversational interactions.

Please note that certain modules and API keys may need to be installed/configured for the code to function correctly.

Feel free to explore and modify the code to suit your needs!
