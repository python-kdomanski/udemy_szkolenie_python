import yaml
import argparse

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Formatowanie pliku YAML do czytelnej postaci.")
    parser.add_argument("input_file", help="Ścieżka do pliku wejściowego YAML.")
    parser.add_argument("output_file", help="Ścieżka do pliku wyjściowego YAML.")
    args = parser.parse_args()

    format_yaml(args.input_file, args.output_file)
