'''
Created on Oct 2, 2013

@author: ASALLAB
'''
f_in = open('stocks.txt', 'r', encoding='utf-8')
f_out = open('stocks.xml', 'w', encoding='utf-8')
f_out_1 = open('stocks_array.txt', 'w', encoding='utf-8')
lines = f_in.readlines()
for line in lines:
    f_out.write('     <Word name="' + line.strip() + '"></Word>\n')
    f_out_1.write('"' + line.strip() + '",\n')
f_in.close()
f_out.close()
f_out_1.close()