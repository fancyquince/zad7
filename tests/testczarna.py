from src.manager import Manager
from src.models import Parameters
def test_blacklisted_tenant_is_detected():
    manager = Manager(Parameters())

    manager.blacklist = [
        {"name": "Jan Kowalski", "reason": "Debt"}
    ]

    assert manager.is_tenant_blacklisted("Jan Kowalski") is True

def test_non_blacklisted_tenant_is_not_detected():
    manager = Manager(Parameters())

    manager.blacklist = [
        {"name": "Jan Kowalski", "reason": "Debt"}
    ]

    assert manager.is_tenant_blacklisted("Adam Nowak") is False
def test_empty_blacklist_returns_false():
    manager = Manager(Parameters())

    manager.blacklist = []

    assert manager.is_tenant_blacklisted("Jan Kowalski") is False