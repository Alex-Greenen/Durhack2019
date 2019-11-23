import numpy as np
import csv

def thereticalUser():

     Method_Of_Communication = np.random.choice(['text', 'email', 'phone', 'mail'])
     Urgency = np.random.random()
     Resource_Allocation = np.random.random()
     CustomerAge = getTheoryAge(Method_Of_Communication, Urgency, Resource_Allocation)
     Current_OverdraftAmount = getTheoryOverdraft(Method_Of_Communication, Urgency, Resource_Allocation)
     Average_Transaction_Amount = getTheoryAverageTransactionAmount(Method_Of_Communication, Urgency, Resource_Allocation)
     Transaction_Frequency_index = getTheoryTransactionFrequency(Method_Of_Communication, Urgency, Resource_Allocation)
     DisabilitySeverityIndex = getTheoryDisabilitySeverityIndex(Method_Of_Communication, Urgency, Resource_Allocation)
     Number_Of_Contacts = getTheoryContacts(Method_Of_Communication, Urgency, Resource_Allocation,CustomerAge)
     DisabilityName = getTheoryDisability(Method_Of_Communication, Urgency, Resource_Allocation, CustomerAge)
     Days_Since_Disability = getTheoryDaysSince(Method_Of_Communication, Urgency, Resource_Allocation, DisabilityName,CustomerAge)

     cvsLine = [CustomerAge,
                Current_OverdraftAmount,
                Average_Transaction_Amount,
                Transaction_Frequency_index,
                DisabilitySeverityIndex,
                Days_Since_Disability,
                Number_Of_Contacts,
                DisabilityName,
                Method_Of_Communication,
                Urgency,
                Resource_Allocation]

     return cvsLine



def getTheoryAge(Method_Of_Communication,Urgency,Resource_Allocation):
     if Method_Of_Communication == 'text':
          return 20
     if Method_Of_Communication == 'email':
          return 30
     if Method_Of_Communication == 'phone':
          return 80
     if Method_Of_Communication == 'mail':
          return (70 + Urgency*50)/2

def getTheoryOverdraft(Method_Of_Communication,Urgency,Resource_Allocation):
     return (Urgency+Resource_Allocation) * 50

def getTheoryAverageTransactionAmount(Method_Of_Communication,Urgency,Resource_Allocation):
     return Urgency+Resource_Allocation/3

def getTheoryTransactionFrequency(Method_Of_Communication,Urgency,Resource_Allocation):
     return Urgency+Resource_Allocation/3

def getTheoryDisabilitySeverityIndex(Method_Of_Communication,Urgency,Resource_Allocation):
     return Urgency/6+Resource_Allocation

def getTheoryDaysSince(Method_Of_Communication,Urgency,Resource_Allocation, DisabilityName, age):
     if DisabilityName in ['Dyslexia', 'Aspergers']:
          return age
     else:
          return 50/(Urgency + Resource_Allocation)

def getTheoryContacts(Method_Of_Communication,Urgency,Resource_Allocation, CustomerAge):
     return (CustomerAge + Resource_Allocation)/30

def getTheoryDisability(Method_Of_Communication,Urgency,Resource_Allocation, CustomerAge):
     if Method_Of_Communication == 'phone':
          if np.random.random() < 0.6:
               return np.random.choice(['Dyslexia', 'Parkinson'])
     if Method_Of_Communication in ['text, phone, email']:
          if np.random.random() < 0.6:
               return 'mobilityImpairment'
     if Method_Of_Communication in ['text, mail']:
          if np.random.random() < 0.6:
               return np.random.choice(['SpeechImpairment', 'mobilityImpairment'])
     return np.random.choice(['Aspergers', 'SpeechImpairment', 'Dyslexia', 'mobilityImpairment', 'SocialAnxiety', 'despression', 'Parkinson'])









def generateUser():
     CustomerAge = getAge()
     Current_OverdraftAmount = getOverdraft()
     Average_Transaction_Amount = getAverageTransactionAmount()
     Transaction_Frequency_index = getTransactionFrequency()
     DisabilitySeverityIndex=getDisabilitySeverityIndex()
     Days_Since_Disability = getDaysSince(CustomerAge)
     Number_Of_Calls = getCalls()
     DisabilityName = getDisability()

     cvsLine = [CustomerAge,
            Current_OverdraftAmount,
            Average_Transaction_Amount,
            Transaction_Frequency_index,
            DisabilitySeverityIndex,
            Days_Since_Disability,
            Number_Of_Calls,
            DisabilityName]

     return cvsLine


def getAge():
     return np.random.randint(19,80)

def getOverdraft():
     if np.random.random()<0.2:
          return 0
     else:
          return np.random.chisquare(4)

def getAverageTransactionAmount():
     return np.random.randint(1, 50000)/100

def getTransactionFrequency():
     return np.random.random()

def getDisabilitySeverityIndex():
     temp = np.random.normal(0.3, 0.2)
     if temp <=0:
          return 0.0
     elif temp >1:
          return 1
     else:
          return temp


def getDaysSince(CustomerAge):
     if (np.random.random() > 0.4):
          temp = CustomerAge-np.random.chisquare(2)*5000
          if temp <0:
               return CustomerAge
          else:
               return temp
     else:
          return CustomerAge

def getCalls():
     return np.random.poisson(1)

def getDisability():
     setOfDisabilities = ['Aspergers', 'SpeechImpairment', 'Dyslexia', 'mobilityImpairment', 'SocialAnxiety', 'despression', 'Parkinson']
     return np.random.choice(setOfDisabilities)












def combineData(theorySet, dataset):
     csvData = []
     for i in range(0,100):
          temp = []
          for j in range(0, 7):
               temp.append(dataset[i][j]*0.3 + theorySet[i][j]*0.8)
          if np.random.random()<0.3:
               temp.append(dataset[i][7])
          else:
               temp.append(theorySet[i][7])
          for j in range(8, 11):
               temp.append(theorySet[i][j])
          csvData.append(temp)

     return csvData









def NormaliseData(csvIn):
     categories= ['CustomerAge',
                 'Current_OverdraftAmount',
                 'Average_Transaction_Amount',
                 'Transaction_Frequency_index',
                 'DisabilitySeverityIndex',
                 'Days_Since_Disability',
                 'Number_Of_Contacts',
                 'Disability_Name']
     for column in range(0,7):
          minValue = 100000000000000
          maxValue = -10000000000000
          for row in range(0, 100):
               value = csvIn[row][column]
               if value > maxValue:
                    maxValue = value
               if value < minValue:
                    minValue = value
          print(categories[column])
          print('minimum: '+str(minValue))
          print('maximum: '+str(maxValue))
          for row in range(0, 100):
               csvIn[row][column] = (csvIn[row][column]-minValue)/(maxValue-minValue)
     return csvIn








if __name__ == '__main__':
     csvData = [['CustomerAge',
                 'Current_OverdraftAmount',
                 'Average_Transaction_Amount',
                 'Transaction_Frequency_index',
                 'DisabilitySeverityIndex',
                 'Days_Since_Disability',
                 'Number_Of_Calls',
                 'Disability_Name',
                 'Number_Of_Contacts',
                 'Urgency',
                 'Resource_Allocation']]

     csvGeneratedData = []
     for i in range(0,100):
          csvGeneratedData.append(generateUser())

     csvTheoreticalData = []
     for i in range(0,100):
          csvTheoreticalData.append(thereticalUser())


     tempData = combineData(csvTheoreticalData, csvGeneratedData)
     csvData += tempData

     with open('Dataset_CustomerService2.csv', 'w') as csvFile:
          writer = csv.writer(csvFile)
          writer.writerows(csvData)
     csvFile.close()

