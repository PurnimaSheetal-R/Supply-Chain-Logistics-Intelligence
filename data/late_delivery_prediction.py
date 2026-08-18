import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score,
    ConfusionMatrixDisplay
)

# ==============================
# 1. LOAD DATA
# ==============================

file_path = "data/DataCoSupplyChainDataset.csv"

df = pd.read_csv(file_path, encoding="latin1")

print("Dataset loaded successfully!")
print("Shape:", df.shape)


# ==============================
# 2. CREATE TARGET
# ==============================

target = "Late_delivery_risk"

print("\n===== TARGET DISTRIBUTION =====")
print(df[target].value_counts())


# ==============================
# 3. SELECT PREDICTION FEATURES
# ==============================
# Avoid using information that is only known after delivery.
# Therefore, actual shipping duration and delivery status
# are excluded from prediction features.

features = [
    "Shipping Mode",
    "Days for shipment (scheduled)",
    "Market",
    "Order Region",
    "Category Name",
    "Customer Segment",
    "Order Item Quantity",
    "Sales",
    "Order Item Discount",
    "Order Item Product Price"
]

X = df[features]
y = df[target]


# ==============================
# 4. TRAIN / TEST SPLIT
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining rows:", len(X_train))
print("Testing rows:", len(X_test))


# ==============================
# 5. PREPROCESSING
# ==============================

categorical_features = [
    "Shipping Mode",
    "Market",
    "Order Region",
    "Category Name",
    "Customer Segment"
]

numerical_features = [
    "Days for shipment (scheduled)",
    "Order Item Quantity",
    "Sales",
    "Order Item Discount",
    "Order Item Product Price"
]

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

numerical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median"))
])

preprocessor = ColumnTransformer([
    ("categorical", categorical_pipeline, categorical_features),
    ("numerical", numerical_pipeline, numerical_features)
])


# ==============================
# 6. LOGISTIC REGRESSION
# ==============================

logistic_model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(
        max_iter=1000,
        class_weight="balanced"
    ))
])

logistic_model.fit(X_train, y_train)

logistic_predictions = logistic_model.predict(X_test)
logistic_probabilities = logistic_model.predict_proba(X_test)[:, 1]

print("\n===================================")
print("LOGISTIC REGRESSION")
print("===================================")

print(classification_report(y_test, logistic_predictions))

logistic_auc = roc_auc_score(
    y_test,
    logistic_probabilities
)

print("ROC-AUC:", round(logistic_auc, 4))


# ==============================
# 7. RANDOM FOREST
# ==============================

random_forest_model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(
        n_estimators=20,
        max_depth=10,
        random_state=42,
        class_weight="balanced",
        n_jobs=-1
    ))
])


random_forest_model.fit(X_train, y_train)

rf_predictions = random_forest_model.predict(X_test)
rf_probabilities = random_forest_model.predict_proba(X_test)[:, 1]

print("\n===================================")
print("RANDOM FOREST")
print("===================================")

print(classification_report(y_test, rf_predictions))

rf_auc = roc_auc_score(
    y_test,
    rf_probabilities
)

print("ROC-AUC:", round(rf_auc, 4))


# ==============================
# 8. MODEL COMPARISON
# ==============================

print("\n===================================")
print("MODEL COMPARISON")
print("===================================")

print("Logistic Regression ROC-AUC:", round(logistic_auc, 4))
print("Random Forest ROC-AUC:", round(rf_auc, 4))


# ==============================
# 9. CONFUSION MATRIX
# ==============================

ConfusionMatrixDisplay.from_predictions(
    y_test,
    rf_predictions
)

plt.title("Random Forest - Late Delivery Prediction")
plt.tight_layout()

output_path = "visualizations/late_delivery_confusion_matrix.png"

plt.savefig(output_path)

plt.show()

print("\nConfusion matrix saved to:")
print(output_path)

print("\n===================================")
print("LATE DELIVERY PREDICTION COMPLETED")
print("===================================")