## pythonbot

<p align="center">
<a href="https://github.com/prajesh8484/pythonbot"><img src="https://img.shields.io/github/languages/code-size/prajesh8484/pythonbot"></a>
<a herf="https://github.com/nextcord/nextcord"><img src="https://img.shields.io/pypi/pyversions/nextcord"></a>
<a href="https://github.com/prajesh8484/pythonbot/commits/main"><img src="https://img.shields.io/github/last-commit/prajesh8484/pythonbot"></a>
<a href="https://github.com/prajesh8484/pythonbot/releases/"><img src="https://img.shields.io/github/v/release/prajesh8484/pythonbot"></a>
<a href="https://github.com/prajesh8484/pythonbot/blob/3229b471a5772099e285e18282439e8b061ae9ba/LICENSE.md"><img src="https://img.shields.io/github/license/prajesh8484/pythonbot"></a>
</p>

This is a general purpose Discord bot built with [Nextcord](https://github.com/nextcord/nextcord)(A Python wrapper for the Discord API). The bot is designed to be easily customizable and extendable, with a modular architecture that allows for the addition of new features and commands. 

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

* Replace:
   * `YOUR_CHANNEL_ID` to channel id, [here](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-) how to get channel id
   * `YOUR_BOT_TOKEN` to bot token 
   * `YOUR_TIME_ZONE` to time zone (e.g. `'Europe/London'`)
## Starting the bot

launch your terminal or your Command Prompt
.

Before running the bot you will need to install all the requirements with this command:

```
python -m pip install -r requirements.txt
```

After that you can start it with

```
python main.py
```
## Contributing
Contributions to the project are welcome! If you have a feature or improvement to suggest, simply open an issue or pull request on GitHub.

## License
This bot is released under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.
