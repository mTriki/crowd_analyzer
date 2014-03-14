import os
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def receive_data(request):
	if request.method == "GET" and 'q' in request.GET:
		file = open('data/data.json', 'w')
		file.write(request.GET['q'])
		file.close()

		return HttpResponse("fouck")
	else:
		return HttpResponse("failed")