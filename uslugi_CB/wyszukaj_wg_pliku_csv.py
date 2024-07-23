import os
import yaml
import csv

file_input = 'uslugi_CB.csv'
file_output = 'uslugi_CB_analiza.csv'
results = []


def get_nested(data, keys):
    """
    Uzyskuje wartość zagnieżdżoną w słowniku `data` za pomocą listy `keys`.

    :param data: Słownik zawierający dane.
    :param keys: Lista kluczy do zagnieżdżonych wartości.
    :return: Wartość zagnieżdżona.
    """
    for key in keys:
        data = data[key]
    return data

def find_services(base_path, base_path_fragment, name_fragment):
    matching_files = []

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".yaml"):
                file_path = os.path.join(root, file)
                file_found, ile_param = file_contains_basepath(file_path, base_path_fragment, name_fragment)
                #if file_contains_basepath(file_path, base_path_fragment, name_fragment):
                if file_found:
                    matching_files.append([file, ile_param])
                    break

    return matching_files

def file_contains_basepath(file_path, base_path_fragment, name_fragment):
    with open(file_path, "r", encoding="utf-8") as f:
        yaml_data = yaml.safe_load(f)
        if "basePath" in yaml_data and base_path_fragment in yaml_data["basePath"]:
            if "tags" in yaml_data:
                for tag in yaml_data["tags"]:
                    if "name" in tag and name_fragment in tag["name"]:
                        print("{} - {} - {}".format(tag["name"],yaml_data["basePath"],file_path))

                        find_params = 0
                        ilosc_param_we = -1
                        for keys, value in yaml_data["paths"].items():
                            if type(value) == dict:
                                for klucz1, wartosc1 in value.items():
                                    if type(wartosc1) == dict:
                                        for klucz2, wartosc2 in wartosc1.items():
                                            if klucz2 == 'tags':
                                                #print(wartosc2[0])
                                                #print(wartosc2[0].find(name_fragment, 0, len(wartosc2[0])))
                                                #if wartosc2[0].find(name_fragment, 0, len(wartosc2[0])) > 0:
                                                if wartosc2[0] == name_fragment:
                                                    print(klucz2, wartosc2, len(wartosc1['parameters']))
                                                    find_params = 1
                                                    ilosc_param_we = len(wartosc1['parameters'])
                                                    break
                                                else:
                                                    break
                                            else:
                                                break
                                        if find_params > 0:
                                            break
                                    else:
                                        break
                                if find_params > 0:
                                    break
                            else:
                                break
                        #if find_params > 0:
                            #break

                        #nested_value = get_nested(yaml_data["paths"], ['get', 'tags'])
                        #print("Nested value:", nested_value)


                        return True, ilosc_param_we
            if "paths" in yaml_data:
                for path, methods in yaml_data["paths"].items():
                    if name_fragment in path:
                        return True, 0
    return False, -1

base_path = "output_files"

with open(file_input, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    line_number=0
    try:
        for row in csvreader:
            line_number=line_number+1
            '''
            print(row[0])  # WE z ABO
            print(row[1])  # typ get/post/delete,...
            print(row[2])  # base_path_fragment
            print(row[3])  # name_fragment
            '''
            matching_files = find_services(base_path, row[2], row[3])
            if not matching_files:
                matching_files=[['Nie znaleziono uslugi',-1]]

            '''
            #testowe
            if line_number==1:
                matching_files=['Business_Development___Product_Management___General_Settings.yaml','Drugi_plik.yaml']
            if line_number == 2:
                matching_files = ['Business_Development___Product_Management___Product_Directory.yaml']
            if line_number == 3:
                matching_files = ['Products___Loans_and_Deposits___Credit_Common.yaml']
            '''
            list_tmp = [row[0],row[1],row[2],row[3], matching_files]
            results.append(list_tmp)
    except IndexError as e:
        print("Błądna struktura csv - linia {}, błąd: {}".format(line_number,e))


print("Pliki zawierające pasujące usługi:")
for lista_tmp in results:
    print(lista_tmp)

with open(file_output, 'w', encoding='utf-8') as file:
    # nagłowek
    line = 'URL - REST CB'+';'+'Typ'+';'+'Sciezka bazowa'+';'+'Nazwa uslugi'+';'+'Nazwa pliku z usluga'+';'+'Ilosc param WE'
    file.write(line)
    file.write("\n")

    for lista_tmp in results:
        for lista_tmp2 in lista_tmp[4]:
            line = lista_tmp[0]+';'+lista_tmp[1]+';'+lista_tmp[2]+';'+lista_tmp[3]+';'+lista_tmp2[0]+';'+str(lista_tmp2[1])
            file.write(line)
            file.write("\n")

'''
# Pytanie użytkownika o base_path_fragment
base_path_fragment = input("Podaj fragment ścieżki bazowej (base_path_fragment) [Domyślnie '/api/']: ") or "/api/"

# Pytanie użytkownika o name_fragment
name_fragment = input("Podaj fragment nazwy usługi (name_fragment): ")

matching_files = find_services(base_path, base_path_fragment, name_fragment)
print("Pliki zawierające pasujące usługi:")
for file in matching_files:
    print(file)
'''