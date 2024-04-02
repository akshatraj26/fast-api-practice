import shutil
import glob
import os
filepaths = glob.glob(r'C:\Users\AkshatRaj\Python\Fast Api\*')

# seprated the folder with all path

only_folder = [file for file in filepaths if not file.endswith('.py')]
print(only_folder)

filter_folder = []

for path in filepaths:
    if not path.endswith('.py'):
        folder = path.split('\\')
        foldername = folder[-1]
        folder_name = foldername.replace(' ', '')
        folder[-1] = folder_name
        filter_folder.append(folder)

# for folde in only_folder:
#     sep_folder = folde.split('\\')
#     fol_name = sep_folder[-1]
#     print(fol_name)


absolute = []
for fol in filter_folder:
        absolute.append("\\".join(fol))

# print(absolute)

# for file, abs in zip(only_folder, absolute):
#     os.renames(file, abs)

print("Hurray! you have done it")