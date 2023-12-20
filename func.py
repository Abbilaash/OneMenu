import os

# Printing current working directory
def Print_cwd(textbox):
    textbox.insert("0.0","[+] current dir>"+os.getcwd())
    textbox.configure(state='disabled')

# Pre processing the command
def process(text,textbox):
    cmd = text.split() #Splitting the command in form of tokens
    if cmd[0].lower() == 'dir':
        textbox.configure(state='normal')
        h = dir()
        h = ['\n']+h
        if ".ipynb_checkpoints" in h:
            h.remove('.ipynb_checkpoints')
        for f in h:
            textbox.insert("2.0",f+"\n")
        textbox.configure(state='disabled')

    elif cmd[0].lower() == "cd":
        textbox.configure(state='normal')
        try:
            f = text.split('"')[1::2][0]
            try:
                os.chdir(f)
                textbox.delete("0.0","end")
                Print_cwd(textbox)
            except:
                textbox.insert("2.0","\n\n[-] No such file or directory: '"+f+"'")
                textbox.configure(state='disabled')
        except:
            f = cmd[1]
            try:
                os.chdir(f)
                textbox.delete("0.0","end")
                Print_cwd(textbox)
            except:
                textbox.insert("2.0","\n\n[-] No such file or directory: '"+f+"'")
                textbox.configure(state='disabled')

    elif cmd[0].lower() == "mkdir":
        f = text.split('"')[1::2]
        CREATE_FOLDER(textbox,f[0])
            
    elif cmd[0].lower() == "cat":
        try:
            f = text.split('"')[1::2][0]
            READ_ANY_FILE(textbox,f)
        except:
            # enter the condition of the file is not found or using ""
            pass






    elif cmd[0].lower() == "close" or cmd[0].lower() == "clear":
        textbox.configure(state='normal')
        textbox.delete("0.0","end")
        Print_cwd(textbox)
        textbox.configure(state='disabled')

    elif cmd[0] == "exit":
        exit()
        
    else:
        textbox.configure(state='normal')
        textbox.insert("2.0","\n\n[-] Command '"+cmd[0]+"' not found!")
        textbox.configure(state='disabled')




def READ_ANY_FILE(textbox,filename):
    try:
        with open(filename, 'rb') as file:
            file_content = file.read()
            textbox.configure(state='normal')
            textbox.delete("0.0","end")
            textbox.insert("2.0",file_content)
            textbox.configure(state='disabled')
    except FileNotFoundError:
        textbox.configure(state='normal')
        textbox.insert("2.0","[-] File not found!")
        textbox.configure(state='disabled')



def CREATE_FOLDER(textbox,folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        textbox.configure(state='normal')
        textbox.insert("2.0","\n\n[+] Directory created: '"+folder_name+"'")
        textbox.configure(state='disabled')
    else:
        textbox.configure(state='normal')
        textbox.insert("2.0","\n\n[-] The directory already exists!")
        textbox.configure(state='disabled')

def dir():
    try:
        if len(os.listdir()) == 0:
            return ["\n[+] The directory is empty!"]
        else:
            return os.listdir()
    except:
        return ["[-] Could not execute command!"]




    