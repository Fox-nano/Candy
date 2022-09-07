import socket
import getpass
import os
computer = socket.gethostname()
account = getpass.getuser()
prompt = "$"
dire = "~"
if account == "Administrator" or account == "root":
    prompt = "#"

print('''
   _____                       _         
  / ____|                     | |        
 | |        __ _   _ __     __| |  _   _ 
 | |       / _` | | '_ \   / _` | | | | |
 | |____  | (_| | | | | | | (_| | | |_| |
  \_____|  \__,_| |_| |_|  \__,_|  \__, |
                                    __/ |
                                   |___/ 
''')
#┌[u0_a191@localhost]-(~)
#└>
while True:
    run = input("┌[" + account + "@" + computer + "]" + "-(" + dire + ")" + '\n' + "└>" + prompt)
    if run == "python":
        os.system("python")
    elif run == "su":
        if prompt == "#":
            print("You are in su!")
        else:
            prompt="#"
    elif run == "nano":
        os.system("nano")
    elif run == "exit":
        break
    elif run == "clean":
        os.system("cls")
    elif run == "":
        continue
    else:
        print(run + ":Not Found")
