from nltk.corpus import wordnet as wn
import numpy as np
import os
import sys
import math
from nltk.corpus import brown
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
from nltk.tokenize import TweetTokenizer
max_count = 0
CONST_ALPHA = 0.2 #As defined in the paper
CONST_BETA = 0.45 #As defined in the paper
CONST_DELTA = 0.85 #As defined in the paper ## indicates the weightage to be assigned b/w semantic and word order similarity
#function to implement sentence similarity , returns the probabilty in range (0-1) indicating the similarity
def sent_sim(sentence_one , sentence_two):
    #extract the sentence and try to see the similarity..
    sent_prob = 0.0
    print("Sentence similarity!")
    return sent_prob



#function to implement file similarity which intrenally uses sent_sim function
def file_sem(file_one):
    #get the contents of the file and do the Sentence similarity for all kind of possible combination of sentences.
    prob = 0.0
    file_one_cont = 
    print("File similarity")
    return prob


#Function to ask a user to input two files or two sentences
def intro():
    print("\nEnter a valid option:\n")
    print("1.Sentence Similarity between two files containing different sentences.")
    print("2.Sentence similarity between two sentences\n")
    option = int(input("Your choice : "))
    if option == 1:
        file_one = input("Enter the path of the first file")
        #file_two = input("Enter the path of the second file")
        prob_sim_sent = file_sem(file_one)
        print("Similarity between the sentences in a single file is : (IN MATRIX FORM)\n")
        
    elif option == 2:
        sent_one = input("Enter the first sentence : ")
        sent_two = input("Enter the second sentence two :")
        prob_sim_sent = sent_sim(sent_one , sent_two)
        print("Similarity between\n"+sent_one+"\n"+sent_two+"\n\n is : ",prob_sim_sent)
    else:
        global max_count
        if max_count < 3 : print("Wrong Choice Try again"); max_count+=1 
        else: print("Wrong choice time exceeded!");exit()
        intro()


if __name__ == "__main__":  
    print("-------------------Sentence Similarity--------------------------")
    intro()
    print("Want to try once again? if yes press 1 or else 0")
    excited = int(input())
    while(excited == 1)
        intro()
        print("Want to try once again?")
        excited = int(input())