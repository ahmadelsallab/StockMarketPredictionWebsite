from datetime import datetime
from app.models import Stocks, Opinion, Tweeter
from django.utils import timezone
from Filter.Filter import Filter
import threading, time
import datetime
import unicodedata
import os

import django
django.setup()


from twython import Twython
twitter = Twython("MGMeNEK5bEqADjJRDJmQ8Yy1f", "eVR1kjrTdHPEiFuLoAEA6pPGSnuZ1NnAa1EwtqBi4wVA1tbRHo", "91079548-uhlRrwtgVQcavlf3lv4Dy1ZFCq5CXvBQFvc5A1l0n", "V6vLsqzqrdfs2YX4I1NVG2gP845gjTrBSDNxHVz496g66")

que = 'يتشميستشم تيس تويت تاسي'
twittes = twitter.search(q=que, result_type='recent', show_all_inline_media='true')
print(twittes['statuses'][0])
