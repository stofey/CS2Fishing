# CS2Fishing
An interactive chat "bot" thing that lets you fish ingame in CS2

Add -condebug -conclearlog to your CS2 launch options

Download and install python 3.13 (https://www.python.org/downloads/) make sure to check the mount path checkbox while installing 

Change line 7-9 in the main.py and line 44 in util.py to the paths to your locations (the console.log will apear after your first start of the game when adding -condebug to your launch options)

In the cfg folder of CS make a new file called message.cfg, needs to be empty 

You can choose the command cooldown bt chaning line 19 in main.py to a number you like (i recommend not putting it below 5 since it tends to bug when repeated to quickly)

To actually run it you open Win PowerShell and navigate to the CS2Fish Folder you downloaded (cd path/to/CS2Fish)
Then just type py main.py to execute and you should be good to go
