import pandas as pd
import math

input_filename = 'conll2003.csv'
output_filename = 'conll2003.conll'
input_data = pd.read_csv(input_filename)

with open(output_filename, 'w') as output_file:
    #previous_sentence_num = 0
    previous_sentence_num = 1
    word_record = zip(input_data['Word'],
                      input_data['Pos'],
                      input_data['class'],
                      input_data['sentence_code'])
    for word, pos, label, sentence_num in word_record:
        #print(word, pos, label, sentence_num)
        if previous_sentence_num == sentence_num:
            output_file.write('{word} {pos} {deprel} {label}\n'
                              .format(word=word,
                                      pos=pos,
                                      deprel='_',
                                      label=label))
        else:
            output_file.write('\n')
            previous_sentence_num = sentence_num

        





