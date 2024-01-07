import keyboard
import pyperclip
import time
import requests as re
import threading

root = "https://xixya.com/api/"
print("loading...")

try:
    styles = re.get(root+"getstyles")
except Exception as e:
    print("broken, yell at lexi (or you have no internet) - could not retrieve stylesheet")
    print(e)
    time.sleep(10000)
stylelist = {}
def initit(printstyles = True):
    global stylelist
    try:
        stylelist = styles.json()["keyedstyles"]
        descs = styles.json()["descs"]
    except Exception as e:
        print("broken, yell at lexi (or you have no internet) - could not retrieve stylesheet")
        print(e)
        time.sleep(10000)
    try:
        if printstyles:
            with open("keybinds.txt", "r") as f:
                ammendedbinds = eval(f.read())
            for i in ammendedbinds.keys():
                stylelist[i] = ammendedbinds[i]
    except:
        pass

    print("styles are:" + str(stylelist))
    if printstyles: print("\n".join(descs))
    return stylelist


def main(stylelist):
    event = keyboard.read_event()
    if not event.name:
        return
    if event.event_type == keyboard.KEY_UP and event.name in stylelist.values() and event.name != "NONE":
        keyboard.press('ctrl')
        keyboard.press('a')
        keyboard.release('a')
        keyboard.press('c')
        time.sleep(0.1)
        keyboard.release('c')
        keyboard.release('ctrl')
        characters = list(pyperclip.paste())[:-1]
        try:
            r = re.post(root+"convertword", json = {'message': characters,"style":list(stylelist.keys())[list(stylelist.values()).index(event.name)] })
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

def info():
    while True:
        print("Type 'rebind' in this console to rebind keys, or type 'changes' to see changes")
        inp = input()
        if inp == "rebind":
            rebind()
            initit(False)
        elif inp == "changes":
            changes()
        else:
            print("invalid input - type 'rebind' or 'changes'")

def rebind():
    print("rebinding selected!")
    while True:
        print("\n".join([i + " : " + stylelist[i] for i in stylelist.keys()]))
        number = input("choose an option to rebind (eg solid_code) ")
        if number in stylelist.keys():
            newbind = False
            print("press a key to bind to " + number + "\nType cancel to cancel, or unbind to unbind, default to set to default. BE CAREFUL BINDING, DO NOT PUT TO SOMETHING USED OFTEN")
            while True:
                inp = input()
                if inp == "cancel":
                    break
                elif inp == "unbind":
                    newbind = "NONE"
                    break
                elif inp == "default":
                    newbind = styles.json()["keyedstyles"][number]
                    break
                elif len (inp) == 1 and inp.lower() not in "abcdefghijklmnopqrstuvwxyz":
                    newbind = inp
                    break
                else:
                    print("invalid input - must be one char, not a-z, or in above options")
            if newbind:
                stylelist[number] = newbind
                try:
                    with open("keybinds.txt", "r") as f:
                        oldbinds = eval(f.read())
                except:
                    oldbinds = {}
                oldbinds[number] = newbind
                with open("keybinds.txt", "w") as f:
                    f.write(str(oldbinds))
                print("\nrebound " + number + " to " + newbind)
            else:
                print("\ncancelled")
            break
def changes():
    print("changes selected!")
    print("\n".join(styles.json()["changelog"]))
    print("\n")

if __name__ == "__main__":
    print("tf|2 chat colourer by @dyslexi - discord")
    stylelist = initit()
    infothread = threading.Thread(target=info).start()

    while True:
        main(stylelist)
