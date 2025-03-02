file_path=r"C:\Users\Kazbek\Documents\Academic Materials of KBTU\PP2 codes\lab6\DirFiles\test_file.txt"
with open(file_path,"r") as a:
    line_counter=len(a.readlines())

    
print(line_counter)