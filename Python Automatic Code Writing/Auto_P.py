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

data_copy=data.copy()

#auquiring_total_from_original_file_list
total=len(OG_imgs_data)

#adjusting_total_count_based_on_pair_of_compare_files(because compare files are in pair of two we have to delete total number of pairs from total so we can get the original number of files)
with open(r'comp_count.txt', 'r') as file:
    comp_data1 = file.read()

comp_count=int(comp_data1)

for i in range(0,comp_count):
    total=total-1

total=total-2
print(total)

print(data)
print(OG_imgs_data)

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
    if file['title']=="pfile_data.txt":
        print(index+1, 'file downloaded : ', file['title'])
        file.GetContentFile(file['title'])
    if file['title']=="pfile_comp_data.txt":
        print(index+1, 'file downloaded : ', file['title'])
        file.GetContentFile(file['title'])
    if file['title']=="pfile_p_data.txt":
        print(index+1, 'file downloaded : ', file['title'])
        file.GetContentFile(file['title'])



########################################_AQUIRING_NAMES_AND_INFO_OF_FILES_FROM_THE_CLIENT_TEXT_FILE_########################################

values=[]
file_values=[]
key=[]
file_key=[]
file_data={}

c_values=[]
c_file_values=[]
c_key=[]
c_file_key=[]
c_file_data={}

p_values=[]
p_file_values=[]
p_key=[]
p_file_key=[]
p_file_data={}

for line in open("pfile_data.txt"):
    li=line.strip()
    if not li.startswith("#"):
        if not li.startswith("$"):
            values.append(line.strip())
        else:
            key.append(line.strip())
            
for line in open("pfile_comp_data.txt"):
    li=line.strip()
    if not li.startswith("#"):
        if not li.startswith("$"):
            c_values.append(line.strip())
        else:
            c_key.append(line.strip())
            
for line in open("pfile_p_data.txt"):
    li=line.strip()
    if not li.startswith("#"):
        if not li.startswith("$"):
            p_values.append(line.strip())
        else:
            p_key.append(line.strip())

for i in key:
    name=i.replace('$','')
    file_key.append(name)
    
for i in c_key:
    name=i.replace('$','')
    c_file_key.append(name)

for i in p_key:
    name=i.replace('$','')
    p_file_key.append(name)

res = []
for ele in values:
    if ele.strip():
        res.append(ele)
        
c_res = []
for ele in c_values:
    if ele.strip():
        c_res.append(ele)
        
p_res = []
for ele in p_values:
    if ele.strip():
        p_res.append(ele)

for i in range(0, len(res), 4):
    x = i
    file_values.append(res[x:x+4])
    
for i in range(0, len(c_res), 4):
    x = i
    c_file_values.append(c_res[x:x+4])
    
for i in range(0, len(p_res), 4):
    x = i
    p_file_values.append(p_res[x:x+4])
    
print("file_key : ",file_key)
print("file_values : ",file_values)

print("c_file_key : ",c_file_key)
print("c_file_values : ",c_file_values)

print("p_file_key : ",p_file_key)
print("p_file_values : ",p_file_values)

for i in range(len(file_key)):
    file_data[file_key[i]]=file_values[i]
    
for i in range(len(c_file_key)):
    c_file_data[c_file_key[i]]=c_file_values[i]
    
for i in range(len(p_file_key)):
    p_file_data[p_file_key[i]]=p_file_values[i]

print("file_data : ",file_data)
print("c_file_data : ",c_file_data)
print("p_file_data : ",p_file_data)

for i in imgs_data:
    for j in file_data:
        if imgs_data[i]==j:
            file_data[j].append(i)
            
for i in imgs_data:
    for j in c_file_data:
        if imgs_data[i]==j:
            c_file_data[j].append(i)
            
for i in imgs_data:
    for j in p_file_data:
        if imgs_data[i]==j:
            p_file_data[j].append(i)
            
print("file_data : ",file_data)
print("file_data : ",c_file_data)
print("file_data : ",p_file_data)



########################################_AQUIRING_NAMES_AND_KEYS_OF_COMPARISON_FILES_########################################

comp_files_name=[]
comp_files_key=[]
comp_files_dict={}

for i in c_file_key:
    x = i.split(".")
    for i in x:
        c=i+"_comp.jpg"
        comp_files_name.append(c)

for i in data_copy:
    for j in comp_files_name:
        if data_copy[i]==j:
            comp_files_key.append(i)
            
for i in range(len(comp_files_key)):
    comp_files_dict[comp_files_key[i]]=comp_files_name[i]

print(c_file_key)
print("Comparison File Names : ",comp_files_name)
print("Comparison File Key : ",comp_files_key)
print("Comparison File Names and Keys : ",comp_files_dict)



########################################_AQUIRING_NAMES_AND_KEYS_OF_PORTRAIT_FILES_########################################

po_files_name=[]
po_files_key=[]
po_files_dict={}

for i in p_file_key:
    x = i.split(".")
    for i in x:
        c=i+"_po.jpg"
        po_files_name.append(c)

for i in data_copy:
    for j in po_files_name:
        if data_copy[i]==j:
            po_files_key.append(i)
            
for i in range(len(po_files_key)):
    po_files_dict[po_files_key[i]]=po_files_name[i]

print(p_file_key)
print("Comparison File Names : ",po_files_name)
print("Comparison File Key : ",po_files_key)
print("Comparison File Names and Keys : ",po_files_dict)



########################################_COMPARING_NEW_FILES_TO_PAIR_IT_WITH_CORRECT_INFO_########################################

main_data={}
c_main_data={}
p_main_data={}

for i in imgs_data:
    for j in file_data:
        if imgs_data[i]==j:
            for k in range(len(imgs_data)):
                main_data[imgs_data[i]]=file_data[j]
                
for i in imgs_data:
    for j in c_file_data:
        if imgs_data[i]==j:
            for k in range(len(imgs_data)):
                c_main_data[imgs_data[i]]=c_file_data[j]
                
for i in imgs_data:
    for j in p_file_data:
        if imgs_data[i]==j:
            for k in range(len(imgs_data)):
                p_main_data[imgs_data[i]]=p_file_data[j]

print("main_data : ",main_data)
print("c_main_data : ",c_main_data)
print("p_main_data : ",p_main_data)


########################################_REPLACING_TEXT_IN_TEMPLATE_CODE_########################################

search_text1 = "card_number"
search_text2 = "link_here"
search_text3 = "shot_on"
search_text4 = "location_here"
search_text5 = "date_here"
search_text6 = "lens_type"
search_text7 = "info_label"
search_text8 = "download_number"

counter=0

for k in main_data:
    replace_text1 = str(total+counter)
    replace_text2 = main_data[k][4]
    replace_text3 = main_data[k][0]
    replace_text4 = main_data[k][1]
    replace_text5 = main_data[k][2]
    replace_text6 = main_data[k][3]
    replace_text7 = "chck"+str(total+counter)
    replace_text8 = "PhotographyHOOD-"+str(total+counter)
    
    print(total)
    counter=counter+1


    with open(r'imgs_template.txt', 'r') as file:
      
        data = file.read()
        data = data.replace(search_text1, replace_text1).replace(search_text2, replace_text2).replace(search_text3, replace_text3).replace(search_text4, replace_text4).replace(search_text5, replace_text5).replace(search_text6, replace_text6).replace(search_text7, replace_text7).replace(search_text8, replace_text8)
      

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

    print("Code Added : ",k)
    
    
    
#_P

########################################_REPLACING_TEXT_IN_TEMPLATE_CODE_########################################

p_search_text1 = "card_number"
p_search_text2 = "link_here"
p_search_text3 = "shot_on"
p_search_text4 = "location_here"
p_search_text5 = "date_here"
p_search_text6 = "lens_type"
p_search_text7 = "info_label"
p_search_text8 = "download_number"

for k in p_main_data:
    p_replace_text1 = str(total+counter)
    p_replace_text2 = p_main_data[k][4]
    p_replace_text3 = p_main_data[k][0]
    p_replace_text4 = p_main_data[k][1]
    p_replace_text5 = p_main_data[k][2]
    p_replace_text6 = p_main_data[k][3]
    p_replace_text7 = "chck"+str(total+counter)
    p_replace_text8 = "PhotographyHOOD-"+str(total+counter)
    
    print(total)
    counter=counter+1


    with open(r'p_imgs_template.txt', 'r') as file:
      
        data3 = file.read()
        data3 = data3.replace(p_search_text1, p_replace_text1).replace(p_search_text2, p_replace_text2).replace(p_search_text3, p_replace_text3).replace(p_search_text4, p_replace_text4).replace(p_search_text5, p_replace_text5).replace(p_search_text6, p_replace_text6).replace(p_search_text7, p_replace_text7).replace(p_search_text8, p_replace_text8)
      

    with open(r'p_imgs_code.txt', 'w') as file:

        file.truncate(0)
        file.write(data3)
        
    print("P_Text replaced")


########################################_ADDING_CODE_TO_THE_MAIN_FILE_########################################
    
    with open('p_imgs_code.txt', 'r') as f:
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

    print("P_Code Added : ",k)

    
    
#_C

########################################_REPLACING_TEXT_IN_TEMPLATE_CODE_########################################

c_search_text1 = "card_number"
c_search_text2 = "link_here"
c_search_text3 = "shot_on"
c_search_text4 = "location_here"
c_search_text5 = "date_here"
c_search_text6 = "lens_type"
c_search_text7 = "info_label"
c_search_text8 = "download_number"
c_search_text9 = "new_html_file_name"

c_counter=1

for k in c_main_data:
    comp_count=comp_count+1
    c_replace_text1 = str(total+c_counter)
    c_replace_text2 = c_main_data[k][4]
    c_replace_text3 = c_main_data[k][0]
    c_replace_text4 = c_main_data[k][1]
    c_replace_text5 = c_main_data[k][2]
    c_replace_text6 = c_main_data[k][3]
    c_replace_text7 = "chck"+str(total+c_counter)
    c_replace_text8 = "PhotographyHOOD-"+str(total+c_counter)
    c_replace_text9 = "comp"+str(comp_count)+"_try.html"
    
    print(total)
    c_counter=c_counter+1


    with open(r'c_imgs_template.txt', 'r') as file:
      
        data1 = file.read()
        data1 = data1.replace(c_search_text1, c_replace_text1).replace(c_search_text2, c_replace_text2).replace(c_search_text3, c_replace_text3).replace(c_search_text4, c_replace_text4).replace(c_search_text5, c_replace_text5).replace(c_search_text6, c_replace_text6).replace(c_search_text7, c_replace_text7).replace(c_search_text8, c_replace_text8).replace(c_search_text9, c_replace_text9)
      

    with open(r'c_imgs_code.txt', 'w') as file:

        file.truncate(0)
        file.write(data1)
        
    print("COMP_Text replaced")



########################################_ADDING_CODE_TO_THE_MAIN_FILE_########################################
    
    with open('c_imgs_code.txt', 'r') as f:
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
        
    with open(r'comp_count.txt', 'w') as file:

        file.truncate(0)
        file.write(str(comp_count))

    print("COMP_Code Added : ",k)
    
    
comp_search_text1 = "original_image_here"
comp_search_text2 = "edited_image_here"
    
    
 
########################################_WRITING_COMPARISON_FILE_########################################
    
for k in comp_files_dict:

    comp_replace_text1 = c_replace_text2
    comp_replace_text2 = k
    
    with open(r'comp_imgs_template.txt', 'r') as file:
      
        data2 = file.read()
        data2 = data2.replace(comp_search_text1, comp_replace_text1).replace(comp_search_text2, comp_replace_text2)
        
    with open(r"comp"+str(comp_count)+"_try.html", 'w') as file:

        file.write(data2)
        
    print("COMP_Code Added : ",k)
