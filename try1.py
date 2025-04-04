from tkinter import *
import os

def run():
    try:
        import blinkDetect
        # import blinkDetect_2
    except Exception as e:
        print(f"Error in run(): {e}")
def video():
    import last_video

root = Tk()
root.title("DROWSINESS DETECTION")

Label(root, text="DROWSINESS DETECTION",font=("times new roman",20),fg="black",bg="aqua",height=2).grid(row=2,rowspan=2,columnspan=5,sticky=N+E+W+S,padx=5,pady=10)

Button(root,text="Run using web cam",font=("times new roman",20),bg="#0D47A1",fg='white',command=run).grid(row=5,columnspan=5,sticky=W+E+N+S,padx=5,pady=5)

Button(root,text="View last video",font=("times new roman",20),bg="#0D47A1",fg='white',command=video).grid(row=7,columnspan=5,sticky=W+E+N+S,padx=5,pady=5)

Button(root,text="Exit",font=("times new roman",20),bg="#0D47A1",fg='white',command=root.destroy).grid(row=9,columnspan=5,sticky=W+E+N+S,padx=5,pady=5)

root.mainloop()