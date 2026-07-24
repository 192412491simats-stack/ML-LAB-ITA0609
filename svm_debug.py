from sklearn import svm

X = [[1,2],[2,3],[3,4],[10,10],[11,11],[12,12]]
y = [0,0,0,1,1,1]

# Bug: Wrong kernel
model = svm.SVC(kernel="linear")

model.fit(X,y)

print(model.predict([[8,8]]))
