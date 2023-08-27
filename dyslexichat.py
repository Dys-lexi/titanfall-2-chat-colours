import keyboard
import random
import pyperclip
import time


def random_ansi_color_code():
    while True:
        colour = random.randint(0,255)
        if colour not in (0, 16, 17, 23,59,60,65,95,102,101, 232, 233, 234, 235, 236, 237, 238, 239, 240): #blacklisted colours (unreadable)  (too dark)
            break
    
    
    choice = "[38;5;"+str(colour)+"m"
    return choice
    

def mainWORDBYWORD():
    print("Waiting for ']' key to be pressed...")
    while True:
        event = keyboard.read_event()
        #if the key pressed is a "T"
        if event.event_type == keyboard.KEY_UP and event.name == ']':
            keyboard.press('ctrl')
            keyboard.press('a')
            keyboard.release('a')
            keyboard.press('c')
            time.sleep(0.1)
            keyboard.release('c')
            keyboard.release('ctrl')
            keyboard.press('backspace')
            characters = list(pyperclip.paste())[:-1]
            message = ""+random_ansi_color_code()

            for character in characters:
                if character == " ":
                    message += " "
                    message += ""+code
                else:
                    code = random_ansi_color_code()
                    message += character
            pyperclip.copy(message)
            keyboard.press('ctrl')
            keyboard.press('v')
            keyboard.release('v')
            keyboard.release('ctrl')
            print(message+"\x1b[0m")        


def mainCHARACYERBYCHARACTER():
    print("Waiting for ']' key to be pressed...")
    while True:
        event = keyboard.read_event()
        #if the key pressed is a "T"
        if event.event_type == keyboard.KEY_UP and event.name == ']':
            keyboard.press('ctrl')
            keyboard.press('a')
            keyboard.release('a')
            keyboard.press('c')
            time.sleep(0.1)
            keyboard.release('c')
            keyboard.release('ctrl')
            keyboard.press('backspace')
            characters = list(pyperclip.paste())[:-1]
            message = ""
            for character in characters:
                if character == " ":
                    message += " "
                else:
                    code = random_ansi_color_code()
                    message += ""+code
                    message += character
            pyperclip.copy(message)
            keyboard.press('ctrl')
            keyboard.press('v')
            keyboard.release('v')
            keyboard.release('ctrl')
            print(message+"\x1b[0m")                   


print("tf|2chattyper by dyslexi")

choice = input("type 1 for word by word\n2 for Character by character\n")

if __name__ == "__main__":
    while True:
        if choice == "1":
            mainWORDBYWORD()
        elif choice == "2":
            mainCHARACYERBYCHARACTER()
        else:
            print("what are you doing?")
            break
   