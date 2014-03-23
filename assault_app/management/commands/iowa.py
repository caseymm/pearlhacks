#!/usr/bin/env python
from django.core.management.base import BaseCommand, CommandError
#from django.db.models import F
from bs4 import BeautifulSoup
from assault_app.models import Schools
#import string
import urllib2
import re

class Command(BaseCommand):
    args = '<url>'
    help = 'Parses and imports latest data'
    
    
    def handle(self, *args, **options):
        try:
            self.stdout.write("scraping stories")
                
            url = 'http://www.google.com/cse?cx=partner-pub-5821368584002875%3A6dpyr5-d3wu&ie=ISO-8859-1&q=sexual+assault&sa=Search&siteurl=www.dailyiowan.com%2F&ref=&ss=2576j545536j14#gsc.tab=0&gsc.q=sexual assault&gsc.page=1' # write the url here
            usock = urllib2.urlopen(url)
            html_data = usock.read()
            usock.close()
            #print html_data
                
            soup = BeautifulSoup(html_data)

            #Find the div that all of the articles live in for the given url
            story_content = str(soup.find_all('table', attrs={'class': 'gsc-table-result'}));
 
            print story_content
            school_stories = Schools.objects.get(name='University of Iowa')
            school_stories.content = story_content
            school_stories.save(update_fields=['content'])
                
        except Schools.DoesNotExist:
            raise CommandError('didn\'t work')

        self.stdout.write("end of scrape.py")
