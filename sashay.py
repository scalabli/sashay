import quo
import os
import sys
from src.menu import *

if __name__ == "__main__":
  try:
    main.menu()
  except KeyboardInterrupt:
    quo.clear()
    quo.echo(f"Exitting...", reverse=True)
    logo.exit()
