from Bio.Seq import Seq

'''The Seq objects no longer have a .alphabet attribute, 
   and do not do type checking on Seq operations like adding protein to DNA anymore. 
   Remove references to Alphabet where necessary:'''
   
#from Bio.Alphabet.IUPAC import unambiguous_dna, ambiguous_dna

#my_seq = Seq( "AGTACACTGGTA", unambiguous_dna ) 
my_seq = Seq( "AGTACACTGGTA" ) 

print( my_seq )

# How many As,Cs, Ts and Gs in this sequence?
print( '# A: ',my_seq.count("A") )
print( '# C: ',my_seq.count("C") )
print( '# G: ',my_seq.count("G") )
print( '# T: ',my_seq.count("T") )

# To get the GC nucleotide content:
from Bio.SeqUtils import GC
print( 'GC content: ', GC(my_seq), '%' )

# Transcription and translation
my_mRNA = my_seq.transcribe()
print( my_mRNA )
my_pept = my_seq.translate()
print( my_pept )

# Complement and reverse complement
print( 'sequence: ',str(my_seq) )
print( 'comp.   : ',my_seq.complement() )
print( 'revcomp : ',my_seq.reverse_complement() )
