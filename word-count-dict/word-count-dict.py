def word_count_dict(sentences):
    ans = {}
    
    for sent in sentences:
        for word in sent:
            if word in ans:
                ans[word] += 1
            else:
                ans[word] = 1
    
    return ans