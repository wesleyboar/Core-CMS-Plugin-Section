# Generated by Django 3.1.13 on 2022-01-12 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('djangocms_style', '0007_style_template'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaccsiteSection',
            fields=[
                ('style_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='djangocms_style.style')),
                ('custom_class_name', models.CharField(choices=[('o-section--style-light', 'Light Background, Dark Text'), ('o-section--style-dark', 'Dark Background, Light Text')], default='o-section--style-light', max_length=255, verbose_name='Style')),
                ('custom_tag_type', models.CharField(choices=[('section', 'section'), ('article', 'article'), ('header', 'header'), ('footer', 'footer'), ('aside', 'aside'), ('div', 'div')], default='section', max_length=255, verbose_name='Tag')),
            ],
            options={
                'abstract': False,
            },
            bases=('djangocms_style.style',),
        ),
    ]
