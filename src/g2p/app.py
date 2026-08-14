from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch 

device = "cuda" if torch.cuda.is_available() else "cpu"
model_id = 'RanaGaber/G2P_DA_Large_country_level'

model = AutoModelForSeq2SeqLM.from_pretrained(model_id).to(device)
tokenizer = AutoTokenizer.from_pretrained(model_id)
model.eval()

def get_phoneme(text: str):
    inputs = tokenizer(text , truncation = True , return_tensors = "pt").to(device)
    with torch.no_grad():
        outputs = model.generate(**inputs)
    pred = tokenizer.decode(outputs[0] , skip_special_tokens = True)
    return pred
    

