
import os
import quo

crl = "clear"
perm = "chmod +x install"
inst1 = "sh install" 
inst2 = "./install"
siri1 = "pip install quo"
siri1 = "pip3 install quo"


os.system(crl)
os.system(perm)
quo.pause()

os.system(inst1)
os.system(inst2)
  
quo.flair(f"You're all set", fg='vcyan')
pass
