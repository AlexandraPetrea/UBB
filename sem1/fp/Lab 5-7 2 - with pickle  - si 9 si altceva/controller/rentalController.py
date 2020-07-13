from shell import * 
from datetime import datetime 
from datetime import date
#import datetime

import time
class RentalController:

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

    def search(self, criteriu):
        return self._repo.search(criteriu)

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


    def mostRented(self):
        mostRentedDict = []
        mostRentedByNumberOfDays = []

        for i in range(0, len(self._repo)):
            mid = self._repo.get(i)[2]

            d1 = self._repo.get(i)[3]
            d2 = self._repo.get(i)[5]

            if d2 is None:
                d2 = self.todaysDate()


            number_of_days = days_between(d1, d2)

            ok = True

            for l in mostRentedDict:
                if l[0] == mid:
                    l[1] += number_of_days
                    ok = False

            if ok:
                mostRentedDict.append([mid, number_of_days])

            ok = True

            for l in mostRentedByNumberOfDays:
                if l[0] == mid:
                    l[1] += number_of_days
                    ok = False

            if ok:
                mostRentedByNumberOfDays.append([mid, number_of_days])

        for i in range(0, len(mostRentedDict) - 1):
            for j in range(i + 1, len(mostRentedDict) - 1):
                a = mostRentedDict[i][1]
                b = mostRentedDict[j][1]
                if a < b:
                    mostRentedDict[i], mostRentedDict[j] = mostRentedDict[j], mostRentedDict[i]

        for i in range(0, len(mostRentedByNumberOfDays) - 1):
            for j in range(i + 1, len(mostRentedByNumberOfDays) - 1):
                a = mostRentedByNumberOfDays[i][1]
                b = mostRentedByNumberOfDays[j][1]
                if a < b:
                    mostRentedByNumberOfDays[i], mostRentedByNumberOfDays[j] = mostRentedByNumberOfDays[j], mostRentedByNumberOfDays[i]

        return mostRentedDict, mostRentedByNumberOfDays

            

    def todaysDate(self):
        today = datetime.now()

        year = today.year
        month = today.month
        day = today.day

        return date(year, month, day)

    def getSortedClients(self):
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
        '''
        for i in range(0, len(sorted_clients)):
            for j in range(i + 1, len(sorted_clients)):
                if sorted_clients[i][1] > sorted_clients[j][1]:
                    sorted_clients[i], sorted_clients[j] = sorted_clients[j], sorted_clients[i]
        '''
        sorted_clients = shellSort(sorted_clients, '>')
        return sorted_clients



    def author(bookRepository):
        mostRented = []
        ok = True
        for i in range(0, len(bookRepository._repo)):
            ok = True
            author = bookRepository._repo.get(i)[3]
            index = bookRepository._repo.get(i)[0]
            mostRented.append([author, index])


        return mostRented

    def getSortedAuthors(self):
        sorted_author = []

        for i in range(0, len(self._repo)):
            indexBook = self._repo.get(i)[2]
            sorted_author.append(indexBook)
        return sorted_author

    def Lista(self, author, author_list):
        noua = []
        for i in range(0, len(author_list)):
            for j in range(0, len(author)):
                if author_list[i] == author[j][1]:
                    ok = False
                    for w in range(0, len(noua)):
                        if noua[w][0] == author[j][0]:
                            noua[w][1] += 1
                            ok = True
                    if ok == False:
                        noua.append([author[j][0], 1])

        for i in range(0, len(noua)-1):
            for j in range(i+1, len(noua)):
                if noua[i][1] < noua[j][1]:
                    noua[i], noua[j] = noua[j], noua[i]
        return noua

    def getRentals(self):
        book_list = []
        for i in range(0, len(self._repo)):
            book_id = self._repo.get(i)[2]
            return_date = self._repo.get(i)[5]

            if return_date is None:
                book_list.append(book_id)

        return book_list

    def getLateRentals(self):
        '''
        descr: a list with late rentals
        out: the list
        '''
        late_rentals = []

        for i in range(0, len(self._repo)):
            id = self._repo.get(i)[0]
            due_date = self._repo.get(i)[4]
            return_date = self._repo.get(i)[5]

            todaysDate = self.todaysDate()

            if return_date is None and due_date < todaysDate:
                number_of_days = due_date - todaysDate

                ok = True

                for l in late_rentals:
                    if l[0] == id:
                        l[1] += number_of_days
                        ok = False

                if ok:
                    late_rentals.append([id, number_of_days])
                print(late_renatls.getAll())

        for i in range(0, len(late_rentals)):
            for j in range(i + 1, len(late_rentals)):
                if late_rentals[i][1] > late_rentals[j][1]:
                    late_rentals[i], late_rentals[j] = late_rentals[j], late_rentals[i]

        return late_rentals

    def getRentalInformation(self, id):
        '''
        descr: gen all the information about a rental
        in: id - the id of rental
        out: the rental
        '''
        s = ''
        for i in range(len(0,self._repo)):
            if self._repo.get(i)[0] == id:
                book_id = self._repo.get(i)[2]
                client_id = self._repo.get(i)[1]
                rental_date = self._repo.get(i)[3]
                due_date = self._repo.get(i)[5]

                s += str(id) + ' ' + str(book_id) + ' ' + str(client_id) + ' ' + str(rental_date) + ' ' + str(due_date)

        return s

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    delta = d2 - d1
    return delta.days
    '''

class ControlerWithUndo(Controller):
    def __init__(self, undoController, rentalController, repository):
        Controller._init(self, repository)
        self.__rentalController = rentalController
        self._undoController = undoController

    def create(self, id, title, descr, author):
        book = bookController.create(self, id, title, descr, author)

        redo = FunctionCall(self.create, id, title, descr, author)
        undo = FunctionCall(self._delete, bookId)
        operation = Operation(redo, undo)
        self._undoController.recordOperation(operation)
        return book
    '''
