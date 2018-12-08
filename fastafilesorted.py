#Type a file name we are gonna input on filename.fasta
#Type a file name we are gonna output on newfilename

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
                
        for i in range(len(ID)):
            print (ID[i], file = fh)
            print (seq[i], file = fh)