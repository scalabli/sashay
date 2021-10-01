#!/usr/bin/env/python3

import os
import quo
import subprocess
import asyncio
import sys
import time
from quo import echo

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
    time.sleep(1)
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
    echo(b'\xe2\x99\x88\xe2\x99\x89\xe2\x99\x8a\xe2\x99\x8b\xe2\x99\x8c\xe2\x99\x8d\xe2\x99\x8e\xe2\x99\x8f\xe2\x99\x90\xe2\x99\x91\xe2\x99\x92\xe2\x99\x93\xe2\x99\x88\xe2\x99\x89\xe2\x99\x8a\xe2\x99\x8b\xe2\x99\x8c\xe2\x99\x8d\xe2\x99\x8e\xe2\x99\x8f\xe2\x99\x90\xe2\x99\x91\xe2\x99\x92')

  @classmethod
  def not_ins(self):
    self.tool_header()
    echo(f'[ x ] sashay cannot be installed at the moment')
    echo(f'[ x ] An error occurred, please try again later')
    self.tool_footer()

  @classmethod
  def ins_tnc(self):
    self.tool_header() 
    echo(f"THE SOFTWARE IS PROVIDED", fg="vblack", nl=False)
    time.sleep(0.25)
    echo(f"'AS IS'", fg="vred", bg="vwhite", nl=False)
    echo(f"WITHOUT WARRANTY OF ANY KIND", fg="vblack", bg="vwhite", nl=False)
    time.sleep(0.25)
    echo(f"INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF", fg="vblack", bg="vwhite", nl=False)
    time.sleep(0.25)
    echo(f"MERRCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE", fg="vblack", bg="vwhite", italic=True, nl=False) 
    echo(F"AND", fg="vblack", bg="vwhite", nl=False)
    echo(f"NONINFRINGEMENT.", fg="vblack", bg="vwhite", italic=True, nl=False)
    time.sleep(0.25)
    echo(f"IN NO EVENT SHALL I BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THIS SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."", fg='vblack', bg='vwhite')
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
    echo(f'[ x ] There is no network connectivity', bold=True, fg='cyan')
    echo(f'[ x ] Please try again later', fg='cyan')
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
    for i in range(3):
        echo(f"{i}",  fg="red", bold=True, bg="white")
        sys.stdout.flush()
        time.sleep(1)
    __banner__ = """
       +=======================================+
       |.................sashay................|
       +---------------------------------------+
       |Author: Gerrishon Sirere               |
       |Contact: secretum.inc@pm.me            |
       |[+]sshy is an automatic tool installer |
       |[+] 370+ tools                         |
       |[+] Python 3.6+                        |
       +---------------------------------------+
       |................sashay.................|
       +=======================================+
       """



    echo(f"{__banner__}", fg="green", bold=True)
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
    print(f'''
\033[1;33m  [ + ] \033[1;32mInstalled Successfully !!
\033[1;33m  [ + ] \033[1;37m'{name}'\033[01;32m is Installed Successfully !!
''')
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
    echo(f'[ 1 ] Show all tools', bg='vyellow', fg='vblack')
    echo(f'[ 2 ] Show all categories', bg='vblack', fg='vyellow')
    echo(f'[ 3 ] Update sashay', fg='vblack', bg='vyellow')
    echo(f'[ 4 ] About us', fg='vyellow', bg='vblack')
    echo(f'[ x ] Exit sashay', fg='vblack', bg='vyellow')
    self.tool_footer()

  @classmethod
  def exit(self):
    self.tool_header()
    echo(f'Geez...where are you going so soon?', fg='black', bg='vred')
    echo(f'Anyway, hope to see you back soon', bg="vred") 
    self.tool_footer()
