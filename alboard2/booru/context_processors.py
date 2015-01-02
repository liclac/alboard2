from .models import *

def context_processor(request):
	return {
		'booru_pools': Pool.objects.all()
	}
