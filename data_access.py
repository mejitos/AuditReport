from classes import Site_Info
from classes import Target
from classes import Audit_Info
from classes import Subject
from classes import Audit_Result
import os.path
import csv

sites_file = "data/sites.csv"
targets_file = "data/targets.csv"
audit_infos_file = "data/audit_infos.csv"
subjects_file = "data/subjects.csv"
audit_results_file = "data/audit_results.csv"
data_path = "./data"


def check_for_dir():
    if os.path.isdir(data_path):
        return
    else:
        os.mkdir(data_path)


def create_site(site):
    sites = convert_to_sites()
    sites.append(site)
    save_to_sites_file(sites)


def convert_to_sites():
    sites = []

    if os.path.isfile(sites_file):
        with open(sites_file, "r") as csv_file:
            csv_reader = csv.reader(csv_file)

            for line in csv_reader:
                site = Site_Info(line[0], line[1], line[2], line[3], line[4])
                sites.append(site)

    return sites


def save_to_sites_file(sites):
    with open(sites_file, "w", newline='') as wf:
        csv_writer = csv.writer(wf)
        for site in sites:
            data = []
            data.append(site.id)
            data.append(site.site_name)
            data.append(site.site_address)
            data.append(site.site_manager)
            data.append(site.manager_contact)
            csv_writer.writerow(data)


def create_target(target):
    targets = convert_to_targets()
    targets.append(target)
    save_to_targets_file(targets)


def convert_to_targets():
    targets = []

    if os.path.isfile(targets_file):
        with open(targets_file, "r") as csv_file:
            csv_reader = csv.reader(csv_file)

            for line in csv_reader:
                target = Target(line[0], line[2])
                target.site_id = line[1]
                targets.append(target)

    return targets


def save_to_targets_file(targets):
    with open(targets_file, "w", newline='') as wf:
        csv_writer = csv.writer(wf)
        for target in targets:
            data = []
            data.append(target.id)
            data.append(target.site_id)
            data.append(target.name)
            csv_writer.writerow(data)


def get_targets_by_site_id(site_id):
    targets = convert_to_targets()
    chosen_targets = []

    with open(targets_file, "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            if line[1] == site_id:
                for target in targets:
                    if line[0] == target.id:
                        chosen_targets.append(target)

    return chosen_targets


def create_subject(subject):
    subjects = convert_to_subjects()
    subjects.append(subject)
    save_to_subjects_file(subjects)


def convert_to_subjects():
    subjects = []

    if os.path.isfile(subjects_file):
        with open(subjects_file, "r") as csv_file:
            csv_reader = csv.reader(csv_file)

            for line in csv_reader:
                subject = Subject(line[0], line[1], line[2])
                subjects.append(subject)

    return subjects


def save_to_subjects_file(subjects):
    with open(subjects_file, "w", newline='') as wf:
        csv_writer = csv.writer(wf)
        for subject in subjects:
            data = []
            data.append(subject.id)
            data.append(subject.category)
            data.append(subject.description)
            csv_writer.writerow(data)


def create_audit_info(info):
    audit_infos = convert_to_audit_infos()
    audit_infos.append(info)
    save_to_audit_info_file(audit_infos)


def convert_to_audit_infos():
    audit_infos = []

    if os.path.isfile(audit_infos_file):
        with open(audit_infos_file, "r") as csv_file:
            csv_reader = csv.reader(csv_file)

            for line in csv_reader:
                info = Audit_Info(line[0], line[2], line[3], line[4])
                info.site_id = line[1]
                audit_infos.append(info)

    return audit_infos


def save_to_audit_info_file(infos):
    with open(audit_infos_file, "w", newline='') as wf:
        csv_writer = csv.writer(wf)
        for info in infos:
            data = []
            data.append(info.id)
            data.append(info.site_id)
            data.append(info.description)
            data.append(info.schedule)
            data.append(info.auditer)
            csv_writer.writerow(data)


def create_audit_result(result):
    results = convert_to_audit_results()
    results.append(result)
    save_to_audit_results_file(results)


def convert_to_audit_results():
    results = []

    if os.path.isfile(audit_results_file):
        with open(audit_results_file, "r") as csv_file:
            csv_reader = csv.reader(csv_file)

            for line in csv_reader:
                result = []
                for i in range(4, len(line)):
                    result.append(line[i])

                audit = Audit_Result(line[0], line[3], result)
                audit.site_id = line[1]
                audit.audit_id = line[2]
                results.append(audit)

    return results


def save_to_audit_results_file(results):
    with open(audit_results_file, "w", newline='') as wf:
        csv_writer = csv.writer(wf)
        for result in results:
            data = []
            data.append(result.id)
            data.append(result.site_id)
            data.append(result.audit_id)
            data.append(result.target)
            for r in result.results:
                data.append(r)
            csv_writer.writerow(data)