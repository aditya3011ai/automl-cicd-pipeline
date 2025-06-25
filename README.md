# 🚀 AutoML CI/CD Pipeline with PyCaret, FastAPI, Docker & GitHub Actions

This project builds and deploys a complete **Machine Learning pipeline** using **AutoML** (PyCaret), **FastAPI** for serving, **Docker** for containerization, and **GitHub Actions** for CI/CD — all deployed on **AWS EC2**.

---

## 📌 Features

- 🔁 **AutoML Model Training** using PyCaret (automatically selects & trains best classifier)
- ⚙️ **REST API** built with FastAPI to serve real-time predictions
- 📦 **Containerized** with Docker for portability
- 🚀 **CI/CD** using GitHub Actions for automatic deployment to AWS
- ☁️ **Hosted** on AWS EC2 (auto-pulls, builds, and restarts Docker container)

---

## 🧠 Use Case

Predicts **credit risk** based on user financial data. Useful in banking/fintech for quick loan assessments.

---

## 🛠️ Tech Stack

| Tool           | Purpose                               |
|----------------|----------------------------------------|
| PyCaret        | AutoML for classification              |
| FastAPI        | API framework                          |
| Docker         | Containerization                       |
| GitHub Actions | CI/CD pipeline                         |
| AWS EC2        | Cloud deployment (hosted inference API)|
| Git            | Version control                        |

---

## 🧱 Project Structure
```bash
automl-api/
│
├── app/ # FastAPI application
│ ├── main.py # API endpoints
│ └── model.py # Load/save model logic
│
├── src/ # ML training scripts
│ └── train.py # PyCaret AutoML pipeline
│
├── models/ # Trained model artifacts
│ └── best_model.pkl
│
├── Dockerfile # Container setup
├── requirements.txt # Dependencies
├── .github/workflows/ # GitHub Actions CI/CD
│ └── deploy.yml
├── README.md # You're here!
```
---

## ⚡ Quickstart

### 🔧 1. Clone & Setup

```bash
git clone https://github.com/your-username/automl-api.git
cd automl-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
🧪 2. Train Model
```bash
python src/train.py
```

🚀 3. Run API Locally
```bash
uvicorn app.main:app --reload
Access at: http://localhost:8000/docs
```
🐳 Docker Usage
✅ Build Docker Image
```bash
docker build -t automl-api .
```
▶️ Run Docker Container
```bash
docker run -d -p 8000:8000 automl-api
```

🔄 CI/CD Pipeline (GitHub Actions)
Every push to main will:
SSH into EC2
Pull the latest code
Rebuild Docker image
Restart the app container
Secrets Required:
EC2_HOST (e.g., ubuntu@your-ec2-ip)
EC2_SSH_KEY (your private key for SSH)

🌐 Sample API Request
POST /predict
```bash
{
  "status": "A11",
  "duration": 6,
  "credit_history": "A34",
  "purpose": "A43",
  "amount": 1169,
  "savings": "A65",
  "employment_duration": "A75",
  "installment_rate": 4,
  "personal_status_sex": "A93",
  "other_debtors": "A101",
  "present_residence": 4,
  "property": "A121",
  "age": 67,
  "other_installment_plans": "A143",
  "housing": "A152",
  "number_credits": 2,
  "job": "A173",
  "people_liable": 1,
  "telephone": "A192",
  "foreign_worker": "A201"
}
```
Response:
```bash
{
  "prediction": 1
}
```
🔍 Here's What It Means in Context:
You trained a classification model to predict creditworthiness (whether a person will default or not). The prediction output is either:

1 → ✅ Good credit risk (safe to approve loan)

0 → ❌ Bad credit risk (likely to default)


