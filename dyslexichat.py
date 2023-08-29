import keyboard
import random
import pyperclip
import time
import requests as re
Colourroot="juvuA24smsol6{suqupfox0dto;:1656epv|jt{xwwjK2965216581725681275615125125125789378563875375212"
a=0
b=[]
while Colourroot[a] != "K":
    b.append(chr(ord(Colourroot[a])-int(Colourroot[-a-1])))
    a+=1
Colourroot = "".join(b)
def main():
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_UP and event.name in '#[]':
        keyboard.press('ctrl')
        keyboard.press('a')
        keyboard.release('a')
        keyboard.press('c')
        time.sleep(0.1)
        keyboard.release('c')
        keyboard.release('ctrl')
        characters = list(pyperclip.paste())[:-1]
        try:
            r = re.post(Colourroot, json = {'message': characters,"style":event.name})
            message = r.json()["message"]
            if r.json()["code"] != "ok":
                print(r.json()["code"])
                return
        except Exception as e:
            print("broken, yell at lexi")
            return
        keyboard.press('backspace')
        pyperclip.copy(message)
        keyboard.press('ctrl')
        keyboard.press('v')
        keyboard.release('v')
        keyboard.release('ctrl')
        keyboard.press('enter')
        keyboard.release('enter')
        print(message+"\x1b[0m")
        #print((message.replace("[38;;", "").replace("m", "")).upper())
print("tf|2chattyper by dyslexi\n")
print("] is character by character, [ is word by word, # is automagic highlighting :O")
if __name__ == "__main__":
    while True:
        main()
