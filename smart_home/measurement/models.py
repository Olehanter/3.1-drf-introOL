from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=30, verbose_name="Dатчик")
    description = models.CharField(max_length=50, null=True, verbose_name="Описание")

    def __str__(self):
        return self.name


class Measurement(models.Model):
    temperature = models.FloatField(verbose_name="Температура")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата-время"
    )
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    photo = models.ImageField(
        blank=True,
        null=True,
        verbose_name="Фото",
    )
