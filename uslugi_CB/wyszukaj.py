import os
import yaml

def find_services(base_path, base_path_fragment, name_fragment):
    matching_files = []

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".yaml"):
                file_path = os.path.join(root, file)
                if file_contains_basepath(file_path, base_path_fragment, name_fragment):
                    matching_files.append(file)

    return matching_files

def file_contains_basepath(file_path, base_path_fragment, name_fragment):
    with open(file_path, "r", encoding="utf-8") as f:
        yaml_data = yaml.safe_load(f)
        if "basePath" in yaml_data and base_path_fragment in yaml_data["basePath"]:
            if "tags" in yaml_data:
                for tag in yaml_data["tags"]:
                    if "name" in tag and name_fragment in tag["name"]:
                        return True
            if "paths" in yaml_data:
                for path, methods in yaml_data["paths"].items():
                    if name_fragment in path:
                        return True
    return False

base_path = "output_files"

# Pytanie użytkownika o base_path_fragment
base_path_fragment = input("Podaj fragment ścieżki bazowej (base_path_fragment) [Domyślnie '/api/']: ") or "/api/"

# Pytanie użytkownika o name_fragment
name_fragment = input("Podaj fragment nazwy usługi (name_fragment): ")

matching_files = find_services(base_path, base_path_fragment, name_fragment)
print("Pliki zawierające pasujące usługi:")
for file in matching_files:
    print(file)
