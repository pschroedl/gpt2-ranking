### GPT2-Ranking

GPT2-Ranking is a lightweight frontend for experiments using the up-down scoring model of Sean Xiang Gao's DialogRPT.  It is based on a GPT-2 medium (345M) model, pre-trained on 147M Reddit conversations, with an added linear layer to model a regression that predicts the likelyhood of upvotes for a comment, given a context ( submission text body ).  The full model was then trained on 133M context/response pairs of Reddit data from 2011-2012.

Experiments are ongoing.

Local Install
* Install Dependencies: `pip install -r requirements.txt`
* Run server: `python main.py`
* Open Web Browser and visit: `http://localhost:8080/`

Docker Image:
* Build: `docker build -t gpt2-ranking .` 
* Run: `docker run -p 8080:8080 --rm -d gpt-ranking`
