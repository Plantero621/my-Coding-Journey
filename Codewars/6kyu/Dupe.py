from ctypes.wintypes import CHAR


text = "tutorialspoint"

def duplicate_count(text):
    for char in text:
        if text.count(char)>1:
            count=+1
            print(count)

duplicate_count(text)

