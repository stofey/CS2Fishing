# CS2Fishing
An interactive chat "bot" thing that lets you fish ingame in CS2

Add ```-condebug -conclearlog``` to your CS2 launch options

Download and install python 3.13 (https://www.python.org/downloads/) make sure to check the mount path checkbox while installing 

![0_oWVwfeB8G7npLFiu](https://github.com/user-attachments/assets/470c2555-634d-4baf-aa5a-59e18760fa9b)

Change line 7-9 in the main.py and line 44 in util.py to the paths to your locations (the console.log will apear after your first start of the game when adding -condebug to your launch options)

In the cfg folder of CS make a new file called message.cfg, needs to be empty 

In the fish.py at line 48 you can change to whichever button you like (you never actually press the button so put it to something you dont need)
Add ```bind button exec message``` to your autoexec or just type it in your in game console

You can choose the command cooldown by chaning line 19 in main.py to a number you like (i recommend not putting it below 5 since it tends to bug when repeated to quickly)

To actually run it you open Win PowerShell and navigate to the CS2Fish Folder you downloaded (```cd path/to/CS2Fish```)
Then just type ```py main.py``` to execute and you should be good to go

alot of this is yoinked from https://github.com/Pandaptable/galls but i couldnt get theirs to work 
