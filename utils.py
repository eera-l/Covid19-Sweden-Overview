import requests
import re
import demjson
from bs4 import BeautifulSoup
import numpy as np
import urllib.request
import json


def get_javascript(URL, index, type):
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    if type:
        return soup.findAll('script', type="text/javascript")[index].prettify()
    else:
        return soup.findAll('script')[index].prettify()


def clean_javascript(javascript, str):
    for s in str:
        javascript = re.sub(s, '', javascript, flags=re.S).strip()
    return javascript


def json_decode(str):
    return demjson.decode(str)


def fetch_index_sweden(info: str) -> int:
    if info == 'total':
        return 0
    elif info == 'deaths':
        return 2
    elif info == 'icu':
        return 4
    elif info == 'hospital':
        return 5


def load_sweden_data(date: int, info: str) -> np.ndarray:
    URL = "https://c19.se/"
    javascript = get_javascript(URL, 10, False)
    cleaned_string = clean_javascript(javascript,
                                      [r'.*Highcharts.chart\(\'container\',{exporting: ',
                                       r'onclick:\s*function\s*\(\){this\.update\({\s*yAxis:\[{type: \'linear\'},\s*' +
                                       r'{type: \'linear\'}\]\s*}\)\s*',
                                       r'onclick:\s*function\s*\(\){this\.update\({\s*yAxis:\[{type: \'logarithmic\'},\s*' +
                                       r'{type: \'logarithmic\'}\]\s*}\)\s*}}}',
                                          r'\);.*'])
    j = json_decode(cleaned_string)
    index = fetch_index_sweden(info)
    return np.array([item['y'] for item in j['series'][index]['data']])[date:]


def load_norway_total() -> np.ndarray:
    URL = "https://www.worldometers.info/coronavirus/country/norway/"
    javascript = get_javascript(URL, 7, True)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'coronavirus-cases-linear\', ',
                                          r'\);\s*</script>', r'\);\s*Highcharts\.chart\(\'coronavirus-cases-log\',.*'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]


def load_norway_active() -> np.ndarray:
    URL = "https://www.worldometers.info/coronavirus/country/norway/"
    javascript = get_javascript(URL, 9, True)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'graph-active-cases-total\', ',
                                          r'\);\s*</script>'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]


def load_norway_deaths() -> np.ndarray:
    URL = "https://www.worldometers.info/coronavirus/country/norway/"
    javascript = get_javascript(URL, 10, True)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'coronavirus-deaths-linear\', ',
                                       r'\);\s*</script>', r'\);\s*Highcharts\.chart\(\'coronavirus-deaths-log\',.*'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]


def load_denmark_total() -> np.ndarray:
    URL = "https://www.worldometers.info/coronavirus/country/denmark/"
    javascript = get_javascript(URL, 9, True)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'coronavirus-cases-linear\', ',
                                          r'\);\s*</script>', r'\);\s*Highcharts\.chart\(\'coronavirus-cases-log\',.*'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]


def load_denmark_active() -> np.ndarray:
    URL = "https://www.worldometers.info/coronavirus/country/denmark/"
    javascript = get_javascript(URL, 11, True)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'graph-active-cases-total\', ',
                                          r'\);\s*</script>'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]


def load_denmark_deaths() -> np.ndarray:
    URL = "https://www.worldometers.info/coronavirus/country/denmark/"
    javascript = get_javascript(URL, 12, True)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'coronavirus-deaths-linear\', ',
                                       r'\);\s*</script>', r'\);\s*Highcharts\.chart\(\'coronavirus-deaths-log\',.*'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]


def load_finland_total() -> np.ndarray:
    URL = "https://www.worldometers.info/coronavirus/country/finland/"
    javascript = get_javascript(URL, 9, True)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'coronavirus-cases-linear\', ',
                                          r'\);\s*</script>', r'\);\s*Highcharts\.chart\(\'coronavirus-cases-log\',.*'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]


def load_finland_active() -> np.ndarray:
    URL = "https://www.worldometers.info/coronavirus/country/finland/"
    javascript = get_javascript(URL, 11, True)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'graph-active-cases-total\', ',
                                          r'\);\s*</script>'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]


def load_finland_deaths() -> np.ndarray:
    URL = "https://www.worldometers.info/coronavirus/country/finland/"
    javascript = get_javascript(URL, 12, True)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'coronavirus-deaths-linear\', ',
                                       r'\);\s*</script>', r'\);\s*Highcharts\.chart\(\'coronavirus-deaths-log\',.*'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]


def fetch_italian_header(info: str) -> str:
    if info == 'total':
        return 'totale_casi'
    elif info == 'positive':
        return 'totale_positivi'
    elif info == 'hospital':
        return 'totale_ospedalizzati'
    elif info == 'icu':
        return 'terapia_intensiva'
    elif info == 'deaths':
        return 'deceduti'


def load_italy_cases(date: int, info: str) -> np.ndarray:
    with urllib.request.urlopen("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json") as url:
        data = json.loads(url.read().decode())
    header = fetch_italian_header(info)
    return np.array([item[header] for item in data])[date:]


def load_cases_by_region(date: int, region: str) -> np.ndarray:
    with urllib.request.urlopen(
            "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni.json") as url:
        data = json.loads(url.read().decode())
    return np.array([item['totale_positivi'] for item in data if item['denominazione_regione'] ==  region])[date:]

