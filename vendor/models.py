from django.db import models

# Create your models here.

class Vendor(models.Model):
    """Model definition for Vendor."""
    name = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta:
        """Meta definition for Vendor."""

        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'

    def __str__(self):
        """Unicode representation of Vendor."""
        return self.name
