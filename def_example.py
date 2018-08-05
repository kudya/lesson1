def get_vat(payment, percent=18):
    print (percent)
    try:
        payment = float(payment)
        vat = payment / 100 * percent
        vat = round(vat, 2)
        return 'final VAT is {}'.format(vat)
    except (TypeError, ValueError):
        return 'can not count, check your input data'

result = get_vat(900, 10)
print(result)
