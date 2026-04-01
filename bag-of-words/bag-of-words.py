import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here

        
    vector = []
    
    for v in vocab:
        count = 0
        for t in tokens:
            
            if t == v:
                count += 1
        vector.append(count)
    ans = np.array(vector,dtype=int)
    return ans
    
    pass