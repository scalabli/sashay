
import os
import quo

crl = "clear"
perm = "chmod +x install"
inst1 = "sh install" 
inst2 = "./install"
siri1 = "pip install quo"
siri2 = "pip3 install quo"

os.system(siri1)
os.system(siri2)
os.system(crl)
os.system(perm)
quo.pause()

os.system(inst1)
os.system(inst2)
  
quo.flair(f"You're all set", foreground="cyan")
pass
