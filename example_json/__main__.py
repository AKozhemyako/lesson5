import json
jsonData = """ {
    "name"     : "Vova Pupkin",
    } """
dictData = json.loads(jsonData)
    print(dictData["name"])

