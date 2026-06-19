from fastapi import FastAPI
from app.recommendation import recommend_mentors

app = FastAPI(
    title="Mentor Recommendation System",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Mentor Recommendation System API is Running"
    }


@app.get("/recommend/{student_id}")
def get_recommendations(student_id: int):

    try:
        result = recommend_mentors(student_id)

        return result.to_dict(orient="records")

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }