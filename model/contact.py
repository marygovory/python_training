from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, id=None,
                 nickname=None, title=None, company=None,
                 address=None, homephone=None, mobilephone=None, workphone=None, secondaryphone=None,
                 email=None, email2=None, email3=None,
                 homepage=None, address2=None, notes=None, phone2=None, all_phones_from_home_page=None,
                 all_email_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
        self.notes = notes
        self.phone2 = phone2
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email_from_home_page = all_email_from_home_page
        self.id = id

    def __repr__(self):
        return "%s:%s%s%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname,
                                                                        self.nickname, self.title,
                                                                        self.company, self.address, self.homephone,
                                                                        self.mobilephone, self.workphone,
                                                                        self.secondaryphone, self.email, self.email2,
                                                                        self.email3, self.homepage, self.address2,
                                                                        self.notes, self.phone2)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname\
            and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
