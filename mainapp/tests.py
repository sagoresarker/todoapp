from django.test import TestCase
from django.urls import reverse
from .models import Todo

class TodoModelTest(TestCase):
    def setUp(self):
        self.todo = Todo.objects.create(title='Title from Testing', description="Sample Description")
    
    def test_todo(self):
        self.assertEqual(str(self.todo), 'Title from Testing')


class OtherTest(TestCase):
    def setUp(self):
        self.todo = Todo.objects.create(title='Title from Testing', description="Sample Description")

    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Title from Testing')
    
    def test_create(self):
        response = self.client.post(reverse('create'), { 'title':'Another todo created', 'description':"Sample Description"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Todo.objects.last().title, 'Another todo created')
    
    def test_update(self):
        response = self.client.post(reverse('update', args=[self.todo.id]), { 'title':'Updated Todo', 'description':'Updated in testing'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Todo.objects.get(id=self.todo.id).title, "Updated Todo")

    def test_delete(self):
        response = self.client.post(reverse('delete', args=[self.todo.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Todo.objects.filter(id=self.todo.id).exists())