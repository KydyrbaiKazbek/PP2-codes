file_path=r"C:\Users\Kazbek\Documents\Academic Materials of KBTU\PP2 codes\lab6\DirFiles\write_a_list.txt"
file_copy=r"C:\Users\Kazbek\Documents\Academic Materials of KBTU\PP2 codes\lab6\DirFiles\to_copy.txt"
with open(file_path,"r") as file:
    content=file.read()
    with open(file_copy,"w") as copy:
        copy.write(content)