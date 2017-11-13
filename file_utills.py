import codecs
import os
import parameters as para

class tools(object):

    def __init__(self):

        self.orig_Txt = para.orig_Txt
        self.your_Txt = para.your_Txt
        self.combine_Txt = para.combine_Txt
        self.ch_txt = para.ch_txt

    def file_to_sentences(self, fileName):

        sentences = []
        with codecs.open(fileName, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f.readlines():
                sentences.append(line.strip('\n'))
        return sentences

    def file_to_words(self, fileName):

        sentences = []
        with codecs.open(fileName, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f.readlines():
                sentences.append(line.strip('\n').split(' ')[:-1])

        return sentences

    def file_combine(self, dir1, dir2, combine_name):
        ''' 合併兩個txt.
        '''
        output_path = combine_name
        file_names = [dir1, dir2]
        with open(output_path, 'w') as outfile:
            for fname in file_names:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)
        return output_path

    def input_data(self, iter=1):
        count = 0
        sentences = []

        while (count < iter):
            count += 1
            Q = input("Q:")
            A = input("A:")
            sentences.append(Q)
            sentences.append(A)

        with open(para.your_Txt, 'w') as text_file:
            for item in sentences:
                text_file.write("%s\n" % item)

    def iter_by_dir(self, dir_name):
        '''
        找這資料夾下的所有corpus
        :param dir_name: txt in this directory
        :return: labeled_list
        '''
        corpus_list = []
        for dirPath, _, fileName in os.walk(dir_name):
            for file in fileName:
                label = '__label__' + os.path.basename(dirPath) + ' , '  # add prefix_label
                file_Path = os.path.join(dirPath, file)

                with open(file_Path, encoding='utf-8') as f:
                    corpus_list.append(label + f.read())

        return corpus_list

    def list_to_txt(self, list, txt_path):

        with open(txt_path, 'w') as f:
            for line in list:
                f.write(line)






