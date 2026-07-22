# K-Nearest Neighbours (K-NN)

# Training Data
X = [[2,4],[4,4],[4,6],[6,2],[6,4],[8,4]]
Y = ["A","A","A","B","B","B"]

# Test Data
test = [6,3]

k = 3

distance = []

# Calculate Euclidean Distance
for i in range(len(X)):
    d = ((X[i][0]-test[0])**2 + (X[i][1]-test[1])**2)**0.5
    distance.append([d,Y[i]])

# Sort Distances
distance.sort()

print("Distances:")
for i in distance:
    print(i)

# Count Nearest Neighbours
countA = 0
countB = 0

for i in range(k):
    if distance[i][1] == "A":
        countA += 1
    else:
        countB += 1

# Prediction
if countA > countB:
    print("\nPredicted Class: A")
else:
    print("\nPredicted Class: B")
