#from nltk.corpus import word_tokenize
from nltk.corpus import wordnet as wn
def get_best_synset_pair(word_1, word_2):
	""" 
	Choose the pair with highest path similarity among all pairs. 
	Mimics pattern-seeking behavior of humans.
	"""
	max_sim = -1.0
	synsets_1 = wn.synsets(word_1)
	synsets_2 = wn.synsets(word_2)
	if len(synsets_1) == 0 or len(synsets_2) == 0:
		return None, None
	else:
		max_sim = -1.0
		best_pair = None, None
		for synset_1 in synsets_1:
			for synset_2 in synsets_2:
				sim = wn.path_similarity(synset_1, synset_2)
				if not sim:
					sim = 0
				if sim > max_sim:
					max_sim = sim
					best_pair = synset_1, synset_2
		return best_pair

print("Get best sysnset pair :of ('asylum', 'fruit')" )
print(get_best_synset_pair("precise","exactly"))