import json
from datetime import *


class CheckUp:
    def __init__(self, file):
        with open(file, 'r', encoding="utf-8") as f:
            self.data = json.load(f)

    @staticmethod
    def checking1(data):
        birth_dt = datetime.strptime(data['birthDate'], "%Y-%m-%dT%H:%M:%S.%fZ")
        now = datetime.now()
        age = int((now - birth_dt).days / 365)
        if age < 20:
            return False
        else:
            return True

    @staticmethod
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

    @staticmethod
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

    def full_checkup(self):
        if CheckUp.checking1(self.data) is True:
            if CheckUp.checking2(self.data) is True:
                if CheckUp.checking3(self.data) is True:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


print(CheckUp('credit_profile.json').full_checkup())
