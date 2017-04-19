from nltk.corpus import wordnet as wn
#syns = wn.synsets("program")
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
#for i in wn.synset("animal.n.01").hypernym_distances():
#    print(i)
#print()
#for i in wn.synset("girl.n.01").hypernym_distances():
#    print(i)
#for i in wn.synset("asylum.n.01").hypernym_distances() :
#    print(i)
synset_one = wn.synset("animal.n.01").lowest_common_hypernyms(wn.synset("boy.n.01"))
synset_two  = wn.synset("girl.n.01").lowest_common_hypernyms(wn.synset("boy.n.01"))
k = 0
for i in synset_one:
    k = i
synset_one = k
for i in synset_two:
    k = i
synset_two = k
print(synset_one)
print(synset_two)
#finding the distance between these two with entity .
print([{i[0] : i[1]} for i in synset_one.hypernym_distances()])
print([{i[0] : i[1]} for i in synset_two.hypernym_distances()])
print(wn.synset('policeman.n.01').lowest_common_hypernyms(wn.synset('chef.n.01')))

