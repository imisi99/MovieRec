from fastapi import FastAPI
import tensorflow as tf
app = FastAPI()


@app.get("/tags")
async def get_tags():
    country_tags = []
    genre_tags = []
    rating_tags = []
    with open("tags.txt") as f:
        for line in f:
            if line.strip().startswith("Rating"):
                rating_tags.append(line.strip()[len("Rating_"):])
            elif line.strip().startswith("Genre"):
                genre_tags.append(line.strip()[len("Genre_"):])
            elif line.strip().startswith("Country"):
                country_tags.append(line.strip()[len("Country_"):])
            else:
                continue

    return country_tags, rating_tags, genre_tags
@app.post("/predict")
async def predict(data):
    model = tf.keras.models.load_model("model")
    model.predict([data, ])
