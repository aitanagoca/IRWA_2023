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
