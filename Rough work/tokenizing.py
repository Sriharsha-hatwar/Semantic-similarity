from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.corpus import wordnet as wn
import numpy as np
from nltk.corpus import brown
import math
CONST_PHI = 0.2
CONST_BETA = 0.45
CONST_ALPHA = 0.2
CONST_PHI = 0.2
CONST_DELTA = 0.875
CONST_ETA = 0.4
total_words = 0
word_freq_brown = {}
def proper_synset(word_one , word_two):
    pair = (None,None)
    maximum_similarity = -1
    synsets_one = wn.synsets(word_one)
    synsets_two = wn.synsets(word_two)
    #print("first word :",word_one)
    #print("second word",word_two)
    #print(synsets_one)
    #print(synsets_two)
    if(len(synsets_one)!=0 and len(synsets_two)!=0):
        for synset_one in synsets_one:
            for synset_two in synsets_two:
                similarity = wn.path_similarity(synset_one,synset_two)
                if(similarity == None):
                    sim = -2
                elif(similarity > maximum_similarity):
                    maximum_similarity = similarity
                    pair = synset_one,synset_two
    else:
        #need to see as for some word there will be no wordset.
        #shuld make it as none
        pair = (None , None)
    return pair
def length_between_words(synset_one , synset_two):
    length = 100000000
    if synset_one is None or synset_two is None:
        return 0
    elif(synset_one == synset_two):
        length = 0
    else:
        words_synet1 = set([word.name() for word in synset_one.lemmas()])
        words_synet2 = set([word.name() for word in synset_two.lemmas()])
        if(len(words_synet1) + len(words_synet2) > len(words_synet1.union(words_synet2))):
            length = 0
        else:
            #finding the actual distance
            length = synset_one.shortest_path_distance(synset_two)
            if(length is None):
                return 0
    return math.exp( -1 * CONST_ALPHA * length)
def depth_common_subsumer(synset_one,synset_two):
    height = 100000000
    if synset_one is None or sentence_two is None:
        return 0
    elif synset_one == synset_two:
        height = max([hypernym[1] for hypernym in synset_one.hypernym_distances()])
    else:
        #get the hypernym set of both the synset.
        hypernym_one = {hypernym_word[0]:hypernym_word[1] for hypernym_word in synset_one.hypernym_distances()}
        hypernym_two = {hypernym_word[0]:hypernym_word[1] for hypernym_word in synset_two.hypernym_distances()}
        common_subsumer = set(hypernym_one.keys()).intersection(set(hypernym_two.keys()))
        if(len(common_subsumer) == 0):
            height = 0
        else:
            height = 0
            for cs in common_subsumer:
                val = [hypernym_word[1] for hypernym_word in cs.hypernym_distances()]
                val = max(val)
                if val > height : height = val

    #print(height) #works
    return (math.exp(CONST_BETA * height) - math.exp(-CONST_BETA * height))/(math.exp(CONST_BETA * height) + math.exp(-CONST_BETA * height))
def word_similarity(word1,word2):
    #depth_common_subsumer(wn.synset('boy.n.01'),wn.synset('life_form.n.01'))
    #print(wn.synset('boy.n.01').lowest_common_hypernym(wn.synset('animal.n.01')))
    #print(wn.synset('boy.n.01').lowest_common_hypernym(wn.synset('girl.n.01')))
    #word1 = input("Enter the first word: ")
    #word2 = input("Enter the second word: ")
    #synset_wordone = wn.synset(word1+".n.01")#doesnt work
    #synset_wordtwo = wn.synset(word2+".n.01")#doesnt work
    synset_wordone,synset_wordtwo = proper_synset(word1,word2) # cant just add +".n.01" to words to convert them to a synset.
    #Need to execute the above as we cant know whether a 'noun' for of the word exists or not.
    return length_between_words(synset_wordone,synset_wordtwo) * depth_common_subsumer(synset_wordone,synset_wordtwo)

def I(search_word):
    global total_words
    if(total_words == 0):
        for sent in brown.sents():
            for word in sent:
                word = word.lower()
                if word not in word_freq_brown:
                    word_freq_brown[word] = 0
                word_freq_brown[word] +=1
                total_words+=1
    count = 0 if search_word not in word_freq_brown else word_freq_brown[search_word]
    ret = 1.0 - (math.log(count+1)/math.log(total_words+1))
    return ret
def most_similar_word(word,sentence):
    most_similarity = 0
    most_similar_word = ''
    for w in sentence:
        #compute the word similarity using the already defined function
        sim  =  word_similarity(w,word)
        if sim > most_similarity:
            most_similarity = sim
            most_similar_word = w
    if most_similarity <= CONST_PHI:
        most_similarity = 0
    return most_similar_word,most_similarity 
def word_order_similarity(sentence_one , sentence_two):
    #print("Sentence one :",sentence_one)
    token_one  = word_tokenize(sentence_one)
    #print("Sentence two : ",sentence_two)
    token_two = word_tokenize(sentence_two)
    joint_word_set = list(set(token_one).union(set(token_two)))
    r1 = np.zeros(len(joint_word_set))
    r2 = np.zeros(len(joint_word_set))
    #filling for the first one
    en_joint_one = {x[1]:x[0] for x in enumerate(token_one)}
    en_joint_two = {x[1]:x[0] for x in enumerate(token_two)}
    set_token_one = set(token_one)
    set_token_two = set(token_two)
    i = 0
    #print(en_joint)
    for word in joint_word_set:
        if word in set_token_one:
            r1[i] = en_joint_one[word]#so wrong.
        else:
            #get best word and check if its greater then a preset threshold
            sim_word , sim = most_similar_word(word , list(set_token_one))
            if sim > CONST_ETA : 
                r1[i] = en_joint_one[sim_word]
            else:
                r1[i] = 0
        i+=1
    j = 0
    for word in joint_word_set:
        if word in set_token_two:
            r2[j] = en_joint_two[word]
        else:
            #get best word and check if its greater then a preset threshold
            sim_word , sim = most_similar_word(word , list(set_token_two))
            if sim > CONST_ETA : 
                r2[j] = en_joint_two[sim_word]
            else:
                r2[j] = 0
        j+=1
    return 1.0 - (np.linalg.norm(r1 - r2) / np.linalg.norm(r1 + r2))
sentence_one = "A RAM keeps things being worked with"
sentence_two = "The CPU uses RAM as a short-term memory store"
word_order_similarity(sentence_one,sentence_two)