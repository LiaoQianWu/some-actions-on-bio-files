#Type a file name we are gonna input on filename.fasta
#Type a file name we are gonna output on newfilename

with open("filename.fasta", "r") as f:
    with open("newfilename", "w")  as fh:
        seq = {}
        for line in f.readlines():
            if line.startswith(">"):
                name = line.split(" ")[0]
                seq[name] = ""   
            else:
                seq[name] += line.replace("\n", "")                
        for name in seq:
            print (name, seq[name], file = fh)