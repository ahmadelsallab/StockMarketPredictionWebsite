import classify
import sys, json

# filter = Filter()
# Class = filter.Classify("@BinSolaiman مبروك طيبه تم التنبيه عليها من 38.30  تحقق 40.70  كما ذكرت لكم لامفر من الارتداد  افتح المحادثه  #تاسي #طيبه")
# print(Class)


try:
	data=sys.argv[1]
except:
    sys.stdout.write ("ERROR")
    sys.exit(1)
result = classify.Classify(data,'Tasi')
print (json.dumps(result))
