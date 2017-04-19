from nltk import sent_tokenize
import numpy as np
def file_sem(f):
    FI= open(f,'r')
    contents = FI.read().strip()
    FI.close()
    ind_sentences = sent_tokenize(contents)
    #print(ind_sentences)
    no_of_sentences = len(ind_sentences)
    sent_sim_matr = np.zeros((no_of_sentences,no_of_sentences))
    i = 0
    while(i < no_of_sentences):
        j = i
        while(j < no_of_sentences):
            sent_sim_matr[i][j] = 1
            sent_sim_matr[j][i] = 1
            j+=1
        i+=1
    of = open("outputnew.txt",'w')
    of.write(str(sent_sim_matr))
file_sem('file.txt')