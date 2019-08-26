{"filter":false,"title":"test_models.py","tooltip":"/todo/templates/test_models.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":20,"column":52},"action":"insert","lines":["from django.test import TestCase","from .models import Item","","","class TestItemModel(TestCase):","","    def test_done_defaults_to_False(self):","        item = Item(name=\"Create a Test\")","        item.save()","        self.assertEqual(item.name, \"Create a Test\")","        self.assertFalse(item.done)","    ","    def test_can_create_an_item_with_a_name_and_status(self):","        item = Item(name=\"Create a Test\", done=True)","        item.save()","        self.assertEqual(item.name, \"Create a Test\")","        self.assertTrue(item.done)","    ","    def test_item_as_a_string(self):","        item = Item(name=\"Create a Test\")","        self.assertEqual(\"Create a Test\", str(item))"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":20,"column":52},"action":"remove","lines":["from django.test import TestCase","from .models import Item","","","class TestItemModel(TestCase):","","    def test_done_defaults_to_False(self):","        item = Item(name=\"Create a Test\")","        item.save()","        self.assertEqual(item.name, \"Create a Test\")","        self.assertFalse(item.done)","    ","    def test_can_create_an_item_with_a_name_and_status(self):","        item = Item(name=\"Create a Test\", done=True)","        item.save()","        self.assertEqual(item.name, \"Create a Test\")","        self.assertTrue(item.done)","    ","    def test_item_as_a_string(self):","        item = Item(name=\"Create a Test\")","        self.assertEqual(\"Create a Test\", str(item))"],"id":2},{"start":{"row":0,"column":0},"end":{"row":20,"column":52},"action":"insert","lines":["from django.test import TestCase","from .models import Item","","","class TestItemModel(TestCase):","","    def test_done_defaults_to_False(self):","        item = Item(name=\"Create a Test\")","        item.save()","        self.assertEqual(item.name, \"Create a Test\")","        self.assertFalse(item.done)","    ","    def test_can_create_an_item_with_a_name_and_status(self):","        item = Item(name=\"Create a Test\", done=True)","        item.save()","        self.assertEqual(item.name, \"Create a Test\")","        self.assertTrue(item.done)","    ","    def test_item_as_a_string(self):","        item = Item(name=\"Create a Test\")","        self.assertEqual(\"Create a Test\", str(item))"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":20,"column":52},"end":{"row":20,"column":52},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1566807476840,"hash":"9450003b14097030ae683bb274e3a7000f162826"}