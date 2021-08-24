'''
Created on 3 Aug 2021
@author: qsong
'''
import requests as requests
import unittest
from bs4 import BeautifulSoup

class gao_message(object):
    '''
    This module provides gao008 functions
    '''
    game_base_url = "http://www.gao008.com/So.asp"

    def __init__(self):
        '''
        Constructor
        '''
        return

    def __del__(self):
        return

    def get_gao008_message(self):
        gao_response = requests.get(self.game_base_url)
        gao_response = gao_response
        if gao_response.status_code == 200:
            gao_file = open('../gao888.html', 'wb')
            gao_file.write(gao_response.content)
            gao_file.close()
            soup = BeautifulSoup(gao_response.content, 'html.parser', from_encoding="gb18030")
            soup.prettify()
            tr_list = soup.select('div[class*="trcolor"]')
            print(len(tr_list))
            for tr_elem in tr_list:
                tr_elem_str = tr_elem.text
                message_content_str = tr_elem_str.split("【")[0]
                message_provider = tr_elem_str.split("【")[-1].split("】")[0]
                message_time = tr_elem_str.split("【")[-1].split("】")[1]
                print(message_time)
        return message_content_str, message_provider, message_time

class Test(unittest.TestCase):

    def setUp(self):
        self.test_obj = gao_message()

    def tearDown(self):
        self.test_obj = None
        return

    def test_get_gao008_message(self):
        self.test_obj.get_gao008_message()
        return