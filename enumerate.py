'''
THIS IS enumerate examples****
it allows us to loop over something and have an automatic counter
'''


c = ['banana', 'apple', 'pear', 'orange']
for index, item in enumerate(c, 2):  # '2' tell the enumerate to start counting from 2
    print(index, item)
	
'''
[CONSOLE]
2 banana
3 apple
4 pear
5 orange
'''