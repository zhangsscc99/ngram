import os

tchunk = os.listdir('../move/output_foreground')

#tchunk = os.listdir('/Users/mac/Desktop/ngram/move/output_foreground')
#print(tchunk)




# %%
tchunk


def change_tchunk(filelist):
    newlist = []
    for i in range(len(filelist)):
        if filelist[i][-6:] == 'tchunk':
            newlist.append(filelist[i])
    return newlist


# %%
tchunk = change_tchunk(tchunk)

# %%
tchunk.sort()
tchunk
#tchunk=tchunk[:10]


# %%


# %%
def change_name(lst):
    for i in range(len(lst)):
        lst[i] = '../move/output_foreground/' + lst[i]
    return lst


change_name(tchunk)

# %%
len(tchunk)

# %%
#tchunk = tchunk[:10]
#print(tchunk)
# %%
#print(tchunk)
with open('../move/tchunkfile.txt', 'w') as f:
    for term in tchunk:
        f.write(term + '\n')

f.close()

import re
import sys



        
      




# !/usr/bin/env python3
import re
import sys

word_processed_by_av = []
word_avmorethan3=[]
def main(all_terms, conll):
    # open unfiltered file list (first argument)
    # 围棋.all_terms
    # input_file  = sys.argv[1]
    input_file = all_terms

    # list of files in CoNLL format
    # BIO data: conll
    # conll_filelist = sys.argv[2]
    conll_filelist = conll
    # print(conll_filelist)
    with open(conll_filelist, "r") as filenames:
        conll_files = filenames.readlines()

    with open(input_file, "r") as f:

        unfiltered = f.readlines()
    for term in unfiltered:
        left_context = []
        left_count = 0
        right_context = []
        right_count = 0
        term_word = term.split("\t")
        current_term = []
        for i in range(0, len(term_word) - 1):
            current_term.append(term_word[i])

        for conll_file in conll_files:
            # modify according to where the conll format files are
            conll_file = conll_file.strip("\n")
            with open(conll_file, "r") as f2:
                conll = f2.readlines()
                current_term_vec = current_term[0].split(" ")
                # print(current_term[0])
                for token in range(0, len(conll)):
                    word2_tag_BIO = conll[token].split("\t")
                    # term matched
                    if current_term[0] == word2_tag_BIO[0]:
                        left = conll[token - 1].split("\t")[0]
                        # if target word length 1
                        # AM 9/11/22
                        if (len(current_term_vec) == 1) and (len(conll) > (token + 1)):
                            right = conll[token + 1].split("\t")[0]
                        else:
                            right = conll[token + len(current_term_vec) - 1].split("\t")[0]
                        left = re.sub(r'[，。!\?\-\/\(\)\\]', '', left)
                        right = re.sub(r'[，。!\?\-\/\(\)\\"]', '', right)
                        if left != "" and left not in left_context:
                            left_context.append(left)
                        if right != "" and right not in right_context:
                            right_context.append(right)
            # check context count
            if (len(left_context) >= 3) and (len(right_context) >= 3):
                break  # if reach target, no need open another file

        if len(left_context) >= 3 and len(right_context) >= 3:
            print (term, len(left_context)+len(right_context),end = "\n")
            word_avmorethan3.append([term,len(left_context)+len(right_context)])
            #print(word_avmorethan3)


        #print(term, len(left_context), len(right_context), end="\n")
        #word_processed_by_av.append([term, len(left_context), len(right_context)])
        # print([term,,end='')
        # pass
    with open("../move/result2.txt",'w') as f:
        for item in word_avmorethan3:

            f.write("%s\n"%item)
    f.close()
main('../move/围棋.all_terms','../move/tchunkfile.txt')



