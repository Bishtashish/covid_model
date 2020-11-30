# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 14:25:11 2020

@author: PJ
"""

#https://www.researchgate.net/search.Search.html?type=project&query=hadoop
#pip install request
#pip install bs4
#pip install lxml


from bs4 import BeautifulSoup
import requests


# downloading files for impact_on_post_secondary_education_plan
files_to_download = []        
for i in range(18):
    url = 'https://www.census.gov/data/tables/2020/demo/hhp/hhp'+str(i+1)+'.html'
    #print(url)
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text,'lxml')
    anchors = soup.find_all('a', {'class': 'uscb-layout-align-start-start', 'href': True})
    for anchor in anchors:
        if(anchor['href'].find('educ6_')>-1 and anchor['href'].find('educ6_se')==-1):
            files_to_download.append(anchor['href'])


print(files_to_download)


base_path = 'D:\\uncc\\curriculum\\fall20\\knowledge_discoveries_in_databases\\project\\education_pse\\'

for file_path in files_to_download:
    dls = 'http:'+file_path
    file_name = file_path.split('/')
    output_file_path = base_path + file_name[9]
    resp = requests.get(dls)
    output = open(output_file_path, 'wb')
    output.write(resp.content)
    output.close()
       
 
# downloading files for education medium 
files_to_download = []        
for i in range(18):
    url = 'https://www.census.gov/data/tables/2020/demo/hhp/hhp'+str(i+1)+'.html'
    #print(url)
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text,'lxml')
    anchors = soup.find_all('a', {'class': 'uscb-layout-align-start-start', 'href': True})
    for anchor in anchors:
        if(anchor['href'].find('educ2_')>-1 and anchor['href'].find('educ2_se')==-1):
            files_to_download.append(anchor['href'])


print(files_to_download)



#html_text = requests.get(files_to_download[0]).text


base_path = 'D:\\uncc\\curriculum\\fall20\\knowledge_discoveries_in_databases\\project\\edu_rec_medium\\'
    

for file_path in files_to_download:
    dls = 'http:'+file_path
    
    file_name = file_path.split('/')
    output_file_path = base_path + file_name[9]
    
    resp = requests.get(dls)
    output = open(output_file_path, 'wb')
    output.write(resp.content)
    output.close()
    


# downloading files for education medium 
files_to_download = []        
for i in range(18):
    url = 'https://www.census.gov/data/tables/2020/demo/hhp/hhp'+str(i+1)+'.html'
    #print(url)
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text,'lxml')
    anchors = soup.find_all('a', {'class': 'uscb-layout-align-start-start', 'href': True})
    for anchor in anchors:
        if(anchor['href'].find('educ3_')>-1 and anchor['href'].find('educ3_se')==-1):
            files_to_download.append(anchor['href'])


print(files_to_download)



#html_text = requests.get(files_to_download[0]).text


base_path = 'D:\\uncc\\curriculum\\fall20\\knowledge_discoveries_in_databases\\project\\edu_computer_and_internet_availability\\'
    

for file_path in files_to_download:
    file_name = file_path.split('/')
    output_file_path = base_path + file_name[9]
    
    dls = 'http:'+file_path
    resp = requests.get(dls)
    output = open(output_file_path, 'wb')
    output.write(resp.content)
    output.close()
    

    

