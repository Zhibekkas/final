from django.db import models
from django.contrib.auth import get_user_model
from phone_field import PhoneField
User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        related_name="profile",
        verbose_name="Profile",
        on_delete=models.CASCADE,
    )

    telephone = PhoneField(
        null=True,
        blank=True,
        verbose_name="Telephone number",
    )

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self) -> str:
        return f"Profile: {self.user.username}. {self.id}"
