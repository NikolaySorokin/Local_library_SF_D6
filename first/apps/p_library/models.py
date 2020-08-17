from django.db import models
from django.urls import reverse


class Author(models.Model):
    full_name = models.CharField("имя автора", max_length=50)
    birth_year = models.SmallIntegerField("год рождения")
    country = models.CharField("страна", max_length=2)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('p_library:authors_list')

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Friend(models.Model):
    friend_name = models.CharField("имя друга", max_length=100)

    def __str__(self):
        return self.friend_name

    class Meta:
        verbose_name = "Друг"
        verbose_name_plural = "Друзья"


class Publisher(models.Model):
    pub_name = models.CharField("название издательства", max_length=100)

    def __str__(self):
        return self.pub_name

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"


class Book(models.Model):
    ISBN = models.CharField("международный книжный номер", max_length=13)
    title = models.TextField("название книги")
    description = models.TextField("описание книги")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="автор книги", related_name="books")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name="издательство", related_name="published_books")
    year_release = models.SmallIntegerField("год издания")
    copy_count = models.SmallIntegerField("количество копий", default=1)
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    took_copy = models.ManyToManyField(
        Friend, verbose_name="взят экземпляр книги",
        related_name="borrowed_books", blank=True)
    book_image = models.ImageField("изображение книги", upload_to="book_images/", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def get_absolute_url(self):
        return reverse('p_library:book_detail', kwargs={'pk': self.pk})

