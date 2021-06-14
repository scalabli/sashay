
import os
import quo

cmd = "clear"
perm = "chmod +x install"
inst1 = "sh install" 
inst2 = "./install"


os.system(cmd)
os.system(perm)
quo.pause()

os.system(inst1)
else:
  os.system(inst2)
  pass
