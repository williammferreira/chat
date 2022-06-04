from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class AppGroup(models.Model):
    """Group Apps together."""

    name = models.CharField(max_length=50, verbose_name=_('name'))

    # 0 is the most important, 1 is very important, 2 is important, 3 is relevent, 4 is least important
    importance = models.PositiveIntegerField(verbose_name=_('importance'), default=4)

    class Meta:
        """Meta definition for AppGroup."""

        verbose_name = _('App Group')
        verbose_name_plural = _('App Groups')

    def __str__(self):
        """Unicode representation of AppGroup."""
        return self.name

class App(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("name"))
    url = models.CharField(_('URL'), max_length=50)
    logo = models.ImageField(_('Logo'), upload_to='app_images')

    # Cost per year
    cost_yearly = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name=_("cost yearly"))
    cost_monthely = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name=_("cost monthely"))
    group = models.ForeignKey(AppGroup, on_delete=models.CASCADE, blank=True, null=True, default=None, verbose_name=_('group'))

    def get_cost(self):
        return "$" + str(self.cost)

    class Meta:
        verbose_name = _('App')
        verbose_name_plural = _('Apps')

    def __str__(self):
        return self.name
