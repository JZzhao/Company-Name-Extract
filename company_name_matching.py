import pandas as pd
df = pd.read_excel('NameMatch.xlsx', sheet_name='Sheet2')
Table_A = [3, 24]  # Replace with the indices of the rows you want to copy
rows_list_A = df.iloc[3:23,0].values.tolist()

Table_B = [3, 21]  # Replace with the indices of the rows you want to copy
rows_list_B = df.iloc[3:23,2].values.tolist()

#----Solution-1------
import pandas as pd
from fuzzywuzzy import fuzz

# Read the data from the Excel file
df_table_a = rows_list_A
df_table_b = rows_list_B

# Function for fuzzy matching
def fuzzy_match(name_a, name_b, threshold=80):
    return fuzz.token_set_ratio(name_a, name_b) >= threshold

# Match and standardize names
matches = []
for name_a in df_table_a:
    match_found = False
    for name_b in df_table_b:
        if fuzzy_match(name_a, name_b):
            matches.append((name_a, name_b))
            match_found = True
            break
    if not match_found:
        matches.append((name_a, None))

# Create a DataFrame with matched names
df_matches = pd.DataFrame(matches, columns=['Company Name (A)', 'Company Name (B)'])

# Print the result
print(df_matches)

#----Solution-2------
df_table_a = rows_list_A
df_table_b = rows_list_B

# Function for fuzzy matching and best match selection
def fuzzy_best_match(name_a, names_b):
    match, score = process.extractOne(name_a, names_b)
    return match if score >= 80 else None

# Match and standardize names
matches_1 = []
for name_a in df_table_a:
    match_b = fuzzy_best_match(name_a, df_table_b)
    matches.append((name_a, match_b))

# Create a DataFrame with matched names
df_matches_1 = pd.DataFrame(matches_1, columns=['Company Name (A)', 'Company Name (B)'])

# Print the result
print(df_matches_1)

#----Solution-3------
#Given enough time and labeled data, we can build modeling-based approach to do the data mapping
#Below is the solution concept with key points
# Step-1 Preprocessing: Preprocess the company names by tokenizing, lowercasing, and removing special characters and stop words.

# Step-2 Embedding: Convert the preprocessed names into dense vector representations using word embeddings or subword embeddings like Word2Vec, GloVe, FastText, or BERT.

# Step-3 Similarity Measure: Use cosine similarity or other distance metrics to measure the similarity between the embeddings of names from Table A and Table B.

# Step-4 Matching and Standardization: Establish a similarity threshold and identify matches based on the similarity score. 
# Group similar names and standardize them based on the most common representation or using additional metadata if available.