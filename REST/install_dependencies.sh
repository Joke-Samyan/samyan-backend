docker run -d -p 27017:27017 --name kodwang mongo
mongorestore --db kodwang --dir dump/kodwang
pip install -r requirements.txt
uvicorn src.server:app --reload