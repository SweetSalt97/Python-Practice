import time
import pyautogui as pyg
#Marks Calculator
a = int(pyg.prompt("What were your grade in English? "))
b = int(pyg.prompt("What were your grade in Maths? "))
c = int(pyg.prompt("What were your grade in Computer Science? "))
d = int(pyg.prompt("What were your grade in Entrepreneurship? "))
e = int(pyg.prompt("What were your grade in Physics "))
cgpa = (a+b+c+d+e)/5
pyg.alert(f"Your CGPA is {cgpa}")
if cgpa>9:
    pyg.alert("Execellent")
elif cgpa<6:
    pyg.alert("Try Harder Next Time")
else:
    pyg.alert("Good work")
time.sleep(10)

