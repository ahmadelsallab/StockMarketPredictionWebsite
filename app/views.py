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
from app.models import Opinion, CorrectionData, StocksPrices, LabledCounter, StockCounter, RelevancyCounter, SentimentCounter
from django.utils import timezone
from Filter.Filter import Filter
from bs4 import BeautifulSoup
from django.db.models import Sum
import urllib
import json
from TwitterCrawler.TwitterCrawler import *
import os
import threading
import django_crontab
#from pytz import timezone
from dateutil.parser import parse

synonyms = {'استثمار': 'البنك السعودي للاستثمار',
'السعودى الهولندى': 'البنك السعودي الهولندي',
'السعودى الفرنسى': 'البنك السعودي الفرنسي',
'ساب': 'ساب للتكافل',
'العربى الوطنى': 'البنك العربي الوطني',
'سامبا': 'مجموعة سامبا المالية',
'تاسي': 'تاسي',
'الرياض': 'بنك الرياض',
'الجزيرة': 'بنك الجزيرة',
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
'اسمنت ام القرى': 'شركة اسمنت ام القرى',
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
'أسواق المزرعة': 'الشركة السعودية للتسويق',
'ساسكو': 'ساسكو',
'ثمار': 'ثمار',
'مجموعة فتيحي ': 'مجموعة فتيحي القابضة',
'جرير': 'شركة جرير للتسويق',
'الدريس': 'شركة الدريس للخدمات البترولية و النقليات',
'الحكير': 'شركة فواز عبدالعزيز الحكير وشركاه',
'الحمادي':'شركة الحمادي للتنمية والاستثمار',
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
'جزيرة تكافل':'شركة الجزيرة تكافل تعاوني',
'الدرع العربي ': 'شركة الدرع العربي للتأمين التعاوني',
'ساب تكافل': 'ساب للتكافل',
'سند': 'شركة سند للتأمين و إعادة التأمين التعاوني',
'سايكو': 'الشركة العربية السعودية للتأمين التعاوني',
'وفا للتأمين': 'وفا للتأمين',
'إتحاد الخليج': 'شركة إتحاد الخليج للتأمين التعاوني',
'الأهلي للتكافل': 'شركة الأهلي للتكافل',
'العربي للتأمين': 'شركة متلايف وايه أي جي والبنك العربي للتأمين التعاوني',
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
'دور': 'دور',
'شمس': 'شمس',
'مجموعة الحكير': 'مجموعة الحكير',
'بوان': 'بوان',
'الشرق الاوسط لصناعه':'شركة الشرق الاوسط لصناعة وانتاج الورق',
}



price_mapping={
'الرياض' : 'الرياض',
'الجزيرة' : 'الجزيرة',
'استثمار': 'استثمار',
'سعودي هولندي': 'السعودي الهولندي',
'السعودي الفرنسي': 'السعودي الفرنسي',
'ساب': 'ساب',
'العربي': 'العربي الوطني',
'سامبا': 'سامبا',
'الراجحي': 'الراجحي',
'البلاد' : 'البلاد',
'الإنماء': 'الإنماء',
'كيمانول': 'كيمانول',
'بتروكيم': 'بتروكيم',
'سابك': 'سابك',
'سافكو': 'سافكو',
'التصنيع': 'التصنيع',
'اللجين': 'اللجين',
'نماء للكيماويات': 'نماء للكيماويات',
'مجموعة السعودية': 'المجموعة السعودية',
'البتروكيماويات': 'الصحراء للبتروكيماويات',
'ينساب': 'ينساب',
'سبكيم العالمية': 'سبكيم العالمية',
'المتقدمة': 'المتقدمة',
'كيان السعودية': 'كيان',
'بترو رابغ': 'بترو رابغ',
'اسمنت حائل': 'أسمنت حائل',
'اسمنت نجران': 'أسمنت نجران',
'اسمنت المدينة': 'اسمنت المدينة',
'اسمنت الشمالية': 'اسمنت الشمالية',
'ﺎﺴﻤﻨﺗ ﺎﻣ ﺎﻠﻗﺭﻯ':'ﺎﺴﻤﻨﺗ ﺎﻣ ﺎﻠﻗﺭﻯ',
'اسمنت العربية': 'الاسمنت العربية',
'اسمنت اليمامة': 'اسمنت اليمامة',
'اسمنت ام القرى': 'اسمنت ام القرى',
'الأسمنت السعودي': 'اسمنت السعوديه',
'اسمنت القصيم': 'اسمنت القصيم',
'اسمنت الجنوب': 'اسمنت الجنوبيه',
'س ينبع': 'اسمنت ينبع',
'اسمنت الشرقية': 'اسمنت الشرقية',
'س تبوك': 'اسمنت تبوك',
'اسمنت الجوف': 'اسمنت الجوف',
'أسواق ع العثيم': 'أسواق ع العثيم',
'ﺎﻠﺤﻣﺍﺪﻳ':'ﺎﻠﺤﻣﺍﺪﻳ',
'المواساة': 'المواساة',
'إكسترا': 'إكسترا',
'دله الصحية': 'دله الصحية',
'رعاية': 'رعاية',
'أسواق المزرعة':'أسواق المزرعة',
'ساسكو': 'ساسكو',
'ثمار': 'ثمار',
'مجموعة فتيحي': 'مجموعة فتيحي',
'جرير': 'جرير',
'الدريس': 'الدريس',
'الحكير': 'الحكير',
'الحمادي':'الحمادي',
'الخليج للتدريب': 'الخليج للتدريب',
'الغاز': 'الغاز والتصنيع',
'كهرباء السعودية': 'كهرباء السعودية',
'صافولا': 'مجموعة صافولا',
'وفرة': 'الغذائية',
'سدافكو': 'سدافكو',
'المراعي': 'المراعي',
'أنعام القابضة': 'أنعام القابضة',
'حلواني إخوان': 'حلواني إخوان',
'هرفي للأغذية': 'هرفي للأغذية',
'التموين': 'التموين',
'نادك': 'نادك',
'جاكو': 'القصيم الزراعيه',
'تبوك الزراعية': 'تبوك الزراعيه',
'الأسماك': 'الأسماك',
'الشرقية للتنمية': 'الشرقية للتنمية',
'الجوف': 'الجوف الزراعيه',
'بيشة': 'بيشة الزراعيه',
'جازادكو': 'جازان للتنمية',
'الاتصالات': 'الاتصالات',
'إتحاد إتصالات': 'اتحاد اتصالات',
'زين السعودية': 'زين السعودية',
'عذيب للاتصالات': 'عذيب للاتصالات',
'المتكاملة': 'المتكاملة',
'التعاونية': 'التعاونية',
'ملاذ للتأمين': 'ملاذ للتأمين',
'العربي للتأمين':'العربي للتأمين',
'ميدغلف للتأمين': 'ميدغلف للتأمين',
'أليانز إس إف': 'أليانز إس إف',
'سلامة': 'سلامة',
'ولاء': 'ولاء للتأمين',
'جزيرة تكافل':'جزيرة تكافل',
'الدرع العربي': 'الدرع العربي',
'ساب تكافل': 'ساب تكافل',
'سند': 'سند',
'سايكو': 'سايكو',
'وفا للتأمين': 'وفا للتأمين',
'إتحاد الخليج': 'إتحاد الخليج',
'الأهلي للتكافل': 'الأهلي للتكافل',
'ﺎﻠﻋﺮﺒﻳ ﻞﻠﺗﺄﻤﻴﻧ':'ﺎﻠﻋﺮﺒﻳ ﻞﻠﺗﺄﻤﻴﻧ',
'الأهلية': 'الأهلية',
'أسيج': 'أسيج',
'التأمين العربية': 'التأمين العربية',
'الاتحاد التجاري': 'الاتحاد التجاري',
'الصقر للتأمين': 'الصقر للتأمين',
'المتحدة للتأمين': 'المتحدة للتأمين',
'الإعادة السعودية': 'الإعادة السعودية',
'بوبا العربية': 'بوبا العربية',
'وقاية للتكافل': 'وقاية للتكافل',
'تكافل الراجحي': 'تكافل الراجحي',
'ايس': 'ايس',
'اكسا- التعاونية': 'اكسا- التعاونية',
'الخليجية العامة': 'الخليجية العامة',
'بروج للتأمين': 'بروج للتأمين',
'العالمية': 'العالمية',
'سوليدرتي تكافل': 'سوليدرتي تكافل',
'الوطنية': 'الوطنية',
'أمانة للتأمين': 'أمانة للتأمين',
'عناية': 'عناية',
'الإنماء طوكيو م': 'الإنماء طوكيو م',
'المصافي': 'المصافي',
'متطورة': 'المتطورة',
'الاحساء': 'الاحساء للتنميه',
'سيسكو': 'سيسكو',
'عسير': 'عسير',
'الباحة': 'الباحة',
'المملكة': 'المملكة',
'تكوين': 'تكوين',
'بى سى آى': 'بى سى آى',
'معادن': 'معادن',
'أسترا الصناعية': 'أسترا الصناعية',
'مجموعة السريع': 'مجموعة السريع',
'شاكر': 'شاكر',
'الدوائية': 'الدوائية',
'زجاج': 'زجاج',
'فيبكو': 'فيبكو',
'معدنية': 'معدنية',
'الكيميائية': 'الكيميائيه السعوديه',
'صناعة الورق': 'صناعة الورق',
'العبداللطيف': 'العبداللطيف',
'صادرات': 'الصادرات',
'أسلاك': 'أسلاك',
'مجموعة المعجل': 'مجموعة المعجل',
'انابيب السعودية': 'الأنابيب السعودية',
'الخضري': 'الخضري',
'الخزف السعودي': 'الخزف',
'جبسكو': 'الجبس',
'الكابلات': 'الكابلات',
'صدق': 'صدق',
'اميانتيت': 'اميانتيت',
'أنابيب': 'أنابيب',
'الزامل للصناعة': 'الزامل للصناعة',
'البابطين': 'البابطين',
'الفخارية': 'الفخارية',
'مسك': 'مسك',
'البحر الأحمر': 'البحر الأحمر',
'العقارية': 'العقارية',
'طيبة': 'طيبة للاستثمار',
'مكة': 'مكة للانشاء',
'التعمير': 'التعمير',
'إعمار': 'إعمار',
'جبل عمر': 'جبل عمر',
'دار الأركان': 'دار الأركان',
'مدينة المعرفة': 'مدينة المعرفة',
'البحري': 'البحري',
'الجماعي': 'النقل الجماعي',
'مبرد': 'مبرد',
'بدجت السعودية': 'بدجت السعودية',
'تهامه': 'تهامه للاعلان',
'الأبحاث و التسويق': 'الأبحاث و التسويق',
'طباعة وتغليف': 'طباعة وتغليف',
'الطيار': 'الطيار',
'دور': 'دور',
'شمس': 'شمس',
'الاهلي' : 'البنك الأهلي',
'صناعات كهربائية': 'الصناعلات الكهرائيه',
'بوان': 'بوان',
'مجموعة الحكير': 'مجموعة الحكير',
'الشرق الاوسط لصناعه': 'none',
'HSBC Saudi 20': 'none',
'Falcom 30': 'none',
'Falcom petrochemical': 'none',
}


class NewsItem:
    title = ""
    link = ""
    pubDate = ""
    
def isNumber(value):
    try:
        float(value)
        return True
    except ValueError:
        return False 
    
    
    
def get_stock_price(stock):
    try:
        urlstr = 'http://www.marketstoday.net/markets/%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D8%A9/Companies/1/ar/'
        fileHandle = urllib.request.urlopen(urlstr)
        html = fileHandle.read()
        soup = BeautifulSoup(html)
        price = 0
        for b in soup.findAll('tr', attrs={'class':'symbolflip'})[1:]:
            if ""+price_mapping[stock]+"" == ""+b.find('a', attrs={'class':'jTip'}).text+"":
                return ""+b.findAll('td')[2].text+""
                break
    except Exception as e:
        print('URL error ' + str(e) )
        return 0
        
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
    naughty_words=" AND ( -ﺰﺑ -ﻂﻳﺯ -ﻂﻴﻇ -ﺲﻜﺳ -ﺲﻜﺴﻳ -ﺲﺣﺎﻗ -ﺞﻨﺳ -ﻦﻴﻛ -ﺞﻨﺳ -ﺏﺯ -ﺏﺯﺍﺯ -ﻚﺳ -ﻒﺤﻟ -ﻒﺣﻮﻠﻫ -ﺬﺑ )"
    query = stock_name + " AND (سهم OR اسهم OR أسهم OR تداول OR ارتفع OR ارتفاع OR انخفض OR انخفاض OR هدف OR دعم OR ارتداد OR نسبة OR % OR %)" + naughty_words
    #query = stock_name 
    
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
        
    # Get the stock price
    try:
                
        stock_price_db_all = StocksPrices.objects.filter(stock_name=stock_name).order_by(time_stamp)
        stock_price_db = stock_price_db_all[0]
        
        
    except:
        # No entry yet in the DB for this stock, create new record
        stock_price_db = StocksPrices(stock_name=stock_name, stock_price=price)
        # Get the price from the market now
        stock_price_db.stock_price = get_stock_price(stock_name)    
        stock_price_db.time_stamp = datetime.datetime.now()
        
    content_return['price'] = stock_price_db.stock_price
    
    stock_price_db.save()
    #tweets['price'] = CorrectionData.objects.get(stock_name=query)
    for tweet in tweets:
        tweet_exist = Opinion.objects.filter(twitter_id=tweet['id_str']);
        if(len(tweet_exist) == 0):
            try:
                item = Opinion()
                item.twitter_id = tweet['id_str']
                item.user_id = tweet['user']['id']
                item.text = tweet['text']
                item.created_at = tweet['created_at']
                item.user_followers_count = tweet['user']['followers_count']
                item.user_profile_image_url = tweet['user']['profile_image_url']
                item.media_url = tweet['entities']
                item.tweeter_sname = tweet['user']['screen_name']
                item.tweeter_name = tweet['user']['name']
                #print('kkkkkkk'+str(tweet['entities']))
                item.pub_date = str(timezone.now())
                item.stock = stock_name
                item.labeled = False
                item.source = "twitter.com"
                item.save()
                item.relevancy = 'none'
                item.sentiment = 'none'
                item.labeled_user = 'none'
            except Exception as e: 
              pass
    
    tweetes_to_render_temp = Opinion.objects.filter(stock=stock_name, labeled = False).values();
    tweetes_to_render = sorted(tweetes_to_render_temp, key=lambda x: time.strptime(x['created_at'],'%a %b %d %X %z %Y'), reverse=True)[0:50];
    #tweetes_to_render = sorted(tweetes_to_render_temp, key=lambda x: time.strptime(x['created_at'],'%a %b %d %X %z %Y'), reverse=True);
    #my_list = list(tweetes_to_render)
    #print(json.dumps(my_list[0]))
    #tweetes_to_render_temp = Opview.objects.filter(stock=stock_name, labeled = False).values();
    #tweetes_to_render = sorted(tweetes_to_render_temp, key=lambda x: time.strptime(x['created_at'],'%a %b %d %X %z %Y'), reverse=True);

    #prevent Duplicate 
    tweets_dict = {}
    tweets_dict[''] = ''
    i = 1
    x = 0
    while x < len(tweetes_to_render):
        tweet_render=tweetes_to_render[x];
        if tweet_render.get('text').strip() in tweets_dict.keys():
            tweet = Opinion.objects.filter(twitter_id=tweet_render.get('twitter_id'))[0]
            tweet.similarId = tweets_dict[tweet_render['text']]
            tweet.save()
            tweetes_to_render.pop(x); 
            if (len(tweetes_to_render_temp) > len(tweetes_to_render)+1):
                tweetes_to_render.append(tweetes_to_render_temp[len(tweetes_to_render)+i])
                i=i+1
        elif(tweet_render.get('labeled_user') == request.user.username):
            x=x+1
            tweetes_to_render.remove(tweet_render)
            if (len(tweetes_to_render_temp) > len(tweetes_to_render)+1):
                tweetes_to_render.append(tweetes_to_render_temp[len(tweetes_to_render)+i])
                i=i+1
        else:
            x=x+1
            tweets_dict[tweet_render.get('text').strip()] = tweet_render.get('twitter_id')

    content_return['statuses'] = tweetes_to_render

    # Fill in total number of entries in DB for this stock
    # Full DB
    content_return['total_entries_in_DB'] = StockCounter.objects.aggregate(Sum('counter'))['counter__sum']
    content_return['total_labeled_entries_in_DB'] = LabledCounter.objects.aggregate(Sum('counter'))['counter__sum']
    content_return['total_relevant_labeled_entries_in_DB'] = RelevancyCounter.objects.extra(where={"`relevancy` = 'relevant' "}).aggregate(Sum('counter'))['counter__sum']
    content_return['total_irrelevant_labeled_entries_in_DB'] = RelevancyCounter.objects.extra(where={"`relevancy` = 'irrelevant' "}).aggregate(Sum('counter'))['counter__sum']
    content_return['total_positive_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`sentiment` = 'positive' "}).aggregate(Sum('counter'))['counter__sum']
    content_return['total_negative_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`sentiment` = 'negative' "}).aggregate(Sum('counter'))['counter__sum']
    content_return['total_neutral_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`sentiment` = 'neutral' "}).aggregate(Sum('counter'))['counter__sum']

    # Stock DB
    try:
        content_return['stock_entries_in_DB'] = StockCounter.objects.extra(where={"`stock` = '"+stock_name+"' "}).values()[0]['counter']
    except:
        content_return['stock_entries_in_DB'] = 0
    try:
        content_return['stock_labeled_entries_in_DB'] = LabledCounter.objects.extra(where={"`stock` = '"+stock_name+"' "}).values()[0]['counter']
    except:
        content_return['stock_labeled_entries_in_DB'] = 0
    try:
        content_return['stock_relevant_labeled_entries_in_DB'] = RelevancyCounter.objects.extra(where={"`stock` = '"+stock_name+"' and `relevancy` = 'relevant' "}).values()[0]['counter']
    except:
        content_return['stock_relevant_labeled_entries_in_DB'] = 0
    try:
        content_return['stock_irrelevant_labeled_entries_in_DB'] = RelevancyCounter.objects.extra(where={"`stock` = '"+stock_name+"' and `relevancy` = 'irrelevant' "}).values()[0]['counter']
    except:
        content_return['stock_irrelevant_labeled_entries_in_DB'] = 0
    try:
        content_return['stock_positive_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`stock` = '"+stock_name+"' and `sentiment` = 'positive' "}).values()[0]['counter']
    except:
        content_return['stock_positive_labeled_entries_in_DB'] = 0
    try:
        content_return['stock_negative_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`stock` = '"+stock_name+"' and `sentiment` = 'negative' "}).values()[0]['counter']
    except:
        content_return['stock_negative_labeled_entries_in_DB'] = 0
    try:
        content_return['stock_neutral_labeled_entries_in_DB'] = SentimentCounter.objects.extra(where={"`stock` = '"+stock_name+"' and `sentiment` = 'neutral' "}).values()[0]['counter']
    except:
        content_return['stock_neutral_labeled_entries_in_DB'] = 0
 
    return content_return 

def getSimilarlabeling():
    duplicate_tweetes = Opinion.objects.exclude(similarId='').values();
    for tweet in duplicate_tweetes:
        parent_tweet =  Opinion.objects.filter(twitter_id = tweet.get("similarId"))
        tweet["voted_relevancy"] = parent_tweet.parent_tweet
        tweet["voted_sentiment"] = parent_tweet.voted_sentiment
        tweet.save()

@ajax
def get_correction(request):
    relevancy = request.POST['relevancy']
    sentiment = request.POST['sentiment']
    tweet_id = request.POST['tweet_id']
    stock = request.POST['stock']
    #print(tweet_id)
    
    try:
        tweet = Opinion.objects.filter(twitter_id=tweet_id)[0]
        if(relevancy == 'none'):
            if(tweet.sentiment == 'none' or tweet.sentiment == ''):
                tweet.sentiment = sentiment
                tweet.voted_sentiment = sentiment
            elif(tweet.sentiment_second == 'none' or tweet.sentiment_second == ''):
                tweet.sentiment_second = sentiment
                if(tweet.sentiment == tweet.sentiment_second):
                    tweet.voted_sentiment = sentiment
            elif(tweet.sentiment_third == 'none' or tweet.sentiment_third == ''):
                tweet.sentiment_third = sentiment
                if(tweet.voted_sentiment == 'none' or tweet.voted_sentiment ==''):
                    if(sentiment == tweet.sentiment):
                        tweet.voted_sentiment = sentiment
                    elif(sentiment == tweet.sentiment_second):
                        tweet.voted_sentiment = sentiment
                    else:
                        tweet.voted_sentiment = 'none'

            #print('Sentiment')
        elif (sentiment == 'none'):
            if(tweet.relevancy == 'none' or tweet.relevancy == ''):
                tweet.relevancy = relevancy
                if request.user.is_authenticated():
                    tweet.labeled_user = request.user.username
            elif(tweet.relevancy_second == 'none' or tweet.relevancy_second == ''):
                tweet.relevancy_second = relevancy
                if request.user.is_authenticated():
                    tweet.labeled_user_second = request.user.username
            elif(tweet.relevancy_third == 'none' or tweet.relevancy_third == ''):
                tweet.relevancy_third = relevancy
                if request.user.is_authenticated():
                    tweet.labeled_user_third = request.user.username
            #print('Relevance')

        if(((tweet.relevancy != 'none') & (tweet.relevancy != '')) & ((tweet.sentiment != 'none') & (tweet.sentiment != ''))
            & ((tweet.relevancy_second != 'none') & (tweet.relevancy_second != '')) & ((tweet.sentiment_second != 'none') & (tweet.sentiment_second != ''))
            & ((tweet.relevancy_third != 'none') & (tweet.relevancy_third != '')) & ((tweet.sentiment_third != 'none') & (tweet.sentiment_third != ''))):
            tweet.labeled = True
            x = 0
            y = 0
            z = 0
            if(tweet.relevancy == 'relevant'):
                x = 1
            if(tweet.relevancy_second == 'relevant' ):
                y = 1
            if(tweet.relevancy_third == 'relevant' ):
                z = 1
            tweet.voted_relevancy = ((x & y) | (x & z) | (y & z))
            #print(tweet.votel_relevancy)
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
def news(request):
    #Select Today's News 
    from django.utils import timezone
    today =datetime.datetime.strftime(timezone.now(),"%Y-%m-%d")
    newsList=Opinion.objects.extra(where={"`pub_date` LIKE CONCAT(  '%%',  '"+today+"',  '%%' ) and `source` != 'twitter.com' "}).values()
    
    News =[]
    for newsItem in newsList:
        n=NewsItem()
        n.link = newsItem['source']
        n.title = newsItem['text']
        News.append(n)
    """Renders the news page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/news.html',
        context_instance = RequestContext(request,
        {
            'title':'News',
            'News':News,
        })
    )


def runPriceCrawling():
    urlstr = 'http://www.marketstoday.net/markets/%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D8%A9/Companies/1/ar/'
    fileHandle = urllib.request.urlopen(urlstr)
    html = fileHandle.read()
    soup = BeautifulSoup(html)
    #print(soup)
    from pytz import timezone 
    localtz = timezone('UTC')
    time_in_site=localtz.localize(parse(soup.findAll('span', attrs={'class':'tradhour'})[0].text.split('\n', 1)[1].split(" :")[1].replace('(local time)\r\n','',1)));
    for b in soup.findAll('tr', attrs={'class':'symbolflip'})[1:]:
        stockname=b.find('a', attrs={'class':'jTip'}).text
        price=b.findAll('td')[2].text
        #print(price_mapping[stockname])
        #print(price)
        item = StocksPrices()
        item.stock_name=price_mapping[stockname]
        item.stock_price=price
        item.time=time_in_site
        item.save()
    return True

def runNewsCrawling():
    rssPage = urllib.request.urlopen('http://www.cma.org.sa/Ar/News/_layouts/listfeed.aspx?List=%7B0622219A-483C-46C4-A066-AA4EDEDD0952%7D')
    rssFeed = minidom.parse(rssPage)

    for item in rssFeed.getElementsByTagName("item"):
        Op = Opinion()
        for a in item.getElementsByTagName("link"):
            Op.source=a.childNodes[1].nodeValue        
        for a in item.getElementsByTagName("title"):
            Op.text=a.childNodes[1].nodeValue
        #for a in item.getElementsByTagName("pubDate"):
        #    Op.pub_date=a.childNodes[0].nodeValue
        Op.pub_date= str(datetime.datetime.utcnow())
        Op.twitter_id = str(datetime.datetime.utcnow())
        Op.user_id = 'none'
        Op.created_at = 'none'
        Op.user_followers_count = 0
        Op.user_profile_image_url = 'none'
        Op.media_url= 'none'
        Op.stock = 'none'
        Op.labeled = False
        Op.relevancy = 'none'
        Op.sentiment = 'none'
        Op.labeled_user= 'none'
        Op.save()
    #Time by seconds
    threading.Timer(86400.0, runNewsCrawling).start()
    #threading.Timer(60.0, runNewsCrawling).start()

#Crawl the News every 24 hours
runNewsCrawling()


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
            'year':datetime.datetime.now().year,
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
            'year':datetime.datetime.now().year,
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

