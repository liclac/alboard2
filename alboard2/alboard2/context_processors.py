from django.contrib.sites.models import Site

def context_processor(request):
	return {
		'site': Site.objects.get_current()
	}
