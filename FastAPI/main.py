from fastapi import FastAPI, HTTPException

app = FastAPI()

test_posts = {
    1: { "title": "Sample Post", "content": "This is a sample post." },
    2: { "title": "Sample Post 2", "content": "This is a sample post 2." },
    3: { "title": "Sample Post 2", "content": "This is a sample post 3." },
    4: { "title": "Sample Post 2", "content": "This is a sample post 4." },
    5: { "title": "Sample Post 2", "content": "This is a sample post 5." },
    6: { "title": "Sample Post 2", "content": "This is a sample post 6." },
    7: { "title": "Sample Post 2", "content": "This is a sample post 7." },
    8: { "title": "Sample Post 2", "content": "This is a sample post 8." },
    9: { "title": "Sample Post 2", "content": "This is a sample post 9." },
    10: { "title": "Sample Post 2", "content": "This is a sample post 10." },
}

@app.get("/posts")
def hello_world():
    return test_posts


@app.get("/posts/{post_id}")
def get_post(post_id: int):
    if post_id not in test_posts:
        raise HTTPException(status_code=404, detail=f"Post {post_id} not found")
    return test_posts.get(post_id)