from django.db import models


class TableSection(models.Model):
    title = models.CharField(100, default='')
    parent_section = models.ForeignKey(
        'TableSection',
        on_delete=models.CASCADE,
        related_name='child_sections',
        blank=True, null=True
    )

    def __str__(self):
        return self.title
