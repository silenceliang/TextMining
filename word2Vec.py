
from gensim.models import KeyedVectors, Word2Vec


def Q_A_input():
    Q = input("Q:")
    A = input("A:")
    print('Are u sure ?', '\nQ:', Q, '\nA:', A)
    flag = input('YorN:')
    if(flag.lower()=='y'): return Q, A
    else: return 0

model = KeyedVectors.load_word2vec_format('model.vec', binary=False)

try:
    Q, A = Q_A_input()
except:
    print('no input!')

#sentences = [Q, A]
#model.build_vocab(sentences)
#model.load(sentences)