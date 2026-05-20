# Fraud Risk Engine

AI-based fraud risk scoring engine for fintech transactions using XGBoost and FastAPI.

## Features
- Synthetic account-based transaction generation
- XGBoost fraud detection model
- Rule-based fraud baseline
- FastAPI endpoints for:
  - single transaction scoring
  - account-level batch scoring
  - all-account scoring

## Tech Stack
- Python
- FastAPI
- XGBoost
- Pandas
- Scikit-learn
- Joblib
- Uvicorn

## Project Structure
- `src/` - data generation, preprocessing, training, evaluation, rules
- `app/` - FastAPI backend
- `data/` - raw and scored transaction files
- `models/` - saved trained model files

## Run Locally
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m src.generate_data
python -m src.train_model
uvicorn app.main:app --reload