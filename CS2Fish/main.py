import asyncio
import time
import pydirectinput
from util import *
from fish import cast_line

cs_path = "S:\\SteamLibrary\\steamapps\\common\\Counter-Strike Global Offensive\\game\\csgo\\console.log" #change to your path
log_dir = "S:\\SteamLibrary\\steamapps\\common\\Counter-Strike Global Offensive\\game\\csgo\\console.log" #change to your path
exec_dir = "S:\\SteamLibrary\\steamapps\\common\\Counter-Strike Global Offensive\\game\\csgo\\cfg\\message.cfg" #you need to make a message.cfg file, leave it empty and put the path to it here

chat_char_limit = 222
chat_delay = 0.5
last_log = ''
each_key_delay = 0.2

last_command_time = 0

# cooldown time in seconds, i recommend not putting this below 5 seconds since it will kinda bug out if too many type the command
COMMAND_DELAY = 5

async def handle_chat():
    global last_command_time
    processed_lines = set()  

    while True:
        new_lines = get_last_chat(log_dir)

        if not new_lines:
            await asyncio.sleep(0.1) 
            continue

        for line in new_lines:
            if line in processed_lines:
                continue

            processed_lines.add(line) 

            if '  [ALL] ' in line:  
                data = line.split(': ')
                if len(data) > 1:
                    username, message = data[0], data[1].strip()

                    if message == '!fish':
                        current_time = time.time() 

                        if current_time - last_command_time < COMMAND_DELAY:
                            remaining_time = COMMAND_DELAY - (current_time - last_command_time)
                            print(f"Command ignored for player '{username}'. Please wait {int(remaining_time)} seconds.")
                            continue 
                        
                        last_command_time = current_time

                        print(f"Player '{username}' has cast their line!")
                        await cast_line(username) 
                        print(f"Fishing process for '{username}' started.")
                        print(f"Pressed 'L' key to trigger in-game action.")

        await asyncio.sleep(0.1) 


        
if __name__ == "__main__":
    print("Fishing bot is running... Press Ctrl+C to stop.")
    try:
        asyncio.run(handle_chat())
    except KeyboardInterrupt:
        print("Bot stopped.")
