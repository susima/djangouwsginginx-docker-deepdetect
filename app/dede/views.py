from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
'''
def dd_service:
    from dd_client import DD

    model_repo = '/home/flt/deepdetect/clothing'
    height = width = 224
    nclasses = 304

    # setting up DD client
    host = '127.0.0.1'
    sname = 'clothing'
    description = 'clothes classification'
    mllib = 'caffe'
    dd = DD(host)
    dd.set_return_format(dd.RETURN_PYTHON)

    # creating ML service
    model = {'repository':model_repo}
    parameters_input = {'connector':'image','width':width,'height':height}
    parameters_mllib = {'nclasses':nclasses}
    parameters_output = {}
    dd.put_service(sname,model,description,mllib,
               parameters_input,parameters_mllib,parameters_output)
'''
def dede(request):
    bashCommand = "../dede"
    import subprocess
    process = subprocess.Popen(bashCommand.split(), shell=True,
             stdin=None, stdout=None, stderr=None, close_fds=True)
    #output, error = process.communicate() 
    #dd_service   
    return HttpResponse("Hello, welcome to our dressing type clarification world.")
