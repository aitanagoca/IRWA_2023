# IRWA_2023
Group G_101_7: Mireia Carbó, Aitana González and Raquel Sans

## Functions

### Text Processing (Part 1)

clean(text: string): string.

built_terms(text: string): list of strings.

separate_by_words(input_string): string.

getHashtagsFromTweet_Original(tweet: dict): list of strings.

getHashtagsFromTweet(tweet: dict): list of strings.

getTweetInfo(tweet: dict): dict.

string_concat(stringList: list of strings): string.

read_json_to_dict(json_to_trans: file): dict. The file must reffer to a json.

read_csv_to_dict(csv_to_trans: file): dict. The file must reffer to a csv.

tweets_dict(json_doc: dict, csv_doc: dict): dict.

### Exploratory Data Analysis (Part 1)

avg_sentence_length(tweets_dic: dic): int.

word_count(tweets_dic: dict, category: string): list of lists.

top_x_wc(words_freq: list, x: int): none.

most_retweeted(tweets_dic: dict): dict.

wordcloud_words(words_w_freq: list): none.

## Output Part 1

The output of the last part of the Text Processing COde is a dictionary where the keys are all the docs name (with doc_xxx format) of the tweets and, for each key, the value is another dictionary with the data of the tweet. An example of a key-value pair from the output dictionary would be the following:

{'ID': 1575164742859378689,
 'Tweet': 'Whether you are visiting Nigeria or you living in Nigeria, we understand the importance of information; we know that a lot of our customers sometimes are looking for ideas of where to go and spend their leisure.\n#WelcomeToIndonesia_NCTDREAM #logistics #usa #UkraineRussiaWar #uk https://t.co/T3I9gNVpne',
 'PreProcesed_Tweet': ['whether', 'visit', 'nigeria', 'live', 'nigeria', 'understand', 'import', 'inform', 'know', 'lot', 'custom', 'sometim', 'look', 'idea', 'go', 'spend', 'leisur'],
 'Username': '@simpreslogistis',
 'Date': '28/09/2022 16:45:14',
 'Hashtags': ['#WelcomeToIndonesia_NCTDREAM', '#logistics', '#usa', '#UkraineRussiaWar', '#uk'],
 'Processed_Hashtags': ['Welcome To Indonesia N C T D R E A M', 'logistics', 'usa', 'Ukraine Russia War', 'uk'],
 'Likes': 3,
 'Retweets': 0,
 'URL': 'https://twitter.com/simpreslogistis/status/1575164742859378689'}
