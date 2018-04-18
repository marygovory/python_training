# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    new_contact = Contact(firstname="111", middlename="111", lastname="111", nickname="111", title="111",
                          company="111", address="111", home="111", mobile="111", work="111", fax="111",
                          email="111", email2="111", email3="111", homepage="111", address2="111",
                          notes="111", phone2="111")
    app.contact.create_contact(new_contact)
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    new_contact = Contact(firstname="", middlename="", lastname="", nickname="", title="",
                              company="", address="", home="", mobile="", work="", fax="",
                              email="", email2="", email3="", homepage="", address2="",
                              notes="", phone2="")
    app.contact.create_contact(new_contact)
    app.session.logout()