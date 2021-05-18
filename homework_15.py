import os

os.getcwd()

if not 'new_dir' in os.listdir():
    os.makedirs('new_dir/Dir1/Dir2')
    os.makedirs('new_dir/Dir1/Dir3/Dir4')
else:
    os.chdir('new_dir')
    if not 'Dir1' in os.listdir():
        os.makedirs('Dir1/Dir2')
        os.makedirs('Dir1/Dir3/Dir4')
    else:
        os.chdir('Dir1')
        if not 'Dir2'in os.listdir():
            os.makedirs('Dir2')
        if not 'Dir3' in os.listdir():
            os.makedirs('Dir3')
        else:
            os.chdir('Dir3')
            if not 'Dir4' in os.listdir():
                os.mkdir('Dir4')


print("Folders are created!!!")
print(os.getcwd())

del_question = input("If you want to delete any of folders, pls specify the name:\n")
if del_question.lower() == 'dir4':
    os.chdir('../Dir3')
    os.rmdir('Dir4')
    print("Dir4 is deleted")
elif del_question.lower() == 'dir3':
    os.chdir('../Dir3')
    os.rmdir('Dir4')
    os.chdir('..')
    os.rmdir('Dir3')
    print("Dir3 is deleted")
elif del_question.lower() == 'dir2':
    os.rmdir('Dir2')
    print("Dir2 is deleted")   
elif del_question.lower() == "dir1":
    os.chdir('../Dir3')
    os.rmdir('Dir4')
    os.chdir('..')
    os.rmdir('Dir3')
    os.rmdir('Dir2')
    os.chdir('..')
    os.rmdir('Dir1')
    print("Dir1 is deleted")
elif del_question.lower() == 'new_dir':
    os.chdir('C:\\Users\\Gohar\\Desktop\\Python\\git-homework\\new_dir\\Dir1\\Dir3')
    os.rmdir('Dir4')
    os.chdir('..')
    os.rmdir('Dir3')
    os.rmdir('Dir2')
    os.chdir('..')
    os.rmdir('Dir1')
    os.chdir('C:\\Users\\Gohar\\Desktop\\Python\\git-homework\\new_dir')
    os.remove('File.txt')
    os.chdir('..')
    os.rmdir('new_dir')
    print("New_dir is deleted")
else:
    raise Exception("Wrong name of folder, pls provide the correct one.")





