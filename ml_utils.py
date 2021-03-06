

def myHotEncode(input_data, max_vocab=0, vocab2idx=None):
    "Return the hot-vecotor and the vocab2idx."

    import numpy as np
    from collections import OrderedDict
    from operator import itemgetter

    if vocab2idx is None:
        vocabFreq = {}
        for i in input_data:
            for j in i:
                if j not in vocabFreq:
                    vocabFreq[j] = 0
                vocabFreq[j] += 1
        vocabFreq = OrderedDict(sorted(vocabFreq.items(), key=itemgetter(1), reverse=True))
        vocab2idx = {}
        count = 0
        for v in vocabFreq:
            count += 1
            if max_vocab > 0 and count > max_vocab:
                break
            vocab2idx[v] = len(vocab2idx)
    vocabEmbeddings = np.identity(len(vocab2idx), dtype='float32')
    data_ret = []
    for i in input_data:
        i_ = []
        for j in i:
            if j in vocab2idx:
                i_.append(vocabEmbeddings[vocab2idx[j]])
        if len(i_) == 0:
            i_ = np.zeros((1, len(vocab2idx)))
        data_ret.append(sum(i_))
    return data_ret, vocab2idx


def myHotDecode(input_data, vocab2idx):
    "Return the decode as final representation and decode as indexs"

    data_ = []
    data_idx = []
    for i in input_data:
        i_ = []
        i_idx = []
        if len(i) != len(vocab2idx):
            print('Erro:', 'The vocab2idx not fit the input data!')
            return
        for _i, j in enumerate(i):
            if j > 0:
                v = [k for k in vocab2idx if vocab2idx[k]==_i][0]
                i_.append(v)
                i_idx.append(_i)
        data_.append(i_)
        data_idx.append(i_idx)
    return data_, data_idx


def text_to_wordEmbedding(text, wordEmbedding):
    import nltk
    import numpy as np
    if type(text) != str:
        ret = []
        for text_ in text:
            text_ = str(text_)
            in_tokens = np.array([token for token in nltk.tokenize.word_tokenize(text_) if token in wordEmbedding])
            if len(in_tokens) > 0:
                ret.append(sum(wordEmbedding[in_tokens]))
            else:
                ret.append(np.zeros(wordEmbedding.vector_size))
        return ret
    in_tokens = [token for token in nltk.tokenize.word_tokenize(text) if token in wordEmbedding]
    if len(in_tokens) > 0:
        return sum(wordEmbedding[in_tokens])
    else:
        return np.zeros(wordEmbedding.vector_size)
