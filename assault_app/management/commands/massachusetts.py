### Didn't work

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
                
            url = 'http://www.thecrimson.com/search/?cx=013815813102981840311%3Aaw6l9tjs1a0&cof=FORID%3A10&ie=UTF-8&q=sexual+assault&sa=' # write the url here
            usock = urllib2.urlopen(url)
            html_data = usock.read()
            usock.close()
            #print html_data
                
            soup = BeautifulSoup(html_data)

            #Find the div that all of the articles live in for the given url
            story_content = str(soup.find_all('div', attrs={'class': 'gsc-result'}));
 
            print story_content
            school_stories = Schools.objects.get(name='Harvard College')
            school_stories.content = story_content
            school_stories.save(update_fields=['content'])
                
        except Schools.DoesNotExist:
            raise CommandError('didn\'t work')

        self.stdout.write("end of scrape.py")
