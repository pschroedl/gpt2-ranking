# Downloads model(s) during docker build
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = 'distilgpt2'

GPT2LMHeadModel.from_pretrained(model_name).save_pretrained('./gpt2')
GPT2Tokenizer.from_pretrained(model_name).save_pretrained('./gpt2')

def download_model(path):
    if path is None:
        return
    import os, subprocess
    if os.path.exists(path):
        return
    links = dict()
    for k in ['updown', 'depth', 'width', 'human_vs_rand', 'human_vs_machine']:
        links['restore/%s.pth'%k] = 'https://xiagnlp2.blob.core.windows.net/dialogrpt/%s.pth'%k
    links['restore/medium_ft.pkl'] = 'https://convaisharables.blob.core.windows.net/lsp/multiref/medium_ft.pkl'
    if path not in links:
        return
    cmd = [ 'wget', links[path], '-P', 'restore']
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    process.communicate()