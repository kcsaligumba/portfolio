import pandas as pd
import spacy

# Load English language model
nlp = spacy.load("en_core_web_sm")

# Read titles from the CSV
df = pd.read_csv("titles.csv")

# Clean each title (remove punctuation)
def clean_text(text):
    doc = nlp(text)
    return " ".join([token.text for token in doc if not token.is_punct])

df["cleaned"] = df["title"].apply(clean_text)

# Save the cleaned titles to a new CSV
df.to_csv("cleaned_titles.csv", index=False)

print("Done cleaning!")
