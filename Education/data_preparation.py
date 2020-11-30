# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 13:46:57 2020

@author: PJ
"""


import os #to get paths of excel
import pandas as pd
import matplotlib.pyplot as plt

# function to get all file paths from provided directory
def get_list_of_files(dir_path):
    # create a list of file and sub directories 
    # names in the given directory 
    files = os.listdir(dir_path)
    all_files = list()
    # Iterate over all the entries
    for file in files:
        # Create full path
        fullPath = os.path.join(dir_path, file)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            all_files = all_files + get_list_of_files(fullPath)
        else:
            all_files.append(fullPath)
                
    return all_files


def get_folder_name_list(dir_path):
   base_path_folder_list=[]
   for entry in os.listdir(dir_path):
       if os.path.isdir(os.path.join(dir_path, entry)):
           base_path_folder_list.append(entry) 
   return base_path_folder_list

base_path = os.path.dirname(os.path.abspath(__file__))

folders = get_folder_name_list(base_path)
print('folder name: '+ str(folders))


## impact_on_post_secondary_education_plan_total_count
## weeks : 13 to 18

xl_file_paths = get_list_of_files(base_path + '\\education_pse')
print('file paths: '+ str(xl_file_paths))

edu_df = pd.DataFrame()

no_of_weeks = len(xl_file_paths)
col_names = ['idx', 'Total*',
       'Plans to take classes this fall have not changed',
       'All plans to take classes this fall have been canceled',
       'Classes will be in different formats in the fall',
       'Fewer classes will be taken this fall',
       'More classes will be taken this fall',
       'Classes will be taken from a different institution',
       'Classes will be taken for a different kind of certificate or degree',
       'Did not report']
idx = 18 - no_of_weeks + 1
print(no_of_weeks)
for file_path in xl_file_paths :
    # open file
    
    week = file_path.split('\\')
    
    week_number = week[7].split('.')[0].split('_')[1].replace('week','')
    
    df_temp = pd.read_excel(file_path, sheet_name='NC',index_col=0,names=col_names,usecols="A:J", )
    
    df_temp['week'] = int(week_number)
    row_for_total_count = df_temp.loc[['Total']] #total
    #print(row_for_total_count)
    #append first row 'total' to final dataframe
    edu_df = edu_df.append(row_for_total_count,ignore_index=True)
    
edu_df = edu_df.sort_values(by=['week'],ascending=True)
print(edu_df)
# create a CSV file 
edu_df.to_csv(base_path+'\\impact_on_post_secondary_education_plan.csv')



## education received medium
## weeks : 1 to 18

xl_file_paths = get_list_of_files(base_path + '\\edu_rec_medium')
print('file paths: '+ str(xl_file_paths))

edu_df = pd.DataFrame()

no_of_weeks = len(xl_file_paths)

col_names = ['idx','total','Using online resources','Using paper materials sent home','Where classes were cancelled','Where classes changed in another way','Where no change to classes becauseschools did not close','Did not report']

#idx = 18 - no_of_weeks + 1
print(no_of_weeks)
for file_path in xl_file_paths :
    # open file
    #print(file_path)
    week = file_path.split('\\')
    week_number = week[7].split('.')[0].split('_')[1].replace('week','')
    
    df_temp = pd.read_excel(file_path, sheet_name='NC',index_col=0,names=col_names,usecols="A:H", )
    #df_temp = pd.read_excel(file_path, sheet_name='NC')
    df_temp['week'] = int(week_number)
    
    row_for_total_count = df_temp.loc[['Total']] #total
    #append first row 'total' to final dataframe
    edu_df = edu_df.append(row_for_total_count,ignore_index=True)
    
    
edu_df = edu_df.sort_values(by=['week'],ascending=True)
print(edu_df)

# create a CSV file 
edu_df.to_csv(base_path+'\\impact_on_education_received_medium.csv')



## Computer and Internet Availability in Households with Children in Public or Private School
## weeks : 1 to 18

xl_file_paths = get_list_of_files(base_path + '\\edu_computer_and_internet_availability')

print('file paths: '+ str(xl_file_paths))

edu_df = pd.DataFrame()

no_of_weeks = len(xl_file_paths)

col_names =['idx','total','Device always available for educational purposes','Device usually available for educational purposes','Device sometimes available for educational purposes','Device rarely available for educational purposes','Device never available for educational purposes','Did not report','Internet always available for educational purposes','Internet usually available for educational purposes','Internet sometimes available for educational purposes','Internet rarely available for educational purposes','Internet never available for educational purposes','Did not report']
#idx = 18 - no_of_weeks + 1
print(no_of_weeks)
for file_path in xl_file_paths :
    # open file
    #print(file_path)
    week = file_path.split('\\')
    week_number = week[7].split('.')[0].split('_')[1].replace('week','')
    
    df_temp = pd.read_excel(file_path, sheet_name='NC',index_col=0,names=col_names,usecols="A:N", )
    
    #df_temp = pd.read_excel(file_path, sheet_name='NC')
    df_temp['week'] = int(week_number)
    
    row_for_total_count = df_temp.loc[['Total']] #total
    #append first row 'total' to final dataframe
    edu_df = edu_df.append(row_for_total_count,ignore_index=True)
    
    
edu_df = edu_df.sort_values(by=['week'],ascending=True)
print(edu_df)

# create a CSV file 
edu_df.to_csv(base_path+'\\computer_and_internet_availability.csv')







    

    
    
    
    