{"filter":false,"title":"models.py","tooltip":"/todo/models.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.db import models","","# Create your models here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":9,"column":24},"action":"insert","lines":["from django.db import models","","# Create your models here.","class Item(models.Model):","    ","    name = models.CharField(max_length=30, blank=False)","    done = models.BooleanField(blank=False, default=False)","","    def __str__(self):","        return self.name"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":24},"end":{"row":9,"column":24},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1566487839730,"hash":"cd5d2473f454592b65715b5794a3a2a991102cbe"}