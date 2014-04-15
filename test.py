import math
'''
import re
q = "أحمد عبد"
word = "أحمد1 1 عبد المنعم أحمد أحمد"
q_a = ['a',
       'b',]
if(q in word):
    print(q+"\n")
    # \\b sets word boundaries
print(re.findall('\\b' + q + '\\b', word))
if(re.findall('\\b' + q + '\\b', word).__len__() == 0):
    print('Not found')
#print(re.findall(q , word))
'''
'''
x = 3
for i in range(10):
    print(str(i)+"\n")
    if(i == x):
        break
     
       '''
'''
import openpyxl
from openpyxl import load_workbook  

wb = load_workbook(filename = "C:\\Non_valeo\\Guru_Kalam\\Code\\Kalam\\DatasetBuilder\\Output\\ManualLabels_4.xlsx")

sheet_ranges = wb.get_sheet_by_name(name = 'ManualLabels_4')
sheet_ranges.cell('C1').value = 'xxx'
wb.save("C:\\Non_valeo\\Guru_Kalam\\Code\\Kalam\\DatasetBuilder\\Output\\ManualLabels_4.xlsx")
'''
        
'''
size = 10
start = 0
dataSet = [0,1, 2,3, 4,5, 6,7]
while(start < dataSet.__len__()):
    remaining = dataSet.__len__() - start
    increment = min(size, remaining)
    end = start + increment
    subDataset = dataSet[start : end]
    print("XXX")
    for d in subDataset:
        print(d)
    start += increment
'''

'''
d = {'a':1, 'b':3, 'x': 4, 'd':5}
d1 = d[1:2]
for key, val in d1:# not working
    print("key: " + key + "val: " + val)
'''
'''
d = {}
d['irrel'] = 1
d['rel'] = 2
print(d['rel'])
'''
reqNumRel = 2
reqNumIrrel = 2

numRel = 0
numIrrel = 0

rel = {}
irrel = {}

rel['word_1'] = 50
rel['word_2'] = 5
rel['word_3'] = 5


irrel['word_1'] = 100
irrel['word_5'] = 5
irrel['word_3'] = 5
irrel['word_4'] = 5
irrel['word_7'] = 5



finalModel = {}
for relKey, relFreq in rel.items():
    if not relKey in irrel:
        if(numRel < reqNumRel):
            finalModel[relKey] = relFreq
            numRel += 1
        
for irrelKey, irrelFreq in irrel.items():
    if not irrelKey in rel:
        if(numIrrel < reqNumIrrel):
            finalModel[irrelKey] = irrelFreq
            numIrrel += 1        
print("aa")


print(max(irrel.values()))
print(sum(irrel.values()))

a = [1, 2, 3]
x = 1
if(x in a):
    print("found")

#irrel['word_7']['w'] = 5

print(abs(-5))