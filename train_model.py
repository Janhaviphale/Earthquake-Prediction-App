import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

df = pd.read_csv("dataset/earthquake_data.csv")

df = df.dropna()

X = df[['latitude', 'longitude', 'depth']]
y = df['magnitude']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

error = mean_absolute_error(y_test, predictions)

print("Model Error:", error)

joblib.dump(model, "earthquake_model.pkl")

print("Model Saved Successfully")