from filterdata.annotations_json import read_json , get_keys

if __name__ == '__main__':
    json_path = r"C:\Users\spars\Downloads\deep_fashion\deep_fashion\annotations\instances_val2024.json"
    f = read_json(json_path)
    
    doc_keys = get_keys(f)
    print("Keys in given JSON: ",doc_keys)