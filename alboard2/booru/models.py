from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.core.urlresolvers import reverse
from sorl.thumbnail import ImageField
from taggit.managers import TaggableManager
import reversion

@reversion.register
class Pool(models.Model):
	class Meta:
		ordering = ['-start_date']
	
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=64)
	start_date = models.DateField()
	end_date = models.DateField()
	
	def get_absolute_url(self):
		return reverse('pool', kwargs={'pk': self.pk})
	
	def __str__(self):
		return "{name} ({start} - {end})".format(name=self.name, start=self.start_date, end=self.end_date)

@reversion.register
class Post(models.Model):
	class Meta:
		ordering = ['created_at']
	
	tags = TaggableManager(help_text=_(u"A comma-separated list of tags, with spaces replaced by underscores."))
	
	created_at = models.DateTimeField(auto_now_add=True, db_index=True)
	pool = models.ForeignKey('Pool', db_index=True)
	image = ImageField(height_field='height', width_field='width')
	width = models.IntegerField()
	height = models.IntegerField()
	description = models.TextField(blank=True)
	signature = models.CharField(max_length=30, blank=True, db_index=True)
	
	def get_absolute_url(self):
		return reverse('post', kwargs={'pid': self.pool_id, 'pk': self.pk})
	
	def __str__(self):
		return "{0}...".format(self.description[:50]) if len(self.description) > 50 else self.description or "No Caption"
