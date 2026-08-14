from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model_id = 'RanaGaber/G2P_DA_Large_country_level'

model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)
model.eval()

def get_phoneme(text: str):
    inputs = tokenizer(text , truncation = True)
    outputs = model(**inputs)
    pred = tokenizer.decode(outputs[0] , skip_special_tokens = True)
    return pred
    

