import pysam


### print sam file 
def printSam(samfile):
    for read in samfile.fetch('seq1',100,120):
        print(read)
        print() 

### pileup function that maps a single base in the reference sequence 
def mapBase(samfile):
    for pileupcolumn in samfile.pileup('seq1',100,120):
        print()
        print("coverage at base %s = %s" % (pileupcolumn.pos, pileupcolumn.n))
        for pileupread in pileupcolumn.pileups:
            if not pileupread.is_del and not pileupread.is_refskip:
                print('\tbase in read %s = %s' % \
                        (pileupread.alignment.query_name,\
                        pileupread.alignment.query_sequence[pileupread.query_position]))


### sort 
def sortBam(filenm): 
    pysam.sort("-o", "output.bam", "ex1.bam") 



filenm="ex1.bam"
samfile=pysam.AlignmentFile(filenm,"rb")


printSam(samfile)

#mapBase(samfile)

#sortBam(filenm) 

samfile.close() 
