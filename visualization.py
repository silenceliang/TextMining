from sklearn.manifold import TSNE
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['YaHei Consolas Hybrid']
#plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

def showTSNE(word, vector):

    tsne = TSNE(n_components=2, random_state=0)
    np.set_printoptions(suppress=True)

    Y = tsne.fit_transform(vector[:, :])

    plt.scatter(Y[:, 0], Y[:, 1])
    for label, x, y in zip(word, Y[:, 0], Y[:, 1]):
        plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords='offset points')
    plt.show()

