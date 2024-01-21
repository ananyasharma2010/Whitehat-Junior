import os
import shutil

# .exe , .msi,  .gif, .png .jpg, .jpeg, .csv, .pdf , .xls , .xlsx , .ppt , .pptx

from_dir = "C:\\Users\\ANANYA SHARMA\\Downloads"
to_dir = "C:/Users/ANANYA SHARMA/Downloads"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

# Move All Image files from Downloads Folder to Another Folder
for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:

        path1 = from_dir + "C:/Users/ANANYA SHARMA/Downloads/C102_assets-main/feather.jfif" + file_name                       # Example path1 : Downloads/ImageName1.jpg        
        path2 = to_dir + "C:/Users/ANANYA SHARMA/Downloads" + "Image_Files"                     # Example path2 : D:/My Files/Image_Files      
        path3 = to_dir + "C:/Users/ANANYA SHARMA/Downloads" + "Image_Files" + "C:/Users/ANANYA SHARMA/Downloads/feather.jfif" + file_name   # Example path3 : D:/My Files/Image_Files/ImageName1.jpg
        #print("path1 " , path1)
        #print("path3 ", path3)

        # Check if Folder/Directory Path Exists Before Moving
        # Else make a NEW Folder/Directory Then Move
        if os.path.exists(path2):
          print("Moving " + file_name + ".....")

          # Move from path1 ---> path3
          shutil.move(path1, path3)

        else:
          os.mkdir(path2)
          print("Moving " + file_name + ".....")
          shutil.move(path1, path3)
