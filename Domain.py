class Domain:

    def __init__(self,contractorID, publisherID, publisher, name, forbidden, currency):
        self.contractorID = contractorID
        self.publisherID = publisherID
        self.publisher = publisher
        self.name = name
        self.forbidden = forbidden
        self.currency = currency
        self.adform = 0
        self.amazon = 0
        self.businessclick = 0
        self.connectad = 0
        self.criteo = 0
        self.eTarget = 0
        self.ix = 0
        self.magnite = 0
        self.openx = 0
        self.pubmatic = 0
        self.rtb = 0
        self.smart = 0
        self.sovrn = 0
        self.teads = 0
        self.xandr = 0
        self.adagio = 0
        self.adaptMx = 0

        self.video = 0
        self.mediafarm = 0
        self.brightcom = 0
        self.yoc = 0
        self.pubCriteo = 0

        self.wholeValue = 0

    def addAdformValue (self, value):
        self.adform = self.adform + value

    def addAmxValue (self, value):
        self.adaptMx = self.adaptMx + value

    def addAdagioValue (self, value):
        self.adagio = self.adagio + value

    def addAmazonValue (self, value):
        self.amazon = self.amazon + value

    def addBusinessClickValue (self, value):
        self.businessclick = self.businessclick + value

    def addConnectAdValue (self, value):
        self.connectad = self.connectad + value

    def addCriteoValue (self, value):
        self.criteo = self.criteo + value

    def addeTarget (self, value):
        self.eTarget =  self.eTarget + value

    def addIXValue (self, value):
        self.ix = self.ix + value

    def addMagniteValue (self, value):
        self.magnite = self.magnite + value

    def addOpenXValue (self, value):
        self.openx = self.openx + value

    def addPubmaticValue (self, value):
        self.pubmatic = self.pubmatic + value

    def addRTBValue (self, value):
        self.rtb = self.rtb + value

    def addSmartValue (self, value):
        self.smart = self.smart + value

    def addSovrnValue (self, value):
        self.sovrn = self.sovrn + value

    def addTeadsValue (self, value):
        self.teads = self.teads + value

    def addXandrValue (self, value):
        self.xandr = self.xandr + value

    def addVideoValue(self, value):
        self.video = self.video + value

    def addMediafarmValue(self, value):
        self.mediafarm = self.mediafarm + value

    def addBrightcomValue(self, value):
        self.brightcom = self.brightcom + value

    def addYocValue(self, value):
        self.yoc = self.yoc + value

    def addPubCriteoValue(self, value):
        self.pubCriteo = self.pubCriteo + value

    def sumValue (self):
        self.wholeValue = self.adform + self.wholeValue
        self.wholeValue = self.amazon + self.wholeValue
        self.wholeValue = self.businessclick + self.wholeValue
        self.wholeValue = self.connectad + self.wholeValue
        self.wholeValue = self.criteo + self.wholeValue
        self.wholeValue = self.eTarget + self.wholeValue
        self.wholeValue = self.ix + self.wholeValue
        self.wholeValue = self.magnite + self.wholeValue
        self.wholeValue = self.openx + self.wholeValue
        self.wholeValue = self.pubmatic + self.wholeValue
        self.wholeValue = self.rtb + self.wholeValue
        self.wholeValue = self.smart + self.wholeValue
        self.wholeValue = self.sovrn + self.wholeValue
        self.wholeValue = self.teads + self.wholeValue
        self.wholeValue = self.xandr + self.wholeValue
        self.wholeValue = self.adagio + self.wholeValue
        self.wholeValue = self.adaptMx + self.wholeValue

        #Nowe SSP
        self.wholeValue = self.video + self.wholeValue
        self.wholeValue = self.mediafarm + self.wholeValue
        self.wholeValue = self.brightcom + self.wholeValue
        self.wholeValue = self.yoc + self.wholeValue
        self.wholeValue = self.pubCriteo + self.wholeValue