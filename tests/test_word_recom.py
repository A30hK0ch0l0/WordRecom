# -*- coding: utf-8 -*-
# +
import pandas as pd
import os

#import inspect
#import sys

#currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
#parentdir = os.path.dirname(currentdir)
#sys.path.insert(0, parentdir) 

from lf_word_recom import word_recom


# -

def test_pickle():
    
    queries = '''
                 پوشاک کلمه ارسال ماسک ماست دایرکت لایحه نانو انرژی فوتبال هدفون
                 سرمایه خاشقچی مرغ بنیاد خندوانه هندوانه خودرو گردشگری رهبری قالیباف
                 اصفهان دیتاک خرگوش دیجیکالا تلگرام معلم نوروز محرم فطر پروتکل کرونا
              '''
    
    list = queries.split()
    list.sort()
    
    output = pd.DataFrame(index = list)
    
    result = [word_recom(query) for query in list]
    
    output['recommendations'] = result
    
    data_path = f'{os.path.dirname(os.path.abspath(__file__))}/'
    
    #output.to_pickle(f'{data_path}test.pickle')
    
    test = pd.read_pickle(f'{data_path}test.pickle')
    
    assert((output['recommendations'].apply(lambda l: sorted(l)) ==
              test['recommendations'].apply(lambda l: sorted(l))).all())
