#!/usr/bin/env/python3

import os
import quo
import subprocess
import asyncio
import sys
import time
from . import __version__ as s_version
from quo import __version__ as q_version
from quo.accordance import WIN
from quo.color import *
from quo import clear, container, echo, print
from quo.console import Console
from quo.keys import bind
from quo.layout import FormattedTextControl, HSplit, Window
from quo.text import Text
from quo.widget import Box, Frame, Label
from quo.widget.core import Border
from quo.widget import TextField

console = Console()
banner = ("""
▃▃▃▃▃▃▃▃▃▃▃
┊ ┊ ┊ ┊ ┊ ┊
┊ ┊ ┊ ┊ ˚✩ ⋆｡˚ ✩
┊ ┊ ┊ ✫
┊ ┊ ︎✧   SCALABLI.
┊ ┊ ✯
┊ . ˚ ˚✩
""")


bann = ("""
███████████████████████████████████
█─▄▄▄▄██▀▄─██─▄▄▄▄█─█─██▀▄─██▄─█─▄█
█▄▄▄▄─██─▀─██▄▄▄▄─█─▄─██─▀─███▄─▄██
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▀▄▀▄▄▀▄▄▀▀▄▄▄▀▀

""")

#f"[ 1 ]", fg="vyellow", bg="vblack", nl=False)
 #   quo.echo(f" ", hidden=True, nl=False)
 #   show_all = """𝕊𝕙𝕠𝕨 𝕒𝕝𝕝 𝕥𝕠𝕠𝕝𝕤"""
  #  quo.echo(f"{show_all}", bg='vyellow', fg='vblack')
#    time.sleep(0.3)
#    quo.echo(f"[ 2 ]", bg="vyellow", fg="vblack", nl=False)
#    quo.echo(f" ", hidden=True, nl=False)
#    show_a = """𝕊𝕙𝕠𝕨 𝕒𝕝𝕝 𝕔𝕒𝕥𝕖𝕘𝕠𝕣𝕚𝕖𝕤"""
 #   quo.echo(f"{show_a}", bg='vblack', fg='vyellow')
#    time.sleep(0.3)
#    quo.echo(f"[ 3 ]", fg="vyellow", bg="vblack", nl=False)
 #   quo.echo(f" ", hidden=True, nl=False)
#    update = """𝕌𝕡𝕕𝕒𝕥𝕖 𝕊𝕒𝕤𝕙𝕒𝕪"""
#    quo.echo(f"{update}", fg='vblack', bg='vyellow')
  #  time.sleep(0.2)
 #   quo.echo(f"[ 4 ]", fg="vblack", bg="vyellow", nl=False)
 #   quo.echo(f" ", hidden=True, nl=False)
#    about = """𝔸𝕓𝕠𝕦𝕥 𝕦𝕤"""
#    quo.echo(f"{about}", fg='vyellow', bg='vblack')
 #   time.sleep(0.2)
#    quo.echo(f"[ x ]", fg="vyellow", bg="vblack", nl=False)
#    quo.echo(f" ", hidden=True, nl=False)
#    exit_s = """𝔼𝕩𝕚𝕥 𝕊𝕒𝕤𝕙𝕒𝕪"""
 #   quo.echo(f"{exit_s}", fg='vblack', bg='vyellow')
 #   self.tool_footer()

#@bind.add("n")
#def _(event):
#    event.app.exit()

#body =  HSplit([
 #           Window(FormattedTextControl(banner, style="fg:red")),
          #  Window(height=1, char=Border.HORIZONTAL)])

#container(body)

#content = Label(f"sashay v {s_version}, using quo v {q_version}")
#container(content)

class logo:
  @classmethod
  def tool_header(self):
      content = Window(FormattedTextControl(f"{bann}", style="fg:yellow bg:blue bold"), align="center")
      return container(content)

  @classmethod
  def tool_footer(self):
      echo(f"  ", hidden=True)
      echo(f"  ", bg="red", nl=False)
      time.sleep(0.0008)
      echo("  ", bg="yellow", nl=False)
      time.sleep(0.0008)
      echo("  ", bg="green", nl=False)
      time.sleep(0.0008)
      echo(f"  ", bg="blue", nl=False)
      time.sleep(0.0008)
      echo("  ", bg="white", nl=False)
      time.sleep(0.0008)
      echo(f"  ", bg="magenta", nl=False)
      time.sleep(0.0008)
      echo("  ", bg="cyan", nl=False)
      time.sleep(0.0008)
      echo("  ", bg=gold, nl=False)
      time.sleep(0.0008)
      echo("  ", bg=aquamarine, nl=False)
      time.sleep(0.0008)
      echo("  ", bg=crimson, nl=False)
      time.sleep(0.0008)
      echo("  ", bg=khaki, nl=False)
      time.sleep(0.0008)
      echo(f"  ", bg=lime, nl=False)
      time.sleep(0.0008)
      echo(f"  ", bg=silver, nl=False)
      time.sleep(0.0008)
      echo(f"  ", bg=indigo, nl=False)
      time.sleep(0.0008)
      echo(f"  ", bg=maroon, nl=False)
      time.sleep(0.0008)
      echo(f"  ", bg=thistle, nl=False)
      time.sleep(0.0008)
      echo("  ", bg="yellow", nl=False)
      time.sleep(0.0008)
      echo("  ", bg="green", nl=False)
      time.sleep(0.0008)
      echo(f"  ", bg="blue", nl=False)
      time.sleep(0.0008)
      echo("  ", bg="white", nl=False)
      time.sleep(0.0008)
      echo(f"  ", bg="magenta", nl=False)
      time.sleep(0.0008)
      echo("  ", bg="cyan")

  @classmethod
  def not_ins(self):
    self.tool_header()
    quo.echo(f"[ x ]", fg=aquamarine, nl=False)
    quo.echo(f" sashay cannot be installed at the moment")
    quo.echo(f'[ x ] An error occurred, please try again later')
    self.tool_footer()

  @classmethod
  def ins_tnc(self):
    self.tool_header()

    quo.echo(f"THE SOFTWARE IS PROVIDED", fg="vblack", bg="vwhite", nl=False)
    time.sleep(0.25)
    quo.echo(f" 'AS IS'", fg="vred", bg="vwhite", nl=False)
    quo.echo(f" WITHOUT WARRANTY OF ANY KIND", fg="vblack", bg="vwhite", nl=False)
    time.sleep(0.25)
    quo.echo(f" INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF", fg="vblack", bg="vwhite", nl=False)
    time.sleep(0.25)
    quo.echo(f" MERRCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE", fg="vblack", bg="vwhite", italic=True, nl=False) 
    quo.echo(f" AND", fg="vblack", bg="vwhite", nl=False)
    quo.echo(f" NONINFRINGEMENT.", fg="vblack", bg="vwhite", italic=True, nl=False)
    time.sleep(0.25)
    quo.echo(f" IN NO EVENT SHALL I BE LIABLE FOR", fg="vblack", bg="vwhite", nl=False)
    quo.echo(f" ANY CLAIM, DAMAGES OR OTHER LIABILITY,", fg="vblack", bg="vwhite", nl=True) 
    quo.echo(f" WHETHER IN AN ACTION OF CONTRACT,OR OTHERWISE, ARISING FROM, OUT OF OR", fg="vblack", bg="vwhite", nl=False)
    time.sleep(0.25)
    quo.echo(f" IN CONNECTION WITH THIS SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.", fg='vblack', bg="vwhite")
    time.sleep(0.5)
    quo.echo(f'Installing this tool means you agree with all terms', fg='vred') 
    self.tool_footer()

  @classmethod
  def ins_sc(self):
    self.tool_header()
    quo.echo(f'[ ✓ ] sashay has been installed successfully', fg='white')
    quo.echo(f'[ ✓ ] Type sashay or sshy from anywhere in your terminal', fg='yellow') 
    self.tool_footer()

  @classmethod
  def update(self):
    self.tool_header()
    console.bar("UPDATES")
    quo.echo(f'[ 1 ] Update sashay', fg='vblue')
    quo.echo(f'[ 0 ] << Go back', fg='vyellow')
    self.tool_footer()
  @bind.add("ctrl-b")
  def goback(event):
      event.app.quo.keys.focus.previous()

  @classmethod
  def updated(self):
    self.tool_header()
    echo(f'[ ✓ ] Congratulations! sashay has been updated successfully', fg='vblack', bg='vgreen') 
    echo(f'[ ✓ ] Press enter to continue', fg='vgreen')
    self.tool_footer()

  @classmethod
  def nonet(self):
    @bind.add("<any>")
    def _(event):
        event.app.exit()

    self.tool_header()
    container(
            Box(
                Window(
                    FormattedTextControl(
                        Text("<red>[ * ]</red> <cyan><b>There is no network connectivity</b></cyan>\n<red>[ * ]</red> <cyan><b>Please try again</b></cyan>\n\n<green>Press any key to go back</green>")
                        )
                    )
                ),
            bind=True,
            full_screen=True
            )
    self.tool_footer()

  @classmethod
  def update_error(self):
    self.tool_header()
    echo(f"[ x ] sshy can't be updated at this time", fg="cyan")
    echo(f"[ x ] Please try again later", fg="cyan") 
    self.tool_footer()


  @classmethod
  def about(self,total):
    from quo.table import _Table
    self.tool_header()

    @bind.add("ctrl-b")
    def _(event):
        event.app.exit()

    data = [
            ["Title", "Author", "Contact"],
            ["sashay", "Gerrishon Sirere", "scalabli@pm.me"]
            ]

    features = [
            ["Features"],
            ["[ + ] Automatic tool installer"],
            ["[ + ] 370+ tools"],
            ["[ + ] Requires python 3.8+"]
            ]
    content =  HSplit([
        Window(
            FormattedTextControl(
                banner, 
                style="fg:red"
                )
            ),
        Window(
            height=1, 
            char=Border.HORIZONTAL
            ),
        Label(f"sashay v {s_version}, using quo v {q_version}"
),
        Window(FormattedTextControl((_Table(data, theme="fancy_grid"))), align="center"),
        Window(FormattedTextControl((_Table(features, theme="fancy_grid"))), align="center"),
        Frame(Label("       https://github.com/scalabli/sashay")),
        Window(FormattedTextControl(Text("\n\n<b><aquamarine>[</aquamarine> <red>»</red> <aquamarine>]</aquamarine> <cyan>With great power, comes great responsibility</cyan>\n\n<green>Press `ctrl-c` or `ctrl-b` to go back</green></b>")))
        ])
    container(content, bind=True, full_screen=True)
    self.tool_footer()


  @classmethod
  def install_tools(self):
    console.bar("SELECT YOUR TOOL")

  @classmethod
  def already_installed(self,name):
      self.tool_header()

      @bind.add("<any>")
      def _(event):
          event.app.exit()

      container(
              Box(
            Label(f"Sorry, {name} is already installed!\nPress any key to go back", style="fg:cyan")), bind=True, full_screen=True)
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
      if WIN:
          text = """00) Go Back"""
      else:
          text = """𝟘𝟘) 𝔾𝕠 𝕓𝕒𝕔𝕜"""
      container(
                  Label(text, style="reverse")
                  )

  @classmethod
  def updating(self):
    quo.echo(f'#############################################', fg='vblack', bg='vcyan')
    quo.echo(f'//////////////////UPDATING///////////////////', fg='vred', bg='vwhite') 
    quo.echo(f'#############################################', fg='vblack', bg='vcyan')

  @classmethod
  def installing(self):
      echo("#############################################")
             #     Label(
            #          "/////////////////INSTALLING//////////////////")
          #        Label(
             #         "#############################################")
             #     )
        #      ])
         #     )

  @classmethod
  def menu(self,total):
      self.tool_header()
      if WIN:
          show_all = """[1] Show all tools"""
          show_cat = """[2] Show all categories"""
          update = """[3] Update Sashay"""
          about = """[4] About us"""
          exit_s = """[x] Exit Sashay"""
      else:
          show_all = """ [1] 𝕊𝕙𝕠𝕨 𝕒𝕝𝕝 𝕥𝕠𝕠𝕝𝕤"""
          show_cat = """ [2] 𝕊𝕙𝕠𝕨 𝕒𝕝𝕝 𝕔𝕒𝕥𝕖𝕘𝕠𝕣𝕚𝕖𝕤"""
          update = """ [3] 𝕌𝕡𝕕𝕒𝕥𝕖 𝕊𝕒𝕤𝕙𝕒𝕪"""
          about = """ [4] 𝔸𝕓𝕠𝕦𝕥 𝕦𝕤"""
          exit_s = """ [x] 𝔼𝕩𝕚𝕥 𝕊𝕒𝕤𝕙𝕒𝕪"""
      container(
              HSplit([
                  Window(FormattedTextControl(f"{show_all}", style="fg:black bg:#006B47"), align="center"),
                  Window(FormattedTextControl(f"{show_cat}", style="fg:black bg:#009965"), align="center"),
                  Window(FormattedTextControl(f"{update}", style="fg:black bg:#00C684"), align="center"),
                  Window(FormattedTextControl(f"{about}", style="fg:black bg:#009965"), align="center"),
                  Window(FormattedTextControl(f"{exit_s}", style="fg:black bg:#006B47"), align="center")
                  ])
              )
      self.tool_footer()

  @classmethod
  def exit(self):
    self.tool_header()

    console.bar("See you soon")
