from django.db import models

# Create your models here.


class AuthorManager(models.Manager):

    def get_authors_with_letter(self, letter):
        return self.filter(name__icontains=letter)


class PostManager(models.Manager):

    def all(self):
        return self.select_related('author_id').all()


class Author(models.Model):
    objects = AuthorManager()

    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=True, blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    objects = PostManager()

    STATUS = (('p', 'Опубликовано'),
              ('d', 'Предварительная версия'),
              ('h', 'Спрятан'))

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATUS, default='p')
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True, related_name='posts')
    categories = models.ManyToManyField('Category', related_name='post_set')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # post_set

