from django.contrib.auth import get_user_model
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

User = get_user_model()

FACTORY = 'factory'
DISTRIBUTOR = 'distributor'
DEALERSHIP = 'dealership'
RETAIL = 'retail'
INDIVIDUAL = 'individual'
CHOICES = (
    (FACTORY, 'Завод'),
    (DISTRIBUTOR, 'Дистрибьютор'),
    (DEALERSHIP, 'Дилерский центр'),
    (RETAIL, 'Крупная розничная сеть'),
    (INDIVIDUAL, 'Индивидуальный предприниматель'),
)


class Product(models.Model):
    """Модель продоваемого продукта."""
    name = models.CharField(max_length=25, verbose_name='Название')
    model = models.CharField(max_length=25, verbose_name='Модель')
    on_sale_date = models.DateField(
        verbose_name='Дата выхода продукта на рынок'
    )

    def __str__(self):
        return f'{self.name}, {self.model}'


class Address(models.Model):
    """Модель адресса организации."""
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=50, verbose_name='Улица')
    house = models.CharField(max_length=10, verbose_name='Номер дома')

    def __str__(self):
        return (f'{self.country}, г. {self.city},'
                f' ул. {self.street}, д. {self.house}')


class Contact(models.Model):
    """Модель контактов организации."""
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        related_name='contacts',
        verbose_name='Адресс'
    )

    def __str__(self):
        return f'{self.email}, Адресс: {self.address}'


class SaleObject(MPTTModel):
    """
    Иерархическая модель торговых объектов, с множеством товаров, сотрудников,
    одним единым емэйлом и юридическим адресом.
    """
    role = models.CharField(max_length=15, choices=CHOICES)
    name = models.CharField(max_length=50, verbose_name='Название')
    contacts = models.OneToOneField(
        Contact,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Контакты'
    )
    products = models.ManyToManyField(Product, verbose_name='Продукты')
    workers = models.ManyToManyField(User, verbose_name='Сотрудники')
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Поставщик'
    )
    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Задолженность перед поставщиком'
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
