from django.db import models
from sorl.thumbnail import ImageField

class Pool(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=64)
	start_date = models.DateField()
	end_date = models.DateField()
	
	def __str__(self):
		return "{name} ({start} - {end})".format(name=self.name, start=self.start_date, end=self.end_date)

class Post(models.Model):
	class Meta:
		ordering = ['created_at']
	
	created_at = models.DateTimeField(auto_now_add=True)
	pool = models.ForeignKey('Pool')
	image = ImageField(height_field='height', width_field='width')
	width = models.IntegerField()
	height = models.IntegerField()
	description = models.TextField(blank=True)
	signature = models.CharField(max_length=30, blank=True)
	
	def prev_post(self):
		try:
			return Post.objects.filter(pool=self.pool).filter(created_at__lt=self.created_at).order_by('-created_at')[0]
		except:
			return None
	
	def next_post(self):
		try:
			return Post.objects.filter(pool=self.pool).filter(created_at__gt=self.created_at).order_by('created_at')[0]
		except:
			return None
	
	def __str__(self):
		return "{0}...".format(self.description[:50]) if len(self.description) > 50 else self.description or "No Caption"
