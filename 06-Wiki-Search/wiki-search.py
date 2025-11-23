import wikipedia
wikipedia.set_lang("en")
topic = input("Topic: ")
try:
    print(wikipedia.summary(topic, sentences=3))
except:
    print("Not found.")