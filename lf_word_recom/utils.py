# -*- coding: utf-8 -*-
# +
#import time
#start  = time.time()

import os
import time
import gensim

#end  = time.time()
#print('Imports                 in {:11.9} Micro Seconds.'.format((end - start)*(10**6)))


# +
# start  = time.time()

data_path = f'{os.path.dirname(os.path.abspath(__file__))}/data'

w2v_model = gensim.models.Word2Vec.load(f'{data_path}/w2v/w2v.model')

# end  = time.time()
# print('Read Model & Stop Words in {:11.9} Micro Seconds.'.format((end - start)*(10**6)))
