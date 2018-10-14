from django.db import models

class Donor(models.Model):
	donor_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	balance = models.DecimalField(decimal_places=2,max_digits=10)

	def increase_balance(self, value):
		self.balance += value

	def decrease_balance(self, value):
		self.balance -= value

	def donate(self, r, val):
		self.decrease_balance(val)
		r.increase_balance(val)
		dono = Donation.objects.create(donor=self,recipient=r,value=val)
		dono.save()

class Recipient(models.Model):
	recipient_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	balance = models.DecimalField(decimal_places=2,max_digits=10)

	def increase_balance(self, value):
		self.balance += value

	def decrease_balance(self, value):
		self.balance -= value

class Donation(models.Model):
	donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
	recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE)
	value = models.DecimalField(decimal_places=2,max_digits=10)
