# Generated by Django 4.1.3 on 2022-11-18 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogger_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcomment',
            options={'ordering': ['-post_date'], 'permissions': (('create_blog', 'Can Create a Blog for himself'), ('modify_blog_own', 'Can Modify his own Blog'), ('create_comment', 'Can Comment any blog'), ('modify_comment_own', 'Can Modify his Own Comments'), ('list_comment_own', 'Can See his Own Comments'))},
        ),
    ]
