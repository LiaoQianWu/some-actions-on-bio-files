with open("c100027", "r") as f:
    with open("c100027.out", "w") as fh:
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
        
        n = 0
        aim = []        
        for i in seq:
            if len(i) < 500:
                aim.append(n)
            n += 1
            
        for p in aim:
            print(ID[p], file = fh)
            print(seq[p], file = fh)