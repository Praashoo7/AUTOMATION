This is an Automation Script used for Adding images to a Photography Website as in adding the code to the Webpage. I had created a Photography website. To add images to that site i have to copy paste same block of code again and again. It is not efficient and if someone who dosen't have any coding knowledge tries to use it as their website and tries to add images, it is not convenient at all. This script solves these problems.

Now with help of this script i only have to upload images to the specified google drive and add information of each image which is going to be added to the website in a text file which is also available on the specified drive. This script will run every 12 hours or any other specific amount of time and will check if new files are added to the drive if there are new files it will match the details of the image to the image and add it to the Website's code and it will be updated. This Script is designed to be completely robust and easy to use.

1. OG_imgs_data.txt :- This file has Dictionary of all file-Keys and file-names which are laready present in the drive. Using this we can identify newly added files.
                    We also write data back in this file as we aquire information about newly added files for further use.
2. comp_count.txt :- This file has a counter which increases by one after every image added. Using which we can give accurate numbers to the images on the webpage.
3. pfile_data.txt :- Information related to images are stored in this file, Script reads information of images and the image name from this file and creates dictionary                        with name and information.
4. imgs_template.txt :- This file has template code where we perform "search and replace" and create a block of code which will be added to the main webpage file.
5. p_try - Copy (3).html :- This is the main webpage file where we add the block of code.

The other files and code of "Comp(or Comparison)" and "P(or Portrait)" is just diffrent code needed for images with extra buttons. It works same as above.


-> Normal code without extra button(Comp and P) is in Auto_P1.py.
In this we don't need comp_count.txt because we don't have extra pair of images so we can count the number using counter inside the code, we don't need a txt for that.
(4 files instead of 5) Everything else is same as above.
