import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data={
    "hours":[1,2,2.5,3,4,5,6,7,8,9],
    "attendance":[50,55,60,65,70,75,80,85,90,95],
    "result":[0,0,0,0,0,1,1,1,1,1]
    
}

df = pd.DataFrame(data)

X=df[["hours","attendance"]]
Y=df["result"]

print("X:")
print(X)

print("Y:")
print(Y)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)
model = LogisticRegression()

model.fit(X_train, y_train)

prediction = model.predict([[7,64]])
print(prediction)
print("alish")