import keyboard
import random
import pyperclip
import time
def random_ansi_color_code():
    while True:
        colour = random.randint(0, 255)
        # blacklisted colours (unreadable)  (too dark)
        if colour not in (0, 16, 17, 23, 59, 60, 65, 95, 102, 101, 232, 233, 234, 235, 236, 237, 238, 239, 240):
            break

    choice = "[38;5;"+str(colour)+"m"
    return choice

def code_words(characters):
    message = ""+random_ansi_color_code()
    for character in characters:
        if character == " ":
            message += " "
            message += ""+code
        else:
            code = random_ansi_color_code()
            message += character
    return message

def code_characters(characters):
    message = ""
    for character in characters:
        if character == " ":
            message += " "
        else:
            code = random_ansi_color_code()
            message += ""+code
            message += character
    return message

def main():
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_UP and event.name in '[]':
        keyboard.press('ctrl')
        keyboard.press('a')
        keyboard.release('a')
        keyboard.press('c')
        time.sleep(0.1)
        keyboard.release('c')
        keyboard.release('ctrl')
        keyboard.press('backspace')
        characters = list(pyperclip.paste())[:-1]

        if event.name == "[":
            message = code_words(characters)
        elif event.name == "]":
            message = code_characters(characters)

        if len(message) > 250:
            print("message too long, word by word done")
            message = code_words(characters)

        pyperclip.copy(message)
        keyboard.press('ctrl')
        keyboard.press('v')
        keyboard.release('v')
        keyboard.release('ctrl')
        print(message+"\x1b[0m")

print("tf|2chattyper by dyslexi\n")
print("] is character by character, [ is word by word")
if __name__ == "__main__":
    while True:
        main()
