import os

crl = "clear"
perm = "chmod +x install"
inst1 = "sh install" 
inst2 = "./install"


os.system("install quo")
os.system("pip3 install quo")

os.system(crl)
os.system(perm)

import quo
from quo import echo, pause
pause()

os.system(inst1)
os.system(inst2)
  
echo(f"You're all set", foreground="cyan")
pass
