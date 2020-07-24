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


def load_sweden_total(date):
    URL = "https://c19.se/"
    javascript = get_javascript(URL, 11, False)
    cleaned_string = clean_javascript(javascript,
                                      [r'.*Highcharts.chart\(\'container\',{exporting: ',
                                       r'onclick:\s*function\s*\(\){this\.update\({\s*yAxis:\[{type: \'linear\'},\s*' +
                                       r'{type: \'linear\'}\]\s*}\)\s*',
                                       r'onclick:\s*function\s*\(\){this\.update\({\s*yAxis:\[{type: \'logarithmic\'},\s*' +
                                       r'{type: \'logarithmic\'}\]\s*}\)\s*}}}',
                                          r'\);.*'])
    j = json_decode(cleaned_string)
    return np.array([item['y'] for item in j['series'][0]['data']])[date:]


def load_sweden_deaths(date):
    URL = "https://c19.se/"
    javascript = get_javascript(URL, 11, False)
    cleaned_string = clean_javascript(javascript,
                                      [r'.*Highcharts.chart\(\'container\',{exporting: ',
                                       r'onclick:\s*function\s*\(\){this\.update\({\s*yAxis:\[{type: \'linear\'},\s*' +
                                       r'{type: \'linear\'}\]\s*}\)\s*',
                                       r'onclick:\s*function\s*\(\){this\.update\({\s*yAxis:\[{type: \'logarithmic\'},\s*' +
                                       r'{type: \'logarithmic\'}\]\s*}\)\s*}}}',
                                       r'\);.*'])
    j = json_decode(cleaned_string)
    return np.array([item['y'] for item in j['series'][2]['data']])[date:]


def load_sweden_hosp(date):
    URL = "https://c19.se/"
    javascript = get_javascript(URL, 11, False)
    cleaned_string = clean_javascript(javascript,
                                      [r'.*Highcharts.chart\(\'container\',{exporting: ',
                                       r'onclick:\s*function\s*\(\){this\.update\({\s*yAxis:\[{type: \'linear\'},\s*' +
                                       r'{type: \'linear\'}\]\s*}\)\s*',
                                       r'onclick:\s*function\s*\(\){this\.update\({\s*yAxis:\[{type: \'logarithmic\'},\s*' +
                                       r'{type: \'logarithmic\'}\]\s*}\)\s*}}}',
                                       r'\);.*'])
    j = json_decode(cleaned_string)
    return np.array([item['y'] for item in j['series'][5]['data']])[date:]


def load_sweden_icu(date):
    URL = "https://c19.se/"
    javascript = get_javascript(URL, 11, False)
    cleaned_string = clean_javascript(javascript,
                                      [r'.*Highcharts.chart\(\'container\',{exporting: ',
                                       r'onclick:\s*function\s*\(\){this\.update\({\s*yAxis:\[{type: \'linear\'},\s*' +
                                       r'{type: \'linear\'}\]\s*}\)\s*',
                                       r'onclick:\s*function\s*\(\){this\.update\({\s*yAxis:\[{type: \'logarithmic\'},\s*' +
                                       r'{type: \'logarithmic\'}\]\s*}\)\s*}}}',
                                       r'\);.*'])
    j = json_decode(cleaned_string)
    return np.array([item['y'] for item in j['series'][4]['data']])[date:]


def load_norway_total():
    URL = "https://www.worldometers.info/coronavirus/country/norway/"
    javascript = get_javascript(URL, 7, True)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'coronavirus-cases-linear\', ',
                                          r'\);\s*</script>', r'\);\s*Highcharts\.chart\(\'coronavirus-cases-log\',.*'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]


def load_norway_active():
    URL = "https://www.worldometers.info/coronavirus/country/norway/"
    javascript = get_javascript(URL, 9, True)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'graph-active-cases-total\', ',
                                          r'\);\s*</script>'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]


def load_norway_deaths():
    URL = "https://www.worldometers.info/coronavirus/country/norway/"
    javascript = get_javascript(URL, 10, True)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'coronavirus-deaths-linear\', ',
                                       r'\);\s*</script>', r'\);\s*Highcharts\.chart\(\'coronavirus-deaths-log\',.*'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]


def load_denmark_total():
    URL = "https://www.worldometers.info/coronavirus/country/denmark/"
    javascript = get_javascript(URL, 9, True)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'coronavirus-cases-linear\', ',
                                          r'\);\s*</script>', r'\);\s*Highcharts\.chart\(\'coronavirus-cases-log\',.*'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]


def load_denmark_active():
    URL = "https://www.worldometers.info/coronavirus/country/denmark/"
    javascript = get_javascript(URL, 11, True)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'graph-active-cases-total\', ',
                                          r'\);\s*</script>'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]


def load_denmark_deaths():
    URL = "https://www.worldometers.info/coronavirus/country/denmark/"
    javascript = get_javascript(URL, 12, True)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'coronavirus-deaths-linear\', ',
                                       r'\);\s*</script>', r'\);\s*Highcharts\.chart\(\'coronavirus-deaths-log\',.*'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]


def load_finland_total():
    URL = "https://www.worldometers.info/coronavirus/country/finland/"
    javascript = get_javascript(URL, 9, True)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'coronavirus-cases-linear\', ',
                                          r'\);\s*</script>', r'\);\s*Highcharts\.chart\(\'coronavirus-cases-log\',.*'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]


def load_finland_active():
    URL = "https://www.worldometers.info/coronavirus/country/finland/"
    javascript = get_javascript(URL, 11, True)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'graph-active-cases-total\', ',
                                          r'\);\s*</script>'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]


def load_finland_deaths():
    URL = "https://www.worldometers.info/coronavirus/country/finland/"
    javascript = get_javascript(URL, 12, True)
    cleaned_string = clean_javascript(javascript,
                                      [r'<script type="text\/javascript">\s*Highcharts\.chart\(\'coronavirus-deaths-linear\', ',
                                       r'\);\s*</script>', r'\);\s*Highcharts\.chart\(\'coronavirus-deaths-log\',.*'])
    j = json_decode(cleaned_string)
    return np.array(j['series'][0]['data'])[26:]


def load_italy_total(date):
    with urllib.request.urlopen("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json") as url:
        data = json.loads(url.read().decode())
    return np.array([item['totale_casi'] for item in data])[date:]


def load_italy_active(date):
    with urllib.request.urlopen("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json") as url:
        data = json.loads(url.read().decode())
    return np.array([item['totale_positivi'] for item in data])[date:]


def load_italy_hosp(date):
    with urllib.request.urlopen("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json") as url:
        data = json.loads(url.read().decode())
    return np.array([item['totale_ospedalizzati'] for item in data])[date:]


def load_italy_icu(date):
    with urllib.request.urlopen("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json") as url:
        data = json.loads(url.read().decode())
    return np.array([item['terapia_intensiva'] for item in data])[date:]


def load_italy_deaths(date):
    with urllib.request.urlopen("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json") as url:
        data = json.loads(url.read().decode())
    return np.array([item['deceduti'] for item in data])[date:]


def load_lombardy_active(date):
    with urllib.request.urlopen("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni.json") as url:
        data = json.loads(url.read().decode())
    return np.array([item['totale_positivi'] for item in data if item['denominazione_regione'] == 'Lombardia'])[date:]


def load_emilia_active(date):
    with urllib.request.urlopen("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni.json") as url:
        data = json.loads(url.read().decode())
    return np.array([item['totale_positivi'] for item in data if item['denominazione_regione'] == 'Emilia-Romagna'])[date:]


def load_veneto_active(date):
    with urllib.request.urlopen("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni.json") as url:
        data = json.loads(url.read().decode())
    return np.array([item['totale_positivi'] for item in data if item['denominazione_regione'] == 'Veneto'])[date:]

