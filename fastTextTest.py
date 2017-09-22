
import fasttext
import numpy as np
import visualization
import file_processing as fp
import random

#model = fasttext.skipgram('chat.txt', 'model')
#print(model.words)


def distance(vec1, vec2):
        return sum(pow(pow(vec1-vec2, 2), 0.5))

def similar_List(word_vector, model):
    dis_list = []
    for word in model.words:
         dis = distance(np.array(word_vector), np.array(model[word]))
         dis_list.append(dis)

    return [x for _, x in sorted(zip(dis_list, list(model.words)))]

def word_vector_buckets(model, limit_num=100):
    words = []
    vectors = []

    word_list = list(model.words)
    random.shuffle(word_list)

    for i, word in enumerate(word_list):
        if(i>limit_num): break
        words.append(word)
        vectors.append(model[word])

    return np.asarray(words), np.asarray(vectors)


def main():
    model = fasttext.load_model('model.bin')
    #words, vectors = word_vector_buckets(model, limit_num=500)
    #visualization.showTSNE(words, vectors)

    fp.input_data(iter=3)
    fp.file_combine()
    model = fasttext.skipgram(fp.combine_Txt, 'model')
    words, vectors = word_vector_buckets(model, limit_num=500)
    visualization.showTSNE(words, vectors)


    #wordVec = model['give']
    #print(similar_List(wordVec, model))


if __name__ == '__main__':
    main()
