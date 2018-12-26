#Type a file name we are gonna input on filename
#Type a file name we are gonna output on newfilename

with open("filename", "r") as f:
    with open("newfilename", "w") as fh:
        name = []
        seq = []
        for line in f:
            if line.startswith(">"):
                line = line.split()[0]
                name.append(line)
                seq.append("")
                order = name.index(line)
            else:
                line = line.strip()
                seq[order] += line
                
        for i in range(len(name)):
            count_A = seq[i].count("A")
            count_T = seq[i].count("T")
            count_C = seq[i].count("C")
            count_G = seq[i].count("G")
            count_N = seq[i].count("N")
            print ("%s: %s bp" % (name[i], len(seq[i])), file = fh)
            print ("A -> %d\nT -> %d\nC -> %d\nG -> %d\nambiguous -> %d" %\
                   (count_A, count_T, count_C, count_G, count_N), file = fh)
