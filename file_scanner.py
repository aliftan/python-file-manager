import os

# scanner function
def file_scanner(dir_name, file_type):
    total_file = 0
    for root, dirs, files in os.walk(dir_name, topdown=True):
        for file in files:
            if file.endswith(file_type):
                # print(os.path.join(root, file))
                total_file += 1

        for file in dirs:
            if file.endswith(file_type):
                # print(os.path.join(root, file))
                total_file += 1
    
    # print report
    print("--------------------------------")
    print("total {} file : {:,}".format(file_type, total_file))

# target path
target_dir = "/Users/omahmac/Desktop/Design-Resources"

# file Type
file_svg = ".svg"
file_sketch = ".sketch"

# run
file_scanner(target_dir, file_svg)
file_scanner(target_dir, file_sketch)