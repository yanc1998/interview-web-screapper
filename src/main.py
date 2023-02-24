from scrape_web import get_page
import numpy as np


def main():
    url = "https://palena.sii.cl/cvc_cgi/dte/ee_empresa_rut"
    payload = 'RUT_EMP=76749144&DV_EMP=1&ACEPTAR=Consultar'
    result = test(url, payload)
    print("Los antecedentes de la empresa son :", result[0])
    print("El contribuyente tiene autorizada la emisión de los siguientes documentos tributarios electrónicos:",
          result[1])


def test(url, payload):
    page = get_page(url, payload)
    tables = page.findAll('table', attrs={"border": 1})
    before = tables[0]
    documents = tables[1]

    values_before = {}
    for value in before.findAll('tr'):
        key = value.text.split('\n')[2].split('\xa0')[1].split(' ')
        string_key = ""
        for i in key:
            if len(i) > 0:
                string_key += i + ' '

        data = value.text.split('\n')[5].split(' ')[-1]
        values_before[string_key] = data

    values_documents = []
    _keys = {}
    key = list(filter(lambda x: len(x) > 0, np.array(list(
        map(lambda x: x.split(' '),
            filter(lambda x: len(x) > 0, documents.findAll('tr')[0].text.split('\n'))))).flatten()))

    # save keys for tables
    for index, value in enumerate(key):
        _keys[index] = value

    for value in documents.findAll('tr')[1:]:
        keys = value.text.split('\n')
        keys = list(map(lambda x: list(filter(lambda x: len(x) > 0, x.split(' '))),
                        filter(lambda x: len(x) > 0, keys)))
        values_document = {}
        for index, key in enumerate(keys):
            string_value = ""
            for s in key:
                string_value += s + ' '
            values_document[_keys[index]] = string_value

        values_documents.append(values_document)

    return values_documents, values_before


if __name__ == '__main__':
    main()
