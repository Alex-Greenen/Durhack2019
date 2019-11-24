# This Python file uses the following encoding: utf-8
import os, sys
import json
import re
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import *
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from csv import *
import math
from ibm_watson import ApiException
import pandas as pd
from collections import Counter

# Authentication via IAM
authenticator = IAMAuthenticator('wdCPVYuTgefiUbrGjYYYYWZ4WaMnvxw-9CYRBj4kcZIc')
service = NaturalLanguageUnderstandingV1(
    version = '2018-03-16',
    authenticator = authenticator)
service.set_service_url('https://gateway-lon.watsonplatform.net/natural-language-understanding/api')

c = 0
data = list()
good_data = list()
bad_data = list()
mixed_data = list()

good_list = list()
bad_list = list()

def split_reviews(csv_file):
    c = 0
    data.clear()
    with open(csv_file, 'r') as csvfile:
        reader = DictReader(csvfile)

        for row in reader:
            data.append(row['Comment'].replace('"', '').replace("'", '').replace("\n", ''))

        for i in data:
            c = c + 1
            print(c)
            try:
                while i[0] == ' ':
                    i = i[1:]
                response = service.analyze(text=i, features=Features(emotion=EmotionOptions(document=True))).get_result()
                response = response["emotion"]["document"]["emotion"]
                response1 = service.analyze(text=i, features=Features(semantic_roles=SemanticRolesOptions())).get_result()
                response1 = response1["semantic_roles"][0]['sentence']
                if response1[0] == ' ':
                    response1 = response1[1:]
            except (IndexError, ApiException):
                response1 = i

            bad = round(math.sqrt(response["sadness"]**2 + response["anger"]**2 + response["fear"]**2 + response["disgust"]**2)/2, 2)
            good = round(response["joy"], 2)

            result = round(good - bad, 2)

            if result >= 0.2:
                good_data.append(response1)
                good_list.append(good)
            elif result <= -0.2:
                bad_data.append(response1)
                bad_list.append(bad)
            else:
                mixed_data.append(response1)

split_reviews('/Users/edlavr/Desktop/natural_language_processing/App_Store_Reviews.csv')
split_reviews('/Users/edlavr/Desktop/natural_language_processing/Feedback_TrustPilot.csv')

print("good: ", good_data)
print("bad: ", bad_data)
print("mixed: ", mixed_data)

good_data.insert(0, 'Good Reviews')
bad_data.insert(0, 'Bad Reviews')
mixed_data.insert(0, 'Mixed Reviews')
good_list.insert(0, 'Good Reviews Rating')
bad_list.insert(0, 'Bad Reviews Rating')

with open('data_result.csv', 'w') as csvFile:
    writer = writer(csvFile)
    writer.writerows([good_data])
    writer.writerows([good_list])
    writer.writerows([bad_data])
    writer.writerows([bad_list])
    writer.writerows([mixed_data])
csvFile.close()
