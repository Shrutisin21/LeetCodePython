import pandas as pd
import collections
import string
#tweetCsv = pd.read_csv("trumptweets.csv")
df = pd.read_csv('trumptweets.csv', usecols=['content'])
print type(df)
tweetList = df.values.tolist()
wordArray = []
for tweet in tweetList:
    wordArray.extend(string.upper(''.join(tweet)).split())
print wordArray[1]

# Pass the split_it list to instance of Counter class.
Counter = collections.Counter(wordArray)

# most_common() produces k frequently encountered
# input values and their respective counts.
most_occur = Counter.most_common(1000)
finalList =[]
print type(most_occur[0])
for pair in enumerate(most_occur):
    print str(pair), str(len(str(pair)))

    if len(str(pair[0])) > 3:
        print 'inside if'
        finalList.append(str(pair[0]),str(pair[1]))
print(finalList)