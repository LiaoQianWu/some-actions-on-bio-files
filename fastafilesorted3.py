#Type a file name we are gonna input on filename.fasta
#Type a file name we are gonna output on newfilename
#Type another file name to get the last sorted file

with open("filename.fasta", "r") as f:
    with open("newfilename", "w") as fh:
        ID = []
        seq = []
        for line in f.readlines():
            if line.startswith(">"):
                line = line.split()[0]
                ID.append(line)
                seq.append("")
                order = ID.index(line)
            else:
                line = line.replace("\n", "")
                seq[order] += line
                
        n = 1
        for i in range(len(ID)):
            print (str(n) + ". " + ID[i], file = fh)
            print (seq[i], file = fh)
            n += 1
            
            
with open("newfilename", "r") as f:
    with open("newfilename2", "w") as fh:
        for line in f.readlines():
            if ">" in line:
                line = line.split()[1].strip()
                print (line, file = fh)
            else:
                for i in range(0, len(line), 70):
                    fragment = line[i:(i+70)].strip()
                    print (fragment, file = fh)