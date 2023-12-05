from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Product(models.Model):
    name = models.CharField(_("name"), max_length=50)
    price = models.DecimalField(_("price"), max_digits=5, decimal_places=2)
    description = models.TextField(_("description"))
    image = models.URLField(_("image"), max_length=200)
    # image = models.ImageField(_("image"), upload_to="images/", max_length=None)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name


class Cateogory(models.Model):
    name = models.CharField(_("name"), max_length=500)

    class Meta:
        verbose_name = _("Cateogory")
        verbose_name_plural = _("Cateogories")

    def __str__(self):
        return self.name
