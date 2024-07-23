import os
import requests
from bs4 import BeautifulSoup
import argparse
import yaml

# Przykładowy tag XML
#xml_data = '''<select id="select"><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=main-page">Asseco Core Banking REST API</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=branch-network-management">Business Development * Channel Management * Branch Network Management</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=general-settings">Business Development * Product Management * General Settings</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=product-design">Business Development * Product Management * Product Design</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=product-directory">Business Development * Product Management * Product Directory</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=financial-gateway">Channels * Channel Specific * Financial Gateway</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=party-authentication">Channels * Cross Channel * Party Authentication</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=market-information">Channels * Information Providers * Market Information</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=public-reference-data">Channels * Information Providers * Public Reference Data</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=servicing-order">Customers * Customer Care * Servicing Order</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=customer-case">Customers * Customer Orders * Customer Case</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=party-data-management">Customers * Party Reference * Party Data Management</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=customer-agreement">Customers * Relationship Management * Customer Agreement</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=customer-offer">Customers * Sales * Customer Offer</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=special-pricing-conditions">Customers * Sales * Special Pricing Conditions</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=general-ledger">Finance and Risk * Financial Control * General Ledger</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=limit-exposure-management">Finance and Risk * Market Risk * Limit and Exposure Management</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=regulatory-compliance">Finance and Risk * Regulatory Compliance * Regulatory Compliance</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=cash-box">Operations * Accounting Services * Cash Box</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=financial-accounting">Operations * Accounting Services * Financial Accounting</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=position-keeping">Operations * Accounting Services * Position Keeping</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=collateral-allocation">Operations * Collateral and Documents * Collateral Allocation</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=dunning">Operations * Operational Services * Dunning</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=cheque-processing">Operations * Payments * Cheque Processing</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=correspondent-bank">Operations * Payments * Correspondent Bank</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=counterparty-administration">Operations * Payments * Counterparty Administration</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=payment-execution">Operations * Payments * Payment Execution</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=payment-order">Operations * Payments * Payment Order</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=credit-charge-card">Products * Cards * Credit/Charge Card</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=credit-charge-card-2">Products * Cards * Credit/Charge Card 2</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=currency-exchange">Products * Consumer Banking * Currency Exchange</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=credit-facility">Products * Corporate Banking * Credit Facility</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=contract-common">Products * Loans and Deposits * Contract Common</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=credit-card-contract">Products * Loans and Deposits * Credit Card Contract</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=credit-common">Products * Loans and Deposits * Credit Common</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=current-account">Products * Loans and Deposits * Current Account</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=deposit-account">Products * Loans and Deposits * Deposit Account</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=loan">Products * Loans and Deposits * Loan</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=syndicated-loan">Products * Loans and Deposits * Syndicated Loan</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=bank-guarantee">Products * Trade Banking * Bank Guarantee</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=employee-access">Resource Management * Human Resources * Employee Access</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=employee-assignment">Resource Management * Human Resources * Employee Assignment</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=employee-data-management">Resource Management * Human Resources * Employee Data Management</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=systems-help-desk">Resource Management * Platform Operations * Systems Help Desk</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=systems-operations">Resource Management * Platform Operations * Systems Operations</option><option value="https://bgk2-ngui.dst.asseco.pl/application/api-docs?group=business-unit-management">Resource Management * Unit Management * Business Unit Management</option></select>'''
xml_data = '''<select id="select"><option value="http://10.17.202.119:8580/application/api-docs?group=main-page">Asseco Core Banking REST API</option><option value="http://10.17.202.119:8580/application/api-docs?group=branch-network-management">Business Development * Channel Management * Branch Network Management</option><option value="http://10.17.202.119:8580/application/api-docs?group=general-settings">Business Development * Product Management * General Settings</option><option value="http://10.17.202.119:8580/application/api-docs?group=product-design">Business Development * Product Management * Product Design</option><option value="http://10.17.202.119:8580/application/api-docs?group=product-directory">Business Development * Product Management * Product Directory</option><option value="http://10.17.202.119:8580/application/api-docs?group=financial-gateway">Channels * Channel Specific * Financial Gateway</option><option value="http://10.17.202.119:8580/application/api-docs?group=party-authentication">Channels * Cross Channel * Party Authentication</option><option value="http://10.17.202.119:8580/application/api-docs?group=market-information">Channels * Information Providers * Market Information</option><option value="http://10.17.202.119:8580/application/api-docs?group=public-reference-data">Channels * Information Providers * Public Reference Data</option><option value="http://10.17.202.119:8580/application/api-docs?group=servicing-order">Customers * Customer Care * Servicing Order</option><option value="http://10.17.202.119:8580/application/api-docs?group=customer-case">Customers * Customer Orders * Customer Case</option><option value="http://10.17.202.119:8580/application/api-docs?group=party-data-management">Customers * Party Reference * Party Data Management</option><option value="http://10.17.202.119:8580/application/api-docs?group=customer-agreement">Customers * Relationship Management * Customer Agreement</option><option value="http://10.17.202.119:8580/application/api-docs?group=customer-offer">Customers * Sales * Customer Offer</option><option value="http://10.17.202.119:8580/application/api-docs?group=special-pricing-conditions">Customers * Sales * Special Pricing Conditions</option><option value="http://10.17.202.119:8580/application/api-docs?group=general-ledger">Finance and Risk * Financial Control * General Ledger</option><option value="http://10.17.202.119:8580/application/api-docs?group=limit-exposure-management">Finance and Risk * Market Risk * Limit and Exposure Management</option><option value="http://10.17.202.119:8580/application/api-docs?group=regulatory-compliance">Finance and Risk * Regulatory Compliance * Regulatory Compliance</option><option value="http://10.17.202.119:8580/application/api-docs?group=cash-box">Operations * Accounting Services * Cash Box</option><option value="http://10.17.202.119:8580/application/api-docs?group=financial-accounting">Operations * Accounting Services * Financial Accounting</option><option value="http://10.17.202.119:8580/application/api-docs?group=position-keeping">Operations * Accounting Services * Position Keeping</option><option value="http://10.17.202.119:8580/application/api-docs?group=collateral-allocation">Operations * Collateral and Documents * Collateral Allocation</option><option value="http://10.17.202.119:8580/application/api-docs?group=dunning">Operations * Operational Services * Dunning</option><option value="http://10.17.202.119:8580/application/api-docs?group=cheque-processing">Operations * Payments * Cheque Processing</option><option value="http://10.17.202.119:8580/application/api-docs?group=correspondent-bank">Operations * Payments * Correspondent Bank</option><option value="http://10.17.202.119:8580/application/api-docs?group=counterparty-administration">Operations * Payments * Counterparty Administration</option><option value="http://10.17.202.119:8580/application/api-docs?group=payment-execution">Operations * Payments * Payment Execution</option><option value="http://10.17.202.119:8580/application/api-docs?group=payment-order">Operations * Payments * Payment Order</option><option value="http://10.17.202.119:8580/application/api-docs?group=credit-charge-card">Products * Cards * Credit/Charge Card</option><option value="http://10.17.202.119:8580/application/api-docs?group=credit-charge-card-2">Products * Cards * Credit/Charge Card 2</option><option value="http://10.17.202.119:8580/application/api-docs?group=currency-exchange">Products * Consumer Banking * Currency Exchange</option><option value="http://10.17.202.119:8580/application/api-docs?group=credit-facility">Products * Corporate Banking * Credit Facility</option><option value="http://10.17.202.119:8580/application/api-docs?group=contract-common">Products * Loans and Deposits * Contract Common</option><option value="http://10.17.202.119:8580/application/api-docs?group=credit-card-contract">Products * Loans and Deposits * Credit Card Contract</option><option value="http://10.17.202.119:8580/application/api-docs?group=credit-common">Products * Loans and Deposits * Credit Common</option><option value="http://10.17.202.119:8580/application/api-docs?group=current-account">Products * Loans and Deposits * Current Account</option><option value="http://10.17.202.119:8580/application/api-docs?group=deposit-account">Products * Loans and Deposits * Deposit Account</option><option value="http://10.17.202.119:8580/application/api-docs?group=loan">Products * Loans and Deposits * Loan</option><option value="http://10.17.202.119:8580/application/api-docs?group=syndicated-loan">Products * Loans and Deposits * Syndicated Loan</option><option value="http://10.17.202.119:8580/application/api-docs?group=bank-guarantee">Products * Trade Banking * Bank Guarantee</option><option value="http://10.17.202.119:8580/application/api-docs?group=employee-access">Resource Management * Human Resources * Employee Access</option><option value="http://10.17.202.119:8580/application/api-docs?group=employee-assignment">Resource Management * Human Resources * Employee Assignment</option><option value="http://10.17.202.119:8580/application/api-docs?group=employee-data-management">Resource Management * Human Resources * Employee Data Management</option><option value="http://10.17.202.119:8580/application/api-docs?group=systems-help-desk">Resource Management * Platform Operations * Systems Help Desk</option><option value="http://10.17.202.119:8580/application/api-docs?group=systems-operations">Resource Management * Platform Operations * Systems Operations</option><option value="http://10.17.202.119:8580/application/api-docs?group=business-unit-management">Resource Management * Unit Management * Business Unit Management</option></select>'''

# Ścieżka do katalogu, w którym mają być zapisywane pliki
output_dir = 'output_files'
output_dir_2 = 'output_files_2'


def format_yaml(input_file, output_file):
    # Otwieranie pliku YAML do odczytu
    with open(input_file, 'r', encoding='utf-8') as file:
        try:
            data = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(f"Błąd przy ładowaniu pliku YAML: {exc}")
            return

    # Zapis sformatowanego pliku YAML
    with open(output_file, 'w', encoding='utf-8') as file:
        try:
            yaml.dump(data, file, default_flow_style=False, sort_keys=False, allow_unicode=True)
        except yaml.YAMLError as exc:
            print(f"Błąd przy zapisywaniu pliku YAML: {exc}")

def save_page_content_to_files(xml_data, output_dir):
    # Sprawdzenie czy katalog istnieje, jeśli nie, utworzenie go
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if not os.path.exists(output_dir_2):
        os.makedirs(output_dir_2)

    # Parsowanie XML
    soup = BeautifulSoup(xml_data, 'html.parser')
    
    # Znalezienie wszystkich tagów <option>
    options = soup.find_all('option')
    safe_filename = ''
    file_path = ''

    for option in options:
        url = option['value']
        print(f"Value:{url}")
        option_text = option.get_text()

        if len(file_path) > 0 and len(safe_filename) > 0:
            file_output = os.path.join(output_dir_2, f"{safe_filename}.yaml")
            format_yaml(file_path, file_output)

        # Pobranie zawartości strony
        try:
            response = requests.get(url)
            response.raise_for_status()
            page_content = response.text

            # Utworzenie nazwy pliku na podstawie tekstu tagu <option>
            # Zamiana niebezpiecznych znaków na podkreślenia
            safe_filename = "".join([c if c.isalnum() else "_" for c in option_text])
            file_path = os.path.join(output_dir, f"{safe_filename}.yaml")

            # Zapisanie zawartości strony do pliku
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(page_content)

            print(f"Zapisano zawartość z {url} do {file_path}")

        except requests.RequestException as e:
            print(f"Błąd podczas pobierania {url}: {e}")



# Wywołanie funkcji
save_page_content_to_files(xml_data, output_dir)


