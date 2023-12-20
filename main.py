import customtkinter
import tkinter
from tkinter import *
import os
import func


# Starting the tk windows
window = customtkinter.CTk()
window.geometry("800x540")
window.resizable(width=0,height=0)
window.configure(fg_color='midnight blue')

# Starting the App()
def App():

    customtkinter.CTkLabel(master=window,text="AutoTask CLI",justify="center",font=("DejaVu Sans Mono",16,"bold")).pack()
    text_input = customtkinter.CTkTextbox(master=window,fg_color="midnight blue",width=770,height=99,font=("DejaVu Sans Mono",14))
    text_input.place(x=30,y=40)
    line_canvas = Canvas(window, width=800, height=1)
    line_canvas.place(x=0,y=139)
    line_canvas.create_line(0,99,800,99,fill="white",width=1)
    text_output = customtkinter.CTkTextbox(master=window,fg_color="midnight blue",width=800,height=400,state="normal",font=("DejaVu Sans Mono",15),text_color='lime green')
    text_output.place(x=0,y=140)
    customtkinter.CTkLabel(master=window,text=">>>",font=("DejaVu Sans Mono",16)).place(x=0,y=43)

    def Process_Command(event):
        cmd = text_input.get("1.0","end-1c")
        text_input.delete("1.0","end-1c")
        text_output.configure(state='normal')
        text_output.delete("2.0","end")
        text_output.configure(state='disabled')
        func.process(cmd,text_output)
    
    func.Print_cwd(text_output)

    text_input.bind('<Return>',Process_Command)

    

App()
window.mainloop()