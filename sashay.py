
import os
import sys
from src.menu import *

if __name__ == "__main__":
  try:
    main.menu()
  except KeyboardInterrupt:
    os.system("clear")
    os.system("echo Exitting...")
    logo.exit()
