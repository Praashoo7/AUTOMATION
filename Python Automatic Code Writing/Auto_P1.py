from Google import Create_Service
import pandas as pd
import re
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import json




########################################_CONNECTION_TO_DRIVE_########################################

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'V3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service =  Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    
folder_id = ''
query = f"parents = '{folder_id}'"

response = service.files().list(q=query).execute()
files=response.get('files')
nextPageToken = response.get('nextPageToken')

while nextPageToken:
    response = service.files().list(q=query).execute()
    files.extend(respnse.get('files'))
    nextpageToken = response.get('nextPageToken')
    
pd.set_option('display.max_columns',100)
pd.set_option('display.max_rows',500)
pd.set_option('display.min_rows',500)
pd.set_option('display.max_colwidth',150)
pd.set_option('display.width',200)
pd.set_option('expand_frame_repr', True)



########################################_AQUIRING_KEYS_AND_NAMES_OF_FILES_FROM_THE_DRIVE_########################################

df = pd.DataFrame(files)
name_list = df.name.values.tolist()
id_list = df.id.values.tolist()


data={}
imgs_data={}

#loading_the_original_list_of_files
OG_imgs_data = json.load(open("OG_imgs_data.txt"))

#aquiring_list_of_all_files_from_the_drive
for i in range(len(id_list)):
    data[id_list[i]]=name_list[i]

total=len(OG_imgs_data)
print(total)

#aquiring_new_files_by_substracting_new_files_from_old_files
imgs_data=dict(data.items() - OG_imgs_data.items())

#writing_list_of_new_files_to_the_original_file_to_use_in_upcoming_operations
json.dump(data, open("OG_imgs_data.txt",'w'))


########################################_DOWNLOADING_THE_IMGS_INFO_FILE_FROM_THE_DRIVE_########################################

gauth = GoogleAuth()

# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)

folder = ''

# Download files
file_list = drive.ListFile({'q' : f"'{folder}' in parents and trashed=false"}).GetList()
for index, file in enumerate(file_list):
    if file['title']=="file_data.txt":
        print(index+1, 'file downloaded : ', file['title'])
        file.GetContentFile(file['title'])



########################################_AQUIRING_NAMES_AND_INFO_OF_FILES_FROM_THE_CLIENT_TEXT_FILE_########################################

values=[]
file_values=[]
key=[]
file_key=[]
file_data={}

for line in open("file_data.txt"):
    li=line.strip()
    if not li.startswith("#"):
        if not li.startswith("$"):
            values.append(line.strip())
        else:
            key.append(line.strip())

for i in key:
    name=i.replace('$','')
    file_key.append(name)

res = []
for ele in values:
    if ele.strip():
        res.append(ele)

for i in range(0, len(res), 2):
    x = i
    file_values.append(res[x:x+2])
    
print(file_key)
print(file_values)

for i in range(len(file_key)):
    file_data[file_key[i]]=file_values[i]

print("file_data : ",file_data)   

for i in imgs_data:
    for j in file_data:
        if imgs_data[i]==j:
            file_data[j].append(i)
            
print("file_data : ",file_data) 



########################################_COMPARING_NEW_FILES_TO_PAIR_IT_WITH_CORRECT_INFO_########################################

main_data={}

for i in imgs_data:
    for j in file_data:
        if imgs_data[i]==j:
            for k in range(len(imgs_data)):
                main_data[imgs_data[i]]=file_data[j]

print("main_data : ",main_data)


########################################_REPLACING_TEXT_IN_TEMPLATE_CODE_########################################

search_text1 = "card_number"
search_text2 = "link_here"
search_text3 = "game_here"
search_text4 = "location_here"
search_text5 = "info_label"
search_text6 = "download_number"

counter=0

for k in main_data:
    replace_text1 = str(total+counter)
    replace_text2 = main_data[k][2]
    replace_text3 = main_data[k][0]
    replace_text4 = main_data[k][1]
    replace_text5 = "chck"+str(total+counter)
    replace_text6 = "PhotographyHood(Gaming-Moments)-"+str(total+counter)
    
    print(total)
    counter=counter+1


    with open(r'imgs_template.txt', 'r') as file:
      
        data = file.read()
        data = data.replace(search_text1, replace_text1).replace(search_text2, replace_text2).replace(search_text3, replace_text3).replace(search_text4, replace_text4).replace(search_text5, replace_text5).replace(search_text6, replace_text6)
      

    with open(r'imgs_code.txt', 'w') as file:

        file.truncate(0)
        file.write(data)
        
    print("Text replaced")


########################################_ADDING_CODE_TO_THE_MAIN_FILE_########################################
    
    with open('imgs_code.txt', 'r') as f:
        # Read the contents of the file into a list of strings
        lines1 = f.readlines()

    str1=""
    for ele in lines1:
        str1+= ele


    with open('p_try - Copy (3).html', 'r', errors="ignore") as f:
        html = f.read()

    old_text="<!--AUTO_CODE_HERE-->"
    new_text=str1

    html = re.sub(old_text, new_text, html)

    with open('p_try - Copy (3).html', 'w') as f:
        f.write(html)

    print("Code Added")
