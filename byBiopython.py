#Type a file name we are gonna input on filename.fasta
#Type a file name we are gonna output on newfilename

from Bio import SeqIO
records = list(SeqIO.parse("filename.fasta", "fasta"))
print ("Found %d records" % len(records))

with open("newfilename", "w") as fh:        
    for i in records:
        print (i.id, file = fh)
        print (i.seq, file = fh)
