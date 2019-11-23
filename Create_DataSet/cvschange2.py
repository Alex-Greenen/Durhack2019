import numpy as np
import csv

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

def NormaliseData(csv):
     categories= ['CustomerAge',
                 'Current_OverdraftAmount',
                 'Average_Transaction_Amount',
                 'Transaction_Frequency_index',
                 'DisabilitySeverityIndex',
                 'Days_Since_Disability',
                 'Number_Of_Calls',
                 'Disability_Name']
     for column in range(0,6):
          minValue = 100000000000000
          maxValue = -10000000000000
          print(categories[column])
          for row in range(1,101):
               value = csv[row][column]
               print(row)
               if value>maxValue:
                    maxValue = value
               if value<minValue:
                    minValue = value
          print('minimum: '+str(minValue))
          print('maximum: '+str(minValue))
          for row in range(1, 101):
               csv[row][column] = (csv[row][column]-minValue)/(maxValue-minValue)
     return csv

def getDisability():
     setOfDisabilities = ['Aspergers', 'SpeechImpairment', 'Dyslexia', 'mobilityImpairment', 'SocialAnxiety', 'despression', 'Parkinson']
     return np.random.choice(setOfDisabilities)

if __name__ == '__main__':
     csvData = [['CustomerAge',
                 'Current_OverdraftAmount',
                 'Average_Transaction_Amount',
                 'Transaction_Frequency_index',
                 'DisabilitySeverityIndex',
                 'Days_Since_Disability',
                 'Number_Of_Calls',
                 'Disability_Name',
                 'Method_Of_Communication',
                 'Urgency',
                 'Resource_Allocation']]

     for i in range(0,100):
          csvData.append(generateUser())

     print(csvData)

     csvData = NormaliseData(csv)

     with open('Dataset_CustomerService2.csv', 'w') as csvFile:
          writer = csv.writer(csvFile)
          writer.writerows(csvData)
     csvFile.close()

