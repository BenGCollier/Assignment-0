# Generated by Django 5.0.9 on 2024-09-29 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_recipe_recipecomment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(blank=True, null=True),
        ),
    ]
