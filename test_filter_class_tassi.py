import classify
import sys, json

# filter = Filter()
# Class = filter.Classify("@BinSolaiman مبروك طيبه تم التنبيه عليها من 38.30  تحقق 40.70  كما ذكرت لكم لامفر من الارتداد  افتح المحادثه  #تاسي #طيبه")
# print(Class)

from xml.dom import minidom
#xmldoc = minidom.parse('/srv/www/htdocs/kalam/Website/xtest.txt.xml')
xmldoc = minidom.parse('xtest.txt.xml')
itemlist = xmldoc.getElementsByTagName('tweet')

'''
try:
	data=sys.argv[1]
except:
    sys.stdout.write ("ERROR")
    sys.exit(1)
result = classify.Classify(data,'Tasi')
print (json.dumps(result))
'''

tArray=[]
for t in itemlist:
	tArray.append(t.childNodes[0].data)
print(len(tArray))
result = classify.Classify(tArray,'Tasi')
print (json.dumps(result))
