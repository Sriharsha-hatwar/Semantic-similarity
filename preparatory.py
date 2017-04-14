from nltk.corpus import wordnet as wn
import math
CONST_ALPHA = 0.2
def length_between_words(synset_one , synset_two):
    length = 100000000000
    if(synset_one == synset_two):
        length = 0
    else:
        words_synet1 = set([word.name() for word in synset_one.lemmas()])
        words_synet2 = set([word.name() for word in synset_two.lemmas()])
        if(len(words_synet1) + len(words_synet2) > len(words_synet1.union(words_synet2))):
            length = 0
        else:
            #finding the actual distance
            length = synset_one.shortest_path_distance(synset_two)
    print(length)
    return math.exp( -1 * CONST_ALPHA * length)
#def depth_common_subsumer(synset_one,synset_two):

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
synset_wordone = wn.synset(word1+".n.01")# erroroneius
synset_wordtwo = wn.synset(word2+".n.01")# #errorneius
print(length_between_words(synset_wordone, synset_wordtwo))