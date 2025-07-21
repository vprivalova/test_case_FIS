import json
from datetime import *

with open('credit_profile.json', 'r', encoding="utf-8") as f:
    f_data = json.load(f)


def checking1(data):
    birth_dt = datetime.strptime(data['birthDate'], "%Y-%m-%dT%H:%M:%S.%fZ")
    now = datetime.now()
    age = int((now - birth_dt).days / 365)
    if age < 20:
        return False
    else:
        return True


def checking2(data):
    issue_dt = datetime.strptime(data['passport']['issuedAt'], "%Y-%m-%dT%H:%M:%S.%fZ")
    birth_dt = datetime.strptime(data['birthDate'], "%Y-%m-%dT%H:%M:%S.%fZ")
    now = datetime.now()
    age = int((now - birth_dt).days / 365)
    if age < 45:
        twenty_dt = birth_dt.replace(year=birth_dt.year + 20)
        if twenty_dt < issue_dt:
            return True
        else:
            return False
    else:
        fortyfive_dt = birth_dt.replace(year=birth_dt.year + 45)
        if fortyfive_dt < issue_dt:
            return True
        else:
            return False


def checking3(data):
    overall_penalty = 0
    second_type_penalty = 0
    for elem in data['creditHistory']:
        if elem['type'] == 'Кредитная карта':
            if elem['currentOverdueDebt'] == 0 and elem['numberOfDaysOnOverdue'] <= 30:
                pass
            else:
                overall_penalty += 1
        else:
            if elem['currentOverdueDebt'] == 0 and elem['numberOfDaysOnOverdue'] <= 15 and second_type_penalty < 2:
                pass
            elif elem['currentOverdueDebt'] == 0 and 15 < elem['numberOfDaysOnOverdue'] <= 60 and second_type_penalty < 2:
                second_type_penalty += 1
            else:
                overall_penalty += 1
    if overall_penalty == 0:
        return True
    else:
        return False


def full_checkup(data):
    if checking1(data) is True:
        if checking2(data) is True:
            if checking3(data) is True:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


print(full_checkup(f_data))
