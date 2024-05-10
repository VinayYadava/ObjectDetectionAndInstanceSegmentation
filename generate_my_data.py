from filterdata.annotations_json import read_json , AnnotationJSON

if __name__ == '__main__':
    #json_path = r"C:\Users\spars\Downloads\deep_fashion\deep_fashion\annotations\instances_val2024.json"
    json_path = r"./instances_train2024.json"

    f = AnnotationJSON(json_path)
    
    print("Keys in given JSON: ",f.keys)
    
    print("Keys in an annotation: ",f.annotations[0].keys())
    print("Values in an landmarks: ",f.annotations[0]["landmarks"])
    print("Values in an category_id: ",f.annotations[0]["category_id"])
    print("Values in an is_crowd: ",f.annotations[0]["is_crowd"])
    print("Values in an category_id: ",f.annotations[0]["bbox"])
    print("Values in an id: ",f.annotations[0]["id"])
    print("Values in an info: ",f.info)