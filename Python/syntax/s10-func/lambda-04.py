def soundwonder(words, callback):
    for word in words:
        print(callback(word))
        
words = ['hi', 'good', 'oh', 'nice']



soundwonder(words, lambda word : word.capitalize() + "!!!")