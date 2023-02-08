from PIL import Image
from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify
from django.urls import reverse


class CategorieBlogs(models.Model):
    slug = models.SlugField()
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class AuteurPost(models.Model):
    name = models.CharField(max_length=500, default="Dominique Megnidro")

    def __str__(self):
        return self.name


class Photo(models.Model):
    image = models.ImageField(verbose_name='image')
    caption = models.CharField(max_length=128, blank=True, verbose_name='légende')
    date_created = models.DateTimeField(auto_now_add=True)

    IMAGE_MAX_SIZE = (1900, 1265)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()

    def __str__(self):
        return self.caption


class BlogPost(models.Model):
    slug = models.SlugField(help_text="Exemple premier-article prendre en considération le tiret")
    categorie = models.ForeignKey(CategorieBlogs, on_delete=models.CASCADE)
    image = models.ForeignKey(Photo, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, verbose_name="titre blog")
    subtitle = models.CharField(max_length=500, verbose_name="sous titre")
    contenu = models.TextField(max_length=800, verbose_name="contenu blog")
    description = models.TextField(max_length=800, verbose_name="contenu blog 2")
    titles = models.CharField(max_length=500, verbose_name="titre 2")
    photo = models.ImageField(upload_to="photo blog")
    contenus = models.TextField(max_length=800, verbose_name="paragraph 2", blank=True)
    descriptions = models.TextField(max_length=800, verbose_name="paragraph contenu 2", blank=True)
    datepub = models.DateField(verbose_name="Date de publication", auto_now_add=True)
    published = models.BooleanField(default=False)
    auteur = models.ForeignKey(AuteurPost, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("posts:home")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-datepub']
        verbose_name = "Blog"
