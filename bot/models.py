from django.db import models

class Facebook(models.Model):
	name = models.CharField(max_length=255, verbose_name='Name App')
	token = models.CharField(max_length=255, verbose_name='Token Page')
	verify_token = models.CharField(max_length=255, verbose_name='Verify Token')
	recipient = models.CharField(max_length=255, verbose_name='Recipient ID', null=True, blank=True)
	
	class Meta:
		verbose_name_plural = 'Facebook'

	def __str__(self):
		return "{}".format(self.name)


class IA(models.Model):
	question = models.CharField(max_length=255, verbose_name='Question')
	answer = models.CharField(max_length=255, verbose_name='Answer')
	verify = models.BooleanField(default=True, verbose_name='Verify')
	payload = models.BooleanField(default=False, verbose_name='Payload')
	
	class Meta:
		verbose_name_plural = 'IA'

	def __str__(self):
		return "{}-{}".format(self.question,self.answer)


class UserFacebook(models.Model):
	sender_id = models.CharField(max_length=255, verbose_name='Sender ID')
	text = models.CharField(max_length=255, verbose_name='Text', null=True, blank=True)
	
	class Meta:
		verbose_name_plural = 'User Facebook'

	def __str__(self):
		return "{}".format(self.sender_id)
