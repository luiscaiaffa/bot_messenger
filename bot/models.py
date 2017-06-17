from django.db import models

class Facebook(models.Model):
	name = models.CharField(max_length=255, verbose_name='Name App')
	token = models.CharField(max_length=255, verbose_name='Token Page')
	verify_token = models.CharField(max_length=255, verbose_name='Verify Token')

	class Meta:
		verbose_name_plural = 'Facebook'

	def __str__(self):
		return "{}".format(self.name)
