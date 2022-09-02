# -*- coding: utf-8 -*-
# +
#import time
#start = time.time()

from .utils import *

#end   = time.time()
#print('Imports                 in {:11.9} Micro Seconds.'.format((end - start)*(10**6)))
# -

def word_recom(query):
    
    try:
        recoms = w2v_model.wv.most_similar(positive = query, topn = 10)
    except:
        recoms = []
    
    words  = [recom[0] for recom in recoms]
    
    return words
