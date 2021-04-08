#This file is part of Sashay and may be subject to redistribution and commercial restrictions. Please visit our website
#for more information on licensing and terms of use.
#
#
__version__ = "2021.01.dev1"

import os
import sys
import subprocess
try:
  import requests
except:
  subprocess.call(['pip install requests'])
  subprocess.call(['pip3 install requests'])
try:
  import quo
except:
  subprocess.call(['pip install quo'])
  subprocess.call(['pip3 install quo']) 
class sys:
  pac=None
  sys=None
  home=os.getenv("HOME")
  bin=None
  sudo=None
  conf_dir=None
  def __init__(self):

    # root access 
    if os.path.exists("/usr/lib/sudo"):
      self.sudo="sudo"
    elif os.path.exists("/lib/sudo"):
      self.sudo="sudo"
    elif os.path.exists("/usr/bin/sudo"):
      self.sudo="sudo"
    elif os.path.exists("/bin/sudo"):
      self.sudo="sudo"
    elif os.path.exists("/usr/sbin/sudo"):
      self.sudo="sudo"
    elif os.path.exists("/sbin/sudo"):
      self.sudo="sudo"

    # configuration directories
    if os.path.exists("/usr/etc"):
      self.conf_dir="/usr/etc"
    elif os.path.exists("/data/data/com.termux/files/usr/etc"):
      self.conf_dir="/data/data/com.termux/files/usr/etc"
    elif os.path.exists("/etc"):
      self.conf_dir="/etc"

    # dir, system bin, and system pkg manager
    if os.path.exists("/usr/bin/yum"):
      self.sys="linux"
      self.bin="/usr/bin"
      self.pac="yum"
    elif os.path.exists("/bin/yum"):
      self.sys="linux"
      self.bin="/bin"
      self.pac="yum"
    elif os.path.exists("/usr/sbin/yum"):
      self.sys="linux"
      self.bin="/usr/sbin"
      self.pac="yum"
    elif os.path.exists("/sbin/yum"):
      self.sys="linux"
      self.bin="/sbin"
      self.pac="yum"
    elif os.path.exists("/usr/bin/apt"):
      self.sys="linux"
      self.bin="/usr/bin"
      self.pac="apt-get"
    elif os.path.exists("/bin/apt"):
      self.sys="linux"
      self.bin="/bin"
      self.pac="apt-get"
    elif os.path.exists("/usr/sbin/apt"):
      self.sys="linux"
      self.bin="/usr/sbin"
      self.pac="apt-get"
    elif os.path.exists("/sbin/apt"):
      self.sys="linux"
      self.bin="/sbin"
      self.pac="apt-get"
    elif os.path.exists("/data/data/com.termux/files/usr/bin/pkg"):
      self.sys="linux"
      self.bin="/data/data/com.termux/files/usr/bin"
      self.pac="pkg"
    elif os.path.exists("/usr/local/bin/brew"):
      self.sys="linux"
      self.bin="/usr/local/bin"
      self.pac="brew"
      self.sudo=None
    elif os.path.exists("/usr/bin/apk"):
      self.sys="linux"
      self.bin="/usr/bin"
      self.pac="apk"
    elif os.path.exists("/bin/apk"):
      self.sys="linux"
      self.bin="/bin"
      self.pac="apk"
    elif os.path.exists("/usr/sbin/apk"):
      self.sys="linux"
      self.bin="/usr/sbin"
      self.pac="apk"
    elif os.path.exists("/sbin/apk"):
      self.sys="linux"
      self.bin="/sbin"
      self.pac="apk"

  def connection(self):
    try:
      if requests.get("https://www.github.com").ok:
        return True
    except:
      return False
