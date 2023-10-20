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

## Output Part 1 (Text Processing)

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
