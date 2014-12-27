"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django_ajax.decorators import ajax
from app.models import Tweet, CorrectionData, StocksPrices
from django.utils import timezone
from Filter.Filter import Filter
from bs4 import BeautifulSoup
import urllib
import json
from TwitterCrawler.TwitterCrawler import *
import os

synonyms = {'استثمار': 'البنك السعودي للاستثمار',
'السعودى الهولندى': 'البنك السعودي الهولندي',
'السعودى الفرنسى': 'البنك السعودي الفرنسي',
'ساب': 'ساب للتكافل',
'العربى الوطنى': 'البنك العربي الوطني',
'سامبا': 'مجموعة سامبا المالية',
'تاسي': 'تاسي',
'الرياض': 'بنك الرياض',
'الجزيرة': 'شركة الجزيرة تكافل تعاوني',
'الراجحي': 'مصرف الراجحي',
'البلاد': 'بنك البلاد',
'الإنماء': 'مصرف الإنماء',
'كيمانول': 'شركة تكوين المتطورة للصناعات',
'بتروكيم ': 'شركة الصحراء للبتروكيماويات',
'سابك': 'شركة الصناعات الكيميائية الأساسية',
'سافكو': 'مجموعة أسترا الصناعية',
'التصنيع': 'شركة مجموعة السريع التجارية الصناعية',
'اللجين': 'شركة الحسن غازي إبراهيم شاكر',
'نماء للكيماويات': 'شركة نماء للكيماويات',
'المجموعة السعودية': 'المجموعة السعودية للإستثمار الصناعي',
'الصحراء للبتروكيماويات': 'شركة الصحراء للبتروكيماويات',
'ينساب': 'ينساب',
'أسمنت حائل': 'شركة أسمنت حائل',
'أسمنت نجران ': 'شركة أسمنت نجران',
'اسمنت المدينة ': 'شركة اسمنت المدينة',
'اسمنت الشمالية ': 'شركة أسمنت المنطقة الشمالية',
'الاسمنت العربية ': 'شركة الاسمنت العربية',
'اسمنت اليمامة ': 'شركة اسمنت اليمامة',
'اسمنت السعوديه ': 'شركة الأسمنت السعودية',
'اسمنت القصيم ': 'شركة اسمنت القصيم',
'اسمنت الجنوبيه ': 'شركة اسمنت المنطقة الجنوبيه',
'اسمنت ينبع': 'شركة اسمنت ينبع',
'اسمنت الشرقية ': 'شركة اسمنت المنطقة الشرقية',
'اسمنت تبوك ': 'شركة اسمنت تبوك',
'اسمنت الجوف ': 'شركة اسمنت الجوف',
'أسواق ع العثيم ': 'شركة أسواق عبدالله العثيم',
'المواساة': 'شركة المواساة للخدمات الطبية',
'إكسترا': '',
'دله الصحية': 'شركة دله للخدمات الصحية القابضة',
'رعاية': 'الشركة الوطنية للرعاية الطبية',
'ساسكو': 'ساسكو',
'ثمار': 'ثمار',
'مجموعة فتيحي ': 'مجموعة فتيحي القابضة',
'جرير': 'شركة جرير للتسويق',
'الدريس': 'شركة الدريس للخدمات البترولية و النقليات',
'الحكير': 'شركة فواز عبدالعزيز الحكير وشركاه',
'الخليج للتدريب ': 'شركة الخليج للتدريب و التعليم',
'الغاز والتصنيع ': 'شركة الغاز والتصنيع الاهلية',
'كهرباء السعودية ': 'الشركة السعودية للكهرباء',
'مجموعة صافولا': 'مجموعة صافولا',
'الغذائية': 'الغذائية',
'سدافكو': 'الشركة السعودية لمنتجات الألبان والأغذية (سدافكو)',
'المراعي': 'شركة المراعي',
'أنعام القابضة ': 'شركة مجموعة أنعام الدولية القابضة',
'حلواني إخوان': 'حلواني إخوان',
'هرفي للأغذية': 'شركة هرفي للخدمات الغذائية',
'التموين': 'شركة الخطوط السعودية للتموين',
'نادك': 'الشركة الوطنية للتنمية الزراعية',
'القصيم الزراعيه': 'شركة القصيم الزراعية',
'تبوك الزراعيه ': 'شركة تبوك للتنمية الزراعية',
'الأسماك': 'الشركة السعودية للأسماك',
'الشرقية للتنمية ': 'الشركة الشرقية للتنمية',
'الجوف الزراعيه': 'شركة الجوف الزراعية',
'بيشة الزراعيه': 'شركة بيشة للتنمية الزراعية',
'جازان للتنمية': 'شركة جازان للتنمية',
'الاتصالات': 'شركة الاتصالات السعودية',
'اتحاد اتصالات': 'شركة إتحاد إتصالات',
'زين السعودية': 'شركة الاتصالات المتنقلة السعودية',
'عذيب للاتصالات': 'شركة إتحاد عذيب للاتصالات',
'المتكاملة': 'الشركة السعودية للإتصالات المتكاملة',
'التعاونية ': 'شركة التعاونية للتأمين',
'ملاذ للتأمين': 'ملاذ للتأمين',
'ميدغلف للتأمين': 'ميدغلف للتأمين',
'أليانز إس إف ': 'أليانز إس إف',
'سلامة': 'شركة سلامة للتأمين التعاوني',
'ولاء للتأمين': 'ولاء للتأمين',
'الدرع العربي ': 'شركة الدرع العربي للتأمين التعاوني',
'ساب تكافل': 'ساب للتكافل',
'سند': 'شركة سند للتأمين و إعادة التأمين التعاوني',
'سايكو': 'الشركة العربية السعودية للتأمين التعاوني',
'وفا للتأمين': 'وفا للتأمين',
'إتحاد الخليج': 'شركة إتحاد الخليج للتأمين التعاوني',
'الأهلي للتكافل': 'شركة الأهلي للتكافل',
'الأهلية': 'الشركة الأهلية للتأمين التعاوني',
'أسيج': 'المجموعة المتحدة للتأمين التعاوني',
'التأمين العربية ': 'شركة التأمين العربية التعاونية',
'الاتحاد التجاري ': 'شركة الاتحاد التجاري للتأمين التعاوني',
'الصقر للتأمين ': 'شركة الصقر للتأمين التعاوني',
'المتحدة للتأمين ': 'المجموعة المتحدة للتأمين التعاوني',
'الإعادة السعودية ': 'الشركة السعودية لإعادة التأمين(إعادة) التعاونية',
'بوبا العربية ': 'بوبا العربية للتأمين التعاوني',
'وقاية للتكافل': 'شركة وقاية للتأمين و إعادة التأمين التكافلي',
'تكافل الراجحي ': 'شركة الراجحي للتأمين التعاوني',
'ايس': 'شركة أيس العربية للتأمين التعاوني',
'اكسا- التعاونية': 'شركة اكسا للتأمين التعاوني',
'الخليجية العامة': 'الشركة الخليجية العامة للتأمين التعاوني',
' بروج للتأمين': 'شركة بروج للتأمين التعاوني',
'العالمية': 'شركة العالمية للتأمين التعاوني',
'سوليدرتي تكافل': 'شركة سوليدرتي السعودية للتكافل',
'الوطنية': 'الشركة الوطنية للتأمين',
'أمانة للتأمين': 'شركة أمانة للتأمين التعاوني',
'عناية': 'شركة عناية السعودية للتأمين التعاوني',
'الإنماء طوكيو مارين': 'شركة الإنماء طوكيو مارين',
'المصافي': 'شركة المصافي العربية السعودية',
'المتطورة': 'الشركة السعودية للصناعات المتطورة',
'الاحساء للتنميه': 'شركة الاحساء للتنمية',
'سيسكو': 'سيسكو',
'عسير': 'شركة عسير للتجارة والسياحة والصناعة',
'الباحة': 'شركة الباحة للإستثمار والتنمية',
'المملكة': 'شركة المملكة القابضة',
'تكوين': 'شركة تكوين المتطورة للصناعات',
'بى سى آى': 'ى سى آى',
'معادن': 'شركة التعدين العربية السعودية',
'أسترا الصناعية': 'مجموعة أسترا الصناعية',
'مجموعة السريع': 'شركة مجموعة السريع التجارية الصناعية',
'شاكر': 'شركة الحسن غازي إبراهيم شاكر',
'الدوائية': 'الشركة السعودية للصناعات الدوائية والمستلزمات الطبية',
'زجاج': 'شركة الصناعات الزجاجية الوطنية',
'فيبكو': 'فيبكو',
'معدنية': 'معدنية',
'الكيميائيه السعوديه': 'الشركة الكيميائية السعودية',
'صناعة الورق': 'الشركة السعودية لصناعة الورق',
'العبداللطيف': 'شركة العبداللطيف للاستثمار الصناعي',
'الصادرات': 'الشركة السعودية للصادرات الصناعية',
'أسلاك': 'شركة إتحاد مصانع الأسلاك',
'مجموعة المعجل': 'شركة مجموعة محمد المعجل',
'الأنابيب السعودية': 'الشركة السعودية لأنابيب الصلب',
'الخضري': 'شركة أبناء عبدالله عبدالمحسن الخضري',
'الخزف': 'شركة الخزف السعودي',
'الجبس': 'شركة الجبس الأهلية',
'الكابلات': 'شركة الكابلات السعودية',
'صدق': 'صدق',
'اميانتيت': 'شركة اميانتيت العربية السعودية',
'أنابيب': 'أنابيب',
'الزامل للصناعة': 'شركة الزامل للاستثمار الصناعي',
'البابطين': 'شركة البابطين للطاقة و الاتصالات',
'الفخارية': 'الشركة السعودية لإنتاج الأنابيب الفخارية',
'مسك': 'مسك',
'البحر الأحمر': 'البحر الأحمر',
'العقارية': 'العقارية',
'طيبة للاستثمار ': 'طيبة للاستثمار',
'مكة للانشاء': 'مكة للانشاء',
'التعمير': 'التعمير',
'إعمار': 'إعمار',
'جبل عمر': 'جبل عمر',
'دار الأركان': 'دار الأركان',
'مدينة المعرفة ': 'مدينة المعرفة',
'البحري': 'البحري',
'النقل الجماعي': 'النقل الجماعي',
'مبرد': 'مبرد',
'بدجت السعودية': 'بدجت السعودية',
'تهامه للاعلان': 'تهامه للاعلان',
'الأبحاث و التسويق': 'الأبحاث و التسويق',
'طباعة وتغليف': 'طباعة وتغليف',
'الطيار': 'الطيار',
'الفنادق': 'الفنادق',
'شمس': 'شمس',
}

stocks_prices = {};

stock_prices_names_mapping_tbl = {'﻿تاسي':'تاسي',
'الرياض':'الرياض',
'الجزيرة':'الجزيرة',
'استثمار':'استثمار',
'السعودي الهولندي':'السعودي الهولندي',
'السعودي الفرنسي':'السعودي الفرنسي',
'ساب':'سـاب',
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

    try:
        urlstr = 'http://www.tadawul.com.sa/Resources/Reports/DailyList_ar.html'
        stock = stock_prices_names_mapping_tbl[stock]
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
        
def index(request):
    """Renders the home page."""
    if 'message' in request.session:
        message = request.session['message']
        del request.session['message']
    if 'error' in request.session:
        message = request.session['error']
        del request.session['error']

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'message': message if 'message' in locals() else "",
            'error': message if 'error' in locals() else "",
        })
    )

#@login_required
def home(request):
    '''
    from twython import Twython
    global twitter
    twitter = Twython("MGMeNEK5bEqADjJRDJmQ8Yy1f", "eVR1kjrTdHPEiFuLoAEA6pPGSnuZ1NnAa1EwtqBi4wVA1tbRHo", "91079548-uhlRrwtgVQcavlf3lv4Dy1ZFCq5CXvBQFvc5A1l0n", "V6vLsqzqrdfs2YX4I1NVG2gP845gjTrBSDNxHVz496g66")
    '''
    
    # Start the TwitterCrawler      
    PROJECT_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    configFileCrawler = os.path.join(PROJECT_DIR, 'TwitterCrawler','Configurations', 'Configurations.xml')
    global twitterCrawler
    twitterCrawler = TwitterCrawler(configFileCrawler, None, None, None)
    #results = twitterCrawler.SearchQueryAPI(query, -1, -1)
    '''
    for stock in synonyms:
        price = get_stock_price(stock)
        stocks_prices[stock] = price
        stock_price_db = StocksPrices(stock_name=stock, stock_price = price) # CHECK: Needs migration
        stock_price_db.save()
    '''
    return render(
        request,
        'app/home.html',
        context_instance = RequestContext(request,
        {
            'title':'Home',
            #'tweets': tweets,
        })
    )

#@login_required
@ajax
def get_tweets(request):
    stock_name = request.POST['query']
    content_return = {}
    #query = stock_name
    #query = synonyms[query]
    query = stock_name + " AND (سهم OR اسهم OR أسهم OR تداول OR ارتفع OR ارتفاع OR انخفض OR انخفاض OR هدف OR دعم OR ارتداد OR نسبة OR % OR %)‎"
    
    '''
    #tweets = twitter.search(q= query + 'OR ' + synonyms[query], result_type='recent')
    try:
        tweets = twitter.search(q=query, result_type='recent')
    except:
        from twython import Twython
        twitter = Twython("MGMeNEK5bEqADjJRDJmQ8Yy1f", "eVR1kjrTdHPEiFuLoAEA6pPGSnuZ1NnAa1EwtqBi4wVA1tbRHo", "91079548-uhlRrwtgVQcavlf3lv4Dy1ZFCq5CXvBQFvc5A1l0n", "V6vLsqzqrdfs2YX4I1NVG2gP845gjTrBSDNxHVz496g66")
        tweets = twitter.search(q=query, result_type='recent')
    '''
    
    try:
        tweets = twitterCrawler.SearchQueryAPI(query, -1, -1)
    except:        
        PROJECT_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
        configFileCrawler = os.path.join(PROJECT_DIR, 'TwitterCrawler','Configurations', 'Configurations.xml')
        twitterCrawler = TwitterCrawler(configFileCrawler, None, None, None)
        tweets = twitterCrawler.SearchQueryAPI(query, -1, -1)
        
    #twittes['price'] = stocks_prices[query] # CHECK: Get from DB?--> use the next line then. You might need migration of DB to update MySQL tables
    price = get_stock_price(stock_name)
    
    try:
        stock_price_db = StocksPrices.objects.get(stock_name=stock_name)
        if(price == 0.0):
            price = stock_price_db.stock_price
        else:
            stock_price_db.stock_price = price
        
    except:
        stock_price_db = StocksPrices(stock_name=stock_name, stock_price=price) # CHECK: Needs migration    
        
    content_return['price'] = price
    stock_price_db.save()
    #tweets['price'] = CorrectionData.objects.get(stock_name=query)
    for tweet in tweets:
        tweet_exist = Tweet.objects.filter(twitter_id=tweet['id_str']);
        if(len(tweet_exist) == 0):
            try:
                item = Tweet()
                item.twitter_id = tweet['id_str']
                item.user_id = tweet['user']['id']
                item.text = tweet['text']
                item.created_at = tweet['created_at']
                item.user_followers_count = tweet['user']['followers_count']
                item.user_profile_image_url = tweet['user']['profile_image_url']
                item.pub_date = str(timezone.now())
                item.stock = stock_name
                item.labeled = False
                item.save()
                item.relevancy = 'none'
                item.sentiment = 'none'
            except Exception as e: 
              pass
    
    tweetes_to_render = Tweet.objects.filter(stock=stock_name, labeled = False).values();
    #my_list = list(tweetes_to_render)
    #print(json.dumps(my_list[0]))
    
    content_return['statuses'] = tweetes_to_render
    
    # Fill in total number of entries in DB for this stock
    # Full DB
    content_return['total_entries_in_DB'] = len(Tweet.objects.all())
    content_return['total_labeled_entries_in_DB'] = len(Tweet.objects.filter(labeled = True))
    content_return['total_relevant_labeled_entries_in_DB'] = len(Tweet.objects.filter(relevancy = 'relevant'))
    content_return['total_irrelevant_labeled_entries_in_DB'] = len(Tweet.objects.filter(relevancy = 'irrelevant'))
    content_return['total_positive_labeled_entries_in_DB'] = len(Tweet.objects.filter(sentiment = 'positive'))
    content_return['total_negative_labeled_entries_in_DB'] = len(Tweet.objects.filter(sentiment = 'negative'))
    content_return['total_neutral_labeled_entries_in_DB'] = len(Tweet.objects.filter(sentiment = 'neutral'))
    
    # Stock DB
    content_return['stock_entries_in_DB'] = len(Tweet.objects.filter(stock=stock_name))
    content_return['stock_labeled_entries_in_DB'] = len(Tweet.objects.filter(stock=stock_name, labeled = True))
    content_return['stock_relevant_labeled_entries_in_DB'] = len(Tweet.objects.filter(stock=stock_name, relevancy = 'relevant'))
    content_return['stock_irrelevant_labeled_entries_in_DB'] = len(Tweet.objects.filter(stock=stock_name, relevancy = 'irrelevant'))
    content_return['stock_positive_labeled_entries_in_DB'] = len(Tweet.objects.filter(stock=stock_name, sentiment = 'positive'))
    content_return['stock_negative_labeled_entries_in_DB'] = len(Tweet.objects.filter(stock=stock_name, sentiment = 'negative'))
    content_return['stock_neutral_labeled_entries_in_DB'] = len(Tweet.objects.filter(stock=stock_name, sentiment = 'neutral'))

    return content_return 

@ajax
def get_correction(request):
    relevancy = request.POST['relevancy']
    sentiment = request.POST['sentiment']
    tweet_id = request.POST['tweet_id']
    stock = request.POST['stock']
    #print(tweet_id)
    
    
    try:
        tweet = Tweet.objects.filter(twitter_id=tweet_id)[0]
        if(relevancy == 'none'):
            tweet.sentiment = sentiment
            #print('Sentiment')
        elif (sentiment == 'none'):
            tweet.relevancy = relevancy
            #print('Relevance')
        if(((tweet.relevancy != 'none') & (tweet.relevancy != '')) & ((tweet.sentiment != 'none') & (tweet.sentiment != ''))):
            tweet.labeled = True
            
        tweet.save()
        
                    
    except Exception as e:
        print('Unexpected error')

    
    #tweet.save()
    
    #retrain()
    
def correction_sentiment(request):
    relevancy = request.POST['relevancy']
    sentiment = request.POST['sentiment']
    text = request.POST['text']
    stock = request.POST['stock']
    
    try:
        correctionData = CorrectionData.objects.get(text=text)
        correctionData.relevancy = relevancy
    except:
        correctionData = CorrectionData(text=text,relevancy=relevancy,sentiment='neutral',stock=stock)

    
    correctionData.save()
    
   
        
def retrain():
    correctionData = CorrectionData.objects.all()
    trainSet= []
    for item in correctionData:
        trainSet.append({'label' : item.relevancy, 'text' :item.text })

    filter = Filter(r"C:\Users\Tarek Abdelhakim\workspace\DjangoWebProject1",item.stock.strip(),True)
    filter.GetBestClassifier(trainSet)
    
@login_required
def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

@login_required
def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

def login_user(request):

    if request.method == 'POST':
        #logout(request)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/home')
                #return HttpResponseRedirect('/about/')
    return redirect('/')

def register(request):
    
    if request.method == 'POST':
        from app.forms import UserForm
        user_form = UserForm(data=request.POST)

        if user_form.is_valid() :
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            request.session['message'] = 'registration done please login'
            return redirect("/")
            #return render(request, 'app/site_layout.html', {'message':'registration done please login'})
        else:
            request.session['error'] = user_form.errors
            return redirect("/")
           #return render(request, 'app/site_layout.html', {'error':user_form.errors})

