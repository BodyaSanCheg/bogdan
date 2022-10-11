from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Product(models.Model):
    """ Модель(класс) описываюзая товар """

    name = models.CharField(max_length=150, verbose_name = 'Имя товара',)
    context = models.TextField(verbose_name = 'Описание',)

    """ 
        Что бы не использовать сложную схему с пересохранением можно ограничеть создание цены
         с двумя знаками после запятой (если дело касается копеек)
        price = models.DecimalField(decimal_places=2, validators=[MinValueValidator(0)])
    """

    price = models.PositiveIntegerField(verbose_name = 'Цена',)
    weight = models.DecimalField(verbose_name = 'Вес',max_digits = 10, decimal_places=2, validators=[MinValueValidator(0)],)
    material = models.CharField(verbose_name = 'Материал', max_length=150,)
    product_manufacturer= models.ForeignKey('Manufacturer', on_delete=models.PROTECT, null=True, verbose_name='Имя продовца')

    class Meta:
        # Имя модели
        verbose_name_plural = ("Товар")
    
    def save(self, *args, **kwargs):
        # Функция вносащая изменения перед сохранением

        self.price = self.price * 100
        super(Product, self).save(*args, **kwargs)

    def __str__(self) -> str:
        # Возвращает имя объекта
        return self.name

 

class Manufacturer(models.Model):
    """ Модель(класс) описываюзая производителя """

    name = models.CharField(verbose_name = 'Имя', max_length=150,)
    context = models.TextField(verbose_name = 'Описание',)

    class Meta:
        # Имя модели
        verbose_name_plural = ("Производитель")

    def __str__(self) -> str:
        # Возвращает имя объекта
        return self.name