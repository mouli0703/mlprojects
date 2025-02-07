import os
import pickle

preprocessor_path = "artifacts/preprocessor.pkl"

# Check if file exists
if not os.path.exists(preprocessor_path):
    print(f"Error: {preprocessor_path} does not exist.")
else:
    with open(preprocessor_path, "rb") as f:
        preprocessor = pickle.load(f)
        print("Preprocessor loaded successfully!")
