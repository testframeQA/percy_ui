import time
from percy import percy_snapshot
import csv
import os

class Helpers:

    def get_data():
        site_data = os.getenv('site')
        if site_data == 'TFQ' or 'TestFrameQA':
            percy_test_file = 'src/tests/test_data/test_data_4wp.csv'
        elif site_data == 'BaseSite':
            percy_test_file = 'src/tests/test_data/test_data_4wd.csv'
        test_file = percy_test_file
        percy_snapshot = 'URL', 'SnapTitle'
        
        with open(test_file, 'r') as file:
            reader = csv.DictReader(file, delimiter=',')
            next(reader, None)
            for row in reader:
                yield row
        
    def gotoURL(self, gotoURL):
        if 'uat' in str(self.baseurl):
            self.driver.get(self.basicauth)
        else:
            pass
        self.driver.get(self.baseurl + gotoURL)
    
    def page_scroller(self):
        sleeptime = 2
        time.sleep(sleeptime)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleeptime)
        
    def percy_take_snapshot(self, snapName):
        percy_snapshot(self.driver, self.site + ' - ' + self.site_env + ' - ' + snapName)
