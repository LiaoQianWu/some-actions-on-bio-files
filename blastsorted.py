#Type a file name we are gonna input on filename
#Type a file name we are gonna output on newfilename
#Notice: It is for line in "f", rather than "f.readlines()"

with open("filename", "r") as f:
    with open("newfilename", "w") as fh:
        query = []
        blast = []
        n = 1
        for line in f:
            if line.startswith("Query="):
                line = str(n) + ". " + line.split()[1]
                query.append(line)
                n += 1
                
                for i in range(5):
                    next(f)
                    
                for p in range(10):
                    s = next(f)
                    accession_num = s.split()[0]
                    name = s.split()[1] + " " + s.split()[2] +\
                    s.split()[3] + " " + s.split()[4]
                    score = s.split()[(-1)-1]
                    evalue = s.split()[-1]
                    data = accession_num + " " + name + " " +\
                    score + " " + evalue
                    blast.append(data)
                    
        m = 0
        for q in range(len(query)):
            print (query[q], file = fh)
            for r in range(10):
                print (blast[r+(10*m)], file = fh)
            m += 1