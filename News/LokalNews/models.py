from audioop import reverse
from django.db import models


class News(models.Model):
    title = models.CharField("Заголовок", max_length=250)
    picture = models.ImageField("Картинка")
    anons = models.CharField("Анонс", max_length=250)
    text = models.TextField("Текст")
    authors = models.ForeignKey(
        "Authors", on_delete=models.CASCADE, verbose_name="Автор"
    )
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE, verbose_name="Жанры")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.pk})

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Authors(models.Model):
    name = models.CharField("Имя", max_length=20)
    lastname = models.CharField("Фамилия", max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Genre(models.Model):
    classic = models.CharField(max_length=250)

    def __str__(self):
        return self.classic

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
