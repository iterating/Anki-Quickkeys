# Ankikeys

Ankikeys turns your modifier keys into single button multifunction keys, adding 9 programmable keys on a standard keyboard. Designed for use with Anki, this tool aims to enhance your productivity by integrating Anki functions directly onto your desktop.

Anki is an effective tool for learning. However, its utility is limited by speed of use, and many students find it difficult to incorporate Anki into thier studies in a timely manner. 

Anki-Quickkey aims to mitigate this problem by incorporating Anki functions onto the desktop.
Read a fact you need to add to Anki? Press a key to bring up Anki.addcard(), type your fact, and press <kbd>ctrl</kbd><kbd>enter</kbd> to add it to your Anki library. 

Need to lookup your anki database? Press a key to bring up Anki.browser and have access to your Anki second brain anytime. 

## Features

- **Single Button Multifunction Keys**: Transform your modifier keys into multifunction keys.
- **Programmable Keys**: Add 9 programmable keys to your standard keyboard.
- **Seamless Integration**: Quickly add cards, browse your Anki database, and more with simple key presses.

## Requirements

- Linux desktop with appropriate permissions.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/iterating/ankikeys.git
    cd ankikeys
    ```

2. Run the setup script:
    ```bash
    ./setup.py
    ```

## Usage

- **Add a Card**: Press a single key to bring up `Anki.addcard()`, type your fact, and press `Ctrl + Enter` to add it to your Anki library.
- **Browse Database**: Press a single key to bring up `Anki.browser` and access your Anki database.
- TBA

## Configuration

Modify the `user_config.json` file to customize the key mappings and other settings.

## License

This project is licensed under the GPL-2.0 License. See the LICENSE file for details.


