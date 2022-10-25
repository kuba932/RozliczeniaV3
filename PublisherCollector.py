from Publisher import Publisher

class PublisherCollector:

    def __init__(self):
        publishers = []

    def createPublisherList(self, domains):

        for i in domains:
            i.sumValue()

        tempList = []
        tempListName = []
        for i in domains:
            if not tempListName.__contains__(i.name):
                tempPublisher = Publisher(i.publisher)
                tempList.append(tempPublisher)
                tempPublisher.domains.append(i)
            else:
                tempList[tempList.index(i.publisher)].domains.append(i)
        self.publishers = tempList
