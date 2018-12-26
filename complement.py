#Type a file name we are gonna input on filename
#Type a file name we are gonna output on newfilename

with open("filename", "r") as f:
    with open("newfilename", "w") as fh:
        name = []
        seq = []
        for line in f.readlines():
            if line.startswith(">"):
                line = line.split()[0]
                name.append(line)
                seq.append("")
                order = name.index(line)
            else:
                line = line.strip()
                seq[order] += line
        
        complement = []
        for i in range(len(name)):
            reverse = seq[i][::-1]
            complement.append("")
            for p in reverse:
                if p == "A":
                    complement[i] += "T"
                if p == "T":
                    complement[i] += "A"
                if p == "C":
                    complement[i] += "G"
                if p == "G":
                    complement[i] += "C"
                if p == "N":
                    complement[i] += "N"
                    
            print (name[i], file = fh)
            print (complement[i], file = fh)