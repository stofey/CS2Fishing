import winreg
import os

def get_cs_path():
    try:
        hKey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\WOW6432Node\\Valve\\cs2')
        path = winreg.QueryValueEx(hKey, 'installpath')[0]
        winreg.CloseKey(hKey)
        return str(path)
    except:
        return None

def get_last_chat(log_dir, n=10):
    try:
        with open(log_dir, encoding='utf-8', errors='replace') as f:
            f.seek(0, 2)  
            current_position = f.tell()
            lines = []
            while len(lines) < n:
                f.seek(max(current_position - 1024, 0), 0)
                lines = f.readlines()
                current_position = f.tell()
            lines.reverse()  
        return lines 
    except Exception as e:
        print(f"Error reading log: {e}")
        return None

def get_last_name_used():
    try:
        hKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'SOFTWARE\\Valve\\Steam')
        name = winreg.QueryValueEx(hKey, 'LastGameNameUsed')[0]
        winreg.CloseKey(hKey)
        return name
    except:
        return None

def write_command(command):
    """
    Writes a given command to the CS:GO message.cfg file.
    This command will be executed when the 'L' key is pressed in CS:GO.
    """
    try:
        cfg_path = "S:\\SteamLibrary\\steamapps\\common\\Counter-Strike Global Offensive\\game\\csgo\\cfg\\message.cfg" #you need to make a message.cfg file, leave it empty and put the path to it here
        with open(cfg_path, 'w', encoding='utf-8') as f:
            f.write(command)
        print(f"Command written to {cfg_path}: {command}")  

    except Exception as e:
        print(f"Error writing command: {e}")


def press_key():
    import pydirectinput
    pydirectinput.write('p')