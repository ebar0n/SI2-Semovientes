import pytest
from accounts import factories
from accounts.models import Account


#    Factories
@pytest.fixture
def account():
    """
    Fixture responsible for build an account
    Returns Account Object:

    """
    obj = factories.AccountFactory.create()
    obj.decrypt_password = obj.password
    obj.set_password(obj.password)
    obj.save()
    return obj


@pytest.fixture
def accounts():
    """
    Fixture responsible for build a list of accounts
    Returns List of Account Objects:

    """
    return factories.AccountFactory.create_batch


#    User Test Cases
@pytest.mark.django_db
def test_add_account_valid(account, accounts):
    """
    Testing add new account correctly
    Args:
        account: Account Object
        accounts: Accounts objects
    """
    assert Account.objects.count() == 1, 'Fails to create one account'
    assert account.check_password(account.decrypt_password) is True, 'The password not match'

    number_of_objects = factories.faker.random_digit_not_null()
    # Create N objects
    accounts(number_of_objects)
    assert Account.objects.count() == number_of_objects + 1, 'Fails to create {} account(s)'.format(number_of_objects)
