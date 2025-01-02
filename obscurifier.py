#Obscurifier

textFile = "this, is; a text: file."

wordsInText = textFile.split()

for x in wordsInText:
    x=x.replace(".","")
    x=x.replace(",","")
    x=x.replace(";","")
    x=x.replace(":","")
    #at this stage bring in the ngrams
    print(x)
