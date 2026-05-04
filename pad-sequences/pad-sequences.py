import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):

    
    if len(seqs) == 0:
        return np.array([])

    
    if max_len is None:
        max_len = 0
        for seq in seqs:
            if len(seq) > max_len:
                max_len = len(seq)

    
    result = []

    
    for seq in seqs:
        new_seq = []


        for num in seq:
            new_seq.append(num)


        while len(new_seq) < max_len:
            new_seq.append(pad_value)

 
        if len(new_seq) > max_len:
            new_seq = new_seq[:max_len]

        result.append(new_seq)


    return np.array(result)