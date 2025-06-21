import pandas as pd
from pycaret.classification import setup, compare_models, finalize_model, save_model
import os

# Step 1: Load Dataset
data_path = os.path.join("data", "credit_risk_dataset.csv")
df = pd.read_csv(data_path)

# Step 2: Set target column
target = 'credit_risk'  # Change to 'loan_status' if 'Class' doesn't exist
# print(df.columns)
# Step 3: Initialize PyCaret setup
clf_setup = setup(
    data=df,
    target=target,
    session_id=42,
    use_gpu=False,
    verbose=False  # Controls logging output
)

# Step 4: Compare and select best model
best_model = compare_models()

# Step 5: Finalize model for deployment
final_model = finalize_model(best_model)

# Step 6: Save model to disk
os.makedirs("models", exist_ok=True)
save_model(final_model, os.path.join("models", "best_model"))

print("✅ Model trained and saved as best_model.pkl")
