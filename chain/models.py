from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Contacts(models.Model):
    email = models.EmailField(unique=True, verbose_name='email')
    country = models.CharField(max_length=100, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город')
    street = models.CharField(max_length=200, verbose_name='улица')
    building = models.CharField(max_length=100, verbose_name='номер дома')

    def __str__(self):
        return f'{self.email}, {self.city}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    model = models.CharField(max_length=100, verbose_name='модель')
    release_date = models.DateField(verbose_name='дата выхода продукта на рынок')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class RetailChain(models.Model):
    COMPANY_TYPES = [
        ('FACTORY', 'Завод'),
        ('RETAIL_NET', 'Розничная сеть'),
        ('IND_ENTREPRENEUR', 'ИП')
    ]
    name = models.CharField(max_length=100, verbose_name='название')
    type = models.CharField(max_length=50, choices=COMPANY_TYPES, verbose_name='тип компании')
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE, verbose_name='контакты')
    products = models.ManyToManyField(Product, verbose_name='продукты', **NULLABLE)
    provider = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='поставщик', **NULLABLE)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='задолженность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'
