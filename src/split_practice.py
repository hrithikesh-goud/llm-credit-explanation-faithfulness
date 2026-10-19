import pandas as pd
from sklearn.model_selection import train_test_split

# 20 fake applicants: 14 good (1), 6 bad (0)
df = pd.DataFrame({
    "age":    [25, 32, 47, 51, 23, 36, 44, 29, 60, 38, 41, 27, 33, 55, 22, 48, 30, 39, 26, 45],
    "kredit": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
})

X = df[["age"]]     # the input (features)
y = df["kredit"]    # the answer (target)

print(y.value_counts())




X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=13)
print("WITH stratify - test set:")
print(y_test.value_counts())