
orig_Txt = 'chat.txt'
your_Txt = 'yourChat.txt'
combine_Txt = 'combine'


def file_combine():
    file_names = [orig_Txt, your_Txt]
    with open(combine_Txt, 'w') as outfile:
        for fname in file_names:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)

def input_data(iter=1):
    count = 0
    sentences = []

    while(count<iter):
        count+=1
        Q = input("Q:")
        A = input("A:")
        sentences.append(Q)
        sentences.append(A)


    with open(your_Txt, 'w') as text_file:
        for item in sentences:
            text_file.write("%s\n" % item)



