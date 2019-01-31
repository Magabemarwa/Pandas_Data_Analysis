Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> zoo = "E:\animal.csv"
>>> pd.read_csv(zoo, delimiter=',')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    pd.read_csv(zoo, delimiter=',')
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\parsers.py", line 678, in parser_f
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\parsers.py", line 440, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\parsers.py", line 787, in __init__
    self._make_engine(self.engine)
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\parsers.py", line 1014, in _make_engine
    self._engine = CParserWrapper(self.f, **self.options)
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\parsers.py", line 1708, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas\_libs\parsers.pyx", line 384, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas\_libs\parsers.pyx", line 695, in pandas._libs.parsers.TextReader._setup_parser_source
FileNotFoundError: File b'E:\x07nimal.csv' does not exist
>>> phone = 'E:\phone.csv'
>>> pd.read_csv(phone. delimiter=',')
SyntaxError: keyword can't be an expression
>>> pd.read_csv(phone, delimiter=',')
             phone
0    2547163992345
1   71639949145678
2        716399492
3        716399493
4        716399494
5        716399495
6        716399496
7        716399497
8        716399498
9        716399499
10       716399493
11       716399495
12       716399496
13       716399497
14        97865789
15       712345678
>>> pd.read_csv(zoo, dilimiter=',')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    pd.read_csv(zoo, dilimiter=',')
TypeError: parser_f() got an unexpected keyword argument 'dilimiter'
>>> pd.read_csv(zoo, delimiter=',')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    pd.read_csv(zoo, delimiter=',')
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\parsers.py", line 678, in parser_f
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\parsers.py", line 440, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\parsers.py", line 787, in __init__
    self._make_engine(self.engine)
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\parsers.py", line 1014, in _make_engine
    self._engine = CParserWrapper(self.f, **self.options)
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\parsers.py", line 1708, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas\_libs\parsers.pyx", line 384, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas\_libs\parsers.pyx", line 695, in pandas._libs.parsers.TextReader._setup_parser_source
FileNotFoundError: File b'E:\x07nimal.csv' does not exist
>>> zoo = 'E:\animal.csv'
>>> pd.read_csv(zoo, delimiter=',')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    pd.read_csv(zoo, delimiter=',')
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\parsers.py", line 678, in parser_f
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\parsers.py", line 440, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\parsers.py", line 787, in __init__
    self._make_engine(self.engine)
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\parsers.py", line 1014, in _make_engine
    self._engine = CParserWrapper(self.f, **self.options)
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\parsers.py", line 1708, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas\_libs\parsers.pyx", line 384, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas\_libs\parsers.pyx", line 695, in pandas._libs.parsers.TextReader._setup_parser_source
FileNotFoundError: File b'E:\x07nimal.csv' does not exist
>>> print(zoo)
E:nimal.csv
>>> clear()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    clear()
NameError: name 'clear' is not defined
>>> animal = 'E:\zoo.csv'
>>> pd.read_csv(animal, delimiter=',')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    pd.read_csv(animal, delimiter=',')
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\parsers.py", line 678, in parser_f
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\parsers.py", line 440, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\parsers.py", line 787, in __init__
    self._make_engine(self.engine)
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\parsers.py", line 1014, in _make_engine
    self._engine = CParserWrapper(self.f, **self.options)
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\parsers.py", line 1708, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas\_libs\parsers.pyx", line 384, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas\_libs\parsers.pyx", line 695, in pandas._libs.parsers.TextReader._setup_parser_source
FileNotFoundError: File b'E:\\zoo.csv' does not exist
>>> animal = 'E:\zool.csv'
>>> pd.read_csv(animal, delimiter=',')
      animal  uniq_id  water_need
0   elephant     1001         500
1   elephant     1002         600
2   elephant     1003         550
3      tiger     1004         300
4      tiger     1005         320
5      tiger     1006         330
6      tiger     1007         290
7      tiger     1008         310
8      zebra     1009         200
9      zebra     1010         220
10     zebra     1011         240
11     zebra     1012         230
12     zebra     1013         220
13     zebra     1014         100
14     zebra     1015          80
15      lion     1016         420
16      lion     1017         600
17      lion     1018         500
18      lion     1019         390
19  kangaroo     1020         410
20  kangaroo     1021         430
21  kangaroo     1022         410
>>> animal_detail = pd.read_csv(animal, delimiter=',')
>>> print(animal_detail)
      animal  uniq_id  water_need
0   elephant     1001         500
1   elephant     1002         600
2   elephant     1003         550
3      tiger     1004         300
4      tiger     1005         320
5      tiger     1006         330
6      tiger     1007         290
7      tiger     1008         310
8      zebra     1009         200
9      zebra     1010         220
10     zebra     1011         240
11     zebra     1012         230
12     zebra     1013         220
13     zebra     1014         100
14     zebra     1015          80
15      lion     1016         420
16      lion     1017         600
17      lion     1018         500
18      lion     1019         390
19  kangaroo     1020         410
20  kangaroo     1021         430
21  kangaroo     1022         410
>>> print(animal_detail['animal', 'water_need')
	  
SyntaxError: invalid syntax
>>> print(animal_detail['animal', 'water_need'])
	  
Traceback (most recent call last):
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\indexes\base.py", line 3078, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('animal', 'water_need')

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(animal_detail['animal', 'water_need'])
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\frame.py", line 2688, in __getitem__
    return self._getitem_column(key)
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\frame.py", line 2695, in _getitem_column
    return self._get_item_cache(key)
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\generic.py", line 2489, in _get_item_cache
    values = self._data.get(item)
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\internals.py", line 4115, in get
    loc = self.items.get_loc(item)
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\indexes\base.py", line 3080, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('animal', 'water_need')
>>> print(animal_detail[['animal', 'water_need']])
	  
      animal  water_need
0   elephant         500
1   elephant         600
2   elephant         550
3      tiger         300
4      tiger         320
5      tiger         330
6      tiger         290
7      tiger         310
8      zebra         200
9      zebra         220
10     zebra         240
11     zebra         230
12     zebra         220
13     zebra         100
14     zebra          80
15      lion         420
16      lion         600
17      lion         500
18      lion         390
19  kangaroo         410
20  kangaroo         430
21  kangaroo         410
>>> animal_detail[['animal', 'water_need']]
	  
      animal  water_need
0   elephant         500
1   elephant         600
2   elephant         550
3      tiger         300
4      tiger         320
5      tiger         330
6      tiger         290
7      tiger         310
8      zebra         200
9      zebra         220
10     zebra         240
11     zebra         230
12     zebra         220
13     zebra         100
14     zebra          80
15      lion         420
16      lion         600
17      lion         500
18      lion         390
19  kangaroo         410
20  kangaroo         430
21  kangaroo         410
>>> animal_detail.head()
	  
     animal  uniq_id  water_need
0  elephant     1001         500
1  elephant     1002         600
2  elephant     1003         550
3     tiger     1004         300
4     tiger     1005         320
>>> animal_detail.head(10)
	  
     animal  uniq_id  water_need
0  elephant     1001         500
1  elephant     1002         600
2  elephant     1003         550
3     tiger     1004         300
4     tiger     1005         320
5     tiger     1006         330
6     tiger     1007         290
7     tiger     1008         310
8     zebra     1009         200
9     zebra     1010         220
>>> animal_detail.animal
	  
0     elephant
1     elephant
2     elephant
3        tiger
4        tiger
5        tiger
6        tiger
7        tiger
8        zebra
9        zebra
10       zebra
11       zebra
12       zebra
13       zebra
14       zebra
15        lion
16        lion
17        lion
18        lion
19    kangaroo
20    kangaroo
21    kangaroo
Name: animal, dtype: object
>>> animal_detail.water_need
	  
0     500
1     600
2     550
3     300
4     320
5     330
6     290
7     310
8     200
9     220
10    240
11    230
12    220
13    100
14     80
15    420
16    600
17    500
18    390
19    410
20    430
21    410
Name: water_need, dtype: int64
>>> animal_detail[animal_detail.water_need == 500]
	  
      animal  uniq_id  water_need
0   elephant     1001         500
17      lion     1018         500
>>> animal_detail[animal_detail.water_need <= 500][['animal', 'uniq_id', 'water_need']].head
	  
<bound method NDFrame.head of       animal  uniq_id  water_need
0   elephant     1001         500
3      tiger     1004         300
4      tiger     1005         320
5      tiger     1006         330
6      tiger     1007         290
7      tiger     1008         310
8      zebra     1009         200
9      zebra     1010         220
10     zebra     1011         240
11     zebra     1012         230
12     zebra     1013         220
13     zebra     1014         100
14     zebra     1015          80
15      lion     1016         420
17      lion     1018         500
18      lion     1019         390
19  kangaroo     1020         410
20  kangaroo     1021         430
21  kangaroo     1022         410>
>>> 
	  


>>> 
	  

>>> animal_detail[animal_detail.water_need <= 500][['animal', 'uniq_id', 'water_need']].head(10)
	  
      animal  uniq_id  water_need
0   elephant     1001         500
3      tiger     1004         300
4      tiger     1005         320
5      tiger     1006         330
6      tiger     1007         290
7      tiger     1008         310
8      zebra     1009         200
9      zebra     1010         220
10     zebra     1011         240
11     zebra     1012         230
>>> animal_detail[animal_detail.water_need >= 500][['animal', 'uniq_id', 'water_need']].head()
	  
      animal  uniq_id  water_need
0   elephant     1001         500
1   elephant     1002         600
2   elephant     1003         550
16      lion     1017         600
17      lion     1018         500
>>> animal_detail[animal_detail.water_need >= 500][['animal', 'uniq_id', 'water_need']].head(10)
	  
      animal  uniq_id  water_need
0   elephant     1001         500
1   elephant     1002         600
2   elephant     1003         550
16      lion     1017         600
17      lion     1018         500
>>> 
