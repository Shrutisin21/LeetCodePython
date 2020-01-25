import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split

df = pd.read_csv("titanic.csv")
print df.head(1)
print ("the end")
df.drop(['PassengerId','Name','SibSp','Parch','Ticket','Cabin','Embarked'],axis='columns', inplace=True)
inputs = df.drop('Survived', axis ='columns')
target = df.Survived
inputs.Sex = inputs.Sex.map({'male': 1, 'female': 2})
inputs.Age = inputs.Age.fillna(inputs.Age.mean())
X_train, X_test, y_train, y_test = train_test_split(inputs, target, test_size=0.3)
print len(X_test)
print len(X_train)
model = tree.DecisionTreeClassifier()
model.fit(X_train, y_train)
print model.score(X_test, y_test)