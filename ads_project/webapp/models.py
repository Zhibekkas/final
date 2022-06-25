from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Category(models.Model):
    category = models.CharField(verbose_name='Title', max_length=300)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category


class Advertisement(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True, verbose_name='Title')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Description")
    image = models.ImageField(verbose_name='Image', null=True, blank=True, upload_to='uploads')
    author = models.ForeignKey(
        User,
        related_name="ads",
        verbose_name="Author",
        on_delete=models.CASCADE

    )
    category = models.ForeignKey('webapp.Category', on_delete=models.CASCADE, verbose_name="Category",
                                 null=False, blank=False, related_name='ads')
    created_at = models.DateField(auto_now_add=True, verbose_name='Created at')
    modified_at = models.DateField(auto_now=True, verbose_name='Modified at')
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    is_moderated = models.BooleanField(default=False, verbose_name='Moderation status')
    published_at = models.DateField(auto_now=True, verbose_name='Published at')

    class Meta:
        verbose_name = 'Ad'
        verbose_name_plural = 'Ads'

    def __str__(self):
        return self.title
