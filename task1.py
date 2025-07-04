# House Price Prediction using Linear Regression
# Internship: SkillCraft Technology
# Task: Machine Learning - Task 01

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/Yatin Singh/OneDrive/Desktop/train.csv")  
print("📊 Dataset Preview:")
print(df.head())
print("\n🧼 Missing Values:")
print(df.isnull().sum())
features = ['GrLivArea', 'BedroomAbvGr', 'FullBath']
target = 'SalePrice'
X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"\n📈 Model Performance:")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared Score: {r2:.2f}")


plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred, color='blue', edgecolor='k')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linewidth=2)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices")
plt.grid(True)
plt.tight_layout()
plt.show()


coefficients = pd.DataFrame(model.coef_, features, columns=['Coefficient'])
print("\n📊 Model Coefficients:")
print(coefficients)

print(f"\n🔹 Intercept: {model.intercept_:.2f}")
