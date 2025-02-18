# Generated by Django 3.1.3 on 2023-07-04 21:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_choice_question_submission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='question',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='question',
            name='text',
        ),
        migrations.AddField(
            model_name='question',
            name='courses',
            field=models.ManyToManyField(to='onlinecourse.Course'),
        ),
        migrations.AddField(
            model_name='question',
            name='marks',
            field=models.FloatField(default=1.0),
        ),
        migrations.AddField(
            model_name='question',
            name='question_text',
            field=models.CharField(default='This is a sample question.', max_length=500),
        ),
        migrations.AddField(
            model_name='submission',
            name='date_submitted',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='submission',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='onlinecourse.question'),
        ),
    ]
