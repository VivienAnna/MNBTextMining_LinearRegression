import re
from collections import Counter
import pandas as pd
import nltk
nltk.download('punkt')
import json
import spacy
import ast

# Hungarian language model
nlp=spacy.load("hu_core_news_lg")
dates=[]
Starter_text=[]

# Preperation for tokenization
def removeTrash(raw_text):
        punctuation = re.sub(r'[^\w\s]', "", raw_text)
        removed = re.sub('[0-9]+', "", punctuation)
        return removed

# Remove empty elements from list
def emptyRemove(txt):
    for i in txt:
        if (len(i) == 0):
            txt.remove(i)
    return txt

# Positive, negative, neutral
def sentimental(word, positive, negative):
    if word in positive:
        return 'pozitív'
    elif word in negative:
        return 'negatív'
    else:
        return 'semleges'

# Ratio calculation function
def norm(pos, neg, sum):
    pos = float(pos)
    neg = float(neg)
    sum = float(sum)
    return pos/sum, neg/sum

# Read the text, remove trash, tokenize, remove stop words, lemmatize, remove affixes, remove empty elements, correct some words, append to list
with open("RawText_MNB/paragraphs.json", "r") as f:
    data=json.load(f)
    for i in data:
        fulltext=removeTrash(i[1])
        doc=nlp(fulltext)

        without_affix=[]
        for token in doc:
            if not token.is_stop:
                root_word=token.lemma_
                without_affix.append(root_word.lower().strip())
        Starter_text.append(emptyRemove(without_affix))
        dates.append(i[0])

text=[]
for i in Starter_text:
    improved_text = []
    for j in i:
        if j=="inflációs" or j=="inflációj":
            new="infláció"
            improved_text.append(new)
        elif j=="ban" or j=="ben" or j=="ig" or j=="ra" or j=="tól" or j=="os" or j=="et" or j=="as" or j=="jei" or j=="án" or j=="ával" or j=="jétől" or j=="től":
            continue
        elif j=="mélypontj":
            new="mélypont"
            improved_text.append(new)
        elif j=="hozamgörb":
            new="hozamgörbe"
            improved_text.append(new)
        elif j=="politikáj" or j=="politiká":
            new="politika"
            improved_text.append(new)
        elif j=="hozamgörb":
            new="hozamgörbe"
            improved_text.append(new)
        elif j=="tendér":
            new="tender"
            improved_text.append(new)
        elif j=="jegybankj":
            new="jegybank"
            improved_text.append(new)
        elif j=="normalizációj":
            new="normalizáció"
            improved_text.append(new)
        elif j=="tonnon" or j=="tonon":
            new="tonna"
            improved_text.append(new)
        elif j=="korlátj":
            new="korlát"
            improved_text.append(new)
        elif j=="lazá":
            new="laza"
            improved_text.append(new)
        elif j=="kommunikációj":
            new="kommunikáció"
            improved_text.append(new)
        elif j=="eurozóná":
            new="eurozóna"
            improved_text.append(new)
        elif j=="rátá" or j=="rát":
            new="ráta"
            improved_text.append(new)
        elif j=="alappályá":
            new="alappálya"
            improved_text.append(new)
        elif j=="árdinamikáj":
            new="árdinamika"
            improved_text.append(new)
        elif j=="reáljövedelm":
            new="reáljövedelem"
            improved_text.append(new)
        elif j=="pályáj" or j=="pályá":
            new="pálya"
            improved_text.append(new)
        elif j=="szintj":
            new="szint"
            improved_text.append(new)
        elif j=="gazdaságpolitikáj":
            new="gazdaságpolitika"
            improved_text.append(new)
        elif j=="adósságrátá":
            new="adósságráta"
            improved_text.append(new)
        elif j=="devizá":
            new="deviza"
            improved_text.append(new)
        elif j=="mozgáster":
            new="mozgástér"
            improved_text.append(new)
        elif j=="het":
            new="hét"
            improved_text.append(new)
        elif j=="futamidej":
            new="futamidő"
            improved_text.append(new)
        elif j=="mozgáster":
            new="mozgástér"
            improved_text.append(new)
        elif j=="tendenciáj":
            new="tendencia"
            improved_text.append(new)
        elif j=="terh":
            new="teher"
            improved_text.append(new)
        elif j=="súlyosbíta":
            new="súlyosbít"
            improved_text.append(new)
        elif j=="reflációs":
            new="refláció"
            improved_text.append(new)
        elif j=="működőtőké":
            new="működőtőke"
            improved_text.append(new)
        elif j=="hiteleszközö":
            new="hiteleszköz"
            improved_text.append(new)
        elif j=="zsugorodhatik":
            new="zsugorodik"
            improved_text.append(new)
        elif j=="alakulhatik":
            new="alakul"
            improved_text.append(new)
        elif j=="mérsékl":
            new="mérsékel"
            improved_text.append(new)
        elif j=="fókuszpontj":
            new="fókuszpont"
            improved_text.append(new)
        elif j=="alátámaszta":
            new="alátámaszt"
            improved_text.append(new)
        elif j=="stratégiáj":
            new="stratégia"
            improved_text.append(new)
        elif j=="kiegyensúlyozot":
            new="kiegyensúlyozott"
            improved_text.append(new)
        elif j=="megugrot":
            new="megugrott"
            improved_text.append(new)
        elif j=="dinamikáj":
            new="dinamika"
            improved_text.append(new)
        elif j=="trendj":
            new="trend"
            improved_text.append(new)
        elif j=="kamatpolitikáj":
            new="kamatpolitika"
            improved_text.append(new)
        elif j=="százalékos":
            new="százalék"
            improved_text.append(new)
        elif j=="energiaszámlá":
            new="energiaszámla"
            improved_text.append(new)
        elif j=="előretekintve" or j=="előretekintő":
            new="előretekint"
            improved_text.append(new)
        elif j=="időzítésű":
            new="időzítés"
            improved_text.append(new)
        elif j=="kamatfixálású":
            new="kamatfixálás"
            improved_text.append(new)
        elif j=="árazású":
            new="árazás"
            improved_text.append(new)
        elif j=="forintosítás":
            new="forintosít"
            improved_text.append(new)
        elif j=="realizálódás":
            new="realizálódik"
            improved_text.append(new)
        elif j=="kkvhitelezési":
            new="kkvhitelezés"
            improved_text.append(new)
        elif j=="devizaswappiaci":
            new="devizaswappiac"
            improved_text.append(new)
        elif j=="horgonyzik" or j=="horgonyzottak" or j=="horgonyzottság":
            new="horgonyoz"
            improved_text.append(new)
        elif j=="újraindítot":
            new="újraindít"
            improved_text.append(new)
        elif j=="félévente":
            new="félév"
            improved_text.append(new)
        elif j=="előrehozás":
            new="előrehoz"
            improved_text.append(new)
        elif j=="újraindulás":
            new="újraindul"
            improved_text.append(new)
        elif j=="swappiaci":
            new="swappiac"
            improved_text.append(new)
        elif j=="újranyitás":
            new="újranyit"
            improved_text.append(new)
        elif j=="swapeszközét":
            new="swapeszköz"
            improved_text.append(new)
        elif j=="toleraciasávba":
            new="toleraciasáv"
            improved_text.append(new)
        elif j=="gdpre":
            new="gdp"
            improved_text.append(new)
        else:
            improved_text.append(j)
    text.append(improved_text)

all_filtered=[]

# Read the dictionary
dictionary=[]
with open("Dictionary/szotar.json", "r", encoding="utf-8") as file:
    dictionary=json.loads(file.read())['data']

pos_neg=[]
positive=dictionary[0]
negative=dictionary[1]

# Sentimental analysis
for i in range(0,len(text)):
    filtered_sentence = []
    sent = []
    for word in text[i]:
        filtered_sentence.append(word)
        sent.append(sentimental(word, positive, negative))
    word_sentimental = []
    word_sentimental.append(dates[i])
    count_PosNeg = Counter(sent)
    word_sentimental.append(dict(count_PosNeg))
    pos_neg.append(word_sentimental)
    temp=[]
    temp.append(dates[i])
    count=Counter(filtered_sentence)
    temp.append(count)
    all_filtered.append(temp)

print(all_filtered)
print(pos_neg)

# Save the filtered text to a csv file
my_df = pd.DataFrame(pos_neg)
my_df.to_csv('cleared_text.csv', index=False, header=False, encoding='utf-8')

pos_neg_ratio=[]

# Ratio calculation
for element in pos_neg:
    initdict = ast.literal_eval(str(element[1]))
    outdict = {}
    # If the key is not in the dictionary, add it with value 0 to the dictionary otherwise add the value
    if 'pozitív' in initdict:
        outdict.update({"pozitív": initdict['pozitív']})
    else:
        outdict.update({"pozitív": 0})

    if 'negatív' in initdict:
        outdict.update({"negatív": initdict['negatív']})
    else:
        outdict.update({"negatív": 0})

    if 'semleges' in initdict:
        outdict.update({"semleges": initdict['semleges']})
    else:
        outdict.update({"semleges": 0})

    # Sum of the values
    outdict.update({"sum": (outdict['pozitív'] + outdict['negatív'] + outdict['semleges'])})

    # Date
    date = element[0]

    pos_r, neg_r = norm(outdict['pozitív'], outdict['negatív'], outdict['sum'])
    ratio='pozitív arány: '+ str(pos_r) + ', negatív arány: ' + str(neg_r)
    ratiosWithDates=[date, pos_r, neg_r]
    pos_neg_ratio.append(ratiosWithDates)

print(pos_neg_ratio)

# Save the ratios to a csv file
my_df = pd.DataFrame(pos_neg_ratio)
my_df.columns = ['Date', 'Positive', 'Negative']
my_df.to_csv('Ratios/ratio.csv', index=False, header=True, encoding='utf-8', sep=';')










