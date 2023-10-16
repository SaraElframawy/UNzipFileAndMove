 #The code attempts to extract all the files in a .zip file into a folder.


import os 
import zipfile
# This is the folder where all of the files will be extracted from the zip file.
zip_folder = '/home/sara/Downloads'
os.makedirs("/home/sara/Downloads/BlFiles", exist_ok=True)
def unzip_and_organize(zip_folder):
    for zip_file in os.listdir(zip_folder):
        if zip_file.endswith('.zip'):
            with zipfile.ZipFile(os.path.join(zip_folder, zip_file), 'r') as zip_ref:
                # Create a folder for each zip file (remove the .zip extension)zip_folder
                folder_name = os.path.splitext(zip_file)[0]
                folder_path = os.path.join("/home/sara/Downloads/BlFiles", folder_name)
                
                #os.chdir("/home/sara/Downloads/BlFiles")
                print(folder_path)

                # Extract the contents of the zip file into the folder
                zip_ref.extractall("/home/sara/Downloads/BlFiles")


                print(f'Extracted {zip_file} to {zip_folder}')

unzip_and_organize(zip_folder)







