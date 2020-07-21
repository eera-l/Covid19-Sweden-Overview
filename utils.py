import requests
import re
import demjson
from bs4 import BeautifulSoup
import numpy as np


def get_javascript(URL, index):
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    return soup.findAll('script', type="text/javascript")[index].prettify()


def clean_javascript(javascript, str):
    for s in str:
        javascript = re.sub(s, '', javascript, flags=re.S).strip()
    return javascript


def json_decode(str):
    return demjson.decode(str)


def load_norway_total():
    URL = "https://www.worldometers.info/coronavirus/country/norway/"
    javascript = get_javascript(URL, 7)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'coronavirus-cases-linear\', ',
                                          r'\);\s*</script>', r'\);\s*Highcharts\.chart\(\'coronavirus-cases-log\',.*'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]


def load_norway_active():
    URL = "https://www.worldometers.info/coronavirus/country/norway/"
    javascript = get_javascript(URL, 9)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'graph-active-cases-total\', ',
                                          r'\);\s*</script>'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]


def load_norway_deaths():
    URL = "https://www.worldometers.info/coronavirus/country/norway/"
    javascript = get_javascript(URL, 10)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'coronavirus-deaths-linear\', ',
                                       r'\);\s*</script>', r'\);\s*Highcharts\.chart\(\'coronavirus-deaths-log\',.*'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]


def load_denmark_total():
    URL = "https://www.worldometers.info/coronavirus/country/denmark/"
    javascript = get_javascript(URL, 9)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'coronavirus-cases-linear\', ',
                                          r'\);\s*</script>', r'\);\s*Highcharts\.chart\(\'coronavirus-cases-log\',.*'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]


def load_denmark_active():
    URL = "https://www.worldometers.info/coronavirus/country/denmark/"
    javascript = get_javascript(URL, 11)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'graph-active-cases-total\', ',
                                          r'\);\s*</script>'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]


def load_denmark_deaths():
    URL = "https://www.worldometers.info/coronavirus/country/denmark/"
    javascript = get_javascript(URL, 12)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'coronavirus-deaths-linear\', ',
                                       r'\);\s*</script>', r'\);\s*Highcharts\.chart\(\'coronavirus-deaths-log\',.*'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]


def load_finland_total():
    URL = "https://www.worldometers.info/coronavirus/country/finland/"
    javascript = get_javascript(URL, 9)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'coronavirus-cases-linear\', ',
                                          r'\);\s*</script>', r'\);\s*Highcharts\.chart\(\'coronavirus-cases-log\',.*'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]


def load_finland_active():
    URL = "https://www.worldometers.info/coronavirus/country/finland/"
    javascript = get_javascript(URL, 11)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'graph-active-cases-total\', ',
                                          r'\);\s*</script>'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]


def load_finland_deaths():
    URL = "https://www.worldometers.info/coronavirus/country/finland/"
    javascript = get_javascript(URL, 12)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'coronavirus-deaths-linear\', ',
                                       r'\);\s*</script>', r'\);\s*Highcharts\.chart\(\'coronavirus-deaths-log\',.*'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]
