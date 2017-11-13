#-*- coding: utf-8 -*-
#!/usr/bin/python3

import file_processing as fp
from gensim.models import Word2Vec
import parameters as parm


# 這裡將文本(corpus)轉成[['sentence1'], ['sentence2'], ['sentence3'],...]
corpus = fp.file_to_sentences(parm.orig_Txt)

# 訓練模型
model = Word2Vec(corpus, min_count=5, sg=1)

# 儲存model : model.save(dir)
model.save('save_model')

# 使用儲存起來的model
model = Word2Vec.load('save_model')

# 一些model的資訊
print(model)

# 所有參與train model的字
for word in model.wv.vocab:
    print(word)

print('-------------------')

# popcorn 這個字的向量
print(model['popcorn'])

