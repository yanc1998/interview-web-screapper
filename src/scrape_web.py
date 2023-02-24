import requests
from bs4 import BeautifulSoup


def get_page(url, payload):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://palena.sii.cl',
        'Cookie': 'dtCookie=v_4_srv_44_sn_EB0247F9C063528FA59A12E678DAD22B_perc_100000_ol_0_mul_1_app-3Aea7c4b59f27d43eb_0; dtSa=true%7CC%7C-1%7CConsultar%7C-%7C1677189960924%7C189640688_955%7Chttps%3A%2F%2Fpalena.sii.cl%2Fcvc%2Fdte%2Fee_5Fempresas_5Fdte.html%7C%7C%7C%7C; rxVisitor=1677189640692U6M4QSCNCJG87557QC3RNCV94JSIFBL9; dtPC=44$189640688_955h-vCFLUBGBFREHPTTILAPGAQPJSKHVWJBKN-0e0; rxvt=1677191447580|1677189640694; dtLatC=837',
        'Content-Length': '43',
        'Accept-Language': 'es-US,es-419;q=0.9,es;q=0.8',
        'Host': 'palena.sii.cl',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15',
        'Referer': 'https://palena.sii.cl/cvc/dte/ee_empresas_dte.html',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup
