from pathlib import Path
from Domain import Domain
from Contractor import Contractor
import pandas as pd
import re
import datetime


class Reader:

    def __init__(self):
        self.path = str(Path(__file__).parent.parent.parent)
        dt = datetime.datetime.today()
        self.date = r"_0" + str(dt.month-1) + r"." + str(dt.year)
        self.domainFile = pd.read_excel(self.path + r"\Domeny.xlsx", "Domeny")
        self.domainData = pd.DataFrame(self.domainFile, columns=["Contractor ID", "Publisher ID", "Publisher", "Domain", "Forbidden", "Currency"])
        self.contractorFile = pd.read_excel(self.path + r"\Kontrahent.xlsx", "Kontrahent")
        self.contractorData = pd.DataFrame(self.contractorFile, columns=["Contractor ID", "Contractor Name"])

    def printPath (self):
        print(self.path)

    def getContractors (self):
        return self.contractorData

    def getDomainsAsList (self):
        # Tworzenie obiektów wyszukiwanych domen
        domains = []
        for i in self.domainData["Domain"]:
            tempName = i
            tempContractorID = self.domainData["Contractor ID"][(self.domainData["Domain"].tolist()).index(i)]
            tempPublisherID = self.domainData["Publisher ID"][(self.domainData["Domain"].tolist()).index(i)]
            tempPublisher = self.domainData["Publisher"][(self.domainData["Domain"].tolist()).index(i)]
            tempForbidden = self.domainData["Forbidden"][(self.domainData["Domain"].tolist()).index(i)]
            tempCurrency = self.domainData["Currency"][(self.domainData["Domain"].tolist()).index(i)]
            domains.append(Domain(tempContractorID, tempPublisherID, tempPublisher, tempName, tempForbidden, tempCurrency))

        return domains

    def getSSPsData (self, domain):
        self.getAdformData(domain)
        self.getAmazonData(domain)
        self.getBusinessClickData(domain)
        self.getConnectAdData(domain)
        self.getCriteoData(domain)
        self.getetargetData(domain)
        self.getIndexData(domain)
        self.getMagniteData(domain)
        self.getOpenXData(domain)
        self.getPubmaticData(domain)
        self.getrtbData(domain)
        self.getSmartData(domain)
        self.getSovrnData(domain)
        self.getTeadsData(domain)
        self.getXandrData(domain)
        self.getAdagioData(domain)
        self.getAdaptMX(domain)
        self.getVideoData(domain)
        self.getMediaFarmData(domain)
        self.getBrightcomFileData(domain)
        self.getYocData(domain)
        self.getPCriteoData(domain)

    def getAdformData(self, domain):
        adformFile = pd.read_excel(self.path + r"\WTG_Adform" + self.date + ".xlsx", "Final")
        adformData = pd.DataFrame(adformFile, columns=["Site", "Revenue EUR Net", "Revenue USD Net", "Revenue PLN Net"])

        match = []

        for i in adformData["Site"]:
            if re.search(domain.name, i, re.IGNORECASE):
                match.append(i)

        tempForbidden = str(domain.forbidden)
        list = tempForbidden.split(", ")

        for x in match[0:]:
            if list != ['nan']:
                for y in list:
                    if re.search(y,x, re.IGNORECASE):
                        match.remove(x)

        end_value = 0

        # Dodawanie wartości SSP
        for i in match:
            if domain.currency == "EUR":
                end_value = end_value + (adformData["Revenue EUR Net"][adformData["Site"][adformData["Site"] == i].index[0]])
            if domain.currency == "USD":
                end_value = end_value + (adformData["Revenue USD Net"][adformData["Site"][adformData["Site"] == i].index[0]])
            if domain.currency == "PLN":
                end_value = end_value + (adformData["Revenue PLN Net"][adformData["Site"][adformData["Site"] == i].index[0]])

        domain.addAdformValue(end_value)

    def getAdaptMX(self, domain):
        amxFile = pd.read_excel(self.path + r"\WTG_AdaptMX" + self.date + ".xlsx", "Final")
        amxData = pd.DataFrame(amxFile, columns=["Site", "Revenue USD Net", "Revenue EUR Net", "Revenue PLN Net"])

        print("getAdaptMX")

        match = []

        for i in amxData["Site"]:
            if re.search(domain.name, i, re.IGNORECASE):
                match.append(i)

        tempForbidden = str(domain.forbidden)
        list = tempForbidden.split(", ")

        for x in match[0:]:
            if list != ['nan']:
                for y in list:
                    if re.search(y,x, re.IGNORECASE):
                        match.remove(x)

        end_value = 0

        # Dodawanie wartości SSP
        for i in match:
            if domain.currency == "EUR":
                end_value = end_value + (amxData["Revenue EUR Net"][amxData["Site"][amxData["Site"] == i].index[0]])
            if domain.currency == "USD":
                end_value = end_value + (amxData["Revenue USD Net"][amxData["Site"][amxData["Site"] == i].index[0]])
            if domain.currency == "PLN":
                end_value = end_value + (amxData["Revenue PLN Net"][amxData["Site"][amxData["Site"] == i].index[0]])

        domain.addAmxValue(end_value)

    def getAdagioData(self, domain):

        adagioFile = pd.read_excel(self.path + r"\WTG_Adagio" + self.date + ".xlsx")
        adagioData = pd.DataFrame(adagioFile, columns=["site", "Revenue EUR Net", "Revenue USD Net", "Revenue PLN Net"])

        match = []

        for i in adagioData["site"]:
            if re.search(domain.name, i, re.IGNORECASE):
                match.append(i)

        tempForbidden = str(domain.forbidden)
        list = tempForbidden.split(", ")

        for x in match[0:]:
            if list != ['nan']:
                for y in list:
                    if re.search(y, x, re.IGNORECASE):
                        match.remove(x)

        end_value = 0

        # Dodawanie wartości SSP
        for i in match:
            if domain.currency == "EUR":
                end_value = end_value + (adagioData["Revenue EUR Net"][adagioData["site"][adagioData["site"] == i].index[0]])
            if domain.currency == "USD":
                end_value = end_value + (adagioData["Revenue USD Net"][adagioData["site"][adagioData["site"] == i].index[0]])
            if domain.currency == "PLN":
                end_value = end_value + (adagioData["Revenue PLN Net"][adagioData["site"][adagioData["site"] == i].index[0]])

        domain.addAdagioValue(end_value)

    def getAmazonData(self, domain):
        amazonFile = pd.read_excel(self.path + r"\WTG_Amazon" + self.date + ".xlsx", "Final")
        amazonData = pd.DataFrame(amazonFile, columns=["Site", "Revenue USD Net", "Revenue EUR Net", "Revenue PLN Net"])


        match = []

        for i in amazonData["Site"]:
            if re.search(domain.name, i, re.IGNORECASE):
                match.append(i)

        tempForbidden = str(domain.forbidden)
        list = tempForbidden.split(", ")

        for x in match[0:]:
            if list != ['nan']:
                for y in list:
                    if re.search(y,x, re.IGNORECASE):
                        match.remove(x)


        end_value = 0

        # Dodawanie wartości SSP
        for i in match:
            if domain.currency == "EUR":
                end_value = end_value + (amazonData["Revenue EUR Net"][amazonData["Site"][amazonData["Site"] == i].index[0]])
            if domain.currency == "USD":
                end_value = end_value + (amazonData["Revenue USD Net"][amazonData["Site"][amazonData["Site"] == i].index[0]])
            if domain.currency == "PLN":
                end_value = end_value + (amazonData["Revenue PLN Net"][amazonData["Site"][amazonData["Site"] == i].index[0]])

        domain.addAmazonValue(end_value)

    def getBusinessClickData(self, domain):
        bcFile = pd.read_excel(self.path + r"\WTG_BusinessClick" + self.date + ".xlsx", "Final")
        bcData = pd.DataFrame(bcFile, columns=["Site", "Revenue PLN Net", "Revenue EUR Net", "Revenue USD Net"])


        match = []

        for i in bcData["Site"]:
            if re.search(domain.name, i, re.IGNORECASE):
                match.append(i)

        tempForbidden = str(domain.forbidden)
        list = tempForbidden.split(", ")

        for x in match[0:]:
            if list != ['nan']:
                for y in list:
                    if re.search(y,x, re.IGNORECASE):
                        match.remove(x)

        end_value = 0

        # Dodawanie wartości SSP
        for i in match:
            if domain.currency == "EUR":
                end_value = end_value + (bcData["Revenue EUR Net"][bcData["Site"][bcData["Site"] == i].index[0]])
            if domain.currency == "USD":
                end_value = end_value + (bcData["Revenue USD Net"][bcData["Site"][bcData["Site"] == i].index[0]])
            if domain.currency == "PLN":
                end_value = end_value + (bcData["Revenue PLN Net"][bcData["Site"][bcData["Site"] == i].index[0]])

        domain.addBusinessClickValue(end_value)

    def getConnectAdData(self, domain):
        connectadFile = pd.read_excel(self.path + r"\WTG_ConnectAd" + self.date + ".xlsx", "Final")
        connectadData = pd.DataFrame(connectadFile, columns=["Site", "Revenue USD Net", "Revenue EUR Net", "Revenue PLN Net"])

        match = []

        for i in connectadData["Site"]:
            if re.search(domain.name, i,re.IGNORECASE):
                match.append(i)

        tempForbidden = str(domain.forbidden)
        list = tempForbidden.split(", ")

        for x in match[0:]:
            if list != ['nan']:
                for y in list:
                    if re.search(y, x, re.IGNORECASE):
                        match.remove(x)

        end_value = 0

        # Dodawanie wartości SSP
        for i in match:
            if domain.currency == "EUR":
                end_value = end_value + (connectadData["Revenue EUR Net"][connectadData["Site"][connectadData["Site"] == i].index[0]])
            if domain.currency == "USD":
                end_value = end_value + (connectadData["Revenue USD Net"][connectadData["Site"][connectadData["Site"] == i].index[0]])
            if domain.currency == "PLN":
                end_value = end_value + (connectadData["Revenue PLN Net"][connectadData["Site"][connectadData["Site"] == i].index[0]])

        domain.addConnectAdValue(end_value)

    def getCriteoData(self, domain):
        criteoFile = pd.read_excel(self.path + r"\WTG_Criteo" + self.date + ".xlsx", "Final")
        criteoData = pd.DataFrame(criteoFile, columns=["Site", "Revenue EUR Net", "Revenue USD Net", "Revenue PLN Net"])


        match = []

        for i in criteoData["Site"]:
            if re.search(domain.name, i, re.IGNORECASE):
                match.append(i)

        tempForbidden = str(domain.forbidden)
        list = tempForbidden.split(", ")

        for x in match[0:]:
            if list != ['nan']:
                print("not nan")
                for y in list:
                    if re.search(y,x, re.IGNORECASE):
                        match.remove(x)

        end_value = 0

        # Dodawanie wartości SSP
        for i in match:
            if domain.currency == "EUR":
                end_value = end_value + (criteoData["Revenue EUR Net"][criteoData["Site"][criteoData["Site"] == i].index[0]])
            if domain.currency == "USD":
                end_value = end_value + (criteoData["Revenue USD Net"][criteoData["Site"][criteoData["Site"] == i].index[0]])
            if domain.currency == "PLN":
                end_value = end_value + (criteoData["Revenue PLN Net"][criteoData["Site"][criteoData["Site"] == i].index[0]])

        domain.addCriteoValue(end_value)

    def getetargetData(self, domain):
        etargetFile = pd.read_excel(self.path + r"\WTG_eTarget" + self.date + ".xlsx", "Final")
        etargetData = pd.DataFrame(etargetFile, columns=["Site", "Revenue Net EUR"])


        match = []

        for i in etargetData["Site"]:
            if re.search(domain.name, i, re.IGNORECASE):
                match.append(i)

        tempForbidden = str(domain.forbidden)
        list = tempForbidden.split(", ")

        for x in match[0:]:
            if list != ['nan']:
                for y in list:
                    if re.search(y,x, re.IGNORECASE):
                        match.remove(x)

        end_value = 0

        # Dodawanie wartości SSP
        for i in match:
            if domain.currency == "EUR":
                end_value = end_value + (etargetData["Revenue Net EUR"][etargetData["Site"][etargetData["Site"] == i].index[0]])

        domain.addeTarget(end_value)

    def getIndexData(self, domain):
        indexFile = pd.read_excel(self.path + r"\WTG_IndexExchange" + self.date + ".xlsx", "Final")
        indexData = pd.DataFrame(indexFile, columns=["Site", "Revenue USD Net", "Revenue EUR Net", "Revenue PLN Net"])


        match = []

        for i in indexData["Site"]:
            if re.search(domain.name, i, re.IGNORECASE):
                match.append(i)

        tempForbidden = str(domain.forbidden)
        list = tempForbidden.split(", ")

        for x in match[0:]:
            if list != ['nan']:
                for y in list:
                    if re.search(y,x, re.IGNORECASE):
                        match.remove(x)

        end_value = 0

        # Dodawanie wartości SSP
        for i in match:
            if domain.currency == "EUR":
                end_value = end_value + (indexData["Revenue EUR Net"][indexData["Site"][indexData["Site"] == i].index[0]])
            if domain.currency == "USD":
                end_value = end_value + (indexData["Revenue USD Net"][indexData["Site"][indexData["Site"] == i].index[0]])
            if domain.currency == "PLN":
                end_value = end_value + (indexData["Revenue PLN Net"][indexData["Site"][indexData["Site"] == i].index[0]])

        domain.addIXValue(end_value)

    def getMagniteData(self, domain):
        magniteFile = pd.read_excel(self.path + r"\WTG_Magnite" + self.date + ".xlsx", "Final")
        magniteData = pd.DataFrame(magniteFile, columns=["Site", "Revenue USD Net", "Revenue EUR Net", "Revenue PLN Net"])


        match = []

        for i in magniteData["Site"]:
            if re.search(domain.name, i, re.IGNORECASE):
                match.append(i)

        tempForbidden = str(domain.forbidden)
        list = tempForbidden.split(", ")

        for x in match[0:]:
            if list != ['nan']:
                for y in list:
                    if re.search(y,x, re.IGNORECASE):
                        match.remove(x)

        end_value = 0

        # Dodawanie wartości SSP
        for i in match:
            if domain.currency == "EUR":
                end_value = end_value + (magniteData["Revenue EUR Net"][magniteData["Site"][magniteData["Site"] == i].index[0]])
            if domain.currency == "USD":
                end_value = end_value + (magniteData["Revenue USD Net"][magniteData["Site"][magniteData["Site"] == i].index[0]])
            if domain.currency == "PLN":
                end_value = end_value + (magniteData["Revenue PLN Net"][magniteData["Site"][magniteData["Site"] == i].index[0]])

        domain.addMagniteValue(end_value)

    def getOpenXData(self, domain):
        openXFile = pd.read_excel(self.path + r"\WTG_OpenX" + self.date + ".xlsx", "Final")
        openXData = pd.DataFrame(openXFile, columns=["Site", "Revenue EUR Net", "Revenue USD Net", "Revenue PLN Net"])


        match = []

        for i in openXData["Site"]:
            if re.search(domain.name, i, re.IGNORECASE):
                match.append(i)

        tempForbidden = str(domain.forbidden)
        list = tempForbidden.split(", ")

        for x in match[0:]:
            if list != ['nan']:
                for y in list:
                    if re.search(y,x, re.IGNORECASE):
                        match.remove(x)

        end_value = 0

        # Dodawanie wartości SSP
        for i in match:
            if domain.currency == "EUR":
                end_value = end_value + (openXData["Revenue EUR Net"][openXData["Site"][openXData["Site"] == i].index[0]])
            if domain.currency == "USD":
                end_value = end_value + (openXData["Revenue USD Net"][openXData["Site"][openXData["Site"] == i].index[0]])
            if domain.currency == "PLN":
                end_value = end_value + (openXData["Revenue PLN Net"][openXData["Site"][openXData["Site"] == i].index[0]])

        domain.addOpenXValue(end_value)

    def getPubmaticData(self, domain):
        pubmaticFile = pd.read_excel(self.path + r"\WTG_Pubmatic" + self.date + ".xlsx", "Final")
        pubmaticData = pd.DataFrame(pubmaticFile, columns=["Site", "Revenue EUR Net", "Revenue USD Net", "Revenue PLN Net"])


        match = []

        for i in pubmaticData["Site"]:
            if re.search(domain.name, i, re.IGNORECASE):
                match.append(i)

        tempForbidden = str(domain.forbidden)
        list = tempForbidden.split(", ")

        for x in match[0:]:
            if list != ['nan']:
                for y in list:
                    if re.search(y,x, re.IGNORECASE):
                        match.remove(x)

        end_value = 0

        # Dodawanie wartości SSP
        for i in match:
            if domain.currency == "EUR":
                end_value = end_value + (pubmaticData["Revenue EUR Net"][pubmaticData["Site"][pubmaticData["Site"] == i].index[0]])
            if domain.currency == "USD":
                end_value = end_value + (pubmaticData["Revenue USD Net"][pubmaticData["Site"][pubmaticData["Site"] == i].index[0]])
            if domain.currency == "PLN":
                end_value = end_value + (pubmaticData["Revenue PLN Net"][pubmaticData["Site"][pubmaticData["Site"] == i].index[0]])

        domain.addPubmaticValue(end_value)

    def getrtbData(self, domain):
        rtbFile = pd.read_excel(self.path + r"\WTG_RTBHouse" + self.date + ".xlsx", "Final")
        rtbData = pd.DataFrame(rtbFile, columns=["Site", "Revenue USD Net", "Revenue EUR Net", "Revenue PLN Net"])

        match = []

        rtbData = rtbData.fillna("Empty")

        for i in rtbData["Site"]:
            if re.search(domain.name, i, re.IGNORECASE):
                match.append(i)

        tempForbidden = str(domain.forbidden)
        list = tempForbidden.split(", ")

        for x in match[0:]:
            if list != ['nan']:
                for y in list:
                    if re.search(y,x, re.IGNORECASE):
                        match.remove(x)

        end_value = 0

        # Dodawanie wartości SSP
        for i in match:
            if domain.currency == "EUR":
                end_value = end_value + (rtbData["Revenue EUR Net"][rtbData["Site"][rtbData["Site"] == i].index[0]])
            if domain.currency == "USD":
                end_value = end_value + (rtbData["Revenue USD Net"][rtbData["Site"][rtbData["Site"] == i].index[0]])
            if domain.currency == "PLN":
                end_value = end_value + (rtbData["Revenue PLN Net"][rtbData["Site"][rtbData["Site"] == i].index[0]])

        domain.addRTBValue(end_value)

    def getSmartData(self, domain):
        smartFile = pd.read_excel(self.path + r"\WTG_Smart" + self.date + ".xlsx", "Final")
        smartData = pd.DataFrame(smartFile, columns=["Site", "Revenue EUR Net", "Revenue USD Net", "Revenue PLN Net"])

        match = []

        for i in smartData["Site"]:
            if re.search(domain.name, i, re.IGNORECASE):
                match.append(i)

        tempForbidden = str(domain.forbidden)
        list = tempForbidden.split(", ")

        for x in match[0:]:
            if list != ['nan']:
                for y in list:
                    if re.search(y,x, re.IGNORECASE):
                        match.remove(x)

        end_value = 0

        # Dodawanie wartości SSP
        for i in match:
            if domain.currency == "EUR":
                end_value = end_value + (smartData["Revenue EUR Net"][smartData["Site"][smartData["Site"] == i].index[0]])
            if domain.currency == "USD":
                end_value = end_value + (smartData["Revenue USD Net"][smartData["Site"][smartData["Site"] == i].index[0]])
            if domain.currency == "PLN":
                end_value = end_value + (smartData["Revenue PLN Net"][smartData["Site"][smartData["Site"] == i].index[0]])

        domain.addSmartValue(end_value)

    def getSovrnData(self, domain):
        sovrnFile = pd.read_excel(self.path + r"\WTG_Sovrn" + self.date + ".xlsx", "Final")
        sovrnData = pd.DataFrame(sovrnFile, columns=["Site", "Revenue USD Net", "Revenue EUR Net", "Revenue PLN Net"])


        match = []

        for i in sovrnData["Site"]:
            if re.search(domain.name, i, re.IGNORECASE):
                match.append(i)

        tempForbidden = str(domain.forbidden)
        list = tempForbidden.split(", ")

        for x in match[0:]:
            if list != ['nan']:
                for y in list:
                    if re.search(y,x, re.IGNORECASE):
                        match.remove(x)

        end_value = 0

        # Dodawanie wartości SSP
        for i in match:
            if domain.currency == "EUR":
                end_value = end_value + (sovrnData["Revenue EUR Net"][sovrnData["Site"][sovrnData["Site"] == i].index[0]])
            if domain.currency == "USD":
                end_value = end_value + (sovrnData["Revenue USD Net"][sovrnData["Site"][sovrnData["Site"] == i].index[0]])
            if domain.currency == "PLN":
                end_value = end_value + (sovrnData["Revenue PLN Net"][sovrnData["Site"][sovrnData["Site"] == i].index[0]])

        domain.addSovrnValue(end_value)

    def getTeadsData(self, domain):
        teadsFile = pd.read_excel(self.path + r"\WTG_Teads" + self.date + ".xlsx", "Final")
        teadsData = pd.DataFrame(teadsFile, columns=["Site", "Revenue EUR Net", "Revenue USD Net", "Revenue PLN Net"])


        match = []

        for i in teadsData["Site"]:
            if re.search(domain.name, i, re.IGNORECASE):
                match.append(i)

        tempForbidden = str(domain.forbidden)
        list = tempForbidden.split(", ")

        for x in match[0:]:
            if list != ['nan']:
                for y in list:
                    if re.search(y,x, re.IGNORECASE):
                        match.remove(x)

        end_value = 0

        # Dodawanie wartości SSP
        for i in match:
            if domain.currency == "EUR":
                end_value = end_value + (teadsData["Revenue EUR Net"][teadsData["Site"][teadsData["Site"] == i].index[0]])
            if domain.currency == "USD":
                end_value = end_value + (teadsData["Revenue USD Net"][teadsData["Site"][teadsData["Site"] == i].index[0]])
            if domain.currency == "PLN":
                end_value = end_value + (teadsData["Revenue PLN Net"][teadsData["Site"][teadsData["Site"] == i].index[0]])

        domain.addTeadsValue(end_value)

    def getXandrData(self, domain):
        xandrFile = pd.read_excel(self.path + r"\WTG_Xandr" + self.date + ".xlsx", "Final")
        xandrData = pd.DataFrame(xandrFile, columns=["Site", "Revenue USD Net", "Revenue EUR Net", "Revenue PLN Net"])


        match = []

        for i in xandrData["Site"]:
            if re.search(domain.name, i, re.IGNORECASE):
                match.append(i)

        tempForbidden = str(domain.forbidden)
        list = tempForbidden.split(", ")

        for x in match[0:]:
            if list != ['nan']:
                for y in list:
                    if re.search(y,x, re.IGNORECASE):
                        match.remove(x)

        end_value = 0

        # Dodawanie wartości SSP
        for i in match:
            if domain.currency == "EUR":
                end_value = end_value + (xandrData["Revenue EUR Net"][xandrData["Site"][xandrData["Site"] == i].index[0]])
            if domain.currency == "USD":
                end_value = end_value + (xandrData["Revenue USD Net"][xandrData["Site"][xandrData["Site"] == i].index[0]])
            if domain.currency == "PLN":
                end_value = end_value + (xandrData["Revenue PLN Net"][xandrData["Site"][xandrData["Site"] == i].index[0]])

        domain.addXandrValue(end_value)

    def getVideoData(self, domain):
        videoFile = pd.read_excel(self.path + r"\WTG_Video" + self.date + ".xlsx", "Final")
        videoData = pd.DataFrame(videoFile, columns=["Site", "Revenue PLN Net", "Revenue EUR Net", "Revenue USD Net"])


        match = []

        for i in videoData["Site"]:
            if re.search(domain.name, i, re.IGNORECASE):
                match.append(i)

        tempForbidden = str(domain.forbidden)
        list = tempForbidden.split(", ")

        for x in match[0:]:
            if list != ['nan']:
                for y in list:
                    if re.search(y,x, re.IGNORECASE):
                        match.remove(x)

        end_value = 0

        # Dodawanie wartości SSP
        for i in match:
            if domain.currency == "EUR":
                end_value = end_value + (
                videoData["Revenue EUR Net"][videoData["Site"][videoData["Site"] == i].index[0]])
            if domain.currency == "USD":
                end_value = end_value + (
                videoData["Revenue USD Net"][videoData["Site"][videoData["Site"] == i].index[0]])
            if domain.currency == "PLN":
                end_value = end_value + (
                videoData["Revenue PLN Net"][videoData["Site"][videoData["Site"] == i].index[0]])

        domain.addVideoValue(end_value)


    def getMediaFarmData(self, domain):
        mediaFarmFile = pd.read_excel(self.path + r"\WTG_Mediafarm" + self.date + ".xlsx", "Final")
        mediaFarmData = pd.DataFrame(mediaFarmFile, columns=["Site", "Revenue PLN Net"])

        match = []

        for i in mediaFarmData["Site"]:
            if re.search(domain.name, i, re.IGNORECASE):
                match.append(i)

        tempForbidden = str(domain.forbidden)
        list = tempForbidden.split(", ")

        for x in match[0:]:
            if list != ['nan']:
                for y in list:
                    if re.search(y, x, re.IGNORECASE):
                        match.remove(x)

        end_value = 0

        # Dodawanie wartości SSP
        for i in match:
            if domain.currency == "PLN":
                end_value = end_value + (
                mediaFarmData["Revenue PLN Net"][mediaFarmData["Site"][mediaFarmData["Site"] == i].index[0]])

        domain.addMediafarmValue(end_value)

    def getBrightcomFileData(self, domain):
        brightcomFile = pd.read_excel(self.path + r"\WTG_Brightcom" + self.date + ".xlsx", "Final")
        brightcomData = pd.DataFrame(brightcomFile, columns=["Site", "Revenue USD net", "Revenue PLN net"])


        match = []

        for i in brightcomData["Site"]:
            if re.search(domain.name, i, re.IGNORECASE):
                match.append(i)

        tempForbidden = str(domain.forbidden)
        list = tempForbidden.split(", ")

        for x in match[0:]:
            if list != ['nan']:
                for y in list:
                    if re.search(y,x, re.IGNORECASE):
                        match.remove(x)

        end_value = 0

        # Dodawanie wartości SSP
        for i in match:
            if domain.currency == "USD":
                end_value = end_value + (brightcomData["Revenue USD net"][brightcomData["Site"][brightcomData["Site"] == i].index[0]])
            if domain.currency == "PLN":
                end_value = end_value + (brightcomData["Revenue PLN net"][brightcomData["Site"][brightcomData["Site"] == i].index[0]])
        domain.addBrightcomValue(end_value)

    def getYocData(self, domain):
        yocFile = pd.read_excel(self.path + r"\WTG_YOC" + self.date + ".xlsx", "Final")
        yocData = pd.DataFrame(yocFile, columns=["Site", "Revenue PLN Net"])

        match = []

        for i in yocData["Site"]:
            if re.search(domain.name, i, re.IGNORECASE):
                match.append(i)

        tempForbidden = str(domain.forbidden)
        list = tempForbidden.split(", ")

        for x in match[0:]:
            if list != ['nan']:
                for y in list:
                    if re.search(y, x, re.IGNORECASE):
                        match.remove(x)

        end_value = 0

        # Dodawanie wartości SSP
        for i in match:
            if domain.currency == "PLN":
                end_value = end_value + (
                yocData["Revenue PLN Net"][yocData["Site"][yocData["Site"] == i].index[0]])

        domain.addYocValue(end_value)

    def getPCriteoData(self, domain):
        pubCriteoFile = pd.read_excel(self.path + r"\PUB_Criteo" + self.date + ".xlsx", "Final")
        pubCriteoData = pd.DataFrame(pubCriteoFile, columns=["Site", "Revenue EUR Net"])

        match = []

        for i in pubCriteoData["Site"]:
            if re.search(domain.name, i, re.IGNORECASE):
                match.append(i)

        tempForbidden = str(domain.forbidden)
        list = tempForbidden.split(", ")

        for x in match[0:]:
            if list != ['nan']:
                for y in list:
                    if re.search(y, x, re.IGNORECASE):
                        match.remove(x)

        end_value = 0

        # Dodawanie wartości SSP
        for i in match:
            if domain.currency == "EUR":
                end_value = end_value + (
                pubCriteoData["Revenue EUR Net"][pubCriteoData["Site"][pubCriteoData["Site"] == i].index[0]])

        domain.addPubCriteoValue(end_value)