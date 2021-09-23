from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название продукта")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self) -> str:
        return self.name
