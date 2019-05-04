import utility
import data_access
from classes import Audit_Result

def get_audit_data(site_id, targets, audit_id, subjects):
    audits = []
    question_pattern_audit = [subject.subject for subject in subjects]
    sep = " > "

    for i in range(len(targets)):
        print(targets[i].name)
        
        results = []
        
        for q in question_pattern_audit:
            result = get_result(q + sep)
            results.append(result)

        id = utility.get_id()

        a = Audit_Result(id, targets[i].name, results)
        a.site_id = site_id
        a.audit_id = audit_id

        data_access.create_audit_result(a)
        audits.append(a)

        print("---------- Audit result saved! ----------")

    return audits


def get_result(subject):
    result = input(subject).strip().lower()

    while result != "ok" and result != "ei" and result != "":
        print("Invalid value")
        result = input(subject).strip().lower()

    if result == "":
        result = "N/A"

    return result


def get_deviation(result):
    deviation = input("Deviation: ")

    return deviation