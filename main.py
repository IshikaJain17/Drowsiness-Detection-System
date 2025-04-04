import customtkinter

customtkinter.set_appearance_mode("light")#options are system and light
customtkinter.set_default_color_theme("dark-blue")  #green

root = customtkinter.CTk()
root.geometry("500x350")

def run():
    try:
        import blinkDetect
        # import blinkDetect_2
    except Exception as e:
        print(f"Error in run(): {e}")

def video():
    import last_video
def on_closing():
    # This function gets called when the window is closed via the 'X' button
    root.destroy()

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Drowsiness Detection System")
label.configure(font=("Times New Roman", 25, "bold"))  # Adjust font size and styling here
label.pack(pady=12, padx=10)


button1 = customtkinter.CTkButton(master=frame, text= "Camera", command=run)
button1.configure(font=("Times New Roman", 20, "bold"))
button1.pack(pady=12, padx=10, fill="both")


button2 = customtkinter.CTkButton(master=frame, text= "Last Alert Video", command=video)
button2.configure(font=("Times New Roman", 20, "bold"))
button2.pack(pady=12, padx=10, fill="both")

button3 = customtkinter.CTkButton(master=frame, text="Exit", command=root.destroy)
button3.configure(font=("Times New Roman", 20, "bold"))
button3.pack(pady=12, padx=10, fill="both")

#checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
#checkbox.pack(pady=12, padx=10)

root.protocol("WM_DELETE_WINDOW", on_closing)  # Bind the close event to the function
root.mainloop()