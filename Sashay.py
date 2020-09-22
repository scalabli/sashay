#This file is part of Sashay and may be subject to redistribution and commercial restrictions. Please visit our website
#for more information on licensing and terms of use.
#
#


import os
import fibo
import sys
from modules.menu import *

if __name__=="__main__":
  try:
    main.menu()
  except KeyboardInterrupt:
    os.system("clear")
    logo.exit()
