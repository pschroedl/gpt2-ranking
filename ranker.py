import torch
from score import get_model
cuda = True if torch.cuda.is_available() else False
model = get_model('restore/updown.pth', cuda)

def rank(context, response):

    model.eval()

    score = model.predict(context, response, max_cxt_turn=None)
    return str(score[0])

if __name__ == "__main__":
    print(test)
