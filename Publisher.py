class Publisher:

    def __init__(self, name):
        self.id = 0
        self.contractorID = 0
        self.name = name
        self.domains = []
        self.sspValue = 0
        self.numberOfDomains = 0
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

    def getByName (self):
        return self.name

    def sumSspValue (self):
        tempAmount = 0
        for i in self.domains:
            tempAmount = tempAmount + i.adform
            tempAmount = tempAmount + i.amazon
            tempAmount = tempAmount + i.businessclick
            tempAmount = tempAmount + i.connectad
            tempAmount = tempAmount + i.criteo
            tempAmount = tempAmount + i.eTarget
            tempAmount = tempAmount + i.ix
            tempAmount = tempAmount + i.magnite
            tempAmount = tempAmount + i.openx
            tempAmount = tempAmount + i.pubmatic
            tempAmount = tempAmount + i.rtb
            tempAmount = tempAmount + i.smart
            tempAmount = tempAmount + i.sovrn
            tempAmount = tempAmount + i.teads
            tempAmount = tempAmount + i.xandr
            tempAmount = tempAmount + i.adagio
            tempAmount = tempAmount + i.adaptMx
        self.sspValue = tempAmount

    def addNumberOfDomains (self):
        self.numberOfDomains = len(self.domains)

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




