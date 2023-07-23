import pandas as pd
import spacy


nlp = spacy.load("en_core_web_sm")

df = pd.read_excel('NameExtraction.xlsx')

def extract_company_names(text):
    doc = nlp(text)
    company_names = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
    return ", ".join(company_names)

df['company names'] = df.apply(lambda row: extract_company_names(row['title'] + " " + row['content']), axis=1)

df.to_excel('NameExtraction_Results.xlsx', index=False)