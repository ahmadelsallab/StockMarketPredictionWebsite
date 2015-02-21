'''
Created on Dec 27, 2014

@author: Ahmad
'''
'''
Created on Dec 11, 2014

@author: asallab
'''

import os
from bs4 import BeautifulSoup
import urllib
os.environ["DJANGO_SETTINGS_MODULE"] = "DjangoWebProject1.settings"
#print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx")
#print(os.environ.get("DJANGO_SETTINGS_MODULE"))
stock_prices_names_mapping_tbl = {'﻿تاسي':'تاسي',
'الرياض':'الرياض',
'الجزيرة':'الجزيرة',
'استثمار':'استثمار',
'السعودي الهولندي':'السعودي الهولندي',
'السعودي الفرنسي':'السعودي الفرنسي',
'سـاب':'سـاب',
'العربي الوطني': 'العربي',
'سامبا':'سامبا',
'الراجحي':'الراجحي',
'البلاد':'البلاد',
'الإنماء':'الإنماء',
'كيمانول':'كيمانول',
'بتروكيم':'بتروكيم',
'سابك':'سابك',
'سافكو':'سافكو',
'التصنيع':'التصنيع',
'اللجين':'اللجين',
'نماء للكيماويات':'نماء للكيماويات',
'المجموعة السعودية':'المجموعة السعودية',
'الصحراء للبتروكيماويات': 'الصحراء',
'ينساب':'ينساب',
'سبكيم العالمية':'سبكيم العالمية',
'المتقدمة':'المتقدمة',
'كيان': 'كيان السعودية',
'بترو رابغ':'بترو رابغ',
'أسمنت حائل': 'اسمنت حائل',
'أسمنت نجران': 'اسمنت نجران',
'اسمنت المدينة':'اسمنت المدينة',
'اسمنت الشمالية':'اسمنت الشمالية',
'الاسمنت العربية':'الاسمنت العربية',
'اسمنت اليمامة':'اسمنت اليمامة',
'اسمنت السعوديه':'اسمنت السعوديه',
'اسمنت القصيم':'اسمنت القصيم',
'اسمنت الجنوبيه':'اسمنت الجنوبيه',
'اسمنت ينبع':'اسمنت ينبع',
'اسمنت الشرقية':'اسمنت الشرقية',
'اسمنت تبوك':'اسمنت تبوك',
'اسمنت الجوف':'اسمنت الجوف',
'أسواق ع العثيم':'أسواق ع العثيم',
'المواساة':'المواساة',
'إكسترا':'إكسترا',
'دله الصحية':'دله الصحية',
'رعاية':'رعاية',
'ساسكو':'ساسكو',
'ثمار':'ثمار',
'مجموعة فتيحي':'مجموعة فتيحي',
'جرير':'جرير',
'الدريس':'الدريس',
'الحكير':'الحكير',
'الخليج للتدريب':'الخليج للتدريب',
'الغاز والتصنيع':'الغاز',
'كهرباء السعودية':'كهرباء السعودية',
'مجموعة صافولا': 'صافولا',
'الغذائية':'الغذائية',
'سدافكو':'سدافكو',
'المراعي':'المراعي',
'أنعام القابضة':'أنعام القابضة',
'حلواني إخوان':'حلواني إخوان',
'هرفي للأغذية':'هرفي للأغذية',
'التموين':'التموين',
'نادك':'نادك',
'القصيم الزراعيه':'القصيم الزراعيه',
'تبوك الزراعيه':'تبوك الزراعيه',
'الأسماك':'الأسماك',
'الشرقية للتنمية':'الشرقية للتنمية',
'الجوف الزراعيه': 'الجوف',
'بيشة الزراعيه':'بيشة',
'جازان للتنمية':'جازان للتنمية',
'الاتصالات':'الاتصالات',
'اتحاد اتصالات': 'اتحاد اتصالات',
'زين السعودية':'زين السعودية',
'عذيب للاتصالات':'عذيب للاتصالات',
'المتكاملة':'المتكاملة',
'التعاونية':'التعاونية',
'ملاذ للتأمين':'ملاذ للتأمين',
'ميدغلف للتأمين':'ميدغلف للتأمين',
'أليانز إس إف':'أليانز إس إف',
'سلامة':'سلامة',
'ولاء للتأمين':'ولاء للتأمين',
'الدرع العربي':'الدرع العربي',
'ساب تكافل':'ساب تكافل',
'سند':'سند',
'سايكو':'سايكو',
'وفا للتأمين':'وفا للتأمين',
'إتحاد الخليج':'إتحاد الخليج',
'الأهلي للتكافل':'الأهلي للتكافل',
'الأهلية':'الأهلية',
'أسيج':'أسيج',
'التأمين العربية':'التأمين العربية',
'الاتحاد التجاري':'الاتحاد التجاري',
'الصقر للتأمين':'الصقر للتأمين',
'المتحدة للتأمين':'المتحدة للتأمين',
'الإعادة السعودية':'الإعادة السعودية',
'بوبا العربية':'بوبا العربية',
'وقاية للتكافل':'وقاية للتكافل',
'تكافل الراجحي':'تكافل الراجحي',
'ايس':'ايس',
'اكسا- التعاونية':'اكسا- التعاونية',
'الخليجية العامة':'الخليجية العامة',
'بروج للتأمين':'بروج للتأمين',
'العالمية':'العالمية',
'سوليدرتي تكافل':'سوليدرتي تكافل',
'الوطنية':'الوطنية',
'أمانة للتأمين':'أمانة للتأمين',
'عناية':'عناية',
'الإنماء طوكيو م':'الإنماء طوكيو م',
'المصافي':'المصافي',
'المتطورة':'المتطورة',
'الاحساء للتنميه':'الاحساء للتنميه',
'سيسكو':'سيسكو',
'عسير':'عسير',
'الباحة':'الباحة',
'المملكة':'المملكة',
'تكوين':'تكوين',
'بى سى آى':'بى سى آى',
'معادن':'معادن',
'أسترا الصناعية':'أسترا الصناعية',
'مجموعة السريع':'مجموعة السريع',
'شاكر':'شاكر',
'الدوائية':'الدوائية',
'زجاج':'زجاج',
'فيبكو':'فيبكو',
'معدنية':'معدنية',
'الكيميائيه السعوديه':'الكيميائيه السعوديه',
'صناعة الورق':'صناعة الورق',
'العبداللطيف':'العبداللطيف',
'الصادرات':'الصادرات',
'أسلاك':'أسلاك',
'مجموعة المعجل':'مجموعة المعجل',
'الأنابيب السعودية':'انابيب السعودية',
'الخضري':'الخضري',
'الخزف':'الخزف السعودي',
'الجبس':'الجبس',
'الكابلات':'الكابلات',
'صدق':'صدق',
'اميانتيت':'اميانتيت',
'أنابيب':'أنابيب',
'الزامل للصناعة':'الزامل للصناعة',
'البابطين':'البابطين',
'الفخارية':'الفخارية',
'مسك':'مسك',
'البحر الأحمر':'البحر الأحمر',
'العقارية':'العقارية',
'طيبة للاستثمار':'طيبة',
'مكة للانشاء':'مكة',
'التعمير':'التعمير',
'إعمار':'إعمار',
'جبل عمر':'جبل عمر',
'دار الأركان':'دار الأركان',
'مدينة المعرفة':'مدينة المعرفة',
'البحري':'البحري',
'النقل الجماعي':'النقل الجماعي',
'مبرد':'مبرد',
'بدجت السعودية':'بدجت السعودية',
'تهامه للاعلان':'تهامه للاعلان',
'الأبحاث و التسويق':'الأبحاث و التسويق',
'طباعة وتغليف':'طباعة وتغليف',
'الطيار':'الطيار',
'الفنادق':'الفنادق',
'شمس':'شمس',
}
def isNumber(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
def get_stock_price(stock):
    urlstr = 'http://www.tadawul.com.sa/Resources/Reports/DailyList_ar.html'
    stock = stock_prices_names_mapping_tbl[stock]
    try:
        
        fileHandle = urllib.request.urlopen(urlstr)
        
        html = fileHandle.read()
        soup = BeautifulSoup(html)
        price = 0.0
        #for b in soup.findAll('div'):
        for b in soup.findAll('tr'):
            td_list= b.findAll('td')
            if(len(td_list) != 0):
                div_list = td_list[0].findAll('div', { "class" : "left-text portlet-padding-5" })
                if(len(div_list) != 0):
                    stock_in_website = div_list[0].text.strip()
                    #stock_in_website.replace('*', '').strip()
                    #if (stock in stock_in_website) | (stock_in_website in stock):
                    if (stock == stock_in_website):
                        try:
                            price = float(td_list[4].text)
                            if(isNumber(price)):                
                                #print('Stock: ' + stock + ' Price: ' + str(price))
                                return price
                                
                        except:
                            continue
                            #print('Not price, skip ' + td_list[1].text)
                            #return ''   
        return 0.0                 
    except Exception as e:
        print('URL error ' + str(e) )
        return 0.0 
     

from TwitterCrawler.TwitterCrawler import TwitterCrawler
PROJECT_DIR = os.path.dirname(__file__)
configFileName = os.path.join(PROJECT_DIR, 'TwitterCrawler', 'Configurations', 'Configurations.xml')
updateRateFileName = 'update_rate.txt'
f_in = open(os.path.join('.', 'TwitterCrawler', 'stocks.txt'), 'r', encoding='utf-8')
lines = f_in.readlines()
stock_prices = []
for line in lines:
    stock = line.strip()
    print('<li>' + stock + '</li>')  
for line in lines:            
    stock = line.strip()
    #twitterCrawler.Crawl("q")
    #print('Stock: ' + stock + ' Price:' + str(get_stock_price(stock)))
    price = get_stock_price(stock)
    stock_prices.append({'name':stock, 'price':price})
    if(price != 0.0):
        #print("'" + stock + "'" + ':' + "'" + stock + "',")
        print("'" + stock + "'" + ':' + "'" + stock + "'," + "Price: " + str(price))
    else:
        #print("'" + stock + "'" + ':,')
        print("'" + stock + "'" + ':,' + "Price: " + str(price))
        
for stock_name in stock_prices:
    print('Stock: ' + stock_name['name'] + ' Price:' + str(stock_name['price']))         
          