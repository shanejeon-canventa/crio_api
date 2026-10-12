import json

def export_to_json(data, output_filepath="export/output.json"):
    if isinstance(data, (str,bytes)):
        data = json.loads(data)
        
    with open(output_filepath, mode="w", encoding="utf-8-sig") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        
    print(f"Successfully exported data to '{output_filepath}")