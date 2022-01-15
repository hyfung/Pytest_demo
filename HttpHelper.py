import requests
import bs4
import time
import json

_lastCad = time.time()
_lastUsd = time.time()
_lastGbp = time.time()
_lastEur = time.time()
_lastCovid = time.time()
_valueCad = ""
_valueUsd = ""
_valueGbp = ""
_valueEur = ""
_valueCovid = ""


_valueForex = None
_lastForex = time.time()

def forex_to_hkd():
    global _valueForex, _lastForex
    if time.time() > _lastForex + 300 or _valueForex == None:
        _valueForex = dict()
        url = "https://www.x-rates.com/table/?from=HKD&amount=1"
        headers = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"}
        x = requests.get(url).text
        cad = [i.replace('\t', '') for i in x.split("\n") if "https://www.x-rates.com/graph/?from=CAD&amp;to=HKD" in i][0]
        cad = cad.replace("<td class='rtRates'><a href='https://www.123.com/graph/?from=CAD&amp;to=HKD'>", "")
        cad = cad.replace("</a></td>", "")
        _valueForex['cad'] = cad.strip(' ')
        usd = [i.replace('\t', '') for i in x.split("\n") if "https://www.x-rates.com/graph/?from=USD&amp;to=HKD" in i][0]
        usd = usd.replace("<td class='rtRates'><a href='https://www.x-rates.com/graph/?from=USD&amp;to=HKD'>", "")
        usd = usd.replace("</a></td>", "")
        _valueForex['usd'] = usd.strip(' ')
        gbp = [i.replace('\t', '') for i in x.split("\n") if "https://www.x-rates.com/graph/?from=GBP&amp;to=HKD" in i][0]
        gbp = gbp.replace("<td class='rtRates'><a href='https://www.x-rates.com/graph/?from=GBP&amp;to=HKD'>", "")
        gbp = gbp.replace("</a></td>", "")
        _valueForex['gbp'] = gbp.strip(' ')
        eur = [i.replace('\t', '') for i in x.split("\n") if "https://www.x-rates.com/graph/?from=EUR&amp;to=HKD" in i][0]
        eur = eur.replace("<td class='rtRates'><a href='https://www.x-rates.com/graph/?from=EUR&amp;to=HKD'>", "")
        eur = eur.replace("</a></td>", "")
        _valueForex['eur'] = eur.strip(' ')
    return _valueForex

def covid_cases() -> dict:
    global _lastCovid, _valueCovid
    if time.time() > _lastCovid + 3600 or _valueCovid == "":
        url = "https://api.opencovid.ca/summary"
        x = json.loads(requests.get(url).text)
        _lastCovid = time.time()
        _valueCovid = x
    else:
        x = _valueCovid
    return x

def cad_to_hkd():
    global _lastCad, _valueCad
    if time.time() > _lastCad + 600 or _valueCad == "":
        url = "https://www.x-rates.com/table/?from=HKD&amount=1"
        headers = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"}
        x = requests.get(url).text
        y = [i.replace('\t', '') for i in x.split("\n") if "https://www.x-rates.com/graph/?from=CAD&amp;to=HKD" in i][0]
        y = y.replace("<td class='rtRates'><a href='https://www.x-rates.com/graph/?from=CAD&amp;to=HKD'>", "")
        y = y.replace("</a></td>", "")
        _lastCad = time.time()
        _valueCad = y
    else:
        return _valueCad

def cad_to_hkd_OLD():
    global _lastCad, _valueCad
    if time.time() > _lastCad + 120 or _valueCad == "":
        url = "https://hk.finance.yahoo.com/quote/CADHKD=X/"
        x = requests.get(url).text
        soup = bs4.BeautifulSoup(x, 'html.parser')
        y = soup.find_all("span", attrs={"data-reactid":"32"})[0].text
        _lastCad = time.time()
        _valueCad = y
    else:
        y = _valueCad
    return y

def usd_to_hkd_OLD():
    global _lastUsd, _valueUsd
    if time.time() > _lastUsd + 120 or _valueUsd == "":
        url = "https://hk.finance.yahoo.com/quote/USDHKD=X/"
        x = requests.get(url).text
        soup = bs4.BeautifulSoup(x, 'html.parser')
        y = soup.find_all("span", attrs={"data-reactid":"32"})[0].text
        _lastUsd = time.time()
        _valueUsd = y
    else:
        y = _valueUsd
    return y

def gbp_to_hkd():
    global _lastGbp, _valueGbp
    if time.time() > _lastGbp + 120 or _valueGbp == "":
        url = "https://hk.finance.yahoo.com/quote/GBPHKD=X/"
        x = requests.get(url).text
        soup = bs4.BeautifulSoup(x, 'html.parser')
        y = soup.find_all("span", attrs={"data-reactid":"32"})[0].text
        _lastGbp = time.time()
        _valueGbp = y
    else:
        y = _valueGbp
    return y

def eur_to_hkd():
    global _lastEur, _valueEur
    if time.time() > _lastEur + 120 or _valueEur == "":
        url = "https://hk.finance.yahoo.com/quote/EURHKD=X/"
        x = requests.get(url).text
        soup = bs4.BeautifulSoup(x, 'html.parser')
        y = soup.find_all("span", attrs={"data-reactid":"32"})[0].text
        _lastEur = time.time()
        _valueEur = y
    else:
        y = _valueEur
    return y
