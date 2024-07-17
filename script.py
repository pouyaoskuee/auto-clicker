import time
import pyautogui
from tkinter import *


def auto_click(methodType,interval,end_time):
    start_time = time.time()
    i = 0



    


    print(f"Auto Clicker Started In ({start_time})")
    print(f"==> Interval Time ({interval})")
    print(f"==> End Time ({end_time})")
    print(f"==> Type ({methodType})")
    print("=====================================")
    time.sleep(3)
    while float(end_time)>i:
        i += 1

        if (methodType == 'click'):
            pyautogui.move(10, 0)  # Move cursor 10 pixels to the right
            pyautogui.move(-10, 0)  # Move cursor back 10 pixels to the left
            pyautogui.click(button='left')
            time.sleep(float(interval))
            print(f"Auto Click ({i})")
        elif (methodType == 'drag'):
            x, y = pyautogui.position()  # Get current mouse cursor position
            pyautogui.moveTo(x, y)  # Move the cursor to the current position (optional)
            pyautogui.drag(10, 0, duration=0.5, button='left')  # Drag the window 10 pixels to the right
            pyautogui.drag(-10, 0, duration=0.5, button='left')  # Drag the window back 10 pixels to the left
            time.sleep(float(interval))
            print(f"Auto drag ({i})")
        else:
            print(f"Auto Clicker {i} | without action type")



window= Tk()
window.geometry("600x700")




lable=Label(window, text= "write 'click' or 'drag'?.")
lable.pack()

methodType1=Entry(window)
methodType1.pack()


lable1=Label(window, text= "How much interruption?")
lable1.pack()

interval1=Entry(window)
interval1.pack()


lable2=Label(window, text= "How many times to run?")
lable2.pack()


end_time1=Entry(window)
end_time1.pack()





def start():



    try:

        methodType=methodType1.get()
        interval=interval1.get()
        end_time=end_time1.get()

        auto_click(methodType,interval, end_time,)


    except KeyboardInterrupt:
        print("Auto clicker stopped.")


button=Button(window, text="stat",command=start)
button.pack()




window.mainloop()








