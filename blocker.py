import time #sleep function = time.sleep(delay, for example: 2.4 (in seconds)), good tutorial: https://www.programiz.com/python-programming/time/sleep
from datetime import datetime #current time
import sys #exit
import os #clear console (cls)
import random
import platform
#alapból elküld egy console-t, majd egy switch átvált
isSent = False
command = ""
redirect="127.0.0.1"
commandList = ["os", "color", "logo", "info", "time", "stop", "q", "quit", "exit", "blocklist", "block", "unblock", "help", "cl", "clear"]
#2p = to print
commandList2p = ["os - Prints out OS\n", "color - Sets CMD colors\n", "logo - Draws out the logo of Blocker\n", "info - Prints out info about Blocker\n", "time - Prints the current time\n", "q/stop/quit/exit - Stops Blocker\n", "blocklist - Prints out the blocked websites\n", "block - Blocks a website\n", "unblock - Unblocks a website\n", "help - Shows you the commands Blocker knows\n", "cl/clear - Clears the console"]
#logo stuff
logo0 = """
 ____ _            _  
| __ | |_____  ___| | _____ _ __  
|____/ |  _  |/ __| |/ / _ \ '__|  
| __ \ | |_| | (__|   <  __/ |   _   _   _ 
|____|_|_____|\___|_|\_\___|_|  |_| |_| |_|
"""
logo1 = """
       /|        |\       
      / |        | \      
     / /          \ \     
 ___( (____    ____) )___ 
|     _(   |__|   )_     |
|    / _\________/_ \    |
 \   \|_| _)  (_ |_|/   / 
  \   \__/  __  \__/   /  
   \_______|  |_______/   
        _|      |_        
       /          \       
      / _        _ \       ____ _            _  
     |_/ |  __  | \_|     | __ | |_____  ___| | _____ _ __ 
         | |  | |         |____/ |  _  |/ __| |/ / _ \ '__|
         | |  | |         | __ \ | |_| | (__|   <  __/ |    
         |_|  |_|         |____|_|_____|\___|_|\_\___|_|   
"""
logo2 = """
   ___________________________        
  / ____   _____   ___   ____ \       
 / |   _| |__ __| | _ | | __ | \     ____ _            _    
|   \ (     | |   || || ||__||  |   | __ | |_____  ___| | _____ _ __   
|   _) \    | |   ||_|| |  __|  |   |____/ |  _  |/ __| |/ / _ \ '__|  
 \ |____|   |_|   |___| |_|    /    | __ \ | |_| | (__|   <  __/ |      
  \___________________________/     |____|_|_____|\___|_|\_\___|_|     
"""
logo3 = """
   __________      
  / ________ \     
 / /     / /\ \    
| |     / /  | |   
| |    / /   | |    ____ _            _    
| |   / /    | |   | __ | |_____  ___| | _____ _ __   
| |  / /     | |   |____/ |  _  |/ __| |/ / _ \ '__|  
 \ \/_/_____/ /    | __ \ | |_| | (__|   <  __/ |      
  \__________/     |____|_|_____|\___|_|\_\___|_|     
"""

def intro():
    logo = random.randint(0,3)
    if logo == 0:
        print(logo0)
    if logo == 1:
        print(logo1)
    if logo == 2:
        print(logo2)
    if logo == 3:
        print(logo3)
    print("By phantazie\nYou're running blocker on " + platform.system() + "!")
#clear console
def clearConsole():
    os.system("cls")
#simulate typing
def print_slow(text):
    for letter in text + "\n":
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(.04)
#main task manager
def doTask(command):
    if command.lower() == "os":
        print("You're using " + platform.system() + ".")
    if "color" in command.lower() and "help" not in command.lower():
        if platform.system() == "Windows":
            if " " in command:
                if command.lower().count(" ") == 2:
                    color1 = command.split(" ")[1]
                    if str(color1) in "0123456789" or str(color1).lower() in "abcdef":
                        color2 = command.split(" ")[2]
                        if str(color2) in "0123456789" or str(color2).lower() in "abcdef":
                            colors = color1 + color2
                            os.system("color " + colors)
                            return
                        else:
                            print("Invalid attributes (second color code is not valid)!")
                            return
                    else:
                        print("Invalid attributes (first color code is not valid)!")
                        return
                print("Invalid attributes (make sure to put one space between the two color codes)!")
                return
            else:
                print("0 = Black\n1 = Blue\n2 = Green\n3 = Aqua\n4 = Red\n5 = Purple\n6 = Yellow\n7 = White\n8 = Gray\n9 = Light Blue\nA = Light Green\nB = Light Aqua\nC = Light Red\nD = Light Purple\nE = Light Yellow\nF = Bright White")
                color1 = input("What color do you want to change the background to? (provide its' code) ")
                color2 = input("What color do you want to change the text to? (provide its' code) ")
                colors = color1 + color2
                os.system("color " + colors)
                return
        if platform.system() == "Linux":
            print("This function is not working on " + platform.system() + " yet...")
            return
    if command.lower() == "logo":
        logo = random.randint(0,3)
        if logo == 0:
            print(logo0)
        if logo == 1:
            print(logo1)
        if logo == 2:
            print(logo2)
        if logo == 3:
            print(logo3)
        return
    if command.lower() == "info":
        print_slow("Blocker is a python console application that can help you with basic tasks, made by phantazie!")
        return
    if command.lower() == "time":
        print("The current time is: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return
    if command.lower() == "stop" or command.lower() == "quit" or command.lower() == "exit" or command.lower() == "q":
        if command.lower() != "q":
            answer = input("Are you sure you want to " + command.lower() + " Blocker? (Y or N) ")
            if answer.lower() != "n" or answer.lower() != "no":
                sys.exit("Blocker will " + command.lower() + " now!")
        else:
            answer = input("Are you sure you want to quit Blocker? (Y or N) ")
            if answer.lower() != "n" or answer.lower() != "no":
                sys.exit("Blocker will quit now!")
        return
    if command.lower() == "blocklist":
        sites = []        
        if platform.system() == "Windows":
            hostsPath = "C:\Windows\System32\drivers\etc\hosts" 
            with open(hostsPath, "r") as hosts:
                content = hosts.readlines()
                hosts.seek(0)
                for line in content:
                    if redirect in line and line.count(" ") == 1:
                        site = line.split(" ")[1]
                        if site.endswith("\n"):
                            site = site.replace("\n", "")
                        sites.append(site)
        if platform.system() == "Linux":
            hostsPath = "/etc/hosts"
            with open(hostsPath, "r") as hosts:
                content = hosts.readlines()
                hosts.seek(0)
                for line in content:
                    if redirect in line and line.count(" ") == 1:
                        site = line.split(" ")[1]
                        if site.endswith("\n"):
                            site = site.replace("\n", "")
                        if site != "localhost" and site != "kali" and site != "ip6-allnodes" and site != "ip6-allrouters":
                            sites.append(site)
        sites1 = str(sites)
        #sites2 = sites1.replace(", ", "\n")
        sites2 = sites1.replace("[", "")
        sites3 = sites2.replace("]", "")
        #sites4 = sites3.replace("'", "")
        #sites5 = sites4.replace(" ", "")
        #sites6 = sites5.replace('""', "")
        if len(sites) > 1:
            print("The following websites are blocked: " + sites3 + "! If you want to unblock any of them, use the command: 'unblock' !")
        if len(sites) == 1:
            print("The following website is blocked: " + sites3 + "! If you want to unblock it, use the command: 'unblock' !")
        if len(sites) == 0:
            print("No website is blocked right now! If you want to block a website, use the command: 'block' !")
        return
    if "block" in command.lower() and "unblock" not in command.lower() and "blocklist" not in command.lower() and "help" not in command.lower():
        if " " not in command:
            #wtb = what to block
            wtb = input("Please provide the site you want to block: ")
        else:
            wtb = command.split(" ")[1].lower()
        if wtb == "" or wtb == " ":
            print("You didn't provide a website!")
            return
        if "." not in wtb:
            if wtb == "localhost":
                print(wtb + " can't be blocked.")
            else:
                answer = input("Blocker detected that you didn't enter a website. Are you sure you want to block '" + wtb + "'? ")
                if answer.lower() == "n" or answer.lower() == "no":
                    return
        if platform.system() == "Windows":
            hostsPath = "C:\Windows\System32\drivers\etc\hosts" 
        if platform.system() == "Linux":
            hostsPath = "/etc/hosts"
        with open(hostsPath, "r+") as hosts:
            content=hosts.read()
            if wtb in content:
                print("This site is already blocked, to check the blocked websites, write: 'blocklist' !")
                return
            else:
                """if platform.system() == "Windows":
                    hosts.write(redirect + " " + wtb + "\n")
                if platform.system() == "Linux":
                    hosts.write(redirect + "    " + wtb + "\n")"""
                hosts.write(redirect + " " + wtb + "\n")
        print("'" + wtb + "' is successfully blocked!")
        return
    if "unblock" in command.lower() and "help" not in command.lower():
        if " " in command:
            wtu = command.split(" ")[1].lower()
        else:
            #wtu = what to unblock
            wtu = input("Please provide the site you want to unblock: ")
        #sl = searched line
        #sl = redirect + " " + wtu
        #sl2 = redirect + " www." + wtu
        if wtu == "":
            print("You didn't provide a website!")
            return
        writable = []
        if platform.system() == "Windows":
            hostsPath = "C:\Windows\System32\drivers\etc\hosts" 
        if platform.system() == "Linux":
            hostsPath = "/etc/hosts"
        with open (hostsPath, "r+") as hosts:
            content = hosts.readlines()
            hosts.seek(0)
            index = 0
            for line in content:
                index = index + 1
                if wtu not in line and line != len(content):
                    writable.append(line)
                if wtu not in line and wtu not in writable and index == len(content):
                    print("This site wasn't blocked, to check the blocked websites, write: 'blocklist' !")
                    return
            print("Blocker successfully unblocked '" + wtu + "'!")
            hosts.truncate()
            for line in writable:
                hosts.write(line)
        return
    if "help" in command.lower():
        if " " in command:
            com = command.split(" ")[1].lower()
            if com == "os":
                print("Usage: os\nDescription: with 'os' function, you can print out your OS!")
            if com == "color":
                print("Usage: color [attr]\n(Optional) attr [2 digits]\nThe first digit corresponds to the background, the second for the text, seperated by one space.\nIf you're not familiar with color codes, don't set attributes!\nExample: 0 6\nIf no attributes set, Blocker will help you with the usage.\nDescription: with 'color' function, you can set your terminal's colors (background and text colors).")
                return
            if com == "logo":
                print("Usage: logo\nDescription: with 'logo' function, you can draw one of Blocker's logo.")
                return
            if com == "info":
                print("Usage: info\nDescription: with 'info' function, you can get basic informations about this project.")
                return
            if com == "time":
                print("Usage: time\nDescription: with 'time' function, you can print out the exact time in your timezone.")
                return
            if com == "q" or com == "stop" or com == "quit" or com == "exit":
                if com != "q":
                    print("Usage: " + com + "\nDescription: with '" + com + "' function, you can " + com + " Blocker.")
                else:
                    print("Usage: " + com + "\nDescription: with '" + com + "' function, you can quit Blocker")
                return
            if com == "blocklist":
                print("Usage: blocklist\nDescription: with 'blocklist' function, you can get the list of currently blocked websites.")
                return
            if com == "block":
                print("Usage: block [attr]\n(Optional) attr [site]\nThe site corresponds to the site you want to block.\nExample: netflix.com\nIf no attributes set, Blocker will help you with the usage.\nDescription: with 'block' function, you can block a website (later on, you can unblock it anytime).")
                return
            if com == "unblock":
                print("Usage: unblock [attr]\n(Optional) attr [site]\nThe site corresponds to the site you want to unblock.\nExample: netflix.com\nIf no attributes set, Blocker will help you with the usage.\nDescription: with 'unblock' function, you can unblock a website that has been blocked earlier.")
                return
            if com == "help":
                print("Usage: help [attr]\n(Optional) attr [command]\nThe command corresponds to the command you want help with.\nExample: block\nIf no attributes set, Blocker will print a short description of all commands.\nDescription: with 'help' function, you can get help with Blocker's usage, and it's commands.")
                return
            if com == "cl" or com == "clear":
                print("Usage: " + com + "\nDescription: with '" + com + "' function, you can clear the terminal.")
                return
            else:
                print("I can't help you with this command.")
        else:
            for com in commandList2p:
                print(com)
            print("If you want a more in-depth description of any command, write 'help your_command'")
        return
    if command.lower() == "clear" or command.lower() == "cl":
        clearConsole()
        intro()
        return
    if not any(com in command for com in commandList):
        print("I don't know this command! To see my all my commands, write: 'help' !")
        return


#console function
def console():
    global isSent
    global command
    if not isSent:
        command = input("Blocker: ")
        isSent = True
    if command != "" and command.isdigit() == False:
        doTask(command)
        command = ""
        isSent = False
    else:
        command = ""
        isSent = False


#main
clearConsole()
intro()
while True:
    console()
