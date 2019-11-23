import numpy as np
import csv

def generateUser():
     CustomerAge = getAge()
     Current_OverdraftAmount = getOverdraft()
     Average_Transaction_Amount = getAverageTransactionAmount()
     Transaction_Frequency_index = getTransactionFrequency()
     PhysDisabilitySeverityIndex=getPhysDisability()
     MentDisabilitySeverityIndex=getMentDisability()
     Days_Since_Disability = getDaysSince(CustomerAge)

     cvsLine = [CustomerAge,
            Current_OverdraftAmount,
            Average_Transaction_Amount,
            Transaction_Frequency_index,
            PhysDisabilitySeverityIndex,
            MentDisabilitySeverityIndex,
            Days_Since_Disability]

     return cvsLine


def getAge():
     return np.random.randint(19,80)

def getOverdraft():
     return np.random.poisson(4)

def getAverageTransactionAmount():
     return np.random.randint(1, 50000)/100

def getTransactionFrequency():
     return np.random.random()

def getPhysDisability():
     temp = np.random.normal(0.3, 0.2)
     if temp <=0:
          return 0.0
     elif temp >1:
          return 1
     else:
          return temp

def getMentDisability():
     temp = np.random.normal(0.3, 0.2)
     if temp <=0:
          return 0.0
     elif temp >1:
          return 1
     else:
          return temp

def getDaysSince(CustomerAge):
     if (np.random.random() > 0.4):
          temp = CustomerAge-np.random.poisson(1)*5000
          if temp <0:
               return CustomerAge
          else:
               return temp
     else:
          return CustomerAge

def NormaliseData(csv):
     for column in range(0,7):
          minValue = 100000000000000
          maxValue = -10000000000000
          for row in range(1,101):
               value = csv[row][column]
               if value>maxValue:
                    maxValue = value
               if value<minValue:
                    minValue = value
          for row in range(1, 101):
               csv[row][column] = (csv[row][column]-minValue)/(maxValue-minValue)
     return csv

if __name__ == '__main__':
     csvData = [['CustomerAge',
                 'Current_OverdraftAmount',
                 'Average_Transaction_Amount',
                 'Transaction_Frequency_index',
                 'PhysDisabilitySeverityIndex',
                 'MentDisabilitySeverityIndex',
                 'Days_Since_Disability']]

     for i in range(0,100):
          csvData.append(generateUser())

     csvData = NormaliseData(csvData)

     with open('Dataset_CustomerService.csv', 'w') as csvFile:
          writer = csv.writer(csvFile)
          writer.writerows(csvData)
     csvFile.close()

