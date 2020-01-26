import os
import shutil

# scanner function
def file_scanner(from_dir, to_dir, file_type):
    total_file = 0
    for root, dirs, files in os.walk(from_dir, topdown=True):
        for file in files:
            if file.endswith(file_type):
                total_file += 1
                current_path = os.path.join(root, file)
                to_path = "{}/{}".format(to_dir, file)
                print("Moving: {}".format(current_path))
                shutil.move(current_path, to_path)
        
        for file in dirs:
            if file.endswith(file_type):
                total_file += 1
                current_path = os.path.join(root, file)
                to_path = "{}/{}".format(to_dir, file)
                print("Moving: {}".format(current_path))
                shutil.move(current_path, to_path)
    
    # print report
    print("--------------------------------")
    print("Completed move {:,} ({}) files".format(total_file, file_type))

# target path
source_dir = "/Users/omahmac/Downloads"
target_dir = "/Users/omahmac/Downloads/FILE ADOBE"

# file Type
file_mp4 = ".mp4"
file_svg = ".svg"
file_ai = ".ai"
file_jpg = ".JPG"
file_jpeg = ".jpeg"
file_sketch = ".sketch"
file_png = ".PNG"
file_dmg = ".dmg"
file_doc = ".docx"
file_xlsx = ".xlsx"
file_pdf = ".pdf"
file_zip = ".zip"
file_mov = ".mov"
file_gif = ".gif"
file_eps = ".eps"

# run
file_scanner(source_dir, target_dir, file_ai)