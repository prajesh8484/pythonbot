## pythonbot

<p align="center">
<a href="https://github.com/prajesh8484/pythonbot"><img src="https://img.shields.io/github/languages/code-size/prajesh8484/pythonbot"></a>
<a herf="https://github.com/nextcord/nextcord"><img src="https://img.shields.io/pypi/pyversions/nextcord"></a>
<a href="https://www.codefactor.io/repository/github/prajesh8484/pythonbot"><img src="https://www.codefactor.io/repository/github/prajesh8484/pythonbot/badge" alt="CodeFactor" /></a>
<a href="https://github.com/prajesh8484/pythonbot/commits/main"><img src="https://img.shields.io/github/last-commit/prajesh8484/pythonbot"></a>
<a href="https://github.com/prajesh8484/pythonbot/releases/"><img src="https://img.shields.io/github/v/release/prajesh8484/pythonbot"></a>
<a href="https://github.com/prajesh8484/pythonbot/blob/3229b471a5772099e285e18282439e8b061ae9ba/LICENSE.md"><img src="https://img.shields.io/github/license/prajesh8484/pythonbot"></a>
</p>

This is a general purpose Discord bot built with [Firebase](https://firebase.google.com/) & [Nextcord](https://github.com/nextcord/nextcord) (A Python wrapper for the Discord API). The bot is designed to be easily customizable and extendable, with a modular architecture that allows for the addition of new features and commands. 

## How to setup

* Clone/Download the repository
    * To clone it and get the updates you can use the command:
    ```
      git clone https://github.com/prajesh8484/pythonbot
    ```
* Create a discord bot [here](https://discord.com/developers/applications)
* Get your bot token
* Invite your bot on servers using the following invite:
  https://discord.com/oauth2/authorize?&client_id=YOUR_APPLICATION_ID_HERE&scope=bot+applications.commands&permissions=PERMISSIONS (
  allow necessary permissions your bot needs that it can be get at the bottom of a this
  page https://discord.com/developers/applications/YOUR_APPLICATION_ID_HERE/bot)

* Create a `.env` file in the root directory of the project and add the following variables:
  ```
  BOT_TOKEN=YOUR_BOT_TOKEN
  FIREBASE_DATABASE_URL=YOUR_FIREBASE_DATABASE_URL
  ```
* Create a `firebase_credentials.json` file in the root directory of the project and add your firebase credentials.
  * You can get your firebase credentials from [here](https://console.firebase.google.com/)
  * Go to your project settings and then to service accounts and generate a new private key.
  * This will download a json file, rename it to `firebase_credentials.json` and place it in the root directory of the project.

## Starting the bot

launch your terminal or your Command Prompt


Before running the bot install all the requirements with this command :

```
python -m pip install -r requirements.txt
```

After that you can start it with

```
python main.py
```
## Contributing
Contributions to the project are welcome! If you have a feature or improvement to suggest, simply open an issue or pull request.

## License
This bot is released under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

## Built With

* [Python 3.13.1](https://www.python.org/downloads/release/python-3106/)