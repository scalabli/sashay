#This file is part of sashay and may be subject to redistribution and commercial restrictions. Please visit our website
#for more information on licensing and terms of use.

import os
import sys
from time import sleep
from src.outlook import *
from src.system import *

class tool:
  @classmethod
  def install(self):
    while True:
      system=sys()
      os.system("clear")
      logo.ins_tnc()
      inp=input("quo.confirm("Do you want to install sashay?:", abort=True)
      if inp=="y" or inp=="Y":
        os.system("clear")
        logo.installing()
        if system.sudo is not None:
          #require root permission
          if os.path.exists(system.conf_dir+"/sashay"):
            pass
          else:
            os.system(system.sudo+" mkdir "+system.conf_dir+"/sashay")
          os.system(system.sudo+" cp -r src assets sashay.py "+system.conf_dir+"/sashay")
          os.system(system.sudo+" cp -r assets/sashay "+system.bin)
          os.system(system.sudo+" cp -r assets/sshy "+system.bin)
          os.system(system.sudo+" chmod +x "+system.bin+"/sashay")
          os.system(system.sudo+" chmod +x "+system.bin+"/sshy")
          os.system("cd .. && "+system.sudo+" rm -rf sashay")
          if os.path.exists(system.bin+"/sashay") and os.path.exists(system.conf_dir+"/sashay"):
            os.system("clear")
            logo.ins_sc()
            tmp=input("\033[1;36m ##> \033[00m")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input("\033[1;36m ##> \033[00m")
            break
        else:
          if os.path.exists(system.conf_dir+"/sashay"):
            pass
          else:
            os.system("mkdir "+system.conf_dir+"/sashay")
          os.system("cp -r src assets sashay.py "+system.conf_dir+"/sashay")
          os.system("cp -r assets/sashay "+system.bin)
          os.system("cp -r assets/sshy "+system.bin)
          os.system("chmod +x "+system.bin+"/sashay")
          os.system("chmod +x "+system.bin+"/sshy")
          os.system("cd .. && rm -rf sashay")
          if os.path.exists(system.bin+"/sashay") and os.path.exists(system.conf_dir+"/sashay"):
            os.system("clear")
            logo.ins_sc()
            tmp=input("\033[1;36m ##> \033[00m")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input("\033[1;36m ##> \033[00m")
            break
      else:
        break

if __name__=="__main__":
  try:
    tool.install()
  except KeyboardInterrupt:
    os.system("clear")
    logo.exit()
