import os
import json
import time

from quo import clear, echo, print
from quo.color.rgb import aquamarine
from quo.keys import bind
from quo.prompt import Prompt
from quo.text import Text
from .outlook import logo
from .system import *



class Main:
  def install_tools(self):
    while True:
      tool=tools()
      num=1
      total=len(tool.names)
      clear()
      logo.install_tools()

        #print(f" ")
      for tool_name in tool.meta:
        echo(f"[", fg="vyellow", bold=True, nl=False)
        echo(f" {num} ", fg="vmagenta", italic=True, nl=False)
        echo(f"]", fg="vyellow", bold=True, nl=False)
        echo(f" Install ", nl=False)
        echo(f"{tool_name}",  fg=aquamarine, bold=True)
        num+=1
      echo(f"")
      logo.back()
    #  echo(f"sshy", fg="vblue", italic=True, bold=True, nl=False)
  #    echo(f">>>", fg="cyan", bold=True, italic=True)

      session = Prompt(bottom_toolbar=Text(' <b>List of</b> <u>all</u> <style bg="red">tools</style>'), placeholder=Text('<gray>(please type something)</gray>'))

      cmd = session.prompt("» ")

      if cmd=="00" or cmd=="back":
          self.menu()
          break
      else:
        try:
            if int(cmd)>=1 and int(cmd)<=int(total):
                clear()
                logo.installing()
                print("<green>Installing...</green>")
                tool.install(tool.names[int(cmd)-1])
            else:
                echo(f"Sorry, '{cmd}', is an invalid input !!", fg="black", bg="red")
                sleep(1)
        except ValueError:
            echo(f"Error:",fg="black", bg="vred", nl=False)
            echo(f" {cmd}", nl=False, fg="yellow")
            echo(f" is an invalid input!!", fg="red")
            time.sleep(1)
  def category(self):
    while True:
      tool=tools()
      total=len(tool.category)
      num=1
      clear()
      logo.tool_header()
      echo(f"")
      for cat in tool.category:
        echo(f"[", fg="yellow", nl=False, bold=True)
        echo(f" {num} ", fg="magenta", nl=False, italic=True)
        echo(f"]", fg="yellow", bold=True, nl=False)
        echo(f" {tool.category_data[cat]}", fg="vblue", bold=True)
        num+=1
      echo("")
      logo.back()
      session = Prompt(bottom_toolbar=Text(' <b>List of</b> <u>all</u> tools in <style bg="red">categories</style>'), placeholder=Text('<gray>(please type something)</gray>'))
      cmd = session.prompt("$» ")

   
      if cmd=="00" or cmd=="back":
        self.menu()
        break
      else:
        try:
          if int(cmd) in range(1,int(total)+1):
            while True:
              print(int(cmd)-1)
              print(tool.category[int(cmd)-1])
              cnt=1
              clear()
              logo.tool_header()
              tmp_cat_tool=[]
              for i in tool.names:
                if tool.category[int(cmd)-1] in tool.data[i]["category"]:
                  tmp_cat_tool.append(tool.data[i]['name'])
                  echo("[", bold=True, fg="vblue", nl=False)
                  echo(f" {cnt} ", bold=True, fg="green", nl=False)
                  echo(f"]", bold=True, fg="vblue", nl=False)
                  echo(" Install", fg="vyellow", nl=False)
                  echo(f" {tool.data[i]['name']}", fg="cyan", bold=True)
                  cnt+=1
              print(f"")
              logo.back()
              if tool.category == "information_gathering":
                  print("ddd")

              session =  Prompt(bottom_toolbar=Text(' <b>List of</b> <u>all</u> tools in <style bg="red">categories</style>'), placeholder=Text('<gray>(please type something)</gray>'))
              tcmd = session.prompt("$» ")
              if tcmd=="00" or tcmd=="back":
                break
              else:
                try:
                  cat_total=len(tmp_cat_tool)
                  if int(tcmd) in range(1,int(cat_total)+1):
                    clear()
                    logo.installing()
                    print(f"<green>Installing ...</green>")
                    tool.install(tmp_cat_tool[int(tcmd)-1])
                  else:
                    print(f"<violate>Sorry</violate> <blue>'{tcmd}'</blue> is an <red>invalid</red> input !!")
                    time.sleep(1)
                except ValueError:
                  print(f"<violate>Sorry</violate> <blue>'{tcmd}'</blue> is an <red>invalid</red> input !!")
                  time.sleep(1)
          else:
            print(f"<violate>Sorry</violate> <blue>'{cmd}'</blue> is an <red>invalid</red> input !!")
            time.sleep(1)
        except ValueError:
          print(f"<violate>Sorry</violate> <blue>'{cmd}'</blue> is an <red>invalid</red> input !!")
          time.sleep(1)
  #######################

 # def category(self):
   # while True:
  #    tool=tools()
   #   total=len(tool.category)
   #   num=1
    #  quo.clear()
      #logo.tool_header()
      #print(f"")
     # for cat in tool.category:
      #  quo.echo(f"[", fg="vyellow", nl=False, bold=True)
      #  time.sleep(0.02)
     #   quo.echo(f"{num}", fg="vmagenta", italic=True, bold=True, nl=False)
     #   time.sleep(0.02)
      #  quo.echo(f" ]", fg="vyellow", nl=False, bold=True)
     #   time.sleep(0.02)
    #    quo.echo(f" {tool.category_data[cat]}", fg=aquamarine, bold=True)
    #    num+=1
  #    quo.echo(f"")
  #    logo.back()
  #    quo.echo(f"sshy ", fg="vgreen",


  def update(self):
    while True:
      session = Prompt(placeholder=Text("<grey>(please type something)</grey>"))
      _inp = session.prompt("$» ")
      clear()
      logo.update()

      session = Prompt(bottom_toolbar=Text(' <b>Check/Download</b> <u>new</u>  <style bg="red">updates</style>'), placeholder=Text('<style color="#888888">(please type something)</style>'))

      cmd= session.prompt("$» ")
      if cmd=="1":
        system=sys()
        if system.connection():
          clear()
          logo.updating()
          if system.sudo != None:
            if os.path.exists(system.home+"/sashay"):
              pass
            else:
              os.system(system.sudo+" git clone https://github.com/scalabli.git "+system.home+"/sashay")
            if os.path.exists(system.home+"/sashay/install.sshy"):
              os.system("cd "+system.home+"/sashay;"+system.sudo+" ./install.sshy")
              if os.path.exists(system.bin+"/sashay") and os.path.exists(system.conf_dir+"/sashay"):
                clear()
                logo.updated()
                cmd = _inp

              else:
                clear()
                logo.update_error()
                cmd = _inp

            else:
              clear()
              logo.update_error()
              cmd = _inp

          else:
            if os.path.exists(system.home+"/sashay"):
              pass
            else:
              os.system("git clone https://github.com/scalabli/sashay.git "+system.home+"/sashay")
            if os.path.exists(system.home+"/sashay/install.sshy"):
              os.system("cd "+system.home+"/sashay;./install.sshy")
              if os.path.exists(system.bin+"/sashay") and os.path.exists(system.conf_dir+"/sashay"):
                clear()
                logo.updated()
                cmd = _inp

              else:
                clear()
                logo.update_error()
                cmd = _inp

            else:
              clear()
              logo.update_error()
              cmd = _inp
        else:
          clear()
          logo.nonet()
          tmp = _inp

      elif cmd=="0" or cmd=="back":
        self.menu()
        break
      else:
        echo(f"Invalid input !!", fg="vred")
        time.sleep(1)
      if cmd == "0" or cmd =="back":
          self.menu()
          break
      else:
          echo(f"")

  def about(self):
    while True:
      tool=tools()
      total=len(tool.names)
      clear()
      logo.about(total)

      session = Prompt(bottom_toolbar=Text(' <b>About <red>Sashay</red></b>'), placeholder=Text('<gray>(please type something)</gray>'))
      cmd = session.prompt("$» ")
      self.menu()
      break

  @classmethod
  def menu(self):
    while True:
      from quo.completion import Completer, Completion
      tool=tools()
      total=len(tool.names)
      clear()
      logo.menu(total)

      suggestions = [
              "1",
              "2",
              "3",
              "4",
              "x"
              ]
      suggestions_family = {
              "1" : "All tools",
              "2" : "Categories",
              "3" : "Updates",
              "4" : "About us",
              "x" : "Exit"
              }

      family_colors = {
              "All tools": "magenta",
              "Categories": "green",
              "Updates": "red",
              "About us": "yellow",
              "Exit": "aquamarine",
              }
      meta = {
              "1" : Text("A list of <green>all</green> tools"),
              "2" : Text("A list of <purple>categories</purple>"),
              "3" : Text("Check if a new <khaki>version</khaki> of sashay is available"),
              "4" : Text("About sashay"),
              "x" : Text("Exit sashay")
              }
      class SuggestionCompleter(Completer):
          def get_completions(self, document, complete_event):
              word = document.get_word_before_cursor()
              for suggestion in suggestions:
                  if suggestion.startswith(word):
                      if suggestion in suggestions_family:
                          family = suggestions_family[suggestion]
                          family_color = family_colors.get(family, "default")
                          display = Text(
                                  "%s<b>:</b> <red>(<" + family_color + ">%s</" + family_color+ ">)</red>") % (suggestion, family)
                      else:
                          display = suggestion

                      yield Completion(
                              suggestion,
                              start_position=-len(word),
                              display=display,
                              display_meta=meta.get(suggestion)
                              )



      session = Prompt(bottom_toolbar=Text('<b>Main</b>  <style bg="red">menu</style>'), completer=SuggestionCompleter(), placeholder=Text('<style color="#888888">(please type something)</style>'))
      
      cmd = session.prompt("$» ")
      if cmd == "1":
        self.install_tools(self)
        break
      elif cmd == "2":
        self.category(self)
        break
      elif cmd == "3":
        self.update(self)
        break
      elif cmd == "4":
        self.about(self)
        break
      elif cmd=="x" or cmd=="X" or cmd=="exit":
        clear()
        logo.exit()
        break
      elif cmd=="rm -sashay" or cmd=="rm -sshy" or cmd=="uninstall sashay" or cmd=="unistall sshy":
        system=sys()
        if system.sudo:
          os.system(system.sudo+" rm -rf "+system.bin+"/sashay")
          os.system(system.sudo+" rm -rf "+system.bin+"/sshy")
          os.system(system.sudo+" rm -rf "+system.conf_dir+"/sashay")
        else:
          os.system("rm -rf "+system.bin+"/sashay")
          os.system("rm -rf "+system.bin+"/sshy")
          os.system("rm -rf "+system.conf_dir+"/sashay")
        clear()
        logo.exit()
        break
      else:
        print(f"<style fg='black' bg='red'><b>Sorry, '{cmd}' is an invalid input !!</b></style>")
        time.sleep(1)

class tools:
  data=None
  names=None
  category=None
  category_data=None

  session = Prompt(placeholder=Text("<grey>(please type something</grey>"))

  def __init__(self):
    from pathlib import Path
    system=sys()

    data_path = Path(__file__).parent / "assets/data.json"
    cat_path = Path(__file__).parent / "assets/cat.json"

    with open(data_path) as data_file:
        self.data=json.load(data_file)
    self.meta = list(self.data.keys())

    with open(cat_path) as cat_file:
      self.category_data=json.load(cat_file)
    self.names=list(self.data.keys())
    self.category=list(self.category_data.keys())

  def install(self,name):
    session = Prompt(placeholder=Text("<grey>(please type something</grey>"))
    package_name=self.data[name]["package_name"]
    package_manager=self.data[name]["package_manager"]
    url=self.data[name]["url"]
    req=list(self.data[name]["dependency"])
    system=sys()

    if system.connection():
      if len(req)!=0 and req[0]!=None:
        for dep in req:
          if os.path.exists(system.bin+"/"+dep):
            pass
          else:
            if system.sudo != None:
              os.system(system.sudo+" "+system.pac+" install "+dep+" -y")
            else:
              os.system(system.pac+" install "+dep+" -y")

      if package_manager=="package_manager":
        if os.path.exists(system.bin+"/"+package_name):
          clear()
          logo.already_installed(name)
          tmp=session.prompt("$» ")
        else:
          if system.sudo != None:
            os.system(system.sudo+" "+system.pac+" install "+package_name+" -y")
          else:
            os.system(system.pac+" install "+package_name+" -y")
          # check tool is installed or not
          if os.path.exists(system.bin+"/"+package_name):
            clear()
            logo.installed(name)
            tmp=session.prompt("$» ")
          else:
            clear()
            logo.not_installed(name)
            tmp=session.prompt("$» ")

      elif package_manager=="git":
        if os.path.exists(system.home+"/"+package_name):
          clear()
          logo.already_installed(name)
          tmp=session.prompt("$» ")
        else:
          if system.sudo != None:
            os.system(system.sudo+" git clone "+url+" "+system.home+"/"+package_name)
          else:
            os.system("git clone "+url+" "+system.home+"/"+package_name)
          # check tool is installed or not
          if os.path.exists(system.home+"/"+package_name):
            clear()
            logo.installed(name)
            tmp=session.prompt("$» ")
          else:
            clear()
            logo.not_installed(name)
            tmp=session.prompt("$» ")

      elif package_manager=="wget":
        if os.path.exists(system.home+"/"+package_name):
          clear()
          logo.already_installed(name)
          tmp=session.prompt("$» ")
        else:
          if system.sudo != None:
            os.system(system.sudo+" wget "+url+" -o "+system.home+"/"+package_name)
          else:
            os.system("wget "+url+" -o "+system.home+"/"+package_name)
          # check tool is installed or not
          if os.path.exists(system.home+"/"+package_name):
            clear()
            logo.installed(name)
            tmp=session.prompt("$» ")
          else:
            clear()
            logo.not_installed(name)
            tmp=session.prompt("$» ")

      elif package_manager=="curl":
        if os.path.exists(system.home+"/"+package_name):
          clear()
          logo.already_installed(name)
          tmp=session.prompt("$» ")
        else:
          if system.sudo != None:
            os.system(system.sudo+" curl "+url+" -o "+system.home+"/"+package_name)
          else:
            os.system("curl "+url+" -o "+system.home+"/"+package_name)
          # check tool is installed or not
          if os.path.exists(system.home+"/"+package_name):
            clear()
            logo.installed(name)
            tmp=session.prompt("$» ")
          else:
            clear()
            logo.not_installed(name)
            tmp=session.prompt("$» ")
    if package_manager == "apt":
        import apt
        cache = apt.Cache()
        if cache[package_name].is_installed:
            clear()
            logo.already_installed(name)
            tmp=session.prompt("$» ")
        else:
            os.system("sudo apt install " + package_name)

       # if os.path.exists(system.home+"/"+package_name):
           # clear()
         #   logo.already_installed(name)
      #      tmp=session.prompt("$» ")
     #   else:
       #     if system.sudo != None:
         #       print("dddd")
            #    os.system(system.sudo+" apt " + package_name)
    else:
      clear()
      logo.nonet()
      tmp=session.prompt("$» ")
