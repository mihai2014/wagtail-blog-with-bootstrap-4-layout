import json

def reply3(request):

    data = {}

    form = False
    if(request.method == "POST"):
        if('form' in request.POST):
            form = True
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']

        if request.FILES:
            file = request.FILES['file']
            data['fileName'] = file.name
            data['fileSize'] = str(file.size) + " bytes"


    data['firstname'] = firstname
    data['lastname'] = lastname
    
    jsonData = json.dumps(data)
    
    return jsonData
