import pyautogui
import keyboard
from pynput.keyboard import Controller
import pyperclip
import time

def main():
    question_pos = getPos("ctrl")
    field_pos = getPos("q")
    r = getPos("w")
    conj_pos = getPos("a")
    conj = ripTextFile()
    while True:
        answer(question_pos, field_pos, r, conj, conj_pos)

def getPos(marker_key):
    while True:
        try: 
            if keyboard.is_pressed(marker_key):
                return pyautogui.position()
        except:
            continue

def getPre(conj_pos):
    pyautogui.moveTo(conj_pos[0], conj_pos[1])
    pyautogui.click()
    pyautogui.click()
    pyautogui.hotkey("ctrl", "c")
    time.sleep(1)
    res = pyperclip.paste()
    print(res)
    if " y " in res:
        if "yo" in res:
            return 3
        else:
            return 4
    if res == "yo":
        return 0
    elif res == "tú":
        return 1
    elif res == "ustedes":
        return 4
    else:
        return 2


def answer(question_pos, field_pos, random, conj, conj_pos):
    pyautogui.moveTo(question_pos[0], question_pos[1])
    pyautogui.click()
    pyautogui.click()
    pyautogui.hotkey("ctrl", "c")
    pyautogui.moveTo(random[0], random[1])
    pyautogui.click()
    save = pyperclip.paste()
    print(save)
    word = conj.get(save)[getPre(conj_pos)]
    pyautogui.moveTo(field_pos[0], field_pos[1])
    pyautogui.click()
    pyautogui.keyDown("backspace")
    pyautogui.keyUp("backspace")
    Controller().type(word)
    pyautogui.keyDown("enter")
    pyautogui.keyUp("enter")
    time.sleep(1)

def ripTextFile():
    conj = {}
    with open("asdfghjkl.txt", 'r', encoding="ANSI") as file:
        lines = file.readlines()
        print(lines)
        print(len(lines))
    for i in range(0,len(lines),6):
        conj[lines[i].strip()] = [lines[i+1].strip(), lines[i+2].strip(), lines[i+3].strip(), lines[i+4].strip(), lines[i+5].strip()]
    print(conj)
    return conj

main()