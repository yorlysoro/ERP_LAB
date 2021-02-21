from django.db import models 
from django.contrib.auth.models import User

class BaseModel(models.Model):
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
        
class Country(BaseModel):
    
    name = models.CharField(max_length=300)
    code = models.CharField(max_length=2)
    currency = models.ForeignKey('Currency', related_name='CountryCurrency', blank=True, null=True, on_delete=models.SET_NULL)
    phone_code = models.SmallIntegerField()
    state = models.OneToOneField('State', related_name='CountryState', blank=True, null=True, on_delete=models.SET_NULL)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name
    
    
class State(BaseModel):
    
    country = models.ForeignKey('Country', related_name='StateCountry', on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    code = models.CharField(max_length=255)
    class Meta:
        ordering = ['code']
        
    def __str__(self):
        return self.name
    
class Currency(BaseModel):
    
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-active', 'name']
        
    def __str__(self):
        return self.name
    

class Company(BaseModel):
    
    name = models.CharField(max_length=255)
    sequence = models.IntegerField(default=10)
    parent_company = models.ForeignKey('Company', related_name='CompanyParent', blank=True, null=True, on_delete=models.SET_NULL)
    partner = models.ForeignKey('Partner', on_delete=models.CASCADE)
    logo = models.BinaryField(blank=True, null=True)
    currency = models.ForeignKey('Currency', related_name='CompanyCurrency', on_delete=models.CASCADE)
    users = models.ManyToManyField('Users', blank=True, related_name='CompanyUsers')
    street = models.CharField(max_length=255, blank=True, null=True)
    street2 = models.CharField(max_length=255, blank=True, null=True)
    state = models.ForeignKey('State', related_name='CompanyState', blank=True, null=True, on_delete=models.SET_NULL)
    zip = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255,blank=True, null=True)
    banks = models.OneToOneField('PartnerBank', related_name='CompanyBanks', blank=True, null=True, on_delete=models.SET_NULL)
    country = models.ForeignKey('Country', related_name='CompanyCountry',blank=True, null=True, on_delete=models.SET_NULL)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    vat = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        ordering  = ['sequence', 'name']
        
    def __str__(self):
        return self.name

class Bank(BaseModel):
    
    name = models.CharField(max_length=255)
    street = models.CharField(max_length=255, blank=True, null=True)
    street2 = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.ForeignKey('State', related_name='BankState', blank=True, null=True, on_delete=models.SET_NULL)
    country = models.ForeignKey('Country', related_name='BaknCountry', blank=True, null=True,  on_delete=models.SET_NULL)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    bic = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.name


class PartnerBank(BaseModel):
    
    active = models.BooleanField(default=True)
    acc_type = models.ForeignKey('Bank', related_name='ParterBankBank', on_delete=models.CASCADE)
    acc_number = models.CharField(max_length=255)
    partner = models.ForeignKey('Partner', related_name='PartnerBank', on_delete=models.CASCADE)
    sequence = models.IntegerField(default=10)
    currency = models.ForeignKey('Currency', related_name='PartnerBankCurrency', blank=True, null=True, on_delete=models.CASCADE)
    company = models.ForeignKey('Company', related_name='PartnerBankCompany', blank=True, null=True, on_delete=models.SET_NULL)
    
    class Meta:
        ordering = ['sequence', 'id']
        
    def __str__(self):
        return self.acc_number
    
        
class PartnerCategory(BaseModel):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('PartnerCategory', related_name='ParentPartnerCategory', blank=True, null=True, on_delete=models.SET_NULL)
    active = models.BooleanField(default=True)
    partner = models.ManyToManyField('Partner')
    
    def __str__(self):
        return self.name
    
class PartnerTitle(BaseModel):
    name = models.CharField(max_length=255)
    shortcut = models.CharField(max_length=255)
    
    def __str__(self):
        return self.shortcut

COMPANY_TYPE = (
    ('individual', 'Individual'),
    ('company', 'Company')
)
class Partner(BaseModel):
    
    name = models.CharField(max_length=255)
    date = models.DateField(blank=True, null=True)
    title = models.ForeignKey('PartnerTitle', related_name='PartnerPartnerTitle', blank=True, null=True, on_delete=models.SET_NULL)
    parent = models.ForeignKey('Partner', related_name='ParentPartner', blank=True, null=True, on_delete=models.SET_NULL)
    lang = models.ForeignKey('Lang', related_name='PartnerLang', blank=True, null=True, on_delete=models.SET_NULL)
    vat = models.CharField(max_length=255, blank=True, null=True)
    bank = models.ForeignKey('PartnerBank', related_name='PartnerBankRel', blank=True, null=True, on_delete=models.SET_NULL)
    website = models.URLField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    category = models.ManyToManyField('PartnerCategory', blank=True, related_name='PartnerCategory')
    active = models.BooleanField(default=True)
    employee = models.BooleanField(default=False)
    function = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    street2 = models.CharField(max_length=255, blank=True, null=True) 
    zip_code = models.CharField(max_length=255, blank=True, null=True) 
    city = models.CharField(max_length=255, blank=True, null=True) 
    state = models.ForeignKey('State', related_name='PartnerState', blank=True, null=True, on_delete=models.SET_NULL)
    country = models.ForeignKey('Country', related_name='PartnerCountry', blank=True, null=True, on_delete=models.SET_NULL)
    email = models.EmailField(blank=True, null=True) 
    phone = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True, choices=COMPANY_TYPE)
    user = models.OneToOneField('Users', related_name='PartnerUser', blank=True, null=True,  on_delete=models.DO_NOTHING)
    
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name
    
        
class Lang(BaseModel):
    
    name = models.CharField(max_length=255) 
    code = models.CharField(max_length=255) 
    iso_code = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-active', 'name']
        
    def __str__(self):
        return self.name

class Users(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    partner = models.ForeignKey('Partner', blank=True, null=True, on_delete=models.CASCADE)
    company = models.ManyToManyField('Company', related_name='UsersCompany', blank=True)
    
    def __str__(self):
        return self.user.name
