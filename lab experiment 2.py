# Candidate Elimination Algorithm (Without Imports)

concepts = [
    ["Sunny", "Warm", "Normal", "Strong", "Warm", "Same"],
    ["Sunny", "Warm", "High", "Strong", "Warm", "Same"],
    ["Rainy", "Cold", "High", "Strong", "Warm", "Change"],
    ["Sunny", "Warm", "High", "Strong", "Cool", "Change"]
]

target = ["Yes", "Yes", "No", "Yes"]

# Initialize Specific Hypothesis
S = concepts[0][:]

# Initialize General Hypothesis
G = [["?" for i in range(len(S))] for j in range(len(S))]

# Candidate Elimination
for i in range(len(concepts)):

    if target[i] == "Yes":
        for j in range(len(S)):
            if concepts[i][j] != S[j]:
                S[j] = "?"
                G[j][j] = "?"

    else:
        for j in range(len(S)):
            if concepts[i][j] != S[j]:
                G[j][j] = S[j]
            else:
                G[j][j] = "?"

print("Final Specific Hypothesis:")
print(S)

print("\nFinal General Hypothesis:")
for g in G:
    if g != ["?", "?", "?", "?", "?", "?"]:
        print(g)
