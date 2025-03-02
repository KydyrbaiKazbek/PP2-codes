file_path=r"C:\Users\Kazbek\Documents\Academic Materials of KBTU\PP2 codes\lab6\DirFiles\write_a_list.txt"
array=["123","QWERTY","098765"]

with open(file_path,"w") as file:
    for item in array:
        file.write(item+" ")