#!/usr/bin/python3

import os
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request,urlopen
import random

#import os

# command = "gsettings set org.gnome.desktop.background picture-uri 'file:///home/khalid/Pictures/khalid.jpg'"

#os.system(command)


def main():

    #USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'

    driver = webdriver.PhantomJS(executable_path='/home/khalid/Downloads/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
    
    driver.get("https://www.brainyquote.com/quotes/quote_pictures.html")    
    
    #req = Request("https://www.brainyquote.com/quotes/keywords/daily.html", headers={'User-Agent':'Mozilla/5.0'})
    
    #html = urllib.request.urlopen(req).read()
    
    #bsObj = BeautifulSoup(html)
    
    source = driver.page_source
    
    bsObj = BeautifulSoup(source, "html.parser")
    
    #print(bsObj.find(id="quotesList").find(id='qpos_1_6').find('div').find('a',title='view image').find('img')['src'])
    
    while True:
        rand_num = random.randrange(1,6)
        
        id_string = 'qpos_1_'+str(rand_num)
        
        try:
            URL = bsObj.find(id="quotesList").find(id=id_string).find('div').find('a',title='view image').find('img')['src']
        except AttributeError:
            continue
        
        imgUrl = "https://www.brainyquote.com" + str(URL)
       
        break
        
    print(imgUrl)
    
    headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
   'Accept-Encoding': 'none',
   'Accept-Language': 'en-US,en;q=0.8',
   'Connection': 'keep-alive'}
   
    request = urllib.request.Request(imgUrl,None,headers)
    response = urllib.request.urlopen(request)
    
    f = open('img.jpg','wb')
    f.write(response.read())
    f.close()
    
    ################ OR ###############
    
    command = "wget -O newimg " + imgUrl
    os.system(command)
    
if __name__=="__main__":
    
    main()
    
    #os.system('PID=$(pgrep gnome-session)')
    #os.system('export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)')
    #os.system('cp /home/khalid/Documents/Python\ Web\ Scrapers/img.jpg /home/khalid/Pictures/')
    #os.system('DIR=\"/home/khalid/Pictures/img.jpg\"')
    #os.system('gsettings set org.gnome.desktop.background picture-uri \"file://$DIR\"')
    
    
    
    
