from Publisher import Publisher
from Contractor import Contractor

class Collector:

    def __init__(self):
        self.publishers = []
        self.contractors = []

    def createPublisherList(self, domains):

        for i in domains:
            i.sumValue()

        tempList = []
        tempListName = []
        for i in domains:
            if not tempListName.__contains__(i.publisher): #gdy tymczasowa lista z publisherami nie zawiera danej nazwy
                tempPublisher = Publisher(i.publisher) # tymaczsowy obiekt publishera
                tempPublisher.id =i.publisherID
                tempPublisher.contractorID = i.contractorID
                tempList.append(tempPublisher) # tymczasowa lista z publisherami
                tempPublisher.domains.append(i) # dodanie domeny z wiersza
                tempListName.append(i.publisher) # Dodanie nazwy publishera z tymczasowymi nazwami wydawców
            else:
                tempList[tempListName.index(i.publisher)].domains.append(i)
        self.publishers = tempList

    def createContractors (self,reader):
        contractorsData = reader.getContractors()

        for i in contractorsData["Contractor Name"]:
            id = contractorsData["Contractor ID"][(contractorsData["Contractor Name"].tolist()).index(i)]

            tempContractor = Contractor()
            tempContractor.id = id
            tempContractor.name = i
            self.contractors.append(tempContractor)

    def matchPublishersAndContractors (self):

        for i in self.contractors:
            for j in self.publishers:
                if i.id == j.contractorID:
                    i.publishers.append(j)



            #
            # for j in i.publishersIDs:
            #     tempID = j
            #     for x in self.publishers:
            #         if x.id == tempID:
            #             i.publishers.append(x)


