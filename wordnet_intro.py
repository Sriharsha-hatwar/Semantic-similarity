from nltk.corpus import wordnet as wn
syns = wn.synsets("program")
'''
for i in syns:
    #k = wn.synset(i.name())
    #print("K is :",k)
    print("i is :",i)
    #So both are same.
    #print("Lemmas : ",i.lemmas()[0].name())
    print("The definition of this synset is :",i.definition())
    for j in i.lemmas():
        print("The lemma is ",j," and the actual word is ",j.name())
    print("Some of the examples of these synset are:",i.examples())
    print("\n")
'''
'''
for i in wn.synset("fly.n.01").lemmas():
    print(i.name()) 
print("\n")
for i in wn.synset("fly.v.01").lemmas():
    print(i.name())
'''
for i in wn.synset("fly.n.01").hypernym_distances() :
    print(i)