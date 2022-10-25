import pandas as pd


class Writer:

    def __init__(self, path):
        print("Utworzono Writer")
        self.path = path

    def write (self, collector):

        setname = []
        setcurrency = []
        setadagio = []
        setadaptmx = []
        setadform = []
        setamazon = []
        setcriteo = []
        setix = []
        setmagnite = []
        setob = []
        setopenx = []
        setpubmatic = []
        setsmart = []
        setsovrn = []
        setxandr = []
        setconnectad = []
        setrtb = []
        setteads = []
        setbusinessclick = []
        seteTarget = []
        setbrightcom = []
        setWholeDomainValue = []
        setPublishers = []

        for i in collector.publishers:
            for j in i.domains:
                setname.append(j.name)
                setcurrency.append(j.currency)
                setadagio.append(j.adagio)
                setadaptmx.append(j.adaptMx)
                setadform.append(j.adform)
                setamazon.append(j.amazon)
                setcriteo.append(j.criteo)
                setix.append(j.ix)
                setmagnite.append(j.magnite)
                setopenx.append(j.openx)
                setpubmatic.append(j.pubmatic)
                setsmart.append(j.smart)
                setsovrn.append(j.sovrn)
                setxandr.append(j.xandr)
                setconnectad.append(j.connectad)
                setrtb.append(j.rtb)
                setteads.append(j.teads)
                setbusinessclick.append(j.businessclick)
                seteTarget.append(j.eTarget)
                setbrightcom.append(j.brightcom)
                setWholeDomainValue.append(j.wholeValue)
                setPublishers.append(j.publisher)


        df = pd.DataFrame(
            {
                "Wydawca":setPublishers,
                "Domena":setname,
                "Waluta":setcurrency,
                "Adagio":setadagio,
                "AdaptMX":setadaptmx,
                "Adform":setadform,
                "Amazon":setamazon,
                "Criteo":setcriteo,
                "Index":setix,
                "Rubicon":setmagnite,
                "OpenX":setopenx,
                "Pubmatic":setpubmatic,
                "Smart":setsmart,
                "Sovrn":setsovrn,
                "Xandr":setxandr,
                "Connectad":setconnectad,
                "RTB House":setrtb,
                "Teads":setteads,
                "Business Click":setbusinessclick,
                "eTarget":seteTarget,
                "SSP SUM":setWholeDomainValue
            }
        )

        printer = pd.ExcelWriter(self.path + r"\rozliczeniaV2_wyniki.xlsx", engine="xlsxwriter")

        df.to_excel(printer, sheet_name='Final')

        try:
            printer.save()
            print("Zapisano!")
        except:
            print("Błąd!")

    def write2 (self, collector):

        contractors = collector.contractors

        setContractorIDs = []
        setContractorNames = []
        setPublisherIDs = []
        setPublishers = []
        setName = []
        setcurrency = []
        setadagio = []
        setadaptmx = []
        setadform = []
        setamazon = []
        setcriteo = []
        setix = []
        setmagnite = []
        setob = []
        setopenx = []
        setpubmatic = []
        setsmart = []
        setsovrn = []
        setxandr = []
        setconnectad = []
        setrtb = []
        setteads = []
        setbusinessclick = []
        seteTarget = []
        setWholeDomainValue = []

        setVideo = []
        setMediaFarm = []
        setBrightcom = []
        setYoc = []
        setPubCriteo = []


        for i in contractors:
            for j in i.publishers:
                for x in j.domains:
                    # print("CONTRACTOR ID: " + str(i.id) + " CONTRACTOR NAME: " + str(i.name) + " PUBLISHER ID: " + str(j.id) + " PUBLISHER NAME: " + str(j.name) + " DOMAIN: " + str(x.name))
                    setContractorIDs.append(str(i.id))
                    setContractorNames.append(str(i.name))
                    setPublisherIDs.append(str(j.id))
                    setPublishers.append(str(j.name))
                    setName.append(x.name)
                    setcurrency.append(x.currency)
                    setadagio.append(x.adagio)
                    setadaptmx.append(x.adaptMx)
                    setadform.append(x.adform)
                    setamazon.append(x.amazon)
                    setcriteo.append(x.criteo)
                    setix.append(x.ix)
                    setmagnite.append(x.magnite)
                    setopenx.append(x.openx)
                    setpubmatic.append(x.pubmatic)
                    setsmart.append(x.smart)
                    setsovrn.append(x.sovrn)
                    setxandr.append(x.xandr)
                    setconnectad.append(x.connectad)
                    setrtb.append(x.rtb)
                    setteads.append(x.teads)
                    setbusinessclick.append(x.businessclick)
                    seteTarget.append(x.eTarget)
                    setWholeDomainValue.append(x.wholeValue)

                    setVideo.append(x.video)
                    setMediaFarm.append(x.mediafarm)
                    setBrightcom.append(x.brightcom)
                    setYoc.append(x.yoc)
                    setPubCriteo.append(x.pubCriteo)


        # print(len(setContractorIDs))
        # print(len(setContractorNames))
        # print(len(setPublisherIDs))
        # print(len(setPublishers))
        # print(len(setName))

        df = pd.DataFrame(
            {
                "ID Kontrahenta":setContractorIDs,
                "Nazwa Kontrahenta":setContractorNames,
                "ID Wydawcy":setPublisherIDs,
                "Nazwa Wydawcy":setPublishers,
                "Domena":setName,
                "Waluta":setcurrency,
                "WTG_Adagio":setadagio,
                "WTG_AdaptMX":setadaptmx,
                "WTG_Adform":setadform,
                "WTG_Amazon":setamazon,
                "WTG_Criteo":setcriteo,
                "WTG_Index":setix,
                "WTG_Rubicon":setmagnite,
                "WTG_OpenX":setopenx,
                "WTG_Pubmatic":setpubmatic,
                "WTG_Smart":setsmart,
                "WTG_Sovrn":setsovrn,
                "WTG_Xandr":setxandr,
                "WTG_Connectad":setconnectad,
                "WTG_RTB House":setrtb,
                "WTG_Teads":setteads,
                "WTG_BusinessClick":setbusinessclick,
                "WTG_eTarget":seteTarget,
                "WTG_Video":setVideo,
                "WTG_MediaFarm":setMediaFarm,
                "WTG_Brightcom":setBrightcom,
                "WTG_YOC":setYoc,
                "PUB_Criteo":setPubCriteo,
                "SSP SUM":setWholeDomainValue
            }
        )

        printer = pd.ExcelWriter(self.path + r"\rozliczeniaV2_wyniki.xlsx", engine="xlsxwriter")

        df.to_excel(printer, sheet_name='Final')

        try:
            printer.save()
            print("Zapisano!")
        except:
            print("Błąd!")