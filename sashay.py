import quo
import os
import sys
from quo import echo
from src.menu import *

if __name__ == "__main__":
  try:
    main.menu()
  except KeyboardInterrupt:
    os.system("clear")
    echo(f"Exitting...", foreground="vred")
    logo.exit()
