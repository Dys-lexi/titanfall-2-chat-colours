import keyboard
import random
import pyperclip
import time
import requests as re

root = "https://xixya.com/api/"

styles = re.get(root+"getstyles")
letters = styles.json()["styles"]
try:
    descs = styles.json()["descs"]
    print("the current commands are:"," ".join(letters),"in order they do\n","\n".join(descs))
except:
    print("the current commands are:"," ".join(letters))


def main():
    event = keyboard.read_event()
    if not event.name:
        return
    if event.event_type == keyboard.KEY_UP and event.name in letters:
        keyboard.press('ctrl')
        keyboard.press('a')
        keyboard.release('a')
        keyboard.press('c')
        time.sleep(0.1)
        keyboard.release('c')
        keyboard.release('ctrl')
        characters = list(pyperclip.paste())[:-1]
        try:
            r = re.post(root+"convertword", json = {'message': characters,"style":event.name})
            message = r.json()["message"]
            if "ok" not in r.json()["code"]:
                print(r.json()["code"])
                return
            elif "ok" != r.json()["code"]:
                print(r.json()["code"])
        except Exception as e:
            print("broken, yell at lexi")
            print(e)
            return
        keyboard.press('backspace')
        pyperclip.copy(message)
        keyboard.press('ctrl')
        keyboard.press('v')
        keyboard.release('v')
        keyboard.release('ctrl')
        keyboard.press('enter')
        keyboard.release('enter')
        print(message,end="")
        print("[38;;m")
        #print((message.replace("[38;;", "").replace("m", "")).upper())
print("tf|2 chattyper by dyslexi\n")
if __name__ == "__main__":
    while True:
        main()
