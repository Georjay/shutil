import os, shutil

#Define the source directory
source_dir = 'C:\\Users\\addai\\Downloads'

#A view at the downloads folder after moving files
files = os.listdir(source_dir)
print("Before moving file:")
print(files)

#Looping through files in the directory and groups them based on .endswith method
for f in files:
        if os.path.join(source_dir, f).endswith(('.pdf','.epub', '.xlsx', '.xls', '.doc', '.docx')):
            shutil.move(os.path.join(source_dir, f), os.path.join(source_dir, "Documents"))
            
        if os.path.join(source_dir, f).endswith(('.png')):
            shutil.move(os.path.join(source_dir, f), os.path.join(source_dir, "Photos"))
            
        if os.path.join(source_dir, f).endswith(('.jpg', '.JPG')):
            shutil.move(os.path.join(source_dir, f), os.path.join(source_dir, "Photos"))
        
        if os.path.join(source_dir, f).endswith(('.mp4', '.MP4')):
            shutil.move(os.path.join(source_dir, f), os.path.join(source_dir, "Photos"))


# A view at the downloads folder after moving files
current_files = os.listdir(source_dir)
print("After moving file:")
print(current_files)