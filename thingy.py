import pyautogui
import win32clipboard
import keyboard
from pynput.keyboard import Controller
import time

def main(): 
    question_pos = getPos("ctrl")
    field_pos = getPos("q")
    translation_dict = ripTextFile()
    while True:
        question = getQuestion(question_pos)
        print(question)
        answerQuestion(field_pos, translation_dict.get(question))
        time.sleep(1.5)

def getPos(marker_key):
    while True:
        try: 
            if keyboard.is_pressed(marker_key):
                return pyautogui.position()
        except:
            continue

def getQuestion(pos):
    try:
        pyautogui.moveTo(pos[0], pos[1])
        pyautogui.click()
        pyautogui.click()
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.5)
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return data
    except:
        time.sleep(1) 
        return getQuestion(pos)   

def answerQuestion(pos, answer):
    pyautogui.moveTo(pos[0], pos[1])
    pyautogui.click()
    Controller().type(answer.split("/")[0])
    pyautogui.keyDown("enter")
    pyautogui.keyUp("enter")

def ripTextFile():
    translation_dict = {}
    f = open("thing.txt", "r", encoding="UTF-8")
    lines = f.readlines()
    for i in range (0, len(lines), 3):
        translation_dict[lines[i].split('. ')[1].strip()] = lines[i+1].split('. ')[1].strip()
    f.close()
    return translation_dict

main()
