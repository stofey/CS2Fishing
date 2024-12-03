# CS2Fishing
An interactive chat "bot" thing that lets you fish ingame in CS2

Install Python

-Go to the official Python website.

-Download and install the latest stable version of Python for your operating system.

-During installation, check the box that says "Add Python to PATH" (important!).

-After installation, verify Python is installed by opening a terminal (Command Prompt) and typing:
```python --version```

Install Required Python Libraries

-The bot uses several external libraries, which must be installed using Python's package manager, ```pip```.

-Open a terminal or Command Prompt.

-Run the following commands to install the required libraries:
```pip install asyncio```
```pip install pydirectinput```

Download the Bot Files
Ensure you have the following files saved in the same directory:
main.py: The main script that handles everything.
fish.py: Contains logic for fishing actions.
util.py: Provides helper functions for interacting with the game.
fishbase.json: A JSON file that contains data about the fish (e.g., names, weights, values).

Prepare CS2

Add ```-condebug -conclearlog``` to your CS2 launch options.

To ensure the bot works correctly with CS2, follow these steps:

Enable the Developer Console:

Launch CS2 and go to Settings > Game > Enable Developer Console. Set it to "Yes".

Find the ```console.log``` File:

```S:\SteamLibrary\steamapps\common\Counter-Strike Global Offensive\game\csgo```

Create the ```message.cfg``` File:

Inside the cfg folder of your CS2 directory (e.g., ...\game\csgo\cfg), create a file named ```message.cfg``` if it doesn’t already exist (should be empty).

Bind a Key to Execute the ```message.cfg``` File:

In the CS2 Developer Console, bind a key (e.g., L) to execute the ```message.cfg``` file:

```bind l "exec message"```

This key can also be changed in the fish.py file.

Check the Paths in the Scripts:

Open ```main.py``` in a text editor and ensure the ```log_dir``` , ```exec_dir``` and ```cs_path``` paths match your CS2 directory:

```cs_path = "S:\\SteamLibrary\\steamapps\\common\\Counter-Strike Global Offensive\\game\\csgo\\console.log" ```
```log_dir = "S:\\SteamLibrary\\steamapps\\common\\Counter-Strike Global Offensive\\game\\csgo\\console.log" ```
```exec_dir = "S:\\SteamLibrary\\steamapps\\common\\Counter-Strike Global Offensive\\game\\csgo\\cfg\\message.cfg" ```

Run the Bot:

Navigate to the folder containing the bot files (main.py, fish.py, etc.) in your terminal:

Example if on Desktop: ```cd .\Desktop\CS2Fish\```

Run the bot: ```py main.py```

Test the Bot:

Open CS2, join a game, and type ```!fish``` in the in-game chat.
The bot should respond in the chat with fishing messages (e.g., weather, catch, or failure messages).


alot of this is yoinked from https://github.com/Pandaptable/galls but i couldnt get theirs to work 
