# Experiment 1: FIND-S Algorithm

# Training Data
# Format:
# [Sky, AirTemp, Humidity, Wind, Water, Forecast, EnjoySport]

training_data = [
    ["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", "Yes"],
    ["Sunny", "Warm", "High", "Strong", "Warm", "Same", "Yes"],
    ["Rainy", "Cold", "High", "Strong", "Warm", "Change", "No"],
    ["Sunny", "Warm", "High", "Strong", "Cool", "Change", "Yes"]
]

# Initialize the hypothesis with the most specific values
hypothesis = ["0"] * (len(training_data[0]) - 1)

print("========== FIND-S ALGORITHM ==========\n")
print("Initial Hypothesis:")
print(hypothesis)
print()

# Process each training example
for sample in training_data:

    print("Processing Sample:", sample)

    # Consider only positive examples
    if sample[-1] == "Yes":

        for i in range(len(hypothesis)):

            if hypothesis[i] == "0":
                hypothesis[i] = sample[i]

            elif hypothesis[i] != sample[i]:
                hypothesis[i] = "?"

        print("Updated Hypothesis:")
        print(hypothesis)

    else:
        print("Negative example ignored.")

    print("-" * 50)

print("\nFinal Hypothesis:")
print(hypothesis)
