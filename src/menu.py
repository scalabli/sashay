import os
import json
from time import sleep
from .outlook import *
from .system import *
from quo import echo, clear
from quo.color import *

red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
blue="\033[1;34m"
violate="\033[1;37m"
nc="\033[00m"

class main:
  def install_tools(self):
    while True:
      tool=tools()
      num=1
      total=len(tool.names)
      clear()
      logo.install_tools()
      print(f"\007")
      for tool_name in tool.names:
        print (f" {green}[ {violate}{num} {green}] {yellow}Install {green}{tool_name}")
        num+=1
      print(f"")
      logo.back()
      echo(f"sshy", fg="green", nl=False, italic=True)
      echo(f"@", fg="red", nl=False, italic=True)
      echo(f"home", fg="blue", nl=False, italic=True)
      echo(f"$", fg="yellow", nl=False, italic=True)
      cmd=input(f" ")
      if cmd=="00" or cmd=="back":
        self.menu()
        break
      else:
        try:
          if int(cmd)>=1 and int(cmd)<=int(total):
            clear()
            logo.installing()
            echo(f"Installing", fg=gold, nl=False)
            sleep(1)
            echo(f".", fg="red", nl=False)
            sleep(1)
            echo(f".", fg=aquamarine, nl=False)
            sleep(1)
            echo(f".", fg=lime, nl=False)
            sleep(1)
            echo(f".", fg=salmon, nl=False)
            sleep(1)
            echo(f".", fg="cyan")
        
            tool.install(tool.names[int(cmd)-1])
          else:
            print(f"\007{red}Sorry,{violate} '{cmd}' {blue}: {red}invalid input !!")
            sleep(1)
        except ValueError:
          print(f"\007{red}Sorry,{violate} '{cmd}' {blue}: {red}invalid input !!")
          sleep(1)

  def category(self):
    while True:
      tool=tools()
      total=len(tool.category)
      num=1
      clear()
      logo.tool_header()
      print(f"")
      for cat in tool.category:
        print (f"  {green}[ {violate}{num} {green}] {yellow}{tool.category_data[cat]}")
        num+=1
      print(f"")
      logo.back()
      echo(f"sshy", fg="green", nl=False, italic=True)
      echo(f"@", fg="red", nl=False, italic=True)
      echo(f"categories", fg="blue", nl=False, italic=True)
      echo(f"$", fg="yellow", nl=False, italic=True)
      cmd=input(f" ")
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
              print(f"")
              tmp_cat_tool=[]
              for i in tool.names:
                if tool.category[int(cmd)-1] in tool.data[i]["category"]:
                  tmp_cat_tool.append(tool.data[i]['name'])
                  print(f" {green}[ {violate}{cnt} {green}] {yellow}Install {green}{tool.data[i]['name']}")
                  cnt+=1
              print(f"")
              logo.back()
              tcmd=input(f"{blue}sshy@{blue}space {yellow}$ ")
              if tcmd=="00" or tcmd=="back":
                break
              else:
                try:
                  cat_total=len(tmp_cat_tool)
                  if int(tcmd) in range(1,int(cat_total)+1):
                    clear()
                    logo.installing()
                    print(f"{green}Installing ....")
                    tool.install(tmp_cat_tool[int(tcmd)-1])
                  else:
                    print(f"\007{red}Sorry,{violate} '{tcmd}' {blue}: {red}invalid input !!")
                    sleep(1)
                except ValueError:
                  print(f"\007{red}Sorry,{violate} '{tcmd}' {blue}: {red}invalid input !!")
                  sleep(1)
          else:
            print(f"\007{red}Sorry,{violate} '{cmd}' {blue}: {red}invalid input !!")
            sleep(1)
        except ValueError:
          print(f"\007{red}Sorry,{violate} '{cmd}' {blue}: {red}invalid input !!")
          sleep(1)

  def update(self):
    while True:
      clear()
      logo.update()
      cmd=input(f"{blue}sshy@{blue}space {yellow}$ ")
      if cmd=="1":
        system=sys()
        if system.connection():
          clear()
          logo.updating()
          if system.sudo != None:
            if os.path.exists(system.home+"/sashay"):
              pass
            else:
              os.system(system.sudo+" git clone https://github.com/rajkumardusad/sashay.git "+system.home+"/sashay")
            if os.path.exists(system.home+"/sashay/install.aex"):
              os.system("cd "+system.home+"/sashay && "+system.sudo+" sh install.aex")
              if os.path.exists(system.bin+"/sashay") and os.path.exists(system.conf_dir+"/sashay"):
                clear()
                logo.updated()
                cmd=input(f"{blue}sshy@{blue}space {yellow}$ ")
              else:
                clear()
                logo.update_error()
                cmd=input(f"{blue}sshy@{blue}space {yellow}$ ")
            else:
              clear()
              logo.update_error()
              cmd=input(f"{blue}sshy@{blue}space {yellow}$ ")
          else:
            if os.path.exists(system.home+"/Tool-X"):
              pass
            else:
              os.system("git clone https://github.com/rajkumardusad/sashay.git "+system.home+"/sashay")
            if os.path.exists(system.home+"/sashay/install.aex"):
              os.system("cd "+system.home+"/sashay && sh install.aex")
              if os.path.exists(system.bin+"/sashay") and os.path.exists(system.conf_dir+"/sashay"):
                clear()
                logo.updated()
                cmd=input(f"{blue}sshy@{blue}space {yellow}$ ")
              else:
                clear()
                logo.update_error()
                cmd=input(f"{blue}sshy@{blue}space {yellow}$ ")
            else:
              clear()
              logo.update_error()
              cmd=input(f"{blue}sshy@{blue}space {yellow}$ ")
        else:
          clear()
          logo.nonet()
          tmp=input(f"{blue}sshy@{blue}space {yellow}$ ")
      elif cmd=="0" or cmd=="back":
        self.menu()
        break
      else:
        print(f"\007{red}Sorry,{violate} '{cmd}' {blue}: {red}invalid input !!")
        sleep(1)

  def about(self):
    while True:
      tool=tools()
      total=len(tool.names)
      clear()
      logo.about(total)
      cmd=input(f"{blue}sshy@{blue}space {yellow}$ ")
      self.menu()
      break

  @classmethod
  def menu(self):
    while True:
      tool=tools()
      total=len(tool.names)
      clear()
      logo.menu(total)
      cmd=input(f"{blue}sshy@{blue}space {yellow}$ ")
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
      elif cmd=="rm -sshy" or cmd=="rm -sashay" or cmd=="uninstall sashay" or cmd=="uninstall sshy":
        system=sys()
        if system.sudo:
          os.system(system.sudo+" rm -rf "+system.bin+"/sashay")
          os.system(system.sudo+" rm -rf "+system.bin+"/toolx")
          os.system(system.sudo+" rm -rf "+system.conf_dir+"/sashay")
        else:
          os.system("rm -rf "+system.bin+"/sashay")
          os.system("rm -rf "+system.bin+"/toolx")
          os.system("rm -rf "+system.conf_dir+"/sashay")
        clear()
        logo.exit()
        break
      else:
        print(f"\007{red}Sorry,{violate} '{cmd}' {blue}: {red}invalid input !!")
        sleep(1)

class tools:
  data=None
  names=None
  category=None
  category_data=None
  def __init__(self):
    system=sys()
    with open(system.conf_dir+"/sashay/assets/data.json") as data_file:
      self.data=json.load(data_file)
    with open(system.conf_dir+"/sashay/assets/cat.json") as cat_file:
      self.category_data=json.load(cat_file)
    self.names=list(self.data.keys())
    self.category=list(self.category_data.keys())

  def install(self,name):
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
          tmp=input(f"{blue}sshy@{blue}space {yellow}$ ")
        else:
          if system.sudo != None:
            os.system(system.sudo+" "+system.pac+" install "+package_name+" -y")
          else:
            os.system(system.pac+" install "+package_name+" -y")
          # check tool is installed or not
          if os.path.exists(system.bin+"/"+package_name):
            clear()
            logo.installed(name)
            tmp=input(f"{blue}sshy@{blue}space {yellow}$ ")
          else:
            clear()
            logo.not_installed(name)
            tmp=input(f"{blue}sshy@{blue}space {yellow}$ ")

      elif package_manager=="git":
        if os.path.exists(system.home+"/"+package_name):
          clear()
          logo.already_installed(name)
          tmp=input(f"{blue}sshy@{blue}space {yellow}$ ")
        else:
          if system.sudo != None:
            os.system(system.sudo+" git clone "+url+" "+system.home+"/"+package_name)
          else:
            os.system("git clone "+url+" "+system.home+"/"+package_name)
          # check tool is installed or not
          if os.path.exists(system.home+"/"+package_name):
            clear()
            logo.installed(name)
            tmp=input(f"{blue}sshy@{blue}space {yellow}$ ")
          else:
            clear()
            logo.not_installed(name)
            tmp=input(f"{blue}sshy@{blue}space {yellow}$ ")

      elif package_manager=="wget":
        if os.path.exists(system.home+"/"+package_name):
          clear()
          logo.already_installed(name)
          tmp=input(f"{blue}sshy@{blue}space {yellow}$ ")
        else:
          if system.sudo != None:
            os.system(system.sudo+" wget "+url+" -o "+system.home+"/"+package_name)
          else:
            os.system("wget "+url+" -o "+system.home+"/"+package_name)
          # check tool is installed or not
          if os.path.exists(system.home+"/"+package_name):
            clear()
            logo.installed(name)
            tmp=input(f"{blue}sshy@{blue}space {yellow}$ ")
          else:
            clear()
            logo.not_installed(name)
            tmp=input(f"{blue}sshy@{blue}space {yellow}$ ")

      elif package_manager=="curl":
        if os.path.exists(system.home+"/"+package_name):
          clear()
          logo.already_installed(name)
          tmp=input(f"{blue}sshy@{blue}space {yellow}$ ")
        else:
          if system.sudo != None:
            os.system(system.sudo+" curl "+url+" -o "+system.home+"/"+package_name)
          else:
            os.system("curl "+url+" -o "+system.home+"/"+package_name)
          # check tool is installed or not
          if os.path.exists(system.home+"/"+package_name):
            clear()
            logo.installed(name)
            tmp=input(f"{blue}sshy@{blue}space {yellow}$ ")
          else:
            clear()
            logo.not_installed(name)
            tmp=input(f"{blue}sshy@{blue}space {yellow}$ ")
    else:
      clear()
      logo.nonet()
      tmp=input(f"{blue}sshy@{blue}space {yellow}$ ")
