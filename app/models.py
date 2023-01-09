from django.db import models
from django.contrib import admin
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=100, unique_for_date="posted", verbose_name="Заголовок")

    description = models.TextField(verbose_name="Краткое содержание")

    content = models.TextField(verbose_name="Полное содержание")

    posted = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name="Опубликована")

    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Автор")

    image = models.FileField(default='temp.jpg', verbose_name="Путь к картинке")

    def get_absolute_url(self):
        return 'Пост %d %s к %s' % (self.id, self.author, self.title)
        # return reverse("blogpost", args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Posts"

        # ordering = ["-posted"]

        verbose_name = "статья блога"

        verbose_name_plural = "статьи блога"


admin.site.register(Blog)


class Comment(models.Model):
    text = models.TextField(verbose_name="Текст комментария")

    date = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name="Дата комментария")

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор комментария")

    post = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="Статья комментария")

    image = models.FileField(default='temp.jpg', verbose_name="Путь к картинке")

    def __str__(self):
        return 'Комментарий %d %s к %s' % (self.id, self.author, self.post)

    class Meta:
        db_table = "Comment"

        ordering = ["-date"]

        verbose_name = "Комментарии к статье блога"

        verbose_name_plural = "Комментарии к статьям блога"


admin.site.register(Comment)


class Catalog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    image = models.FileField(default='temp.jpg', verbose_name="Путь к картинке")

    # def get_absolute_url(self):
    #
    #     return reverse("catalog", args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Catalog"

        # ordering = ["-posted"]

        verbose_name = "услуга"

        verbose_name_plural = "услуги"


admin.site.register(Catalog)


class Shoplist(models.Model):
    user_id = models.IntegerField(verbose_name="ID пользователя")
    product_id = models.IntegerField(verbose_name="ID продукта")
    employer_id = models.IntegerField(verbose_name="ID мастера")
    count = models.IntegerField(verbose_name="Количество")
    price = models.FloatField(verbose_name="Цена")

    # def get_absolute_url(self):
    #
    #     return reverse("catalog", args=[str(self.id)])

    # def __str__(self):
    #
    #     return f'Заказ %d %s к %s'

    class Meta:
        db_table = "Shoplist"

        # ordering = ["-posted"]

        verbose_name = "Корзина"

        verbose_name_plural = "Корзины"


admin.site.register(Shoplist)

class Order(models.Model):
    user_id = models.IntegerField(verbose_name="ID пользователя")
    product_id = models.IntegerField(verbose_name="ID продукта")
    count = models.IntegerField(verbose_name="Количество")
    price = models.FloatField(verbose_name="Цена")
    status = models.CharField(default='заказано', max_length=100, verbose_name="Статус")


    # def get_absolute_url(self):
    #
    #     return reverse("catalog", args=[str(self.id)])

    # def __str__(self):
    #
    #     return f'Заказ %d %s к %s'


    class Meta:

        db_table = "Order"

        # ordering = ["-posted"]

        verbose_name = "Заказ"

        verbose_name_plural = "Заказы"

admin.site.register(Order)


class Employer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    bio = models.TextField(verbose_name="Биография")
    image = models.FileField(default='temp.jpg', verbose_name="Путь к картинке")
    category = models.CharField(max_length=50, verbose_name="Категория")


    # def get_absolute_url(self):
    #
    #     return reverse("catalog", args=[str(self.id)])

    # def __str__(self):
    #
    #     return f'Заказ %d %s к %s'


    class Meta:

        db_table = "Employer"

        # ordering = ["-posted"]

        verbose_name = "Работник"

        verbose_name_plural = "Работники"

admin.site.register(Employer)


# гость
# клиент
# менеджер - все заказы
# администратор - добавление каталога продукции, добавление менеджеров, клиентов