#This file is part of Sashay and may be subject to redistribution and commercial restrictions. Please visit our website
#for more information on licensing and terms of use.
#
#
class logo:
  @classmethod
  def tool_header(self):
    print('''\007

\033[1;33m                                                                                                            
                                   888                       
                                   888                      
              .oooo.o    .oooo.o   888888bo.    ooo    ooo
             d88(  "8   d88(  "8  o888888888b   `88.  .8'
             `"Y88b.    `"Y88b.    888    888    `88..8'
             o.  )88b   o.  )88b   888    888     `888'
             8""888P'   8""888P'  o888o  o888o    "888"      d8'
                                              .o...P'  \033[1;91mBy Gerrishon




\033[1;36m ===============================================================\033[1;m
\033[1;33m|                   Install Useful Tools                       |
\033[1;36m ===============================================================\033[00m''')

  @classmethod
  def tool_footer(self):
    print('''\033[1;36m__________________________________________________
=========================================================================\033[00m''')


  @classmethod
  def not_ins(self):
    self.tool_header()
    print ('''
\033[1;31m  [ x ]  \033[1;31mWe can't install Sashay at the moment.\033[1;m
\033[1;31m  [ x ]  \033[1;31mAn error occurred.\033[1;m
\033[1;31m  [ x ]  \033[1;31mPlease try again after some time.\033[1;m''')
    self.tool_footer()

  @classmethod
  def ins_tnc(self):
    self.tool_header()
    print ('''
\033[1;33m  [ ✓ ] \033[1;32mUse It At Your Own Risk.
\033[1;33m  [ ✓ ] \033[1;32mThis tool is provided as is, without warranties or guarantees of any kind.
\033[1;33m  [ ✓ ] \033[1;32mUse it legal purpose only.
\033[1;33m  [ ✓ ] \033[1;32mWe are not responsible for your actions.
\033[1;33m  [ ✓ ] \033[1;32mDo not do things that are forbidden.

\033[1;31m If you are installing this tool.
 that means you are agree with all terms.''')
    self.tool_footer()

  @classmethod
  def ins_sc(self):
    self.tool_header()
    print ('''
\033[1;33m    [ ✓ ] \033[1;32mSashay is installed successfully.
\033[1;33m    [ ✓ ] \033[1;32mType Sashay or sshy to run this tool in your terminal.''')
    self.tool_footer()

  @classmethod
  def update(self):
    self.tool_header()
    print ('''
\033[1;33m  [ 1 ] \033[1;32mUpdate Sashay.
\033[1;33m  [ 0 ] \033[1;32m<< Go Back.\033[00m''')
    self.tool_footer()

  @classmethod
  def updated(self):
    self.tool_header()
    print ('''
\033[1;33m      [ ✓ ] \033[1;32mCongratulations!! Sashay has been updated successfully.
\033[1;33m      [ ✓ ] \033[1;32mPress Enter to continue.\033[00m''')
    self.tool_footer()

  @classmethod
  def nonet(self):
    self.tool_header()
    print ('''
\033[1;31m  [ x ]  \033[1;31mNo network connectivity.\033[1;m
\033[1;31m  [ x ]  \033[1;31mPlease try again after some time.\033[00m''')
    self.tool_footer()

  @classmethod
  def update_error(self):
    self.tool_header()
    print ('''
\033[1;31m  [ x ]  \033[1;31mWe can't Update Sashay.\033[1;m
\033[1;31m  [ x ]  \033[1;31mPlease try again after some time.\033[00m''')
    self.tool_footer()


  @classmethod
  def about(self,total):
    self.tool_header()
    print (f'''
\033[1;33m [✓] Sashay
\033[1;33m [✓] By Gerrishon Sirere(chouette254)
\033[1;3   [✓] "With great power comes great responsibility"
\033[1;33  [✓] Total tools :- \033[1;32mtotal {total} tools.\033[1;m

\033[1;33m [✓] \033[1;32mSashay is automatic tool installer.
\033[1;33m [✓] \033[1;32mMade for linux based systems.
\033[1;31m [✓] This tool is provided as is, without warranties or guarantees of any kind"''')
    self.tool_footer()


  @classmethod
  def install_tools(self):
    print ("""\033[01;33m =============================================
\033[01;32m|_____________ Select your tool ______________|
 \033[01;33m=============================================\033[00m""")

  @classmethod
  def already_installed(self,name):
    self.tool_header()
    print(f'''
\033[1;33m  [ + ] \033[1;32mSorry ??
\033[1;33m  [ + ] \033[1;37m'{name}'\033[01;32m is already Installed !!
''')
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
    print(f'''
\033[1;33m  [ + ] \033[1;31mSorry ??
\033[1;33m  [ + ] \033[1;37m'{name}'\033[01;31m is not Installed !!
''')
    self.tool_footer()

  @classmethod
  def back(self):
    print ("""\033[01;36m =============================================
\033[01;33m|  00) Back                                   |
 \033[01;36m=============================================\033[00m""")

  @classmethod
  def updating(self):
    print ("""\033[01;33m =============================================
\033[01;32m|______________ Updating Sashay ______________|
 \033[01;33m=============================================\033[00m""")

  @classmethod
  def installing(self):
    print ("""\033[01;33m =============================================
\033[01;32m|________________ Installing _________________|
 \033[01;33m=============================================\033[00m""")

  @classmethod
  def menu(self,total):
    self.tool_header()
    print (f'''
\033[1;33m  [ 1 ] \033[1;32mShow all tools.\033[1;33m [ \033[1;91mAlmost {total} tools\033[1;33m ]
\033[1;33m  [ 2 ] \033[1;32mShow all categories.
\033[1;33m  [ 3 ] \033[1;32mUpdate Sashay.
\033[1;33m  [ 4 ] \033[1;32mAbout Us.
\033[1;33m  [ x ] \033[1;32mTo Exit Sashay.''')
    self.tool_footer()

  @classmethod
  def exit(self):
    self.tool_header()
    print ('''
\033[1;33m         [ ✓ ] \033[1;32mHoping to see you back soon. 
\033[1;33m         [ + ] \033[1;32mGood By..... :)\033[00m''')
    self.tool_footer()
