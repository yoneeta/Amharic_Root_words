import re
from Yoni_Word_Generator import *

def check_Word_in_paragraphV2(theParagraph,amharicTimewords,jsonhead):
    #data={}#main json structure
    findvalue=[]#array set
    brokenPharagraph=theParagraph.split()
    wordCounter=0
    for wordToBeVisited in brokenPharagraph:

        findoutlocations_x={}
        #step 3
        
        wordCounter=wordCounter+1
        clean_string=remove_WildCard_From_The_Passage(wordToBeVisited)
        for locatindat in amharicTimewords:
            if locatindat in clean_string:
                #findoutlocations_x['mainvalue']=clean_string
                #findoutlocations_x['indexof']=wordCounter
                #findoutlocations_x['searchitem']=locatindat
                #findvalue.append(findoutlocations_x)
                findvalue.append(clean_string)
        #data[jsonhead] = clean_string
    return findvalue

def check_Word_in_paragraph(theParagraph,amharicTimewords,jsonhead):
    data={}#main json structure
    findvalue=[]#array set
    brokenPharagraph=theParagraph.split()
    wordCounter=0
    for wordToBeVisited in brokenPharagraph:

        findoutlocations_x={}
        #step 3
        
        wordCounter=wordCounter+1
        clean_string=remove_WildCard_From_The_Passage(wordToBeVisited)
        for locatindat in amharicTimewords:
            if locatindat in clean_string:
                findoutlocations_x['mainvalue']=clean_string
                findoutlocations_x['indexof']=wordCounter
                findoutlocations_x['searchitem']=locatindat
                findvalue.append(findoutlocations_x)
        data[jsonhead] = findvalue
    return data


def remove_WildCard_From_The_Passage(currentParagraph):
    char_removed_string = re.sub(r'\W', '', currentParagraph)
    #string = re.sub(r'[^\w]', ' ',currentParagraph)
    #print(string)
    return char_removed_string


def yoni_clear_special_char(theWord):
    punctuations = ["[","!","@","#","$","%","^","&","*","(","\"",")","]","}","{",";",":","፡","፣","-",",",".","/","<",">","?","\/","|","`","~","-","=","_","+","]","፡","-","::","/","፡፡","፤"]#"[!@#$%^&*(\")[]}{;:፡፣-,./<>?\|`~-=_+]፡-::/፡፡፤"
    for i in theWord:
      if i in punctuations:
            #print("i foutn this mark ",i)
            theWord=theWord.replace(i,"")
    return theWord



def yoni_check_The_number(theNumberToCheck):
    
    theParagraph=yoni_clear_special_char(theNumberToCheck)

    amharicAlphabet=Yoni_general_word_generator("numeric_data")

    if theParagraph in amharicAlphabet or theParagraph.isnumeric() or theParagraph.isdecimal():
        return True
    else:
        return False
    
def yoni_check_The_month(theSearchWord):
    if theSearchWord in Yoni_general_word_generator("month_list"):
        return True
    else:
        return False
          
    #return theParagraph#json_data

#print(yoni_check_The_number("ሁለት"))#("20.0\"9)"))