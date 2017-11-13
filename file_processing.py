import codecs
import parameters as parm

def file_combine():
    print('- do combine text !! -')
    file_names = [[parm.orig_Txt, parm.your_Txt]]
    with open(parm.combine_Txt, 'w') as outfile:
        for fname in file_names:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)

    print('- combine ok ! -')

def input_data(iter=1):
    count = 0
    sentences = []

    while(count<iter):
        count+=1
        Q = input("Q:")
        A = input("A:")
        sentences.append(Q)
        sentences.append(A)

    with open(parm.your_Txt, 'w') as text_file:
        for item in sentences:
            text_file.write("%s\n" % item)

def file_to_sentences(fileName):
    sentences = []
    with codecs.open(fileName, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f.readlines():
            sentences.append(line.strip('\n').split(' '))
    return sentences
