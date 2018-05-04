import urllib2,sys
from os.path import expanduser
import pip
import os,time
import urllib,os
class runinstaller():
    start=time.time() #recording the start time
    folder=None
    #if we don't have the correct folder name keep doing it
    while folder is None:
        try:
            folder=str(input("What folder on the desktop do you want to put these executables in (enter a string in quotes)?").lstrip())
        except:
            print ("enter a string in quotes")
    home=str(expanduser("~")+"\Desktop\\"+folder) #this is a OS library to get the home path
    directory=home
    if not os.path.exists(directory): #make it if we don't have it
        os.makedirs(directory)
    #this is the simplest of libraries to use for getting url's just pass in the url and the location you want to use
    print ("starting download of java")
    urljava="http://javadl.oracle.com/webapps/download/AutoDL?BundleId=233172_512cd62ec5174c3487ac17c61aaa89e8"
    urllib.urlretrieve(urljava,home+"/javatry.exe")
    print ("java is downloaded")
    print ("starting download of ntp")
    urlntp="https://www.meinbergglobal.com/download/ntp/windows/ntp-4.2.8p11-win32-setup.exe"
    urllib.urlretrieve(urlntp,home+"/ntp.exe")
    print ("ntp is downloaded")
    print ("starting download of 7zip")
    url7zip="https://www.7-zip.org/a/7z1805-x64.exe"
    urllib.urlretrieve(url7zip,home+"/7zip.exe")
    print ("7ZIP is downloaded")
    print ("starting download of VNC")
    urltightvnc="https://www.tightvnc.com/download/2.8.8/tightvnc-2.8.8-gpl-setup-64bit.msi"
    urllib.urlretrieve(urltightvnc,home+"/tightvnc.exe")
    print ("tightvnc is downloaded")
    print ("starting download of notepad")
    urlnotepad="https://notepad-plus-plus.org/repository/7.x/7.5.6/npp.7.5.6.Installer.x64.exe"
    urllib.urlretrieve(urlnotepad,home+"/notepad.exe")
    print ("notepad is downloaded")
    print ("starting download of ipscanner")
    urlipscanner="https://github.com/angryip/ipscan/releases/download/3.5.2/ipscan-win64-3.5.2.exe"
    urllib.urlretrieve(urlipscanner,home+"/ipscanner.exe")
    print ("ip scanner is downloaded")
    print ("Everything is in your folder now, complete in "+str(time.time()-start)+" seconds")
    #add anything else you want to download in a similar fashion
runinstaller()
