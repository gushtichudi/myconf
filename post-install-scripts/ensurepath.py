# This script will ensure that ~/.local/bin is in your $PATH
# Very simple script nothing to worry about

# Doesn't work either too lol

import os

a = os.popen("echo $PATH").read()
b = os.popen("echo $USER").read().replace("\n", "")

for c in a.split(":"):
    if f"/home/{b}/.local/bin" not in c:
        print("ensuring path in bash_profile")
        with open(f"/home/{b}/.profile", 'a') as d:
            d.write("\n# written by confi3\n")
            d.write("export $PATH=$PATH:$HOME/.local/bin\n")
            break
    else:
        exit(0)

os.system("source ~/.profile")
