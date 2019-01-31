Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> animal_detail = 'E:\zool.csv'
>>> animal_detail
'E:\\zool.csv'
>>> animal = 'E:\zool.csv'
>>> animal_detail = pd.read_csv(animal, delimiter=',')
>>> animal_detail
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
>>> animal.count()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    animal.count()
TypeError: count() takes at least 1 argument (0 given)
>>> animal_detail.count()
animal        22
uniq_id       22
water_need    22
dtype: int64
>>> # the above statement counts the total number of rows in the dataframe
>>> # the below statement sums the total amount of water the animals need
>>> animal_detail['water_need'].sum()
7650
>>> # it does not output the name of the column. This works similar like below
>>> animal_detail.water_need.sum()
7650
>>> #when we want to output column name we use double square brackets [[]] like below
>>> animal_detail[['water_need']].sum()
water_need    7650
dtype: int64
>>> # let us calculate the minumum and maximum values of water needed
>>> animal_detail[['water_need']].min()
water_need    80
dtype: int64
>>> # let us calculate the minumum and maximum values of water needed (Maximum)
>>> animal_detail[['water_need']].max()
water_need    600
dtype: int64
>>> #let us get the animal with the largest water need
>>> animal_detail[['animal', 'water_need']].max()
animal        zebra
water_need      600
dtype: object
>>> #let us get the animal with the minimum water need
>>> animal_detail[['animal', 'water_need']].min()
animal        elephant
water_need          80
dtype: object
>>> # if you look keenly you realise we have lost track. The two most recent statements above do not give us waht we want. We can solve this by boolean statements like below now that we know the maximum and min water_need:
>>> animal_detail[animal_detail.water_need == 600][['animal', 'uniq_id', 'water_need']]
      animal  uniq_id  water_need
1   elephant     1002         600
16      lion     1017         600
>>> animal_detail[animal_detail.water_need == 80][['animal', 'uniq_id', 'water_need']]
   animal  uniq_id  water_need
14  zebra     1015          80
>>> # let us find the mean and median of the dataset that we have above
>>> #let us calculate the mean of water_need (statistical averages)
>>> animal_detail[['water_need']].mean()
water_need    347.727273
dtype: float64
>>> #let us calculate the median of water_need (statistical median)
>>> animal_detail[['water_need']].median()
water_need    325.0
dtype: float64
>>> # let us find the animals that fall below the average water_need (mean)
>>> animal_detail[animal_detail.water_need <= 347.727273][['animal', 'uniq_id', 'water_need']]
   animal  uniq_id  water_need
3   tiger     1004         300
4   tiger     1005         320
5   tiger     1006         330
6   tiger     1007         290
7   tiger     1008         310
8   zebra     1009         200
9   zebra     1010         220
10  zebra     1011         240
11  zebra     1012         230
12  zebra     1013         220
13  zebra     1014         100
14  zebra     1015          80
>>> # capturing the float value of the mean value is hectic. We could assign it to a variable that is easy to reference. Like below
>>> water_need_mean = animal_detail[['water_need']].mean()
>>> # the reference it like this
>>> animal_detail[animal_detail.water_need <= water_need_mean][['animal', 'uniq_id', 'water_need']]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    animal_detail[animal_detail.water_need <= water_need_mean][['animal', 'uniq_id', 'water_need']]
  File "C:\Users\James_Magabe\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\core\ops.py", line 1190, in wrapper
    raise ValueError("Can only compare identically-labeled "
ValueError: Can only compare identically-labeled Series objects
>>> water_need_mean
		     
water_need    347.727273
dtype: float64
>>> # error arises becuase our variable contains values (key/value pair)yet we wanted to reference the integer value alone. Now lets try this and see
		     
>>> water_need
		     
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    water_need
NameError: name 'water_need' is not defined
>>> water_need_mean = animal_detail.water_need.mean()
		     
>>> animal_detail[animal_detail.water_need <= water_need_mean][['animal', 'uniq_id', 'water_need']]
		     
   animal  uniq_id  water_need
3   tiger     1004         300
4   tiger     1005         320
5   tiger     1006         330
6   tiger     1007         290
7   tiger     1008         310
8   zebra     1009         200
9   zebra     1010         220
10  zebra     1011         240
11  zebra     1012         230
12  zebra     1013         220
13  zebra     1014         100
14  zebra     1015          80
>>> #yes it has worked. HOORAY!
		     
>>> 
