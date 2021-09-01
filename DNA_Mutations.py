
#Define the known and unknown variables for Genes 1 and 2. This will allow the user to choose what they want the functions to use.
kn_func_1 = "ATGCTGGTCATGACCACAAACCACCGCCTCATCTACCTCATCGGCGCGCCCGGCGCGGGCAAGTCGACCATGATGGCCCACCTCACCGA\
CTGCTTTGACCGAGAGCATGTACCGGGCACCGACACCGCCCCGGCATACGACCTGCTCAAGTACACCGACGGCGAGGTCGCCGGTGTCGAGCTCGGCA\
AGCGGCGGCCCAAGTTCTCGGGCACCGACGCGCTGCCCGCCTCGATCATCGAGAAGGCCATCCCGTGGCTCAACACCAAACCGTTTCGGCTGGTGTTC\
GCCGAGGGTGCCCGGCTGGCCAACAAGCGGTTCCTCGACGCGGCGGTGGCCGCCGGATACGAGGTCCACCTCGGTTGGCTCAACCACCCCGATGTCGA\
TACGTGGCGGGCAGCTCGCTCGGCAGAAGTCGGCAAGGTCCAGTCCGAGTCGTGGGTCAAAGGTCGCGTCACGGCGGTGACCAAGCTGGTCGAGAACT\
ACATCAACCGGCCCGAGCGAGGCGTCAAGGTCTACGTTGGTGGTCCAGAGCAGTTGACCTCGGATATGGAGCACCTGTTGGGATGA"

kn_func_2 = "ATGCTGGTCATGACCACAAACCACCGCCTCATCTACCTCATCGGCGCGCCCGGCGCGGGCAAGTCGACCATGATGGCCCACCTCACCGACTG\
CTTTGACCGAGAGCATGTACCGGGCACCGACACCGCCCCGGCGTACGACCTGCTCAAGTACACCGATGGCGAGGTCGCCGGGGTCGAGCTCGGCAAGCG\
GCGACCCCAGTTCTCGGGCACCGACGCGCTGCCCGCCTCGATCATCGAGAAGGCCATCCCGTGGCTCAACACCAAGCCGTTTCGACTGGTGTTCGCCGA\
GGGTGCCCGGCTGGCCAACAAGCGGTTCCTTGACGCTGCGGTGGCCGCCGGATACGAGGTCCACCTCGGTTGGCTCAACCACCCCGATGTCGACGCGTG\
GCGGGCAGCTCGCTCGGCAGAAGTCGGCAAGGTCCAGTCCGAGGCGTGGGTCAAAGGTCGCGTCACGGCGGTGACCAAGCTGGTCGAGAACTACATCAA\
CCGGCCCGAGCGAGGCGTCAAGGTCTACGTTGGTGGTCCAGAGCAGTTGACCTCGGATATGGAGCACCTGTTGGGATGA"

ukn_func_1 = "ATGAAGACCTCGCTGATGGGCACCGCCCGCAACGAGTGGCAGTCCGAGGCATGGGACTTTTCCGAGAGCATCGGCGAGCTGAGCTA\
CTACGTCTCGTGGCGCGCGAACTCGTGCTCGCGCACCACGTTGATCCCGTCGGCTATCGACCCCGATACCGGGCTGCCGACCGGCGAGGTCGACATCGAG\
GAAGATCCCGACGCACAGACAGTCGCCGACTACGTCAAGGGCATCGCCGACGGGCCGCTCGGTCAGGCGGCATTGATCAAGCGCGCGGTCGAGTGCATG\
ACCGTGGTCGGTGAGGTGTGGATCGCCGTGCTGATCCGGCAAGAGAAAGATCCGGTCACCGGCCTCGCCGCGCCTCGGGCGCGGTGGTATGCCGTCACGC\
GCGAGGAAATCAAATCCAAGGCGGGGGAGACCGCCGAGATCTCGCTGCCGGACGGTAAGACCCACGAGTTCAATCGCGACCTCGACTCGCTCGTGCGGAT\
ATGGAATCCACGCCCACGCAAGGCCAGCCAGGCCACCTCGCCGGTACGCGCTTGCCTCGAAACGCTGCGCGAGATCGAGCGGACCACACGCAAGATCAAG\
AACGCGGCCAAGTCGCGCGTGATGAACAACGGTGTGCTGTTCGTGCCCGCCGAGATGTCGCTACCGGCTGCGCAGGCCCCGATCCCCGCTGGGCAGGCGC\
AGATCCCCGGCGCGCCGGTGCCCGAGGTGTCCGGCGTCCCGGCCAGCGAGCAGCTCGCCACGATGATCTATCAGGCGTCGGTGGCCGCCATGGAGGACGA\
GAACAGCCAGGCGGCGTATATCCCGCTCGTCGCGTCGGTGGCCGCCGAGCACCTCGAAAAGGTCCAGCACATCAAGTTTGGCAACGAGGTCACCGAAGTC\
GAGATCAAGACCCGTATCGACGCGATCACGCGGTTGGCCATGGGCCTCGATGTCTCGCCCGAGCGGCTGCTCGGCATGAGCAAGGGCAACCATTGGTCGG\
CGTGGGCCATCGGCGACGAGGACGTGCAGCTTCACATCAAGCCCGTCATGGACCTGATCTGCCAGGCAATCTACAACGACATCCTGACCCCGCTGCTCGC\
ACGTGAAGGCATCGACCCGACCAAGTACATCCTCTGGTACGACGCGTCGGGTCTGACCAGCGACCCCGATCTGTCTGACGAGGCGGTCGAGGCGCACGAC\
CGGGGTGCGATCACCTCGGCGGCGCTGCGGCGGCTGCTCAACGTGGGCGAGGACAGCGGCTACGACCTCACCACCCTCGACGGCTGCCGTGAGTTCGCAG\
CCGATGTCGTCACCAAGAACCCTGAGCTCATCGCGATGTACGCACCGCTGCTGTCGAGTCAGCTCGCGGGCATCGAGTTCCCACAGCCTGCCAATGCCAT\
CGAGTCGACGCGCGAGGACGAGGAAGACGACGAGGACAGCGGTGCCCGGCAGCAGCGCGAGCCGCAAACCGAGGACGAGCGTAGTACCGAGGAAGCGGCG\
TCGCTCAATGACCGAGCGGCCTACCTCGTCGCCGAGCGGCTGCTCGTCAACCGCGCGCTCGACCTCGCGGGCAAGCGGCGCTTCAAGGTGAATGACGCGG\
CGCTCAAGACCAAGCTGCGCGACGTTCCGGCCCACGAGTACCACCGCGTACTGCCGCCGGTCCGGTCGAGCGAGATCCCCCGCCTGATCGCCGGATGGGA\
CACCGCACTCGAGGACGAGGTCGTGGCCTCGCTCGGTCTCGACAACGAGAAGCTACGCAATGCGGTGCTGGCCACGGTGCGGCGTCAGCTCACACAGCCT\
CTCATCGAGGGCGAGGTCGTCTGA"

ukn_func_2 = "ATGGCTGCTACTTCATTGCGCGTCGTTCGCCGCCCCAAGGGCAGCGCCCCGGCAGCTCGTCGGCGATCCCTCACGGCTGCATCGCA\
GCTCATCACCGACCCACAAAAGCAGATGAAGACCTCGCTGATGGGCACCGCCCGCAACGAGTGGCAGTCCGAGGCATGGGACTTTTCCGAGAGCATCGGC\
GAGCTGAGCTACTACGTCTCGTGGCGCGCGAACTCGTGCTCGCGCACCACGTTGATCCCGTCGGCTATCGACCCCGATACCGGGCTGCCGACCGGCGAGG\
TCGACATCGAGGAAGATCCCGACGCACAGACAGTCGCCGACTACGTCAAGGGCATCGCCGACGGGCCGCTCGGTCAGGCGGCATTGATCAAGCGCGCGGT\
CGAGTGCATGACCGTGGTCGGTGAGGTGTGGATCGCCGTGCTGATCCGGCAAGAGAAAGATCCGGTCACCGGCCTCGCCGCGCCTCGGGCGCGGTGGTAT\
GCCGTCACGCGCGAGGAAATCAAATCCAAGGCGGGGGAGACCGCCGAGATCTCGCTGCCGGACGGTAAGACCCACGAGTTCAATCGCGACCTCGACTCGC\
TCGTGCGGATATGGAATCCACGCCCACGCAAGGCCAGCCAGGCCACCTCGCCGGTACGCGCTTGCCTCGAAACGCTGCGCGAGATCGAGCGGACCACACG\
CAAGATCAAGAACGCGGCCAAGTCACGCGTGATGAACAACGGTGTGCTGTTCGTGCCCGCCGAGATGTCGCTACCGGCTGCGCAGGCCCCGATCCCCGCT\
GGGCAGGCGCAGATCCCCGGCGCGCCGGTGCCCGAGGTGTCCGGCGTCCCGGCCAGCGAGCAGCTCGCCACGATGATCTATCAGGCGTCGGTGGCCGCCA\
TGGAGGACGAGAACAGCCAGGCGGCGTATATCCCGCTCGTCGCGTCGGTGGCCGCCGAGCACCTCGAAAAGGTCCAGCACATCAAGTTTGGCAACGAGGT\
CACCGAAGTCGAGATCAAGACCCGTATCGACGCGATCACGCGGTTGGCCATGGGCCTCGATGTCTCGCCCGAGCGGCTGCTCGGCATGAGCAAGGGCAAC\
CATTGGTCGGCGTGGGCCATCGGCGACGAGGACGTGCAGCTTCACATCAAGCCCGTCATGGACCTGATCTGCCAGGCGATCTACAACGACATCCTGACCC\
CGCTGCTCGCACGTGAAGGCATCGACCCGACCAAGTACATCCTCTGGTACGACGCGTCGGGTCTGACCAGCGACCCCGATCTGTCTGACGAGGCGGTCGA\
GGCGCACGACCGGGGTGCGATCACCTCGGCGGCGCTGCGGCGGCTGCTCAACGTGGGCGAGGACAGCGGCTACGACCTCACCACCCTCGACGGCTGCCGT\
GAGTTCGCAGCCGATGTCGTCACCAAGAACCCTGAGCTCATCGCGATGTACGCACCGCTGCTGTCGAGTCAGCTCGCGGGCATCGAGTTCCCACAGCCTG\
CCAATGCCATCGAGTCGACGCGCGAGGACGAGGAAGACGACGAGGACAGCGGTGCCCGGCAGCAGCGCGAGCCGCAAACCGAGGACGAGCGTAGTACCGA\
GGAAGCGGCGTCGCTCAATGACCGAGCGGCCTACCTCGTCGCCGAGCGGCTGCTCGTCAACCGCGCGCTCGACCTCGCGGGCAAGCGGCGCTTCAAGGTG\
AATGACGCGGCGCTCAAGACCAAGCTGCGCGACGTTCCGGCCCACGAGTACCACCGCGTACTGCCGCCGGTCCGGTCGAGCGAGATCCCCCGCCTGATCG\
CCGGATGGGACACCGCACTCGAGGACGAGGTCGTGGCCTCGCTCGGTCTCGACAACGAGAAGCTACGCAATGCGGTGCTGGCCACGGTGCGGCGTCAGCT\
CACACAGCCTCTCATCGAGGGCGAGGTCGTCTGA"


choice = input("Please type 1 to use the known fucntion and 2 to use the unknown fuction: ")

#Define variables for Sequence 1 and Sequence 2
if choice == "1":
    seq_1 = kn_func_1
    seq_2 = kn_func_2

if choice == "2":
    seq_1 = ukn_func_1
    seq_2 = ukn_func_2
 
#Converting Sequence 1 and Sequence 2 into a list 
magic_list_1 = list(seq_1) #The list function takes the seq_1 variable and turns it into a list.
magic_list_2 = list(seq_2) #The list function takes the seq_2 variable and turns it into a list.

#print("List of sequence 1")
#print(magic_list_1) #outputs the list of elements in seq_1
#print("List of sequence 2")
#print(magic_list_2) #outputs the list of elements in seq_2


#A function for identifying the count and locations of mutations in the DNA
def dnaCount(seq_1, seq_2):

    #identifying the length of each sequence. This will helps us in our loop statements.
    Number_of_elements_1 = len(magic_list_1) #The len function counts how many elements (or nucleotides) are in seq_1. We are storing that value in the variable called "Number_of_elements_1"
    Number_of_elements_2 = len(magic_list_2) #The len function counts how many elements (or nucleotides) are in seq_2. We are storing that value in the variable called "Number_of_elements_2"

    print("Number of elements in sequence 1: ", Number_of_elements_1)
    print("Number of elements in sequence 2: ", Number_of_elements_2)
    
    #Defining varibales for our loop statments to act as the start of our counters
    n = 0
    counter_sim = 0
    counter_diff = 0
    
    #This for loop combined with an if statement finds the counts the number of mutations and finds the positions where those mutations occur.
    for t in magic_list_1:
        varPosition_1 = magic_list_1[n]
        #print(varPosition_1)
        for x in magic_list_2:
            varPosition_2 = magic_list_2[n]
            #print(varPosition_1, varPosition_2)   
        if varPosition_1 == varPosition_2:
            counter_sim = counter_sim + 1
        if varPosition_1 != varPosition_2:
            counter_diff = counter_diff + 1
            for i in magic_list_2:
                #This part of the code brings back the location of each mutation.
                #In this function test_2 is the element whose position we are looking for, n is the starting point for where we are going to start looking for the next mutation
                #(This is becuase the index function only returns the first instance of the element), and end specifies which element to stop indexing.
                end = Number_of_elements_2
                index_2 = magic_list_2.index(varPosition_2, n, end) #Equals the position of the mutation depending on the value of n within the for loop
            print("There is a mutation located at element ", index_2, varPosition_1, "-->", varPosition_2)
            #print("There is a mutation located at element ", index_2, varChunk_1, "-->", varChunk_2, varPosition_1, "-->", varPosition_2)
        n = n + 1

    print("Number of nucleotides that did not change: ", counter_sim)
    print("Number of mutations: ", counter_diff)



#A function for identifying transitions/transversions in the DNA
def transIV(seq_1, seq_2):

    #identifying the length of each sequence. This will helps us in our loop statements.
    Number_of_elements_1 = len(magic_list_1) #The len function counts how many elements (or nucleotides) are in seq_1. We are storing that value in the variable called "Number_of_elements_1"
    Number_of_elements_2 = len(magic_list_2) #The len function counts how many elements (or nucleotides) are in seq_2. We are storing that value in the variable called "Number_of_elements_2"

    print("Number of elements in sequence 1: ", Number_of_elements_1)
    print("Number of elements in sequence 2: ", Number_of_elements_2)

    #Defining varibales for our loop statments to act as the start of a counters
    n = 0
    transi_counter = 0
    transv_counter = 0

    for t in magic_list_1:
        varPosition_1 = magic_list_1[n]
        #print(test_1) # A
        for x in magic_list_2:
            varPosition_2 = magic_list_2[n]
        #print(test_1, test_2) # A, A 
        if varPosition_1 != varPosition_2: #if test_1 does not equal test_2 do the following code indented below.
            end = Number_of_elements_2
            for i in magic_list_2:
                index_2 = magic_list_2.index(varPosition_2, n, end)
                    #varPosition_2 equals the nucleotide we are looking for.
                    #n equals the starting point of where to look.
                    #end equals the point (or number) at which the for loop should stop indexing though the list
            if varPosition_1 == "T" and varPosition_2 == "C":
                transi_counter = transi_counter + 1
                print("There is a tranisition mutation located at element ", index_2,":", varPosition_1, "-->", varPosition_2)
            elif varPosition_1 == "C" and varPosition_2 == "T":
                transi_counter = transi_counter + 1
                print("There is a tranisition mutation located at element ", index_2,":", varPosition_1, "-->", varPosition_2)
            elif varPosition_1 == "A" and varPosition_2 == "G":
                transi_counter = transi_counter + 1
                print("There is a tranisition mutation located at element ", index_2,":", varPosition_1, "-->", varPosition_2)
            elif varPosition_1 == "G" and varPosition_2 == "A":
                transi_counter = transi_counter + 1
                print("There is a tranisition mutation located at element ", index_2,":", varPosition_1, "-->", varPosition_2)
            elif varPosition_1 == "T" or varPosition_1 == "C" and varPosition_2 == "A" or varPosition_2 == "G":
                transv_counter = transv_counter + 1
                print("There is a transversion mutation located at element ", index_2,":", varPosition_1, "-->", varPosition_2)
            elif varPosition_1 == "A" or varPosition_1 == "G" and varPosition_2 == "T" or varPosition_2 == "C":
                transv_counter = transv_counter + 1
                print("There is a transversion mutation located at element ", index_2,":", varPosition_1, "-->", varPosition_2)
        n = n + 1

    print("Total number of transitions: ", transi_counter)
    print("Total number of transversions: ", transv_counter)
    print("Total number of mutations: ", transi_counter + transv_counter)


#A Function for dividing lists into chunks where the number of elements in each sub-list is determined by n.
def divide_chunks(l, n):
    
    # looping untill length l (the length of your sequence/list) and n equals how many elements each chuck should have.
    for i in range(0, len(l), n):  
        yield l[i:i + n]

# A function for converting DNA to amino acids
# we want our list to be divided into chucks of 3 (representing codons)
def DNA_to_Amino():
    n = 3

    chuncked_list_1 = list(divide_chunks(magic_list_1, n))
    chuncked_list_2 = list(divide_chunks(magic_list_2, n))

    print("List of sequence 1")
    print(chuncked_list_1) #outputs the list of elements in seq_1
    print("List of sequence 2")
    print(chuncked_list_2) #outputs the list of elements in seq_2
    

#A function for identifying synonymous/nonsynonymous mutations
def synonymous():

    #Defining a variable for grouping nucleotides into groups of 3's (forming an amino acid)
    n = 3 
    chucked_list_1 = list(divide_chunks(magic_list_1, n))
    chucked_list_2 = list(divide_chunks(magic_list_2, n))
    
    #identifying the length of each sequence. This will helps us in our loop statements.
    Number_of_elements_1 = len(chucked_list_1) #The len function counts how many elements (or nucleotides) are in seq_1. We are storing that value in the variable called "Number_of_elements_1"
    Number_of_elements_2 = len(chucked_list_2) #The len function counts how many elements (or nucleotides) are in seq_2. We are storing that value in the variable called "Number_of_elements_2"

    print("Number of elements in sequence 1: ", Number_of_elements_1)
    print("Number of elements in sequence 2: ", Number_of_elements_2)

    #Defining all the different amino acids into lists
    Start = ['A', 'U', 'G']
    Phe = [['U', 'U', 'U'], ['U', 'U', 'C']]
    Leu = [['U', 'U', 'A'], ['U', 'U', 'G'], ['C', 'U', 'U'], ['C', 'U', 'C'], ['C', 'U', 'A'], ['C', 'U', 'G']]       
    Ser = [['U', 'C', 'U'], ['U', 'C', 'C'], ['U', 'C', 'A'], ['U', 'C', 'G'], ['A', 'G', 'U'], ['A', 'G', 'C']]
    Tyr = [['U', 'A', 'U'], ['U', 'A', 'C']]
    Trp = ['U', 'G', 'G']
    Cys = [['U', 'G', 'U'], ['U', 'G', 'C']]             
    Pro = [['C', 'C', 'U'], ['C', 'C', 'C'], ['C', 'C', 'A'], ['C', 'C', 'G']]
    His = [['C', 'A', 'U'], ['C', 'A', 'C']]
    Gln = [['C', 'A', 'A'], ['C', 'A', 'G']]
    Arg_C = [['C', 'G', 'U'], ['C', 'G', 'C'], ['C', 'G', 'A'], ['C', 'G', 'G']]
    Ile = [['A', 'U', 'U'], ['A', 'U', 'C'], ['A', 'U', 'A']]
    Thr = [['A', 'C', 'U'], ['A', 'C', 'C'], ['A', 'C', 'A'], ['A', 'C', 'G']]
    Asn = [['A', 'A', 'U'], ['A', 'A', 'C']]
    Lys = [['A', 'A', 'A'], ['A', 'A', 'G']]
    Arg_A = [['A', 'G', 'A'], ['A', 'G', 'G']]
    Val = [['G', 'U', 'U'], ['G', 'U', 'C'], ['G', 'U', 'A'], ['G', 'U', 'G']]
    Ala = [['G', 'C', 'U'], ['G', 'C', 'C'], ['G', 'C', 'A'], ['G', 'C', 'G']]
    Asp = [['G', 'A', 'U'], ['G', 'A', 'C']]
    Glu = [['G', 'A', 'A'], ['G', 'A', 'G']]
    Gly = [['G', 'G', 'U'], ['G', 'G', 'C'], ['G', 'G', 'A'], ['G', 'G', 'G']]    
    Stop = [['U', 'A', 'A'], ['U', 'A', 'G'], ['U', 'G', 'A']]

    #Defining counter variables
    p = 0
    counter_chuck_sim = 0
    counter_chuck_diff = 0
    baseloc_1 = 0
    baseloc_2 = 0
    baseloc_3 = 0
    transi_bas_1 = 0
    transv_bas_1 = 0
    transi_bas_2 = 0
    transv_bas_2 = 0
    transi_bas_3 = 0
    transv_bas_3 = 0
    syn_counter = 0
    nonsyn_counter = 0

    for tt in chucked_list_1:
        varChunk_1 = chucked_list_1[p]
        #print(varChunk_1)
        for xx in chucked_list_2:
            varChunk_2 = chucked_list_2[p]
            #print(varChunk_1, varChunk_2)
        if varChunk_1 == varChunk_2:
            counter_chuck_sim = counter_chuck_sim + 1
        if varChunk_1 != varChunk_2:
            counter_chuck_diff = counter_chuck_diff + 1
            for i in chucked_list_2:
                #This part of the code brings back the location of each mutation.
                #In this function varChunk_2 is the element whose position we are looking for, n is the starting point for where we are going to start looking for the next mutation
                #(This is becuase the index function only returns the first instance of the element), and end specifies which element to stop indexing.
                end = Number_of_elements_2
                index_2 = chucked_list_2.index(varChunk_2, p, end) #Equals the position of the mutation depending on the value of n within the for loop
            #
            #Manually checking the conditions for synonymous mutations
            #
            if varChunk_1 in Phe and varChunk_2 in Phe:
                am1 = "Phe"
                am2 = "Phe"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Leu and varChunk_2 in Leu:
                am1 = "Leu"
                am2 = "Leu"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Ser and varChunk_2 in Ser:
                am1 = "Ser"
                am2 = "Ser"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Tyr and varChunk_2 in Tyr:
                am1 = "Tyr"
                am2 = "Tyr"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Trp and varChunk_2 in Trp:
                am1 = "Trp"
                am2 = "Trp"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Cys and varChunk_2 in Cys:
                am1 = "Cys"
                am2 = "Cys"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Pro and varChunk_2 in Pro:
                am1 = "Pro"
                am2 = "Pro"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in His and varChunk_2 in His:
                am1 = "His"
                am2 = "His"
                sn = "Synonymous"
            elif varChunk_1 in Gln and varChunk_2 in Gln:
                am1 = "Gln"
                am2 = "Gln"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Arg_C and varChunk_2 in Arg_C:
                am1 = "Arg_C"
                am2 = "Arg_C"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Ile and varChunk_2 in Ile:
                am1 = "Ile"
                am2 = "Ile"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Thr and varChunk_2 in Thr:
                am1 = "Thr"
                am2 = "Thr"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Asn and varChunk_2 in Asn:
                am1 = "Asn"
                am2 = "Asn"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Lys and varChunk_2 in Lys:
                am1 = "Lys"
                am2 = "Lys"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Arg_A and varChunk_2 in Arg_A:
                am1 = "Arg_A"
                am2 = "Arg_A"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Val and varChunk_2 in Val:
                am1 = "Val"
                am2 = "Val"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Ala and varChunk_2 in Ala:
                am1 = "Ala"
                am2 = "Ala"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Asp and varChunk_2 in Asp:
                am1 = "Asp"
                am2 = "Asp"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Glu and varChunk_2 in Glu:
                am1 = "Glu"
                am2 = "Glu"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Gly and varChunk_2 in Gly:
                am1 = "Gly"
                am2 = "Gly"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Stop and varChunk_2 in Stop:
                am1 = "Stop"
                am2 = "Stop"
                sn = "Synonymous"
                syn_counter += 1
            else:
                am1 = ""
                am2 = ""
                sn = "Non-synonymous"
                nonsyn_counter += 1
                    #print("There is a tranisition mutation located at element ", index_2,":", varChunk_1[2], "-->", varChunk_2[2])
            print("There is a mutation located at element ", index_2, varChunk_1, "-->", varChunk_2, sn)
        p = p + 1

    print("Number of nucleotides that did not change: ", counter_chuck_sim)
    print("Number of mutations: ", counter_chuck_diff)
    print("Total number of Synonymous mutations: ", syn_counter)
    print("Total number of Non-synonymous mutations: ", nonsyn_counter)


#A function that identifies the location of a mutation within a codon and whether or not that mutatation is a transition or transversion mutation and Synonymous or Non-synonymous.
def Chunky():

    #Defining a variable
    n = 3 
    chucked_list_1 = list(divide_chunks(magic_list_1, n))
    chucked_list_2 = list(divide_chunks(magic_list_2, n))
    
    #identifying the length of each sequence. This will helps us in our loop statements.
    Number_of_elements_1 = len(chucked_list_1) #The len function counts how many elements (or nucleotides) are in seq_1. We are storing that value in the variable called "Number_of_elements_1"
    Number_of_elements_2 = len(chucked_list_2) #The len function counts how many elements (or nucleotides) are in seq_2. We are storing that value in the variable called "Number_of_elements_2"

    print("Number of elements in sequence 1: ", Number_of_elements_1)
    print("Number of elements in sequence 2: ", Number_of_elements_2)

    #Defining all the different amino acids into lists
    Start = ['A', 'U', 'G']
    Phe = [['U', 'U', 'U'], ['U', 'U', 'C']]
    Leu = [['U', 'U', 'A'], ['U', 'U', 'G'], ['C', 'U', 'U'], ['C', 'U', 'C'], ['C', 'U', 'A'], ['C', 'U', 'G']]       
    Ser = [['U', 'C', 'U'], ['U', 'C', 'C'], ['U', 'C', 'A'], ['U', 'C', 'G'], ['A', 'G', 'U'], ['A', 'G', 'C']]
    Tyr = [['U', 'A', 'U'], ['U', 'A', 'C']]
    Trp = ['U', 'G', 'G']
    Cys = [['U', 'G', 'U'], ['U', 'G', 'C']]             
    Pro = [['C', 'C', 'U'], ['C', 'C', 'C'], ['C', 'C', 'A'], ['C', 'C', 'G']]
    His = [['C', 'A', 'U'], ['C', 'A', 'C']]
    Gln = [['C', 'A', 'A'], ['C', 'A', 'G']]
    Arg_C = [['C', 'G', 'U'], ['C', 'G', 'C'], ['C', 'G', 'A'], ['C', 'G', 'G']]
    Ile = [['A', 'U', 'U'], ['A', 'U', 'C'], ['A', 'U', 'A']]
    Thr = [['A', 'C', 'U'], ['A', 'C', 'C'], ['A', 'C', 'A'], ['A', 'C', 'G']]
    Asn = [['A', 'A', 'U'], ['A', 'A', 'C']]
    Lys = [['A', 'A', 'A'], ['A', 'A', 'G']]
    Arg_A = [['A', 'G', 'A'], ['A', 'G', 'G']]
    Val = [['G', 'U', 'U'], ['G', 'U', 'C'], ['G', 'U', 'A'], ['G', 'U', 'G']]
    Ala = [['G', 'C', 'U'], ['G', 'C', 'C'], ['G', 'C', 'A'], ['G', 'C', 'G']]
    Asp = [['G', 'A', 'U'], ['G', 'A', 'C']]
    Glu = [['G', 'A', 'A'], ['G', 'A', 'G']]
    Gly = [['G', 'G', 'U'], ['G', 'G', 'C'], ['G', 'G', 'A'], ['G', 'G', 'G']]    
    Stop = [['U', 'A', 'A'], ['U', 'A', 'G'], ['U', 'G', 'A']]

    #Defining counter variables
    p = 0
    counter_chuck_sim = 0
    counter_chuck_diff = 0
    baseloc_1 = 0
    baseloc_2 = 0
    baseloc_3 = 0
    transi_bas_1 = 0
    transv_bas_1 = 0
    transi_bas_2 = 0
    transv_bas_2 = 0
    transi_bas_3 = 0
    transv_bas_3 = 0
    syn_counter = 0
    nonsyn_counter = 0

    for tt in chucked_list_1:
        varChunk_1 = chucked_list_1[p]
        #print(varChunk_1)
        for xx in chucked_list_2:
            varChunk_2 = chucked_list_2[p]
            #print(varChunk_1, varChunk_2)
        if varChunk_1 == varChunk_2:
            counter_chuck_sim = counter_chuck_sim + 1
        if varChunk_1 != varChunk_2:
            counter_chuck_diff = counter_chuck_diff + 1
            for i in chucked_list_2:
                #This part of the code brings back the location of each mutation.
                #In this function varChunk_2 is the element whose position we are looking for, n is the starting point for where we are going to start looking for the next mutation
                #(This is becuase the index function only returns the first instance of the element), and end specifies which element to stop indexing.
                end = Number_of_elements_2
                index_2 = chucked_list_2.index(varChunk_2, p, end) #Equals the position of the mutation depending on the value of n within the for loop
            #
            #Manually checking the conditions for synonymous mutations / amino_acids = [Start, Phe, Leu, Ser, Tyr, Trp, Cys, Pro, His, Gln, Arg_C, Ile, Thr, Asn, Lys, Arg_A, Val, Ala, Asp, Glu, Gly, Stop]
            #
            if varChunk_1 in Phe and varChunk_2 in Phe:
                am1 = "Phe"
                am2 = "Phe"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Leu and varChunk_2 in Leu:
                am1 = "Leu"
                am2 = "Leu"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Ser and varChunk_2 in Ser:
                am1 = "Ser"
                am2 = "Ser"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Tyr and varChunk_2 in Tyr:
                am1 = "Tyr"
                am2 = "Tyr"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Trp and varChunk_2 in Trp:
                am1 = "Trp"
                am2 = "Trp"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Cys and varChunk_2 in Cys:
                am1 = "Cys"
                am2 = "Cys"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Pro and varChunk_2 in Pro:
                am1 = "Pro"
                am2 = "Pro"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in His and varChunk_2 in His:
                am1 = "His"
                am2 = "His"
                sn = "Synonymous"
            elif varChunk_1 in Gln and varChunk_2 in Gln:
                am1 = "Gln"
                am2 = "Gln"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Arg_C and varChunk_2 in Arg_C:
                am1 = "Arg_C"
                am2 = "Arg_C"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Ile and varChunk_2 in Ile:
                am1 = "Ile"
                am2 = "Ile"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Thr and varChunk_2 in Thr:
                am1 = "Thr"
                am2 = "Thr"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Asn and varChunk_2 in Asn:
                am1 = "Asn"
                am2 = "Asn"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Lys and varChunk_2 in Lys:
                am1 = "Lys"
                am2 = "Lys"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Arg_A and varChunk_2 in Arg_A:
                am1 = "Arg_A"
                am2 = "Arg_A"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Val and varChunk_2 in Val:
                am1 = "Val"
                am2 = "Val"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Ala and varChunk_2 in Ala:
                am1 = "Ala"
                am2 = "Ala"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Asp and varChunk_2 in Asp:
                am1 = "Asp"
                am2 = "Asp"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Glu and varChunk_2 in Glu:
                am1 = "Glu"
                am2 = "Glu"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Gly and varChunk_2 in Gly:
                am1 = "Gly"
                am2 = "Gly"
                sn = "Synonymous"
                syn_counter += 1
            elif varChunk_1 in Stop and varChunk_2 in Stop:
                am1 = "Stop"
                am2 = "Stop"
                sn = "Synonymous"
                syn_counter += 1
            else:
                am1 = ""
                am2 = ""
                sn = "Non-synonymous"
                nonsyn_counter += 1
            #
            #Conditions for all mutations in Base locations 1, 2, and 3 of each amino acids
            #
            if varChunk_1[0] != varChunk_2[0]:
                identify_1 = varChunk_1[0]
                identify_2 = varChunk_2[0]
                baseloc = 1
                baseloc_1 = baseloc_1 + 1
                if varChunk_1[0] == "T" and varChunk_2[0] == "C":
                    transi_bas_1 = transi_bas_1 + 1
                    tv = "Transition"
                    #print("There is a tranisition mutation located at element ", index_2,":", varChunk_1[0], "-->", varChunk_2[0])
                elif varChunk_1[0] == "C" and varChunk_2[0] == "T":
                    transi_bas_1 = transi_bas_1 + 1
                    tv = "Transition"
                    #print("There is a tranisition mutation located at element ", index_2,":", varChunk_1[0], "-->", varChunk_2[0])
                elif varChunk_1[0] == "A" and varChunk_2[0] == "G":
                    transi_bas_1 = transi_bas_1 + 1
                    tv = "Transition"
                    #print("There is a tranisition mutation located at element ", index_2,":", varChunk_1[0], "-->", varChunk_2[0])
                elif varChunk_1[0] == "G" and varChunk_2[0] == "A":
                    transi_bas_1 = transi_bas_1 + 1
                    tv = "Transition"
                    #print("There is a tranisition mutation located at element ", index_2,":", varChunk_1[0], "-->", varChunk_2[0])
                elif varChunk_1[0] == "T" or varChunk_1[0] == "C" and varChunk_2[0] == "A" or varChunk_2[0] == "G":
                    transv_bas_1 = transv_bas_1 + 1
                    tv = "Transversion"
                    #print("There is a transversion mutation located at element ", index_2,":", varChunk_1[0], "-->", varChunk_2[0])
                elif varChunk_1[0] == "A" or varChunk_1[0] == "G" and varChunk_2[0] == "T" or varChunk_2[0] == "C":
                    transv_bas_1 = transv_bas_1 + 1
                    tv = "Transversion"
                    #print("There is a transversion mutation located at element ", index_2,":", varChunk_1[0], "-->", varChunk_2[0])
            elif varChunk_1[1] != varChunk_2[1]:
                identify_1 = varChunk_1[1]
                identify_2 = varChunk_2[1]
                baseloc = 2
                baseloc_2 = baseloc_2 + 1
                if varChunk_1[1] == "T" and varChunk_2[1] == "C":
                    transi_bas_2 = transi_bas_2 + 1
                    tv = "Transition"
                    #print("There is a tranisition mutation located at element ", index_2,":", varChunk_1[1], "-->", varChunk_2[1])
                elif varChunk_1[1] == "C" and varChunk_2[1] == "T":
                    transi_bas_2 = transi_bas_2 + 1
                    tv = "Transition"
                    #print("There is a tranisition mutation located at element ", index_2,":", varChunk_1[1], "-->", varChunk_2[1])
                elif varChunk_1[1] == "A" and varChunk_2[1] == "G":
                    transi_bas_2 = transi_bas_2 + 1
                    tv = "Transition"
                    #print("There is a tranisition mutation located at element ", index_2,":", varChunk_1[1], "-->", varChunk_2[1])
                elif varChunk_1[1] == "G" and varChunk_2[1] == "A":
                    transi_bas_2 = transi_bas_2 + 1
                    tv = "Transition"
                    #print("There is a tranisition mutation located at element ", index_2,":", varChunk_1[1], "-->", varChunk_2[1])
                elif varChunk_1[1] == "T" or varChunk_1[1] == "C" and varChunk_2[1] == "A" or varChunk_2[1] == "G":
                    transv_bas_2 = transv_bas_2 + 1
                    tv = "Transversion"
                    #print("There is a tranisition mutation located at element ", index_2,":", varChunk_1[1], "-->", varChunk_2[1])
                elif varChunk_1[1] == "A" or varChunk_1[1] == "G" and varChunk_2[1] == "T" or varChunk_2[1] == "C":
                    transv_bas_2 = transv_bas_2 + 1
                    tv = "Transversion"
                    #print("There is a tranisition mutation located at element ", index_2,":", varChunk_1[1], "-->", varChunk_2[1])
            elif varChunk_1[2] != varChunk_2[2]:
                identify_1 = varChunk_1[2]
                identify_2 = varChunk_2[2]
                baseloc = 3
                baseloc_3 = baseloc_3 + 1
                if varChunk_1[2] == "T" and varChunk_2[2] == "C":
                    transi_bas_3 = transi_bas_3 + 1
                    tv = "Transition"
                    #print("There is a tranisition mutation located at element ", index_2,":", varChunk_1[2], "-->", varChunk_2[2])
                elif varChunk_1[2] == "C" and varChunk_2[2] == "T":
                    transi_bas_3 = transi_bas_3 + 1
                    tv = "Transition"
                    #print("There is a tranisition mutation located at element ", index_2,":", varChunk_1[2], "-->", varChunk_2[2])
                elif varChunk_1[2] == "A" and varChunk_2[2] == "G":
                    transi_bas_3 = transi_bas_3 + 1
                    tv = "Transition"
                    #print("There is a tranisition mutation located at element ", index_2,":", varChunk_1[2], "-->", varChunk_2[2])
                elif varChunk_1[2] == "G" and varChunk_2[2] == "A":
                    transi_bas_3 = transi_bas_3 + 1
                    tv = "Transition"
                    #print("There is a tranisition mutation located at element ", index_2,":", varChunk_1[2], "-->", varChunk_2[2])
                elif varChunk_1[2] == "T" or varChunk_1[2] == "C" and varChunk_2[2] == "A" or varChunk_2[2] == "G":
                    transv_bas_3 = transv_bas_3 + 1
                    tv = "Transversion"
                    #print("There is a tranisition mutation located at element ", index_2,":", varChunk_1[2], "-->", varChunk_2[2])
                elif varChunk_1[2] == "A" or varChunk_1[2] == "G" and varChunk_2[2] == "T" or varChunk_2[2] == "C":
                    transv_bas_3 = transv_bas_3 + 1
                    tv = "Transversion"
                    #print("There is a tranisition mutation located at element ", index_2,":", varChunk_1[2], "-->", varChunk_2[2])
            print("There is a mutation located at element ", index_2, varChunk_1, "-->", varChunk_2, "Base location is: ", baseloc, identify_1, "-->", identify_2, tv, "|", sn, ":", am1, "-->", am2)
        p = p + 1

    print("Number of nucleotides that did not change: ", counter_chuck_sim)
    print("Number of mutations: ", counter_chuck_diff)
    print("Total number of mutations at position 1: ", baseloc_1)
    print("Total number of mutations at position 2: ", baseloc_2)
    print("Total number of mutations at position 3: ", baseloc_3)
    print("Total transition mutations at postion 1: ", transi_bas_1)
    print("Total transversion mutations at postion 1: ", transv_bas_1)
    print("Total transition mutations at postion 2: ", transi_bas_2)
    print("Total transversion mutations at postion 2: ", transv_bas_2)
    print("Total transition mutations at postion 3: ", transi_bas_3)
    print("Total transversion mutations at postion 3: ", transv_bas_3)
    print("Total number of transition mutations: ", transi_bas_1 + transi_bas_2 + transi_bas_3)
    print("Total number of transversion mutations: ", transv_bas_1 + transv_bas_2 + transv_bas_3)
    print("Total number of Synonymous mutations: ", syn_counter)
    print("Total number of Non-synonymous mutations: ", nonsyn_counter)



    


def done():
    done = input("Feel free to close the program when you are done.")

if __name__ == '__main__':
    #print("***Function A***")
    #dnaCount(seq_1, seq_2)
    #print("***Function B***")
    #transIV(seq_1, seq_2)
    #print("***Function C***")
    DNA_to_Amino()
    print("***Number of elements, their location, and type of mutation***")
    synonymous()
    print("***Combination of Functions***")
    Chunky()
    #print("Chunked List 1")
    #print(chucked_list_1)
    #print("Chunked List 2")
    #print(chucked_list_2)
    done()
    

























