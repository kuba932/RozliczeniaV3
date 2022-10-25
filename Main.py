from Domain import Domain
from Publisher import Publisher
from Reader import Reader
from Collector import Collector
from Writer import Writer
import pandas as pd
import re

reader = Reader()

domains = reader.getDomainsAsList()

for i in domains:
    reader.getSSPsData(i)

collector = Collector()

collector.createPublisherList(domains)

for i in collector.publishers:
    i.sumSspValue()

collector.createContractors(reader)

collector.matchPublishersAndContractors()

writer = Writer(reader.path)

writer.write2(collector)