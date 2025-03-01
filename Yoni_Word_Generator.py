import json

#አፈላለጋችን በሁለት ፊደሎች ለማድረግ ነበር ማለትም
#ለምሳሌ 'ሁለ' በጽሁፍ ውስጥ ብንፈልግ 'ሁለት' 'ሁለቴ' 'ሁለተኛ' ....
#እያለ ይሄዳል ነገር ግን ለምሳሌ 'ሁለንተናዊ' 'ሁለገብ' .... የምሳሰሉ
#ቃላት ከቁጥራዊ አመላካችነት ውጭ ነው
#ስለዚህ 
out_put_number_array=[]
out_put_location_array=[]
out_put_time_array=[]

#function 1
def yoni_read_myJson():
    #ጄሰን ፋይሉን አንብቦ የጠየቅነውን ሴክሽን ይመልስልናል
    FileName = "Text to Data set/To Excel/numberdefination.json"
    with open(FileName, encoding='utf-8', errors='ignore') as file:
        data = file.read()
        x = json.loads(data, strict=False)
    return x

#function 2       
def yoni_return_section_from_json(section_name):
    #i call function 1
    jsonElement=yoni_read_myJson()
    return jsonElement[section_name]

#function 3
def alphabet_gen(x):# this swithc fuctio return Amharic alphabet in marix as array
    return{
        'ሀ':['ሀ','ሁ','ሂ','ሃ','ሄ','ህ','ሆ'],
        'ለ':['ለ','ሉ','ሊ','ላ','ሌ','ል','ሎ'],
'ሐ':['ሐ','ሑ','ሒ','ሓ','ሔ','ሕ','ሖ'],
'መ':['መ','ሙ','ሚ','ማ','ሜ','ም','ሞ'],
'ሠ':['ሠ','ሡ','ሢ','ሣ','ሤ','ሥ','ሦ'],
'ረ':['ረ','ሩ','ሪ','ራ','ሬ','ር','ሮ'],
'ሰ':['ሰ','ሱ','ሲ','ሳ','ሴ','ስ','ሶ'],
'ሸ':['ሸ','ሹ','ሺ','ሻ','ሼ','ሽ','ሾ'],
'ቀ':['ቀ','ቁ','ቂ','ቃ','ቄ','ቅ','ቆ'],
'በ':['በ','ቡ','ቢ','ባ','ቤ','ብ','ቦ'],
'ተ':['ተ','ቱ','ቲ','ታ','ቴ','ት','ቶ'],
'ቸ':['ቸ','ቹ','ቺ','ቻ','ቼ','ች','ቾ'],
'ኀ':['ኀ','ኁ','ኂ','ኃ','ኄ','ኅ','ኆ'],
'ነ':['ነ','ኑ','ኒ','ና','ኔ','ን','ኖ'],
'ኘ':['ኘ','ኙ','ኚ','ኛ','ኜ','ኝ','ኞ'],
'አ':['አ','ኡ','ኢ','ኣ','ኤ','እ','ኦ'],
'ከ':['ከ','ኩ','ኪ','ካ','ኬ','ክ','ኮ'],
'ኸ':['ኸ','ኹ','ኺ','ኻ','ኼ','ኽ','ኾ'],
'ወ':['ወ','ዉ','ዊ','ዋ','ዌ','ው','ዎ'],
'ዐ':['ዐ','ዑ','ዒ','ዓ','ዔ','ዕ','ዖ'],
'ዘ':['ዘ','ዙ','ዚ','ዛ','ዜ','ዝ','ዞ'],
'ዠ':['ዠ','ዡ','ዢ','ዣ','ዤ','ዥ','ዦ'],
'የ':['የ','ዩ','ዪ','ያ','ዬ','ይ','ዮ'],
'ደ':['ደ','ዱ','ዲ','ዳ','ዴ','ድ','ዶ'],
'ጀ':['ጀ','ጁ','ጂ','ጃ','ጄ','ጅ','ጆ'],
'ገ':['ገ','ጉ','ጊ','ጋ','ጌ','ግ','ጎ'],
'ጠ':['ጠ','ጡ','ጢ','ጣ','ጤ','ጥ','ጦ'],
'ጨ':['ጨ','ጩ','ጪ','ጫ','ጬ','ጭ','ጮ'],
'ጰ':['ጰ','ጱ','ጲ','ጳ','ጴ','ጵ','ጶ'],
'ጸ':['ጸ','ጹ','ጺ','ጻ','ጼ','ጽ','ጾ'],
'ፀ':['ፀ','ፁ','ፂ','ፃ','ፄ','ፅ','ፆ'],
'ፈ':['ፈ','ፉ','ፊ','ፋ','ፌ','ፍ','ፎ'],
'ፐ':['ፐ','ፑ','ፒ','ፓ','ፔ','ፕ','ፖ'],
'ቨ':['ቨ','ቩ','ቪ','ቫ','ቬ','ቭ','ቮ']

    }.get(x, -1)
#print(number_in_words())

#function 3
def Yoni_number_generator():

    vg=yoni_return_section_from_json("numeric_data")#json.loads(number_in_words())
    #print(vg)
    for itterator in vg:
        #print(itterator['sequencefamily'])
        prifix=itterator["prefix"]
        postfix=itterator["postfix"]
        #print(len(prifix))
        #print(len(postfix))
        if len(prifix)>0:
            for mlist in prifix:
                #print(alphabet_gen(mlist))
                for eachwords in alphabet_gen(mlist):
                    #print(eachwords+itterator["mainword"])
                    out_put_number_array.append(eachwords+itterator["mainword"])

        if len(postfix)>0:
            #print("im in postfix")
            for mlist_pf in postfix:
                #print(mlist_pf)
                #print(alphabet_gen(mlist_pf))
                for eachwords_pf in alphabet_gen(mlist_pf):
                    #print(itterator["mainword"]+eachwords_pf)

                    out_put_number_array.append(itterator["mainword"]+eachwords_pf)
        if len(postfix)==0 and len(prifix)==0:
            out_put_number_array.append(itterator["mainword"])
    return out_put_number_array

def Yoni_location_generator():

    vg=yoni_return_section_from_json("location_data")
    for itterator in vg:
        #print(itterator['sequencefamily'])
        prifix=itterator["prefix"]
        postfix=itterator["postfix"]
        #print(len(prifix))
        #print(len(postfix))
        if len(prifix)>0:
            for mlist in prifix:
                #print(alphabet_gen(mlist))
                for eachwords in alphabet_gen(mlist):
                    #print(eachwords+itterator["mainword"])
                    out_put_location_array.append(eachwords+itterator["mainword"])

        if len(postfix)>0:
            #print("im in postfix")
            for mlist_pf in postfix:
                #print(mlist_pf)
                #print(alphabet_gen(mlist_pf))
                for eachwords_pf in alphabet_gen(mlist_pf):
                    #print(itterator["mainword"]+eachwords_pf)

                    out_put_location_array.append(itterator["mainword"]+eachwords_pf)
        if len(postfix)==0 and len(prifix)==0:
            out_put_location_array.append(itterator["mainword"])
    return out_put_location_array

def Yoni_time_generator():
    vg=yoni_return_section_from_json("time_data")
    for itterator in vg:
        #print(itterator['sequencefamily'])
        prifix=itterator["prefix"]
        postfix=itterator["postfix"]
        #print(len(prifix))
        #print(len(postfix))
        if len(prifix)>0:
            for mlist in prifix:
                #print(alphabet_gen(mlist))
                for eachwords in alphabet_gen(mlist):
                    #print(eachwords+itterator["mainword"])
                    out_put_location_array.append(eachwords+itterator["mainword"])

        if len(postfix)>0:
            #print("im in postfix")
            for mlist_pf in postfix:
                #print(mlist_pf)
                #print(alphabet_gen(mlist_pf))
                for eachwords_pf in alphabet_gen(mlist_pf):
                    #print(itterator["mainword"]+eachwords_pf)

                    out_put_time_array.append(itterator["mainword"]+eachwords_pf)
        if len(postfix)==0 and len(prifix)==0:
            out_put_time_array.append(itterator["mainword"])
    return out_put_time_array


def Yoni_general_word_generator(section_selection):
    out_put_general_array=[]
    vg=yoni_return_section_from_json(section_selection)
    #print(vg)
    for itterator in vg:
        #print(itterator['sequencefamily'])
        prifix=itterator["prefix"]
        postfix=itterator["postfix"]
        #print(len(prifix))
        #print(len(postfix))
        if len(prifix)>0:
            for mlist in prifix:
                #print(alphabet_gen(mlist))
                for eachwords in alphabet_gen(mlist):
                    #print(eachwords+itterator["mainword"])
                    out_put_general_array.append(eachwords+itterator["mainword"])

        if len(postfix)>0:
            #print("im in postfix")
            for mlist_pf in postfix:
                #print(mlist_pf)
                #print(alphabet_gen(mlist_pf))
                for eachwords_pf in alphabet_gen(mlist_pf):
                    #print(itterator["mainword"]+eachwords_pf)

                    out_put_general_array.append(itterator["mainword"]+eachwords_pf)
        if len(postfix)==0 and len(prifix)==0:
            out_put_general_array.append(itterator["mainword"])

        #print(out_put_general_array)
    return out_put_general_array
#print(Yoni_general_word_generator("numeric_data"))