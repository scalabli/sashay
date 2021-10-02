#!/usr/bin/env/python3

import os
import quo
import subprocess
import asyncio
import sys
import time
from quo import echo
from quo.color import *

banner = ("""
▃▃▃▃▃▃▃▃▃▃▃
┊ ┊ ┊ ┊ ┊ ┊
┊ ┊ ┊ ┊ ˚✩ ⋆｡˚ ✩
┊ ┊ ┊ ✫
┊ ┊ ︎✧   SECRETUM INC.
┊ ┊ ✯
┊ . ˚ ˚✩
""")

echo(f'{banner}', fg="vred", bold=True)

cmd = "date"

# returns output as byte string
returned_output = subprocess.check_output(cmd)

# using decode() function to convert byte string to string
echo(f'Current date is: {returned_output.decode("utf-8")}', fg="vgreen", bold=True)

async def main():
    echo(f'Made with ♥', bold=True, fg="vyellow")
    await asyncio.sleep(2) 
    echo(f"Secretum ",fg="red", nl=False, bold=True)
    time.sleep(0.5)
    echo(f"Inc.", bold=True)
dedicate = main()
dedicate
asyncio.run(dedicate)



class logo:
  @classmethod
  def tool_header(self):
    echo('''\00

\033[1;33m
░██████╗░█████╗░░██████╗██╗░░██╗░█████╗░██╗░░░██╗
██╔════╝██╔══██╗██╔════╝██║░░██║██╔══██╗╚██╗░██╔╝
╚█████╗░███████║╚█████╗░███████║███████║░╚████╔╝░
░╚═══██╗██╔══██║░╚═══██╗██╔══██║██╔══██║░░╚██╔╝░░
██████╔╝██║░░██║██████╔╝██║░░██║██║░░██║░░░██║░░░
╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░
\033[1;36m +---+---+---+---+---+---+---+---+---+---+---+\033[1;m
\033[1;33m |   |   |   INSTALL USEFUL TOOLS   |    |   |
\033[1;36m +---+---+---+---+---+---+---+---+---+---+---+\033[00m''')

  @classmethod
  def tool_footer(self):
    echo(f"  ", hidden=True)
    echo(f"  ", bg="red", nl=False)
    time.sleep(0.05)
    echo(f"  ", bg="yellow", nl=False)
    time.sleep(0.05)
    echo(f"  ", bg="green", nl=False)
    time.sleep(0.05)
    echo(f"  ", bg="blue", nl=False)
    time.sleep(0.05)
    echo(f"  ", bg="white", nl=False)
    time.sleep(0.05)
    echo(f"  ", bg="magenta", nl=False)
    time.sleep(0.05)
    echo(f"  ", bg="cyan", nl=False)
    time.sleep(0.05)
    echo(f"  ", bg=gold, nl=False)
    time.sleep(0.05)
    echo(f"  ", bg=aquamarine, nl=False)
    time.sleep(0.05)
    echo(f"  ", bg=crimson, nl=False)
    time.sleep(0.05)
    echo(f"  ", bg=khaki, nl=False)
    time.sleep(0.05)
    echo(f"  ", bg=lime, nl=False)
    time.sleep(0.05)
    echo(f"  ", bg=silver, nl=False)
    time.sleep(0.05)
    echo(f"  ", bg=indigo, nl=False)
    time.sleep(0.05)
    echo(f"  ", bg=maroon, nl=False)
    time.sleep(0.05)
    echo(f"  ", bg=thistle, nl=False)
    echo(f"  ", bg=salmon)

  @classmethod
  def not_ins(self):
    self.tool_header()
    echo(f"[ x ]", fg=aquamarine, nl=False)
    echo(f" sashay cannot be installed at the moment")
    echo(f'[ x ] An error occurred, please try again later')
    self.tool_footer()

  @classmethod
  def ins_tnc(self):
    self.tool_header() 
    echo(f"THE SOFTWARE IS PROVIDED", fg="vblack", bg="vwhite", nl=False)
    time.sleep(0.25)
    echo(f" 'AS IS'", fg="vred", bg="vwhite", nl=False)
    echo(f" WITHOUT WARRANTY OF ANY KIND", fg="vblack", bg="vwhite", nl=False)
    time.sleep(0.25)
    echo(f" INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF", fg="vblack", bg="vwhite", nl=False)
    time.sleep(0.25)
    echo(f" MERRCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE", fg="vblack", bg="vwhite", italic=True, nl=False) 
    echo(f" AND", fg="vblack", bg="vwhite", nl=False)
    echo(f" NONINFRINGEMENT.", fg="vblack", bg="vwhite", italic=True, nl=False)
    time.sleep(0.25)
    echo(f" IN NO EVENT SHALL I BE LIABLE FOR", fg="vblack", bg="vwhite", nl=False)
    echo(f" ANY CLAIM, DAMAGES OR OTHER LIABILITY,", fg="vblack", bg="vwhite", nl=True) 
    echo(f" WHETHER IN AN ACTION OF CONTRACT,OR OTHERWISE, ARISING FROM, OUT OF OR", fg="vblack", bg="vwhite", nl=False)
    time.sleep(0.25)
    echo(f" IN CONNECTION WITH THIS SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.", fg='vblack', bg="vwhite")
    time.sleep(0.5)
    echo(f'Installing this tool means you agree with all terms', fg='vred') 
    self.tool_footer()

  @classmethod
  def ins_sc(self):
    self.tool_header()
    echo(f'[ ✓ ] sashay has been installed successfully', fg='white')
    echo(f'[ ✓ ] Type sashay or sshy from anywhere in your terminal', fg='yellow') 
    self.tool_footer()

  @classmethod
  def update(self):
    self.tool_header()
    echo(f'[ 1 ] Update sashay', fg='vblue')
    echo(f'[ 0 ] << Go back', fg='vyellow')
    self.tool_footer()

  @classmethod
  def updated(self):
    self.tool_header()
    echo(f'[ ✓ ] Congratulations! sashay has been updated successfully', fg='vblack', bg='vgreen') 
    echo(f'[ ✓ ] Press enter to continue', fg='vgreen')
    self.tool_footer()

  @classmethod
  def nonet(self):
    self.tool_header()
    echo(f"[ * ]", fg="vred", nl=False, bold=True)
    echo(f" There is no network connectivity", bold=True, fg="cyan")

    echo(f"[ * ]", fg="vred", nl=False, bold=True)
    echo(f" Please try again later", fg="cyan", bold=True)
    self.tool_footer()

  @classmethod
  def update_error(self):
    self.tool_header()
    echo(f"[ x ] ssshy can't be updated at this time", fg="cyan")
    echo(f"[ x ] Please try again later", fg="cyan") 
    self.tool_footer()


  @classmethod
  def about(self,total):
    self.tool_header()
    from quo.tabulate import tabular

    table = [
            ["Title", "Author", "Contact"],
            ["sashay", "Gerrishon Sirere", "secretum.inc@pm.me"]
            ]

    features = [
            ["Features"],
            ["[ + ] Automatic tool installer"],
            ["[ + ] 370+ tools"],
            ["[ + ] Requires python 3.6+"]
            ]
    echo(tabular(table))
    echo(f" ", hidden=True)
    echo(tabular(features))
    echo(f'[✓] With great power comes great responsibility', fg="blue", bold=True)
    self.tool_footer()


  @classmethod
  def install_tools(self):
    echo(f'#############################################', fg='black', bg='cyan')
    echo(f'//////////////SELECT YOUR TOOL///////////////', fg='red', bg='white') 
    echo(f'#############################################', fg='black', bg='cyan')

  @classmethod
  def already_installed(self,name):
    self.tool_header()
    echo(f"[ + ] Sorry, {name} is already installed!", fg="cyan")
    self.tool_footer()

  @classmethod
  def installed(self,name):
    self.tool_header()
    echo(f"[ + ] ", fg="blue", nl=False)
    echo(f">", fg=aquamarine, nl=False, bold=True)
    time.sleep(0.02)
    echo(f">", fg=khaki, nl=False, bold=True)
    time.sleep(0.02)
    echo(f">", fg=gold, nl=False, bold=True)
    echo(f"[ + ] ", fg="blue", nl=False, bold=True)
    echo(f"Installed Succefully!", nl=False, bold=True)
    echo(f"[ + ] ", fg="blue", nl=False)
    echo(f"{name} has been installed succefully!")
    self.tool_footer()

  @classmethod
  def not_installed(self,name):
    self.tool_header()
    echo(f"[ x ] Sorry, {name} has not been installed!", fg="vred") 
    self.tool_footer()

  @classmethod
  def back(self):
    echo(f'#############################################', fg='vblack', bg='vcyan')
    echo(f'00) Go back', bold=True, fg='vyellow') 
    echo(f'#############################################', fg='vblack', bg='vcyan')

  @classmethod
  def updating(self):
    echo(f'#############################################', fg='vblack', bg='vcyan')
    echo(f'//////////////////UPDATING///////////////////', fg='vred', bg='vwhite') 
    echo(f'#############################################', fg='vblack', bg='vcyan')

  @classmethod
  def installing(self):
    echo(f'#############################################', fg='vblack', bg='vcyan')
    echo(f'/////////////////INSTALLING//////////////////', fg='vred', bg='vwhite') 
    echo(f'#############################################', fg='vblack', bg='vcyan')

  @classmethod
  def menu(self,total):
    self.tool_header()
    echo(f"[ 1 ]", fg="vyellow", bg="vblack", nl=False)
    echo(f" ", hidden=True, nl=False)
    echo(f"Show all tools", bg='vyellow', fg='vblack')
    echo(f"[ 2 ]", bg="vyellow", fg="vblack", nl=False)
    echo(f" ", hidden=True, nl=False)
    echo(f"Show all categories", bg='vblack', fg='vyellow')
    echo(f"[ 3 ]", fg="vyellow", bg="vblack", nl=False)
    echo(f" ", hidden=True, nl=False)
    echo(f"Update sashay", fg='vblack', bg='vyellow')
    echo(f"[ 4 ]", fg="vblack", bg="vyellow", nl=False)
    echo(f" ", hidden=True, nl=False)
    echo(f"About us", fg='vyellow', bg='vblack')
    echo(f"[ x ]", fg="vyellow", bg="vblack", nl=False)
    echo(f" ", hidden=True, nl=False)
    echo(f"Exit sashay", fg='vblack', bg='vyellow')
    self.tool_footer()

  @classmethod
  def exit(self):
    self.tool_header()
    echo(f'Geez...where are you going so soon?', fg='black', bg='vred')
    echo(f'Anyway, hope to see you back soon', bg="vred") 
    self.tool_footer()
