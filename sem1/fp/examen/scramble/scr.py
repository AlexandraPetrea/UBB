
# -*- coding: utf-8 -*-

def scramble(unscrambled):
    ''' 
    Scrambles the word(s) in unscrambled such that the first and last letter remain the same,
    but the inner letters are scrambled. Preserves the punctuation.
    See also: http://science.slashdot.org/story/03/09/15/2227256/can-you-raed-tihs
    '''
    import string, random, re
    splitter = re.compile(r'\s')
    words = splitter.split(u''.join(ch for ch in unscrambled if ch not in set(string.punctuation)))
    for word in words:
        len_ = len(word)
        if len_ < 4: continue
        if len_ == 4:
            scrambled = u'%c%c%c%c' % (word[0], word[2], word[1], word[3])
        else:
            mid = list(word[1:-1])
            random.shuffle(mid)
            scrambled = u'%c%s%c' % (word[0], ''.join(mid), word[-1])
        unscrambled = unscrambled.replace(word, scrambled, 1)
    
    return unscrambled

if __name__ == '__main__':
    print (scramble('Indeed, here be some scrÖmbled words!'))