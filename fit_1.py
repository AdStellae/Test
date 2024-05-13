import requests
import req
import json
import matplotlib.pyplot as plt
import random

#requests data from the url with a data load
def loadData(url, data):
    #Specify the appropriate header for the POST request
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, headers=headers, data=data) #request the data
    return json.loads(response.text) #return the json data

#selects correct key from 
def keySelector(labels):
    result = []
    for key in labels:
        result.append(key)
    return result

#selects correct key from 
def valueSelector(labels):
    result = []
    for key in labels:
        result.append(labels[key])
    return result

#calculates change over time periods between values, returns a list of percentage values
def percentChangeOverTime(values):
    result = [0]
    for t in range(len(values)-1):
        percentChange = ((values[t+1])/(values[t])-1)*100
        result.append(round(percentChange))
    return result

#newData = loadData('https://pxdata.stat.fi:443/PxWeb/api/v1/sv/StatFin/asen/statfin_asen_pxt_11zs.px', req.sauna_data)
#newData = loadData('https://pxdata.stat.fi:443/PxWeb/api/v1/sv/StatFin/asen/statfin_asen_pxt_11zs.px', req.sauna_data)
#newData = loadData('https://pxdata.stat.fi:443/PxWeb/api/v1/sv/StatFin/asen/statfin_asen_pxt_11zs.px', req.sauna_data)

seafareData = loadData('https://pxdata.stat.fi:443/PxWeb/api/v1/sv/StatFin/uvliik/statfin_uvliik_pxt_12it.px', req.seafare_data)

seafareGoodsDict = seafareData["dimension"]["Tavaralaji"]["category"]["label"]
seafareGoods = valueSelector(seafareGoodsDict)

amountOfGoods = seafareData["value"]
print(amountOfGoods) #10000 kg | 10 ton

goodsResult = []
for i in range(len(amountOfGoods)//2):
    goodsResult.append(round(((amountOfGoods[2*i+1]/amountOfGoods[2*i])-1)*100, 2))
highestChangeInGoods = max(goodsResult)

lowestChangeInGoods = min(goodsResult)

########################
#
#   Question 1 & 2
#
########################

birthsData = loadData('https://pxdata.stat.fi:443/PxWeb/api/v1/sv/StatFin/synt/statfin_synt_pxt_12dl.px', req.birth_data)
birthYearDict = birthsData["dimension"]["Vuosi"]["category"]["label"] #'2013' : '2013'
birthYears = keySelector(birthYearDict) #list of the used years

birthMonthDict = birthsData["dimension"]["Tapahtumakuukausi"]["category"]["label"] #'M01': 'Januari'
birthMonths = valueSelector(birthMonthDict) #list of months
birthMonths = birthMonths[1:] #remove "Månader totalt"

birthsPerMonth = birthsData["value"] #list of births per month

highestBirthMonthPerYear = []
for y in range(len(birthYears)):
    #selects the birthsPerMonth for a certain year through slicing
    #the first value of each slice is removed, since it is the year's total number of births
    birthsDuringYear = birthsPerMonth[13*y+1: 13*(y+1)]
    highestValue = max(birthsDuringYear) #select the highest value from birthsDuringYear
    highestMonth = birthMonths[birthsDuringYear.index(highestValue)] #select the month that has the highestValue
    highestBirthMonthPerYear.append(highestMonth) #adds highestMonth of year y to the list


print(100*"#" + "\n#")
print("#\tFråga 1: Under vilken månad föddes flest barn under 2022?") #TODO kommentera hur fråga 1 besvaras
print("#\n" + 100*"#" + "\n#")
print("#\tSvar: Månaden med flest födslar 2022 är " + highestMonth.lower() + " med " + str(highestValue) + " födslar.")
print("#\n" + 100*"#")

input("Tryck på enter för att se statistik...")
print()

plt.figure(figsize=(12,6))
plt.ylim((0, 5000))
plt.title("Födslar år 2022")
plt.plot(birthMonths, birthsDuringYear, marker="o", linestyle="-")
plt.grid()
plt.show()

input("Tryck på enter för att se nästa fråga...")
print()

print(100*"#" + "\n#")
print("#\tFråga 2: Finns det variationer i resultatet från år 2013 till 2022?")
print("#\n" + 100*"#" + "\n#")


listOfAnomalies = []
for m in range(len(highestBirthMonthPerYear)):
    if highestBirthMonthPerYear[m] != highestMonth:
        listOfAnomalies.append(birthYears[m])

if len(listOfAnomalies) > 0:
    chosenBirthYear = random.choice(listOfAnomalies)
    print("#\tSvar: Ja, till exempel", chosenBirthYear, "var", highestBirthMonthPerYear[int(chosenBirthYear)-2013].lower(), "månaden med flest födslar.")
else:
    print("#\tSvar: Nej!")
print("#\n" + 100*"#")

input("Tryck på enter för att se nästa fråga...")
print()

########################
#
#   Question 3 & 4
#
########################


deathsData = loadData('https://pxdata.stat.fi:443/PxWeb/api/v1/sv/StatFin/kuol/statfin_kuol_pxt_12ah.px', req.death_data)
deathYearDict = deathsData['dimension']['Vuosi']['category']['label'] #'2013' : '2013'
deathYears = keySelector(deathYearDict) #list of the used years

deathMonthDict = deathsData["dimension"]["Tapahtumakuukausi"]["category"]["label"] #'M01': 'Januari'
deathMonths = valueSelector(deathMonthDict) #list of months

deathPerMonth = deathsData['value'] #list of deaths per month

highestDeathMonthPerYear = []
for y in range(len(deathYears)):
    #selects the deathsPerMonth for a certain year through slicing
    deathsDuringYear = deathPerMonth[12*y: 12*(y+1)]
    highestValue = max(deathsDuringYear) #select the highest value from deathsDuringYear
    highestMonth = deathMonths[deathsDuringYear.index(highestValue)] #select the month that has the highestValue
    highestDeathMonthPerYear.append(highestMonth) #adds highestMonth of year y to the list

print(100*"#" + "\n#")
print("#\tFråga 3: Vilken månad hade flest dödsfall år 2022?") #TODO kommentera hur fråga 3 besvaras
print("#\n" + 100*"#" + "\n#")
print("#\tSvar: Månaden med flest dödsfall 2022 är " + highestMonth.lower() + " med " + str(highestValue) + " dödsfall.")
print("#\n" + 100*"#")

input("Tryck på enter för att se statistik...")
print()

plt.figure(figsize=(12,6))
plt.ylim((0, 6500))
plt.title("Dödsfall år 2022")
plt.plot(deathMonths, deathsDuringYear, marker="o", linestyle="-")
plt.grid()
plt.show()

input("Tryck på enter för att se nästa fråga...")
print()

print(100*"#" + "\n#")
print("#\tFråga 4: Finns det variationer i resultatet från år 2013 till 2022?")
print("#\n" + 100*"#" + "\n#")

listOfAnomalies = []
for m in range(len(highestDeathMonthPerYear)):
    if highestDeathMonthPerYear[m] != highestMonth:
        listOfAnomalies.append(deathYears[m])

if len(listOfAnomalies) > 0:
    chosenDeathYear = random.choice(listOfAnomalies)
    print("#\tSvar: Ja, till exempel", chosenDeathYear, "var", highestDeathMonthPerYear[int(chosenDeathYear)-2013].lower(), "månaden med flest dödsfall.")
else:
    print("#\tSvar: Nej!")
print("#\n" + 100*"#")

input("Tryck på enter för att se nästa fråga...")
print()

########################
#
#   Question 5 & 6
#
########################


electionsData = loadData('https://pxdata.stat.fi:443/PxWeb/api/v1/sv/StatFin/pvaa/statfin_pvaa_pxt_14da.px', req.election_data)
electionYearDict = electionsData['dimension']['Vuosi']['category']['label']
electionYears = keySelector(electionYearDict)

electionParticipation = electionsData['value']

relativeDifference = []
for e in range(0, len(electionParticipation), 2):
    difference = (electionParticipation[e+1]/electionParticipation[e])*100-100
    relativeDifference.append(round(difference, 2))

print(100*"#" + "\n#")
print("#\tFråga 5: Vad är den relativa procentskillnaden för mäns och kvinnors valdeltagande i presidentvalen 1994-2024?")
print("#\n" + 100*"#")

input("Tryck på enter för att se statistik...")
print()


plt.figure(figsize=(6,6))
plt.ylim((0, 10))
plt.title("Relativ procentuell skillnad mellan mäns och kvinnors valdeltagande i presidentvalen 1994-2024")
plt.plot(electionYears, relativeDifference, marker="o", linestyle="-")
plt.grid()
plt.show()

input("Tryck på enter för att se nästa fråga...")
print()

print(100*"#" + "\n#")
print("#\tFråga 6: Vad är den relativa procentskillnaden för mäns och kvinnors valdeltagande i riksdagsvalen 1995-2023?")
print("#\n" + 100*"#")

parliamentData = loadData('https://pxdata.stat.fi:443/PxWeb/api/v1/sv/StatFin/evaa/statfin_evaa_pxt_12i9.px', req.parliament_data)
parliamentYearDict = parliamentData['dimension']['Vuosi']['category']['label']
parliamentYears = keySelector(parliamentYearDict)

parliamentParticipation = parliamentData['value']

relativeParliamentDifference = []
for e in range(0, len(parliamentParticipation), 2):
    parliamentDifference = (parliamentParticipation[e+1]/parliamentParticipation[e])*100-100
    relativeParliamentDifference.append(round(parliamentDifference, 2))

input("Tryck på enter för att se statistik...")
print()

plt.figure(figsize=(6,6))
plt.ylim((0, 10))
plt.title("Relativ procentuell skillnad mellan mäns och kvinnors valdeltagande i riksdagsval 1995-2023")
plt.plot(parliamentYears, relativeParliamentDifference, marker="o", linestyle="-")
plt.grid()
plt.show()

input("Tryck på enter för att se nästa fråga...")
print()

########################
#
#   Question 7 & 8
#
########################

print(100*"#" + "\n#")
print("#\tFråga 7: Vad är den absoluta och procentuella årsförändringen i tågtrafik under 2013-2022?")
print("#\n" + 100*"#")


trainData = loadData('https://pxdata.stat.fi:443/PxWeb/api/v1/sv/StatFin/rtie/statfin_rtie_pxt_12m1.px', req.train_data)
trainYearDict = trainData["dimension"]["Vuosi"]["category"]["label"] #'2013' : '2013'
trainYears = keySelector(trainYearDict) #list of the used years

distance = trainData['value']
percentDistance = percentChangeOverTime(distance)

input("Tryck på enter för att se statistik...")
print()
    
fig,ax1 = plt.subplots()

color = 'tab:blue'
ax1.set_xlabel('Year')
ax1.set_ylabel('Absolute Value (million km)', color=color)
ax1.plot(trainYears, distance, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Percent Change (%)', color=color)
ax2.plot(trainYears, percentDistance, color=color)
ax2.tick_params(axis='y', labelcolor=color)

ax2.set_ylim(-25,25)
plt.title('Absolute Values and Percent Change Over Years')
plt.show()

input("Tryck på enter för att se nästa fråga...")
print()