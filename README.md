# 🎓 AI Mentor Recommendation System Using Content-Based Filtering

## 📌 Overview

The AI Mentor Recommendation System is an intelligent recommendation platform that helps students discover the most suitable mentors based on their skills, interests, mentor expertise, ratings, and geographical proximity.

The system uses Content-Based Filtering techniques, TF-IDF Vectorization, Cosine Similarity, and GeoPy distance calculations to generate personalized mentor recommendations.

---

## 🎯 Project Objective

Students often struggle to find mentors who match their learning goals and career interests. This project aims to simplify the mentor discovery process by automatically recommending mentors whose expertise closely aligns with a student's profile.

The recommendation engine considers:

* Student Skills
* Student Interests
* Student Location
* Mentor Skills
* Mentor Expertise
* Mentor Ratings
* Geographic Distance

---

## 🚀 Features

✅ Content-Based Mentor Recommendation

✅ TF-IDF Vectorization

✅ Cosine Similarity Matching

✅ Geographic Distance Calculation using GeoPy

✅ Weighted Recommendation Scoring

✅ FastAPI REST API

✅ Interactive Streamlit Dashboard

✅ Student Profile Analysis

✅ Top Mentor Ranking

✅ Clean JSON API Response

---

## 🛠️ Tech Stack

| Component              | Technology                 |
| ---------------------- | -------------------------- |
| Programming Language   | Python                     |
| Backend API            | FastAPI                    |
| Frontend Dashboard     | Streamlit                  |
| Data Processing        | Pandas                     |
| Machine Learning       | Scikit-Learn               |
| Similarity Calculation | TF-IDF + Cosine Similarity |
| Distance Calculation   | GeoPy                      |
| Numerical Computation  | NumPy                      |

---

## 📂 Project Structure

```text
mentor-recommendation-system/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── recommendation.py
│
├── data/
│   ├── students.csv
│   └── mentors.csv
│
├── streamlit_app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Recommendation Workflow

1. Load Student and Mentor Data
2. Create Combined Profiles

   * Skills + Interests
   * Skills + Expertise
3. Apply TF-IDF Vectorization
4. Calculate Cosine Similarity
5. Compute Geographic Distance
6. Generate Weighted Recommendation Score
7. Rank Mentors
8. Return Top 5 Recommendations

---

## 📊 Recommendation Formula

```python
final_score = (
    0.6 * similarity_score
    + 0.2 * location_score
    + 0.2 * rating_score
)
```

Where:

* Similarity Score → TF-IDF + Cosine Similarity
* Location Score → Based on GeoPy Distance
* Rating Score → Mentor Rating / 5

---

## 🌐 FastAPI Endpoints

### Home Endpoint

```http
GET /
```

Response:

```json
{
  "message": "Mentor Recommendation System API is Running"
}
```

### Mentor Recommendation Endpoint

```http
GET /recommend/{student_id}
```

Example:

```http
GET /recommend/1
```

Response:

```json
[
  {
    "mentor_id": 1,
    "mentor_name": "Rahul",
    "similarity": 1.0,
    "distance_km": 249.91,
    "rating": 4.8,
    "final_score": 0.793
  }
]
```

---

## ▶️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd mentor-recommendation-system
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run FastAPI

```bash
python -m uvicorn app.main:app --reload
```

Open Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## ▶️ Run Streamlit Dashboard

```bash
python -m streamlit run streamlit_app.py
```

---

## 📈 Sample Output

The system recommends mentors based on profile similarity, ratings, and location.

Example:

| Mentor | Similarity | Distance (km) | Rating | Final Score |
| ------ | ---------- | ------------- | ------ | ----------- |
| Rahul  | 1.000      | 249.91        | 4.8    | 0.793       |
| Suresh | 0.516      | 289.11        | 4.7    | 0.498       |
| Priya  | 0.294      | 510.89        | 4.9    | 0.373       |

---

## 🔮 Future Enhancements

* MySQL Database Integration
* SQLAlchemy ORM
* Language-Based Matching
* Mentor Availability Tracking
* Experience-Based Ranking
* User Authentication
* Docker Deployment
* AWS/Render Deployment
* Real-Time Recommendation Engine

---

## 💡 Key Learning Outcomes

* Recommendation Systems
* Content-Based Filtering
* Natural Language Processing
* TF-IDF Vectorization
* Cosine Similarity
* FastAPI Development
* Streamlit Dashboard Development
* GeoPy Distance Calculations
* API Development and Testing

---

## 👨‍💻 Author

**Pingali Gopi Reddy**

AI/ML Enthusiast | Python Developer | FastAPI Developer

Passionate about Artificial Intelligence, Machine Learning, Recommendation Systems, and Real-World AI Applications.
