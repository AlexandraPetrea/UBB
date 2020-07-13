from domaine import * 
from datetime import datetime 
from datetime import date
#import datetime
import time
class ClientController:

    def __init__(self, repo):
        self._repo = repo

    def add(self, item):
        return self._repo.add(item)

    def delete(self, index):
        return self._repo.remove(index)

    def update(self, object):
        return self._repo.update(object)

    def returns(self, id):
        index = self._repo.find(id)

        returnDate = datetime.today()
        self._repo[index].setDate(returnDate)

    def searchC(self, criteriu):
        return self._repo.search1(criteriu)

    def list1(self):
        return self._repo.__str__()

    def validity(self, id):
        for i in range(0, len(self._repo)):
            if self._repo.get(i)[0] == id:
                return False
        return True

    def status(self, op):
        if op == '1':
            a, b = self.mostRented()
            return a, b
        elif op == '2':
            client_list = self.getSortedClients()
            return client_list
        elif op == '3':
            rental_list = self.getSortedAuthors()
            return rental_list
        else:
            late_rentals = self.getLateRentals()
            return late_rentals

    def todaysDate(self):
        '''
        descr: today date in a specific format
        '''
        today = datetime.now()

        year = today.year
        month = today.month
        day = today.day

        return date(year, month, day)

    def getSortedClients(self):
        '''
        descr: a list with most actived clients 
        '''
        sorted_clients = []

        for i in range(0, len(self._repo)):
            client_id = self._repo.get(i)[1]
            rental_date = self._repo.get(i)[3]
            return_date = self._repo.get(i)[5]

            if return_date is None:
                return_date = self.todaysDate()

            number_of_days = days_between(rental_date, return_date)

            ok = True

            for l in sorted_clients:
                if l[0] == client_id:
                    l[1] += number_of_days
                    ok = False

            if ok:
                sorted_clients.append([client_id, number_of_days])

        for i in range(0, len(sorted_clients)):
            for j in range(i + 1, len(sorted_clients)):
                if sorted_clients[i][1] > sorted_clients[j][1]:
                    sorted_clients[i], sorted_clients[j] = sorted_clients[j], sorted_clients[i]

        return sorted_clients
    

    

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    delta = d2 - d1
    return delta.days

class ClientValidator:
    def validate(self,cl):
        '''
        verify if the parameters of cl object are valid
        raise errors if there is at least 1 invalid data
        input: cl:client object
        '''
        errors=''
        if cl[0] != int(cl[0]):
            errors+='Id must be an integer number\n'
        elif cl[0] < 0:
            errors+='Id must be greater than 0\n'
        if len(cl[1])==0:
            errors+='Client name must have at list 3 caracters'
        p=cl[1]
        for i in range(0,len(p)):
            if ((ord(p[i])<65)or((ord(p[i])>90)and(ord(p[i])<97))or(ord(p[i])>122))and ord(p[i])!=32:
                    errors+='Client name must contain only letters'
        if len(errors)>0:
            return 1
    