import pandas as pd
import utils

data = pd.read_csv("dataset.csv")
tweets = []

for index, row in data.iterrows():
    row['text'] = utils.limpa_links(row['text'])        #Remover links
    row['text'] = utils.limpa_entidades(row['text'])    #Remover hashtags
    row['text'] = utils.limpa_emoji(row['text'])        #Remover emojis
    tweets.append(row)

df = pd.DataFrame(tweets, columns = ['text', 'label'])
df.to_csv (r'new_dataset.csv', index = None, header=True)