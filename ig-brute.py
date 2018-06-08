import mechanize
import cookielib,re,urllib2,urllib,threading
import platform,os




br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(False)
br.set_handle_gzip(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_handle_redirect(True)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Iceweasel/31.5.0')]



def keluar():
    os.sys.exit()



def login():
    username = raw_input("[?] Username : ")
    password = raw_input("[?] Password : ")
    print "[*] Sedang Login ..."
    br.open('https://www.instagram.com/accounts/login/?force_classic_login')
    br.select_form(nr=0)
    br.form[ 'username' ] = username
    br.form[ 'password' ] = password
    br.submit()
    log = br.geturl()
    if log == "https://www.instagram.com/":
        print "[+] Berhasil Login ..."
        print ""
        dapat()
    else:
        print "[-] Gagal Login ..."
        print ""
        login(   )


def dapat_():
    f = open ('hasil.txt','w')
    f.write("Username " + username + ">>> " + "Password " + password)
    f.close
    keluar()


def menu():
    print ""
    print " _   __  ___   _   _ _____ _____ _____"
    print "| | / / / _ \ | \ | /  __ \  _  |_   _|"
    print "| |/ / / /_\ \|  \| | /  \/ | | | | |"
    print "|    \ |  _  || . ` | |   | | | | | |"
    print "| |\  \| | | || |\  | \__/\ \_/ / | |"
    print "\_| \_/\_| |_/\_| \_/\____/\___/  \_/"
    print  ""
    print "========================================"
    print "=       www.github.com/kancotdiq       ="
    print "=            LINE : lazz110            ="
    print "========================================"
    print "[1] Mulai"
    print "[2] Keluar"
    print ""
    pmN = input("Pilih [1/2] : ")
    if pmN == 1:
        print ""
        login()
    else:
        print "[!] Keluar"
        keluar()




menu()
