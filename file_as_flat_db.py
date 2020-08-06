class Employee:
	def __init__(slef, name, email_address, title, phone_number=None, identifier=None):
		self.name = name
		self.email_address = email_address
		self.title = title
		self.phone_number = phone_number

	def email_signature(self, include_phone=False):
		email_signature = f"{self.name} - {self.title}\n{self.email_address}"