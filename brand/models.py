from django.db import models

# Create your models here.
class Bond(models.Model):
	u_name=models.TextField()
	u_mail=models.TextField()
	u_job=models.TextField()
	u_msg=models.TextField()

	def __str__(self):
		return self.u_name
