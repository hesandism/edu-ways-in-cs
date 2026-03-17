from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
import numpy as np

def train_model(df):
    features = ["EducationType", "YearsCodePro", "DevType", "Country"]
    target = "ConvertedCompYearly"

    df = df.dropna()

    X = df[features]
    y = df[target]

    X = pd.get_dummies(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, preds))
    r2 = r2_score(y_test, preds)

    return model, rmse, r2