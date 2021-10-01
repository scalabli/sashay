import quo
import os
import sys
from quo import clear, echo
from src.menu import *

if __name__ == "__main__":
  try:
    main.menu()
  except KeyboardInterrupt:
    clear()
    echo(f"Exitting...", foreground="vred")
    logo.exit()
