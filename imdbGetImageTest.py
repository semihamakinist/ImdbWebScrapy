# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 15:08:21 2019

@author: semiha
"""

import tool_unit as tls
import os

if __name__ == "__main__":
    
    
    mainFolder = os.getcwd()
    testFolder = os.path.join(mainFolder, "test")
    
    main_url = "https://www.imdb.com"
    url = "https://www.imdb.com/name/nm5634768/mediaindex?ref_=nm_phs_md_sm"
    
    sp_main = tls.getRequest(url)
    personFolderPath = sp_main.find("div", {"class":"parent"}).find("a").text.lower().replace(" ", "_")
    (_, nextPageUrl) = tls.nexPage(tagName="div", tagInfoName="id", tagInfo="right", sp=sp_main)
    
#    print()
    
    tls.createFolder(os.path.join(testFolder, personFolderPath))
    
    imgLinks = sp_main.find("div", {"id":"media_index_thumbnail_grid"}).find_all("a")
    
    for imgLink in imgLinks:
        imgName = imgLink.get("href").split("?")[0].split("/")[-1]
        
        subUrl = "{}{}".format(main_url, imgLink.get("href"))
        print(subUrl)
        sp_image = tls.getRequest(subUrl)      
        print(sp_image)
        break
    