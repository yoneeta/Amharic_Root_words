import json
import re
import codecs
from difflib import SequenceMatcher
from docx import Document



isithit=[]
#ሲሚላሪቲን ቼክ ለማድረግ     
def charSequencSimilarity(str1,str2):
    
    s = SequenceMatcher(None, str1,str2)
    s.ratio()
    #print(jellyfish.damerau_levenshtein_distance(str1,str2))
    #print(jellyfish.jaro_distance(str1,str2))
    #print(jellyfish.levenshtein_distance(str1,str2))
    #print( s.ratio())

    return s.ratio()

#this called from main WA and it calles for every word on source language
#it extract the target language and put on the array
def targetLanguageExt(theword,dorun):
        if len(theword) > 2 and dorun not in isithit:
            
            if len(theword)==len(dorun):#checking the word similarity and steam the word
                intersectoral=list(set(theword)& set(dorun))# intersection among the two amharic words
                if len(intersectoral) >= round(len(theword)/2) and charSequencSimilarity(theword,dorun) > 0.5:
                    #print("x",theword,dorun)
                    isithit.append(dorun)
                    return "x"
            else:
                if theword in dorun:
                    #print("d",theword,dorun)
                    isithit.append(dorun)
                    return "d"
               


sourceLanguage=[]
with open('/BBC2amharic.txt', mode="r", encoding="utf-8") as s_my_file:
    for line in s_my_file:
        #print(type(line))
        #print(re.sub('\W+',' ',line))
        sourceLanguage.append(re.sub('\W+',' ',line))


# # def tableViziter():
# #     for table in doc.tables:
# #         for row in table.rows:
# #             for cellz in row.cells:
# #                 print cellz.text

allWords=[]
for jagz in sourceLanguage:
    for i in jagz.split():
        allWords.append(i)

print(allWords)
#step 3
for inx,para in enumerate(allWords): # find this word 
    for zindx,zi in enumerate(allWords[inx:]): # the location were we searching
        #print(para,zi)
        #print(len(zi))
        resultindex=targetLanguageExt(para,zi)
        if resultindex != None:
            allWords.pop(zindx)
            #print(resultindex,para,zi)
        #print(len(zi))
