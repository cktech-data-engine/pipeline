import json
def save_trusted(data, filename):
    path = f"storage/trusted/{filename}"
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Dados TRUSTED salvos em: {path}")