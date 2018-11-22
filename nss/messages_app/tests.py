from django.test import TestCase
from django.contrib.auth.models import User
from .models import Thread, Message
from project_app.models import project


class ThreadTestCase(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'user1',
            'password': 'test1234'}
        self.user1= User.objects.create_user(**self.credentials)
        self.user2= User.objects.create_user('user2', None, 'tes1234')
        self.user3= User.objects.create_user('user3', None, 'tes1234')

        self.thread = Thread.objects.create()

    def test_add_users_to_thread(self):
        self.thread.users.add(self.user1, self.user2)
        self.assertEqual(len(self.thread.users.all()),2)

    def test_filter_test_by_users(self):
        self.thread.users.add(self.user1, self.user2)
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertEqual(self.thread, threads[0])

    def test_filter_non_existent_thread(self):
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertEqual(len(threads),0)

    def test_add_message_to_thread(self):
        self.thread.users.add(self.user1, self.user2)
        message1 = Message.objects.create(user=self.user1, content="HOLa krnal")
        message2 = Message.objects.create(user=self.user2, content="Sup")
        self.thread.messages.add(message1, message2)
        self.assertEqual(len(self.thread.messages.all()),2)

        for message in self.thread.messages.all():
            print("({}): {}".format(message.user, message.content))
        #The number of messages in the thread is 2

    def test_add_message_from_user_not_in_thread(self):
        self.thread.users.add(self.user1, self.user2)
        message1 = Message.objects.create(user=self.user1, content="HOLa krnal")
        message2 = Message.objects.create(user=self.user2, content="Sup")
        message3 = Message.objects.create(user=self.user3, content="Soy espía")
        self.thread.messages.add(message1, message2, message3)
        self.assertEqual(len(self.thread.messages.all()),2)

    def test_find_thread_with_custom_manager(self):
        self.thread.users.add(self.user1, self.user2)
        thread = Thread.objects.find(self.user1, self.user2)
        self.assertEqual(self.thread,thread)

    def test_find_or_create_thread_with_custom_manager(self):
        self.thread.users.add(self.user1, self.user2)
        thread = Thread.objects.find_or_create(self.user1, self.user2)
        self.assertEqual(self.thread,thread)
        #not exist a thread with these two, then it has too create it
        thread = Thread.objects.find_or_create(self.user1, self.user3)
        self.assertIsNotNone(thread)

    def test_send_message_to_user(self):
        response = self.client.post('/user/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)




        ###Evitar que se envíen mensajes vacíos
