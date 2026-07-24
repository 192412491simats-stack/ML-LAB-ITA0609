from sklearn import svm
from sklearn.preprocessing import StandardScaler

X = [[1,2],[2,3],[3,4],[10,10],[11,11],[12,12]]
y = [0,0,0,1,1,1]

scaler = StandardScaler()
X = scaler.fit_transform(X)

model = svm.SVC(kernel="rbf", C=1.0, gamma="scale")

model.fit(X,y)

test = scaler.transform([[8,8]])

print("Prediction:", model.predict(test))
