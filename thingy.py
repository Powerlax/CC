import pyautogui
import win32clipboard
import keyboard
from pynput.keyboard import Controller

def main(): 
    question_pos = getPos("ctrl")
    field_pos = getPos("q")
    translation_dict = ripTextFile()
    while True:
        question = getQuestion(question_pos)
        answerQuestion(field_pos, translation_dict.get(question))

def getPos(marker_key):
    while True:
        try: 
            if keyboard.is_pressed(marker_key):
                return pyautogui.position()
        except:
            continue

def getQuestion(pos):
    pyautogui.moveTo(pos[0], pos[1])
    pyautogui.click()
    pyautogui.click()
    pyautogui.hotkey("ctrl", "c")
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data

def answerQuestion(pos, answer):
    pyautogui.moveTo(pos[0], pos[1])
    pyautogui.click()
    Controller().type(answer.split("/")[0])
    pyautogui.keyDown("enter")
    pyautogui.keyUp("enter")

def ripTextFile():
    translation_dict = {}
    f = open("thing.txt", "r", encoding="UTF-8")
    for line in f:
        key, value = line.split('\t')
        translation_dict[key.split('. ')[1].strip()] = value.split('. ')[1].strip()
    f.close()
    return translation_dict

