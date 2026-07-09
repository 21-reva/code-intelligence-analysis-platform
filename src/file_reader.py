import os
def get_python_files(folder_path):
    python_files=[]

    for item in os.listdir(folder_path):
        full_path=os.path.join(folder_path,item)

        if os.path.isfile(full_path) and item.endswith(".py"):
            python_files.append(full_path)
    return python_files

