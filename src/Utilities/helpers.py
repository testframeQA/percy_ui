import time
from percy import percy_snapshot
import csv
import os

class Helpers:

    def get_data():
        site_data = os.getenv('site')
        if site_data == '4WP-US' or '4WP-CA':
            percy_test_file = 'src/tests/test_data/test_data_4wp.csv'
        elif site_data == '4WD':
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
        self.driver.execute_script("window.scrollTo(0, 500);")
        time.sleep(sleeptime)
        self.driver.execute_script("window.scrollTo(0, 1500);")
        time.sleep(sleeptime)
        self.driver.execute_script("window.scrollTo(0, 2000);")
        time.sleep(sleeptime)
        self.driver.execute_script("window.scrollTo(0, 2500);")
        time.sleep(sleeptime)
        self.driver.execute_script("window.scrollTo(0, 3000);")
        time.sleep(sleeptime)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleeptime)
        
    def percy_take_snapshot(self, snapName):
        percy_snapshot(self.driver, self.site + ' - ' + self.site_env + ' - ' + snapName)