from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class UserFeedback(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    feedback_text = models.TextField()

class UserNeedModel(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    need_json = models.JSONField()

class PitchScript(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    script = models.TextField()
    version = models.IntegerField(default=1)
