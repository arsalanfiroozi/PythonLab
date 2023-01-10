import json

j = {
    'name' : 'AsgharAgha',
    'ID' : 'Befarma97102225'
}

json_obj = json.dumps(j)
print(json_obj)

json_data = json.loads(json_obj);
print(json_data['ID'])