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

### Indexing (Part 2)

create_index(lines: list): two lists (index & title_index)

search(query: str, index: list): list (with ids).

create_index_tfidf(lines: list, num_documents: int): lists (index, tf, df, idf, title_index)

rank_documents(terms: string, docs: list, index: list, idf: list, tf: list): two lists (one with ids and the other with scores)

search_tf_idf(query: str, index: list): two lists (one with ids and the other with scores)

### Evaluation (Part 2)

precision_at_k(doc_score: list, y_score: list, k: int): float.

recall_at_k(doc_score: list, y_score: list, k: int): float.

avg_precision_at_k(doc_score: list, y_score: list, k: int): float.

f1_score_at_k(doc_score: list, y_score: list, k: int): float.

map_at_k(search_res: list, k: int): float.

rr_at_k(doc_score: list, y_score: list, k: int): float.

mrr_at_k(search_res: list, k: int): float.

dcg_at_k(doc_score: list, y_score: list, k: int): float.

ndcg_at_k(doc_score: list, y_score: list, k: int): float.

### Ranking (Part 3)

create_mapping(lines: list): list

rank_our_score(terms: list, docs: list, index: list, idf, tf, tweets: list, doc_to_tweet: dict): two lists (one with result_docs and the other with result_scores)

search_our_score(query: list, index: list, tweets: list, doc_to_tweet: dict): two lists (one with result_docs and the other with result_scores)

embedding_w2v(terms: list, wmodel: dict): float

rank_Word2Vec(query: list, docs: list, doc_to_tweet: dict, tweets: list): two lists (one with result_docs and the other with result_scores)

search_word2vec(query: list, index: list, doc_to_tweet: dict, tweets: list): two lists (one with ranked_docs and the other with rank_scores)


## Output Part 1 (Text Processing)

The output of the last part of the Text Processing Code is a dictionary where the keys are all the docs name (with doc_xxx format) of the tweets and, for each key, the value is another dictionary with the data of the tweet. An example of a key-value pair from the output dictionary would be the following:

***example with key: doc_3904***

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

 ## Output Part 1 (Exploratory Data Analysis)

 ### Average Sentence Length

 The average sentence length of a tweet is: 11 words.

 ### TOP 10 Words (with their frequencies)

 --Top 10 words and their frequencies--

Word: ukrain - Frequency: 1088

Word: russian - Frequency: 1022

Word: russia - Frequency: 609

Word: the - Frequency: 563

Word: putin - Frequency: 510

Word: ukrainian - Frequency: 469

Word: war - Frequency: 467

Word: forc - Frequency: 277

Word: i - Frequency: 267

Word: region - Frequency: 253

### Most Retweeted Tweets

--We consider the most retweeted tweets the tweets that have more than 100 retweets.--
So the most retweeted tweets are:

** TOP 1 ** (number of retweets: 646)
Username: @Militarylandnet

🗺️Situation around Lyman - Sep 30 11:00:
- UA forces liberated Yampil and advancing north
- RU troops are reportedly abandoning its positions in Drobysheve
- The only exit route from Lyman is within the firing range of UA forces
#UkraineRussiaWar https://t.co/jGJUhXcr1y

** TOP 2 ** (number of retweets: 338)
Username: @Militarylandnet

📷Unique and rare photos of Ukrainian forward command post during the offensive in #Kharkiv Oblast. News reporters aren't usually invited to such places, but here seems to be an exception.
#UkraineRussiaWar https://t.co/AmSijyM59c

** TOP 3 ** (number of retweets: 283)
Username: @Militarylandnet

📽️Operation Interflex: Ukrainian recruits continue to master their skills under the guidance of British and Canadian instructors in the UK.
#UkraineRussiaWar https://t.co/oYWThs8qNe

** TOP 4 ** (number of retweets: 251)
Username: @OSINTschizo

The following countries have urged their citizens to leave 🇷🇺 will update if other governments make similar statements. 
#UkraineRussiaWar #AnnexationofUkraine
#NAFO 

Poland 🇵🇱
Estonia 🇪🇪
Latvia 🇱🇻
Italy 🇮🇹
United States 🇺🇲
Bulgaria 🇧🇬
Romania 🇷🇴
Taiwan 🇹🇼
Canada  🇨🇦
Portugal 🇵🇹

** TOP 5 ** (number of retweets: 247)
Username: @Militarylandnet

📽️Russians shelled the outskirts of #Zaporizhzhia and hit a civilian humanitarian convoy heading towards the occupied parts. 23 people were killed, a dozen more wounded.
#UkraineRussiaWar https://t.co/365j43jy51

** TOP 6 ** (number of retweets: 236)
Username: @CyberMartiansio

The war will not end with the so called annexation referendums which are not genuine expression of the popular will. We are taking a stance to protect our national sovereignty and territorial integrity.
#Ukraine #UkraineRussiaWar  #NFTs https://t.co/yfZAeV7K8d

** TOP 7 ** (number of retweets: 184)
Username: @Ukraine66251776

Russia may have dropped 11 meters long X-22 missile that weighs more than 900 kg, on Ukrainian/NATO forces in #Dnipro 
Russia to use FAB papa bombs and heavy missiles to end this war 
#NATORussiaWar #UkraineRussiaWar #Kherson https://t.co/NuRQPVMzkJ

** TOP 8 ** (number of retweets: 171)
Username: @Militarylandnet

📽️🇺🇦 Ukrainian forces liberated Drobysheve in #Donetsk Oblast. 
#UkraineRussiaWar https://t.co/7wUCdcA7NZ

** TOP 9 ** (number of retweets: 136)
Username: @Militarylandnet

🗞️Kostyantyn Nemichev, the commander of Kraken Special Unit, recently revelated that Kraken has more than 1500 people and is size of regiment. That makes it currently one of the largest Ukrainian unit formed by volunteers.
#UkraineRussiaWar https://t.co/vpQcmL92q7

** TOP 10 ** (number of retweets: 133)
Username: @Militarylandnet

📽️Ukrainian paratroopers on BTR-3 during the offensive in #Kharkiv/#Donetsk Oblast.
#UkraineRussiaWar https://t.co/00LrzsG7QO

** TOP 11 ** (number of retweets: 114)
Username: @ZaidZamanHamid

Baltic pipeline to Poland opens up... Almost on the same day US blows up the Russian pipeline.

But this pipeline from Scandinavia is only going to serve Poland, not the rest of the Europe. Now every country is on its own as the battle for survival begins. 

#UkraineRussiaWar https://t.co/vBTxLm4qMu

** TOP 12 ** (number of retweets: 114)
Username: @Militarylandnet

📷🇨🇿 Czech volunteer during the ongoing offensive of Ukrainian Forces in #Kharkiv Oblast. #UkraineRussiaWar https://t.co/u9tnLGvXlw

### Most Frequent Hashtags (WordCloud)

<img width="720" alt="Captura de pantalla 2023-10-20 a les 16 48 32" src="https://github.com/raquel-sb/IRWA_2023/assets/92036724/fc9c14b6-e77c-4ff2-baa8-65eb991852b9">

## Output Part 2 (Indexing)

### Adaptation of data to create inverted indexes

***example: tweet_lines_list[1]***

1575918081461080065|doc_2|the arm forc liber villag urban territori commun region drobysheve lymansk donetsk ukraine russia war ukraine war ukraine ukraine will win ukrainian army ukrainecounteroffensive ukraine war news slava ukra stand with ukraine

### Inverted index 

**- WITH term position information:** Total time to create the index: 2.95 seconds.

**- WITHOUT term position information:** Total time to create the index: 304.12 seconds

### Example search_tf_idf()

**QUERY 1**

Eastern separatists groups

======================
Top 10 results out of 55 for the searched query:


tweet_id = 1575842840768569344 - tweet_title: doc_538 - score: 9.068672454039067
tweet_text: The spokesman of the Eastern group of troops Cherevaty reported that the encirclement of the Russian group near Lyman in Donetsk region is "at the stage of completion"
#UkraineRussiaWar https://t.co/drAsg9PDes

tweet_id = 1575818569857658880 - tweet_title: doc_812 - score: 7.9992014749313505
tweet_text: First Official APU Report on Lyman:  "The operation to encircle the Russian group in the Estuary is at the completion stage" —  Sergey Cherevaty, Eastern Grouping 

#UkraineRussiaWar 
#OSINT
#Fellas #NAFO

tweet_id = 1575821202064834560 - tweet_title: doc_776 - score: 7.348035242319465
tweet_text: Cherevaty, the spokesperson of the Eastern group of troops, reported the encirclement of the #Russian group near #Lyman in the #Donetsk region is “at the stage of completion.” #Ukraine #UkraineRussiaWar #UkraineWar 

📷 Tpyxa https://t.co/jUcJncxRJ6

tweet_id = 1575820237010006017 - tweet_title: doc_790 - score: 7.255889456636643
tweet_text: Update: Addition comments from APU Eastern Grouping

#UkraineRussiaWar 
#OSINT
#Fellas #NAFO https://t.co/svKSKcy403

tweet_id = 1575180675002486785 - tweet_title: doc_3778 - score: 6.671130033545804
tweet_text: @nytimes Wherever these 200k draft dodgers have gone, they're many enough to be the future Russian separatists beloved by Putin #UkraineRussiaWar #RussianArmy #Russians

tweet_id = 1575818037130731520 - tweet_title: doc_820 - score: 6.655307724400341
tweet_text: ❗️Official comment on the situation in Lyman from the military

 💬 "The operation to encircle the Russian group in Lyman is "at the stage of completion", - the representative of the Eastern group Serhiy Chereviy.
#UkraineWillWin 
#UkraineWar 
#UkraineRussiaWar 
#Russian https://t.co/vuKHUpOfoF

tweet_id = 1575785557896007682 - tweet_title: doc_1183 - score: 5.720494003765528
tweet_text: The head of the Russian-backed separatist administration in east Ukraine's Donetsk region said the Russian stronghold of Lyman was "semi-encircled" by the Ukrainian army and that news from the front was "alarming."

#Russia | #Donetsk | #UkraineRussiaWar 

https://t.co/sGp1vw7334

tweet_id = 1575488992929513473 - tweet_title: doc_2382 - score: 4.629911409155417
tweet_text: Ukrainian Forces at the Eastern front in action. https://t.co/ocDykq9rI5 lewat @YouTube #war #ukraine #russia #ukrainerussiawar #nowar

tweet_id = 1575353426564857857 - tweet_title: doc_2977 - score: 3.6605877681494445
tweet_text: Russian attack hits a school in eastern Ukraine's town of Mykolaivka being used by residents as a shelter.

#UkraineRussiaWar 
https://t.co/s5ji7BpJ8h

tweet_id = 1575822314586808320 - tweet_title: doc_745 - score: 3.3648667793298763
tweet_text: Reports of #Russian battle groups and bombers en route to #Lyman are just to cover the retreat, I think.  The settlement is gone. #UkraineRussiaWar

### Selected queries

**- Query 1:** "Eastern separatists groups"

**- Query 2:** "Humanitarian impact"

**- Query 3:** "Media coverage of war"

**- Query 4:** "Negotiations in war"

**- Query 5:** "Russian propaganda and disinformation"

## Output Part 2 (Evaluation)

### Dataframe created with the queries (.head())

<img width="472" alt="Captura de pantalla 2023-10-28 a les 23 31 17" src="https://github.com/raquel-sb/IRWA_2023/assets/92036724/16f7e06b-a5c4-43f4-84fb-76d83a0c3e75">

### Evaluation techniques (Selected queries)

#### Precision@k

Query1 -  Precision@4: 1.0

Query2 -  Precision@4: 0.5

Query3 -  Precision@4: 0.5

Query4 -  Precision@4: 0.5

Query5 -  Precision@4: 0.75

Query1 -  Precision@8: 0.75

Query2 -  Precision@8: 0.625

Query3 -  Precision@8: 0.625

Query4 -  Precision@8: 0.5

Query5 -  Precision@8: 0.625

Query1 -  Precision@12: 0.5

Query2 -  Precision@12: 0.6666666666666666

Query3 -  Precision@12: 0.75

Query4 -  Precision@12: 0.5833333333333334

Query5 -  Precision@12: 0.5

Query1 -  Precision@16: 0.4375

Query2 -  Precision@16: 0.5625

Query3 -  Precision@16: 0.625

Query4 -  Precision@16: 0.5

Query5 -  Precision@16: 0.4375

Query1 -  Precision@20: 0.5

Query2 -  Precision@20: 0.5

Query3 -  Precision@20: 0.5

Query4 -  Precision@20: 0.5

Query5 -  Precision@20: 0.5

#### Recall@k

Query1 -  Recall@4: 0.4

Query2 -  Recall@4: 0.2

Query3 -  Recall@4: 0.2

Query4 -  Recall@4: 0.2

Query5 -  Recall@4: 0.3

Query1 -  Recall@8: 0.6

Query2 -  Recall@8: 0.5

Query3 -  Recall@8: 0.5

Query4 -  Recall@8: 0.4

Query5 -  Recall@8: 0.5

Query1 -  Recall@12: 0.6

Query2 -  Recall@12: 0.8

Query3 -  Recall@12: 0.9

Query4 -  Recall@12: 0.7

Query5 -  Recall@12: 0.6

Query1 -  Recall@16: 0.7

Query2 -  Recall@16: 0.9

Query3 -  Recall@16: 1.0

Query4 -  Recall@16: 0.8

Query5 -  Recall@16: 0.7

Query1 -  Recall@20: 1.0

Query2 -  Recall@20: 1.0

Query3 -  Recall@20: 1.0

Query4 -  Recall@20: 1.0

Query5 -  Recall@20: 1.0

#### AvgPrecision@20

Query1 -  Average Precision@20: 0.7575271512113617

Query2 -  Average Precision@20: 0.670554298642534

Query3 -  Average Precision@20: 0.6098701298701299

Query4 -  Average Precision@20: 0.5729698028150041

Query5 -  Average Precision@20: 0.6145588235294117

#### F1-Score@k

Query1 -  F1-Score@4: 0.5714285714285715

Query2 -  F1-Score@4: 0.28571428571428575

Query3 -  F1-Score@4: 0.28571428571428575

Query4 -  F1-Score@4: 0.28571428571428575

Query5 -  F1-Score@4: 0.4285714285714285

Query1 -  F1-Score@8: 0.6666666666666665

Query2 -  F1-Score@8: 0.5555555555555556

Query3 -  F1-Score@8: 0.5555555555555556

Query4 -  F1-Score@8: 0.4444444444444445

Query5 -  F1-Score@8: 0.5555555555555556

Query1 -  F1-Score@12: 0.5454545454545454

Query2 -  F1-Score@12: 0.7272727272727272

Query3 -  F1-Score@12: 0.8181818181818182

Query4 -  F1-Score@12: 0.6363636363636365

Query5 -  F1-Score@12: 0.5454545454545454

Query1 -  F1-Score@16: 0.5384615384615384

Query2 -  F1-Score@16: 0.6923076923076923

Query3 -  F1-Score@16: 0.7692307692307693

Query4 -  F1-Score@16: 0.6153846153846154

Query5 -  F1-Score@16: 0.5384615384615384

Query1 -  F1-Score@20: 0.6666666666666666

Query2 -  F1-Score@20: 0.6666666666666666

Query3 -  F1-Score@20: 0.6666666666666666

Query4 -  F1-Score@20: 0.6666666666666666

Query5 -  F1-Score@20: 0.6666666666666666

#### MAP@k

MAP@4: 0.195

MAP@8: 0.3537380952380952

MAP@12: 0.49712193362193363

MAP@16: 0.5544424464424464

MAP@20: 0.6450960412136884

#### MRR@k

MRR@4 = MRR@8 = MRR@12 = MRR@16 = MRR@20: 0.7667

#### NDCG@k

Query1 -  NDCG@4: 1.0

Query2 -  NDCG@4: 0.5585

Query3 -  NDCG@4: 0.3633

Query4 -  NDCG@4: 0.4144

Query5 -  NDCG@4: 0.7537

Query1 -  NDCG@8: 0.8224

Query2 -  NDCG@8: 0.6296

Query3 -  NDCG@8: 0.4974

Query4 -  NDCG@8: 0.4565

Query5 -  NDCG@8: 0.6582

Query1 -  NDCG@12: 0.7156

Query2 -  NDCG@12: 0.7372

Query3 -  NDCG@12: 0.6835

Query4 -  NDCG@12: 0.5885

Query5 -  NDCG@12: 0.6322

Query1 -  NDCG@16: 0.7706

Query2 -  NDCG@16: 0.795

Query3 -  NDCG@16: 0.7374

Query4 -  NDCG@16: 0.6463

Query5 -  NDCG@16: 0.6873

Query1 -  NDCG@20: 0.9234

Query2 -  NDCG@20: 0.8478

Query3 -  NDCG@20: 0.7374

Query4 -  NDCG@20: 0.75

Query5 -  NDCG@20: 0.842

### Vector representation

<img width="566" alt="Captura de pantalla 2023-10-28 a les 23 37 37" src="https://github.com/raquel-sb/IRWA_2023/assets/92036724/56cc769c-be5f-4e11-9b2b-b8a2edb28150">

<img width="414" alt="Captura de pantalla 2023-10-28 a les 23 38 03" src="https://github.com/raquel-sb/IRWA_2023/assets/92036724/d5e7480c-aaee-4a62-83d1-1850de80d158">

## Output Part 3 

### TF-IDF+cosine similarity vs Our score+cosine similarity
The proposed scoring mechanism also takes into account the number of likes (20%), the number of retweets (20%) and the presence of relevant hashtags (60%). This change has caused some changes in the ranking of search results compared to the TF-IDF + Cosine Similarity.

This new scoring approach prioritizes tweets with higher engagement (likes and retweets) and a stronger presence of relevant hashtags, potentially capturing more popular and widely discussed content about the query in question. However, it is important to keep in mind that, as we have seen in the tweets obtained for each query, the nature of the participation (likes and retweets) does not always reflect the accuracy or credibility of the information.

To carry out the comparison of both methods, we performed different Precision@k with 5 different K's. First of all, we review the tweets returned by our_score and assign them a ground_truth that we consider correct in order to perform this check. Regarding the ground_truth of the tweets returned by tf-idf, we already had a ground_truth selected in the previous part of this project, so we used the same values ​​in that case.

We obtain the following results for TF-IDF + Cosine Similarity and for Our-Score + Cosine SImilarity respectively:
<img width="396" alt="image" src="https://github.com/raquel-sb/IRWA_2023/assets/72573624/d9c92450-7491-4641-9e1e-ab4b13a76a00">
