import json, sys
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def convert(frame:int, fpsin:int, fpsout:int):
    return round((int(frame)/int(fpsin))*int(fpsout))

Tk().withdraw()
filename = askopenfilename()
f = open(filename)
data = json.load(f)
framerate = data["framerate"]
print(data["inputs"])
inputs = data["inputs"]
uin = input("new fps > ")
if uin.isdigit() == False:
    print("not a value")
    sys.exit()

again = False

if int(uin) < framerate:
    print("This may break your macro are you sure you want to continue (y/n)")
    uin2 = input(" > ")
    if uin2 in ["y", "Y", "yes", "Yes"]:
        pass
    elif uin2 in ["n", "N", "no", "No"]:
        sys.exit()
    else:
        print("not a valid input")
        print("valid inputs: ")
        print("y, Y, yes, Yes")
        print("n, N, no, No")
        sys.exit()
    again = True

if int(uin) > framerate:
    if int(uin) % framerate != 0:
            if again == False:
                print("This may break your macro are you sure you want to continue (y/n)")
            elif again == True:
                print("This may break your macro (again and btw how unstable are you trying to make your macro) are you sure you want to continue (y/n)")
            uin2 = input(" > ")
            if uin2 in ["y", "Y", "yes", "Yes"]:
                pass
            elif uin2 in ["n", "N", "no", "No"]:
                sys.exit()
            else:
                print("not a valid input")
                print("valid inputs: ")
                print("y, Y, yes, Yes")
                print("n, N, no, No")
                sys.exit()

for i in range(len(inputs)):
    inputs[i]["frame"] = convert(inputs[i]["frame"], framerate, int(uin))

data["framerate"] = int(uin)
data["inputs"] = inputs

with open(filename, 'w') as wf:
    json.dump(data, wf, sort_keys=True, indent=4)