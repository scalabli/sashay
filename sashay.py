import os
import sys
from quo import clear, echo
from src.menu import *

if __name__ == "__main__":
  try:
    Main.menu()
  except KeyboardInterrupt:
    clear()
    echo("Exitting...", reverse=True)
    logo.exit()
