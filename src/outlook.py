#!/usr/bin/env/python3

import os
import quo
import subprocess
import asyncio

banner = ("""
▃▃▃▃▃▃▃▃▃▃▃
┊ ┊ ┊ ┊ ┊ ┊
┊ ┊ ┊ ┊ ˚✩ ⋆｡˚ ✩
┊ ┊ ┊ ✫
┊ ┊ ︎✧   SECRETUM INC.
┊ ┊ ✯
┊ . ˚ ˚✩
""")

quo.flair(f'{banner}', foreground="vred", bold=True)

cmd = "date"

# returns output as byte string
returned_output = subprocess.check_output(cmd)

# using decode() function to convert byte string to string
quo.flair(f'Current date is: {returned_output.decode("utf-8")}', foreground="vgreen", bold=True)

async def main():
    quo.flair(f'Made with ♥', bold=True, foreground="vyellow")
    await asyncio.sleep(4) 
    quo.flair(f'Secretum Inc.', bold=True, foreground="vyellow")
dedicate = main()
dedicate
asyncio.run(dedicate)


class logo:
  @classmethod
  def tool_header(self):
    quo.flair('''\00

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
    quo.flair(b'\xe2\x99\x88\xe2\x99\x89\xe2\x99\x8a\xe2\x99\x8b\xe2\x99\x8c\xe2\x99\x8d\xe2\x99\x8e\xe2\x99\x8f\xe2\x99\x90\xe2\x99\x91\xe2\x99\x92\xe2\x99\x93\xe2\x99\x88\xe2\x99\x89\xe2\x99\x8a\xe2\x99\x8b\xe2\x99\x8c\xe2\x99\x8d\xe2\x99\x8e\xe2\x99\x8f\xe2\x99\x90\xe2\x99\x91\xe2\x99\x92')

  @classmethod
  def not_ins(self):
    self.tool_header()
    quo.echo(f'[ x ] sashay cannot be installed at the moment')
    quo.echo(f'[ x ] An error occurred, please try again later')
    self.tool_footer()

  @classmethod
  def ins_tnc(self):
    self.tool_header() 
    quo.flair(f'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERRCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL I BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THIS SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.', foreground='vblack', background='vwhite')
    quo.flair(f'Installing this tool means you agree with all terms', foreground='vred') 
    self.tool_footer()

  @classmethod
  def ins_sc(self):
    self.tool_header()
    quo.flair(f'[ ✓ ] sashay has been installed successfully', foreground='white')
    quo.flair(f'[ ✓ ] Type sashay or sshy from anywhere in your terminal', foreground='yellow') 
    self.tool_footer()

  @classmethod
  def update(self):
    self.tool_header()
    quo.flair(f'[ 1 ] Update sashay', foreground='vblue')
    quo.flair(f'[ 0 ] << Go back', foreground='vyellow')
    self.tool_footer()

  @classmethod
  def updated(self):
    self.tool_header()
    quo.flair(f'[ ✓ ] Congratulations! sashay has been updated successfully', foreground='vblack', background='vgreen') 
    quo.flair(f'[ ✓ ] Press enter to continue', foreground='vgreen')
    self.tool_footer()

  @classmethod
  def nonet(self):
    self.tool_header()
    quo.flair(f'[ x ] There is no network connectivity', bold=True, foreground='cyan')
    quo.flair(f'[ x ] Please try again later', foreground='cyan')
    self.tool_footer()

  @classmethod
  def update_error(self):
    self.tool_header()
    quo.flair(f"[ x ] ssshy can't be updated at this time", foreground="cyan")
    quo.flair(f"[ x ] Please try again later", foreground="cyan") 
    self.tool_footer()


  @classmethod
  def about(self,total):
    self.tool_header()
    quo.flair(f'[✓] sashay', foreground='vblack', background='vyellow')
    quo.flair(f'[✓] By Gerrishon Sirere(code-plug)', foreground='vblue')
    quo.flair(f'[✓] With great power comes great responsibility', underline=True, foreground='vblue')
    quo.flair(f'[✓] 360+ tools', foreground='red') 
    quo.flair(f'[✓] Made for Linux based systems', foreground='blue')
    quo.flair(f'Social media [yn] ', foreground="cyan", nl=False)
    c = quo.interpose()
    quo.echo()
    if c == 'y':
        quo.launch('https://linktr.ee/secretum')
    elif c == 'n':
          quo.flair(f':-', foreground="yellow")
    else:
        quo.echo('Invalid input :(',)
    self.tool_footer()


  @classmethod
  def install_tools(self):
    quo.flair(f'#############################################', foreground='black', background='cyan')
    quo.flair(f'//////////////SELECT YOUR TOOL///////////////', foreground='red', background='white') 
    quo.flair(f'#############################################', foreground='black', background='cyan')

  @classmethod
  def already_installed(self,name):
    self.tool_header()
    quo.flair(f"[ + ] Sorry, {name} is already installed!", foreground="cyan")
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
    quo.flair(f"[ x ] Sorry, {name} has not been installed!", foreground="vred") 
    self.tool_footer()

  @classmethod
  def back(self):
    quo.flair(f'#############################################', foreground='vblack', background='vcyan')
    quo.flair(f'00) Go back', bold=True, foreground='vyellow') 
    quo.flair(f'#############################################', foreground='vblack', background='vcyan')

  @classmethod
  def updating(self):
    quo.flair(f'#############################################', foreground='vblack', background='vcyan')
    quo.flair(f'//////////////////UPDATING///////////////////', foreground='vred', background='vwhite') 
    quo.flair(f'#############################################', foreground='vblack', background='vcyan')

  @classmethod
  def installing(self):
    quo.flair(f'#############################################', foreground='vblack', background='vcyan')
    quo.flair(f'/////////////////INSTALLING//////////////////', foreground='vred', background='vwhite') 
    quo.flair(f'#############################################', foreground='vblack', background='vcyan')

  @classmethod
  def menu(self,total):
    self.tool_header()
    quo.flair(f'[ 1 ] Show all tools', background='vyellow', foreground='vblack')
    quo.flair(f'[ 2 ] Show all categories', background='vblack', foreground='vyellow')
    quo.flair(f'[ 3 ] Update sashay', foreground='vblack', background='vyellow')
    quo.flair(f'[ 4 ] About us', foreground='vyellow', background='vblack')
    quo.flair(f'[ x ] Exit sashay', foreground='vblack', background='vyellow')
    self.tool_footer()

  @classmethod
  def exit(self):
    self.tool_header()
    quo.flair(f'Geez...where are you going so soon?', foreground='black', background='vred')
    quo.flair(f'Anyway, hope to see you back soon', background="vred") 
    self.tool_footer()
