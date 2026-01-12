from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Intermediary model for Project <-> Skill with ordering
class ProjectSkill(models.Model):
    project = models.ForeignKey('platform_web.Project', on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        unique_together = ('project', 'skill')

    def __str__(self):
        return f"{self.project} - {self.skill} (Order: {self.order})"
