# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 16:38:29 2019

@author: semiha
"""

import tool_unit as tls
import time as tm
import os



if __name__ == "__main__":
    
    start_number = 5101
    main_folder = os.getcwd()
    main_url = "https://www.imdb.com"
    filePath = os.path.join(main_folder, "startUrl.txt") 
    
    url = tls.readFile(filePath)
    
#    url = "https://www.imdb.com/search/name?gender=male,female&ref_=nv_cel_m&start={}".format(start_number)        
    (sp_main, nextPageUrl) = tls.nexPage(tagName="div", tagInfoName="class", tagInfo="desc", url=url)
    
    while nextPageUrl != None and start_number <5001:
        
        celib_lists = tls.celibrity_list(sp_main)
        
        for celib in celib_lists:
#            person_url = "{}{}".format(main_url, celib)
            sp_person = tls.getRequest("{}{}".format(main_url, celib))
            
#            set data
            name = sp_person.find("h1", {"class":"header"}).find("span").text.lower().replace(" ","_")   
            try:
                foldefName = sp_person.find("div", {"class", "infobar"}).find("span").text.lower().replace("\n","")
            except:
                print("no_gender: {}{}".format(main_url, celib))
                foldefName = "no_gender"
#                tls.writeFile(filePath, url)
#                break
            try:
                imgUrl = sp_person.find("div", {"class", "image"}).find("img").get("src")
            except Exception as e:
                print("no_image: {}{}".format(main_url, celib))
                continue
            
#            set path
            folderPath = os.path.join(main_folder, "train", foldefName)                        
            saveImagePath = os.path.join(folderPath, name+".jpg")
            
#            save image
            tls.createFolder(folderPath)
            if not os.path.exists(saveImagePath):
                tls.saveImage(imgUrl, saveImagePath)
#            if not os.path.exists(os.path.join(main_folder, "{}_clear".format(foldefName), name+".jpg")):
#                tls.saveImage(imgUrl, saveImagePath)
#            else:
#                tls.createFolder(os.path.join(main_folder, "{}_dont_save".format(foldefName)))
#                tls.saveImage(imgUrl, os.path.join(main_folder, "{}_dont_save".format(foldefName), name+".jpg"))
#        break
        start_number += len(celib_lists)
        
        url = "{}{}".format(main_url, nextPageUrl)
        (sp_main, nextPageUrl) = tls.nexPage(tagName="div",
                                             tagInfoName="class", 
                                             tagInfo="desc",
                                             url=url) #nexPage(url)
        
       
        print(url)
        tls.writeFile(filePath, url)
        
        tm.sleep(30)

