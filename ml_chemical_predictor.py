from sklearn.tree import DecisionTreeClassifier

# Training data (pH values)
X = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13]]

# Labels: 0 = Acid, 1 = Neutral, 2 = Base

y = [0,0,0,0,0,0,1,2,2,2,2,2,2]
# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X, y)

# Take input
pH = float(input("Enter pH value: "))

# Predict
prediction = model.predict([[pH]])

# Output result
if prediction == 0:
    print("Acid")
elif prediction == 1:
    print("Neutral")
else:
    print("Base")
