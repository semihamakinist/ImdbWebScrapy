# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 16:40:03 2019

@author: semiha
"""

from bs4 import BeautifulSoup
from urllib import urlretrieve
import requests
import os

# file and folder job
def writeFile(filePath, data):   
    with open(filePath, 'w') as fb:
        fb.write(data)
    fb.close()

def readFile(filePath): 
    data = ""
    with open(filePath, 'r') as fb:
        data = fb.read()
    fb.close()
    
    return data

def createFolder(folderPath):
    if not os.path.exists(folderPath):
        os.makedirs(folderPath) 

def getRequest(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    req.close()
    
    return soup

def saveImage(img_url, save_img):
    urlretrieve(img_url, save_img)


def celibrity_list(sp):
    celib_urls = []
    celib_lists = sp.find_all("h3", {"class": "lister-item-header"})
    
    for h3 in celib_lists:
        celib_urls.append(h3.find("a").get("href"))
    
    return celib_urls    

def nexPage(tagName, tagInfoName, tagInfo, url=1, sp=1):
    if url!=1 and sp==1:
        sp_next = getRequest(url)
    elif url==1 and sp!=1:
        sp_next = sp
#    list_number = sp.find("div", {"class": "desc"}).find("span").text.split(" ")[2]
#    list_number = int("".join([c for c in list_number.split(",")]))
    
    nextPageUrl = [link.get("href") for link in sp_next.find(tagName, {tagInfoName: tagInfo}).find_all("a") if link.text.startswith("Next")]
    return (sp_next, nextPageUrl[0])