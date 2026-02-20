import pyautogui
import keyboard
from pynput.keyboard import Controller
import pyperclip
import time

def main():
    question_pos = getPos("ctrl")
    field_pos = getPos("q")
    r = getPos("w")
    conj_pos = getPos("r")
    emotion_pos = getPos("s")
    conj = ripTextFile()
    while True:
        try:
            answer(question_pos, field_pos, r, conj, conj_pos, emotion_pos)
        except Exception as e:
            x = 1
            continue

def getPos(marker_key):
    while True:
        try: 
            if keyboard.is_pressed(marker_key):
                return pyautogui.position()
        except:
            continue

def copy_from_pos(pos):
    pyautogui.moveTo(pos[0], pos[1])
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.hotkey("ctrl", "c")
    time.sleep(1)
    return pyperclip.paste().strip()


def get_subject_index(conj_pos):
    res = copy_from_pos(conj_pos).lower()
    if "tú" in res or "tu" in res:
        return 0
    if "usted" in res:
        if "ustedes" in res:
            return 3
        return 1
    if "nosotros" in res:
        return 2
    if "ustedes" in res:
        return 3
    raise ValueError(f"Unknown subject: {res}")


def get_emotion_index(emotion_pos):
    res = copy_from_pos(emotion_pos).lower()
    if "neg" in res or "negative" in res:
        return 1
    if "pos" in res or "positive" in res:
        return 0
    if "no " in res:
        return 1
    return 2


def answer(question_pos, field_pos, random, conj, conj_pos, emotion_pos):
    pyautogui.moveTo(question_pos[0], question_pos[1])
    pyautogui.click()
    pyautogui.click()
    pyautogui.hotkey("ctrl", "c")
    pyautogui.moveTo(random[0], random[1])
    pyautogui.click()
    save = pyperclip.paste()
    print(save)
    try:
        subject_index = get_subject_index(conj_pos)
        emotion_index = get_emotion_index(emotion_pos)
        index = subject_index * 2 + emotion_index
        print("is index check")
        print(subject_index)
        print(emotion_index)
        print(index == 0)
        print(type(conj.get(save)))
        word = conj.get(save)[index]
    except:
        pyautogui.moveTo(random[0], random[1])
        pyautogui.click()
        subject_index = get_subject_index(conj_pos)
        emotion_index = get_emotion_index(emotion_pos)
        index = subject_index * 2 + emotion_index
        word = conj.get(save)[index]
    pyautogui.moveTo(field_pos[0], field_pos[1])
    pyautogui.click()
    pyautogui.keyDown("backspace")
    pyautogui.keyUp("backspace")
    Controller().type(word)
    pyautogui.keyDown("enter")
    pyautogui.keyUp("enter")
    time.sleep(3)

def ripTextFile():
    conj = {}
    with open("asdfghjkl.txt", 'r', encoding="UTF-8") as file:
        lines = [line.strip() for line in file if line.strip()]
    for i in range(0, len(lines), 9):
        if i + 8 >= len(lines):
            break
        conj[lines[i]] = [
            lines[i + 1],
            lines[i + 2],
            lines[i + 3],
            lines[i + 4],
            lines[i + 5],
            lines[i + 6],
            lines[i + 7],
            lines[i + 8],
        ]
    print(conj)
    return conj

main()
