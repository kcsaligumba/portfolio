import spacy

nlp = spacy.load("output/model-best")

text = "2007 Toyota Camry Headlight Assembly Kit"

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)
