class Audit:

    def __init__(self, site, audit_info):
        self.site = site
        self.targets = []
        self.audit_info = audit_info
        self.subjects = []
        self.results = []
        self.deviations = []


class Audit_Result:

    def __init__(self, id, target, results):
        self.id = id
        self.site_id = None
        self.audit_id = None
        self.target = target
        self.results = results


class Site_Info:

    def __init__(self, id, site_name, site_address, site_manager, manager_contact):
        self.id = id
        self.site_name = site_name
        self.site_address = site_address
        self.site_manager = site_manager
        self.manager_contact = manager_contact


class Audit_Info:

    def __init__(self, id, description, schedule, auditer):
        self.id = id
        self.site_id = None
        self.description = description
        self.schedule = schedule
        self.auditer = auditer


class Target:

    def __init__(self, id, name):
        self.id = id
        self.site_id = None
        self.name = name


class Subject:

    def __init__(self, id, subject, description):
        self.id = id
        self.subject = subject
        self.description = description


class Deviation:

    def __init__(self, id,  subject_id, deviation):
        self.id = id
        self.deviation = deviation


class Person:

    def __init__(self, id, first_name, last_name, cellphone, email):
        self.id = id
        self.fist_name = first_name
        self.last_name = last_name
        self.cellphone = cellphone
        self.email = email
