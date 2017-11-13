
import fasttext
import numpy as np
import visualization
import file_processing as fp
import random
import time


def dis(vec1, vec2, part):
    return list(map(lambda x, y: y + part*(x - y), vec1, vec2))

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

    return words, vectors


def main():

    #tStart = time.time()
    #model = fasttext.skipgram(fp.orig_Txt, 'model1', min_count=5, thread=4)
    #tEnd = time.time()
    #print('%fs' % (tEnd-tStart))

    #model = fasttext.load_model('model.bin')
    #words, vectors = word_vector_buckets(model, limit_num=500)

    #visualization.showTSNE(words, np.asarray(vectors))

    #fp.input_data(iter=1)


    #print('training....')
    #another_model = fasttext.skipgram(fp.your_Txt, 'model2', min_count=1, thread=8)
    #print(' finish ! ')
    #words, vectors = word_vector_buckets(another_model, limit_num=300)

    another_model = fasttext.load_model('model/wiki.en.vec')

    a = another_model['man']
    b = another_model['woman']
    print(similar_List(dis(a, b, 0.8), another_model)[:5])
    print(similar_List(dis(a, b, 0.5), another_model)[:5])
    print(similar_List(dis(a, b, 0.2), another_model)[:5])

    a = another_model['see']
    b = another_model['saw']
    print(similar_List(dis(a, b, 0.8), another_model)[:5])
    print(similar_List(dis(a, b, 0.5), another_model)[:5])
    print(similar_List(dis(a, b, 0.2), another_model)[:5])

    a = another_model['good']
    b = another_model['bad']
    print(similar_List(dis(a, b, 0.8), another_model)[:5])
    print(similar_List(dis(a, b, 0.5), another_model)[:5])
    print(similar_List(dis(a, b, 0.2), another_model)[:5])

    a = another_model['red']
    b = another_model['purple']
    print(similar_List(dis(a, b, 0.8), another_model)[:5])
    print(similar_List(dis(a, b, 0.5), another_model)[:5])
    print(similar_List(dis(a, b, 0.2), another_model)[:5])

    a = another_model['slow']
    b = another_model['fast']
    print(similar_List(dis(a, b, 0.8), another_model)[:5])
    print(similar_List(dis(a, b, 0.5), another_model)[:5])
    print(similar_List(dis(a, b, 0.2), another_model)[:5])

    a = another_model['never']
    b = another_model['always']
    print(similar_List(dis(a, b, 0.8), another_model)[:5])
    print(similar_List(dis(a, b, 0.5), another_model)[:5])
    print(similar_List(dis(a, b, 0.2), another_model)[:5])


    #for item in another_model.words:
    #    words.append(item)
    #    vectors.append(model[item])

    #print('drawing~~~~')
    #visualization.showTSNE(words, np.array(vectors))


    #wordVec = model['give']
    #print(similar_List(wordVec, model))


if __name__ == '__main__':
    main()
