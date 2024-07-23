

def ProcessInvoice(netto, brutto):
    if netto >= brutto:
        raise ValueError("Netto should be lower or equal to brutto")
    else:
        print("Processing invoice: netto={} brutto={}".format(netto, brutto))

def EndOfMoth():
    netto = 1230
    brutto = 1000

    try:
        #1/0
        ProcessInvoice(netto,brutto)

    except ValueError as e:
        print("The values on invoice are incorect: {}".format(e))
        raise ValueError('Error when processing invoices') from e
    except Exception as e:
        print("Error Processing invoice: {}".format(e))
        raise Exception("General error")

EndOfMoth()