from urllib2 import urlopen
from bs4 import BeautifulSoup
import re
import os
import subprocess
import urllib2

PRINT_YES=True
PRINT_NO =False
cwd=''
fileSet=set()

def getFileName(link):
    lastSlash=-1
    while link.find('/',lastSlash+1)!=-1:
        lastSlash=link.find('/',lastSlash+1)
    fileName = link[lastSlash+1:]
    return fileName

def fileExists(link, shouldIPrint):
    global cwd, fileSet
    if os.getcwd()!=cwd:
        fileList = [f for f in os.listdir('.') if os.path.isfile(f)]
        fileSet = set(fileList)
        cwd=os.getcwd()
    lastSlash=-1
    fileName = getFileName(link)
    if fileName not in fileSet:
        return False
    else:
        if shouldIPrint:
            print '['+fileName+']--'+'File Already Exists'
        return True

def getLinks(url):
    html = urlopen(url)
    bs = BeautifulSoup(html, "lxml")
    links = bs.find("div", {"id": "bodyDivID"}).findAll("a", href=re.compile("(a/)+(AUDI)+"))
    #for link in links:
        #print link['title']
        #print link['href']
    return links

def getMp3s(url):
    print "---------------------------------------------------"
    print url
    print "---------------------------------------------------"
    links = getLinks(url)
    urlDir = url.replace("/","_")
    os.system("mkdir "+urlDir)
    os.chdir(urlDir)
    for link in links:
        mp3Link = "causelessmercy.com/"+link['href']
        if not fileExists(link['href'], PRINT_YES):
            #os.system("wget "+mp3Link)
            fileName = getFileName(link['href'])
            fileInfo = urllib2.urlopen('http://'+mp3Link)
            print '['+fileName+']'+' [DOWNLOADING]'
            with open(fileName, 'wb') as outputFile:
                outputFile.write(fileInfo.read())
    os.chdir("..")

def fileSizesMatching(fileName, fileSizeInternet):
    statinfo = os.stat(fileName)
    #print "localFileSize --", statinfo.st_size
    #print type(statinfo.st_size), type(fileSizeInternet)
    #print statinfo.st_size == fileSizeInternet
    #print "-------------------------------------"
    return statinfo.st_size == fileSizeInternet

def checkSize(url):
    print "---------------------------------------------------"
    print "Checking sizes for :", url
    print "---------------------------------------------------"
    links = getLinks(url)
    urlDir = url.replace("/","_")
    os.chdir(urlDir)
    for link in links:
        mp3Link = "causelessmercy.com/"+link['href']
        fileInfo = urllib2.urlopen('http://'+mp3Link)
        fileSizeInternet = int(fileInfo.headers["Content-Length"])
        #print "fileSizeInternet --", fileSizeInternet
        lastSlash=-1
        fileName = getFileName(link['href'])
        printString = '['+fileName+'] fileSizeInternet='+str(fileSizeInternet)
        if int(fileInfo.getcode())==404:
            printString += ' [404 Not Found]'
            print printString
            continue
        print printString
        if (not fileExists(fileName, PRINT_NO)) or (not fileSizesMatching(fileName, fileSizeInternet)):
            #print "Downloading", fileName
            printString2=''
            try:
                os.remove(fileName)
                print '[DELETING] '+fileName
            except:
                printString2+='[EXCEPT]'
            #os.system("wget "+mp3Link)
            printString2+=' [DOWNLOADING]'
            print printString2
            with open(fileName, 'wb') as outputFile:
                outputFile.write(fileInfo.read())
    os.chdir('..')
    #change names of the directories
    firstPos=urlDir.find('Prabhupadas')+11
    lastPos =urlDir.find('Links')
    os.rename(urlDir, urlDir[firstPos:lastPos])

def main():
    urls=[]
    urls.append("http://causelessmercy.com/?P=_Prabhupadas1976MP3Links")
    urls.append("http://causelessmercy.com/?P=_Prabhupadas1977MP3Links")
    urls.append("http://causelessmercy.com/?P=_PrabhupadasMP3Links")
    urls.append("http://causelessmercy.com/?P=_PrabhupadasMusicMP3Links")
    urls.append("http://causelessmercy.com/?P=_PrabhupadasNonmusicMP3Links")
    
    for url in urls:
        getMp3s(url)
    
    
    #check sizes of downloads
    #Run this just to verify that all your downloads are complete
    for url in urls:
        checkSize(url)
    

if __name__=="__main__":
    main()
