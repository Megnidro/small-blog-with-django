from django.contrib import admin

from .models import BlogPost, AuteurPost, CategorieBlogs, Photo

admin.site.register(AuteurPost)
admin.site.register(CategorieBlogs)
admin.site.register(Photo)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("categorie", "image", "title", "subtitle", "contenu", "description", "titles",
                    "photo", "contenus", "descriptions", "datepub", "published", "auteur")

    list_editable = ("published",)


admin.site.register(BlogPost, BlogPostAdmin)
