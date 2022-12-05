from keyboard import keyboard as kb 

x = [ 'alt', 'alt gr', 'ctrl', 'left alt', 'left ctrl', 'left shift', 'left windows', 'right alt', 'right ctrl', 'right shift', 'right windows', 'shift', 'windows', 'enter']
y = ""

def callback(key):
    global y
    
    if key.name in x:
        y += " " + key.name + " "
    elif key.name == "backspace":
        y = y[0: len(y)-1]
    elif key.name == "space":
        y += " "
    else:
        y += key.name

    print(y)

kb.on_release(lambda key: callback(key))
