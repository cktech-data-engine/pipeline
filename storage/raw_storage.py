import json
def save_raw(data, filename):
    path = f"storage/raw/{filename}"
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Dados RAW salvos em: {path}")