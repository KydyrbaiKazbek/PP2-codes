file_names = ["A.txt", "B.txt", "C.txt", "D.txt", "E.txt", "F.txt", "G.txt", 
              "H.txt", "I.txt", "J.txt", "K.txt", "L.txt", "M.txt", "N.txt", 
              "O.txt", "P.txt", "Q.txt", "R.txt", "S.txt", "T.txt", "U.txt", 
              "V.txt", "W.txt", "X.txt", "Y.txt", "Z.txt"]

for file_name in file_names:
    file = r'C:\Users\Kazbek\Documents\Academic Materials of KBTU\PP2 codes\lab6\DirFiles\task_6\ ' + file_name
    with open(file, "w") as file:
        file.write(f"This is file {file_name}\n")
print("Created files from A to Z")