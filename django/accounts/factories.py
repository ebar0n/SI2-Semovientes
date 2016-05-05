import factory
from accounts.models import Account
from faker import Factory as FakerFactory

faker = FakerFactory.create()


class AccountFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Account

    first_name = factory.LazyAttribute(lambda x: faker.name())
    last_name = factory.LazyAttribute(lambda x: faker.last_name())
    username = factory.LazyAttribute(lambda x: faker.user_name())
    password = factory.LazyAttribute(lambda x: faker.md5())
    email = factory.LazyAttribute(lambda x: faker.email())
    is_active = True
    is_staff = factory.LazyAttribute(lambda x: faker.boolean())
    is_superuser = factory.LazyAttribute(lambda x: faker.boolean())
