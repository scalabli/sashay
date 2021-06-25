import quo
import os
import sys
from src.menu import *

if __name__ == "__main__":
  try:
    main.menu()
  except KeyboardInterrupt:
    os.system("clear")
    quo.flair(f"Exitting...", foreground="vred")
    logo.exit()
