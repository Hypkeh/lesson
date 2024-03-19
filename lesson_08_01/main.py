from abc import ABC, abstractmethod

class Order:

    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def make_order(self):
        for subscriber in self.subscribers:
            subscriber()
        print("Сделать заказ")


    def cancel_order(self):
        for subscriber in self.subscribers:
            subscriber.event(False)
        print("Отменить зака")


class Subscriber(ABC):

    @abstractmethod
    def event(self, order_status):
        pass


class ManagerNotification(Subscriber):

    def event(self, order_status):
        if order_status:
            self.notify_manager()
        else:
            print('Заказ отменен')

    def notify_manager(self):
        print('уведомили менеджеров')


class TreasuryNotifier(Subscriber):

    def notify_treasurer(self):
        print('Уведомили бухгалтера')

    def event(self, order_status):
        self.notify_treasurer()


class Model:

    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def save(self):
        print('Модель сохранена')
        self.post_save()

    def post_save(self):
        for subscriber in self.subscribers:
            subscriber()


class Subscriber2(ABC):

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass


class PostSaveSub(Subscriber2):

    def __call__(self, *args, **kwargs):
        print('Подписчик после сохранения модели')




m = Model()
sub = PostSaveSub()


def random_func():
    print('Function is called')

m.subscribe(sub)
m.subscribe(random_func)
m.save()