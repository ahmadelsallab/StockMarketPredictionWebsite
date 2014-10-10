import classify
import sys, json
from xml.dom import minidom

#xmldoc = minidom.parse('/srv/www/htdocs/kalam/Website/xtest.txt.xml')
xmldoc = minidom.parse('xtest.txt.xml')
itemlist = xmldoc.getElementsByTagName('tweet')
tArray=[]
for t in itemlist:
	tArray.append(t.childNodes[0].data)
# filter = Filter()
# Class = filter.Classify("@BinSolaiman مبروك طيبه تم التنبيه عليها من 38.30  تحقق 40.70  كما ذكرت لكم لامفر من الارتداد  افتح المحادثه  #تاسي #طيبه")
# print(Class)

'''
try:
	data=sys.argv[1]
except:
    sys.stdout.write ("ERROR")
    sys.exit(1)
result = classify.Classify(data,'other')
print (json.dumps(result))
'''

result = classify.Classify(tArray,'other')
print (json.dumps(result))
