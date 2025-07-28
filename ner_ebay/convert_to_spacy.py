import json
import spacy
from spacy.tokens import DocBin

nlp = spacy.blank("en")
doc_bin = DocBin()

with open("annotated_data.json", "r") as f:
    training_data = json.load(f)

for entry in training_data:
    text = entry["text"]
    entities = entry["entities"]
    doc = nlp.make_doc(text)
    ents = []
    for start, end, label in entities:
        span = doc.char_span(start, end, label=label)
        if span:
            ents.append(span)
    doc.ents = ents
    doc_bin.add(doc)

doc_bin.to_disk("train.spacy")
print("Data converted!")
