from filterdata.annotations_json import read_json , AnnotationJSON, CocoFormat

if __name__ == '__main__':
    
    #json_path = r"C:\Users\spars\Downloads\deep_fashion\deep_fashion\annotations\instances_val2024.json"
    json_path = r"./instances_train2024.json"

    f_object = AnnotationJSON(json_path)
    f = f_object()
    
    for i in f["annotations"]:
        if i['id'] != 1:
            print(i['id'])
            break