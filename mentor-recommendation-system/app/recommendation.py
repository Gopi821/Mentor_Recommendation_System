import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from geopy.distance import geodesic


def recommend_mentors(student_id):

    # Load data
    students = pd.read_csv("data/students.csv")
    mentors = pd.read_csv("data/mentors.csv")

    # Create profiles
    students["profile"] = (
        students["skills"] + " " +
        students["interests"]
    )

    mentors["profile"] = (
        mentors["skills"] + " " +
        mentors["expertise"]
    )

    # Get student
    student = students[
        students["student_id"] == student_id
    ].iloc[0]

    student_profile = student["profile"]

    # TF-IDF
    vectorizer = TfidfVectorizer()

    mentor_vectors = vectorizer.fit_transform(
        mentors["profile"]
    )

    student_vector = vectorizer.transform(
        [student_profile]
    )

    # Cosine Similarity
    similarities = cosine_similarity(
        student_vector,
        mentor_vectors
    )[0]

    final_scores = []

    student_location = (
        student["latitude"],
        student["longitude"]
    )

    # Calculate scores
    for i, mentor in mentors.iterrows():

        mentor_location = (
            mentor["latitude"],
            mentor["longitude"]
        )

        distance = geodesic(
            student_location,
            mentor_location
        ).km

        location_score = 1 / (1 + distance)

        rating_score = mentor["rating"] / 5

        final_score = (
            0.6 * similarities[i]
            + 0.2 * location_score
            + 0.2 * rating_score
        )

        final_scores.append(final_score)

    # Add scores to dataframe
    mentors["similarity"] = similarities
    mentors["final_score"] = final_scores

    # Sort by final score
    recommended = mentors.sort_values(
        by="final_score",
        ascending=False
    )

    # Select top 5 mentors
    result = recommended[
        [
            "mentor_id",
            "mentor_name",
            "similarity",
            "rating",
            "final_score"
        ]
    ].head(5).copy()

    # Round values
    result["similarity"] = result["similarity"].round(3)
    result["final_score"] = result["final_score"].round(3)

    return result