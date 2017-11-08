#!/usr/bin/env python3

# This program saves data from KSE website
# and stores them in a CSV file

from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import os
import math

stop_words = [u'i', u'me', u'my', u'myself', u'we', u'our', u'ours', u'ourselves', u'you', u'your', u'yours', u'yourself', u'yourselves', u'he', u'him', u'his', u'himself', u'she', u'her', u'hers', u'herself', u'it', u'its', u'itself', u'they', u'them', u'their', u'theirs', u'themselves', u'what', u'which', u'who', u'whom', u'this', u'that', u'these', u'those', u'am', u'is', u'are', u'was', u'were', u'be', u'been', u'being', u'have', u'has', u'had', u'having', u'do', u'does', u'did', u'doing', u'a', u'an', u'the', u'and', u'but', u'if', u'or', u'because', u'as', u'until', u'while', u'of', u'at', u'by', u'for', u'with', u'about', u'against', u'between', u'into', u'through', u'during', u'before', u'after', u'above', u'below', u'to', u'from', u'up', u'down', u'in', u'out', u'on', u'off', u'over', u'under', u'again', u'further', u'then', u'once', u'here', u'there', u'when', u'where', u'why', u'how', u'all', u'any', u'both', u'each', u'few', u'more', u'most', u'other', u'some', u'such', u'no', u'nor', u'not', u'only', u'own', u'same', u'so', u'than', u'too', u'very', u's', u't', u'can', u'will', u'just', u'don', u'should', u'now', u'd', u'll', u'm', u'o', u're', u've', u'y', u'ain', u'aren', u'couldn', u'didn', u'doesn', u'hadn', u'hasn', u'haven', u'isn', u'ma', u'mightn', u'mustn', u'needn', u'shan', u'shouldn', u'wasn', u'weren', u'won', u'wouldn']


totalDocsList = []


def docsListInitializer(numOfDocs):
    global totalDocsList
    
    for i in range(numOfDocs):
        totalDocsList.append(dict())

def getWebPage(pageURL):
    
    try:
        html = urlopen(pageURL)
    except HTTPError:
        return None
        
    bsObj = BeautifulSoup(html.read())
    
    return bsObj
    
def dataParser(bsObj):          # Parse the data from the webpage
    
    ll = bsObj.find("div",id="mw-content-text").findAll("p")
    
    data_string = ""
    
    for i in range(len(ll)):
        data_string += ll[i].get_text()
        
    split_data = data_string.split()
       
    return data_string
   
def dataCleanser(data_string):  # Remove stop words
    
    regex = re.compile('[^a-zA-Z]')
    
    cleansed = re.sub(regex,' ',data_string)
    
    split_data = cleansed.split()
    
    data_string = ' '.join([word for word in split_data if word != "" and word.lower() not in stop_words and len(word) > 1])
    
    return data_string
    
def wordMappingToValues(data,doc_num):      # Count the freequency of the words
    global totalDocsList 
    
    split_data = data.split()
    
    for word in split_data:
        if word in totalDocsList[doc_num]:
            totalDocsList[doc_num][word] += 1
        
        else:
            totalDocsList[doc_num][word] = 1
    
    
######## I can also include TF-IDF scores here ########
def computeCosineSimilarity():
    global totalDocsList
    
    sqrt_sums = 0
    numerator_sum = 0
    temp = 1
    
    docs_sqrts = [0] * len(totalDocsList)
    denominator_product = 1
    
    for key,value in totalDocsList[0].items():
        temp = 1
        try:
            for i in range(len(totalDocsList)):
                temp *= totalDocsList[i][key]
                docs_sqrts[i] += math.pow(totalDocsList[i][key],2)
                
            numerator_sum += temp            
            temp = 1
            
        except KeyError:
            continue    
    
    for i in range(len(docs_sqrts)):
        denominator_product *= math.sqrt(docs_sqrts[i])
        
    result = numerator_sum / denominator_product
    
    print("\n\nThe cosine similarity between the two Wikipedia Articles is : %.3f or %.1f%% \n\n" %(result,(result*100)))
       
if __name__=="__main__":
    
    names_list = ["Kevin_Bacon","Mark_Hamill"]
    
    print('\n\nThe Documents given are : {}'.format(names_list))
    
    docsListInitializer(len(names_list))
    
    for i in range(len(names_list)):
        handle = getWebPage("https://en.wikipedia.org/wiki/"+names_list[i])
        
        if handle != None:
            
            data_handle = dataParser(handle)
            
            data = dataCleanser(data_handle)
            
            wordMappingToValues(data,i)
            
        else:
            print("None")
        
    computeCosineSimilarity()    
        
        
