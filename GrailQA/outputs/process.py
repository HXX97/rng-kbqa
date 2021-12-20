import json

def redump_dataset(split):
    split = 'train'
    with open(f'grailqa_v1.0_{split}.json','r',encoding='utf8') as f:
        json_arr = json.load(f)

    with open(f'grailqa_v1.0_{split}_indented.json','w',encoding='utf8') as f:
        json.dump(json_arr,f,indent=2)

def redump_entityLinking(split):
    # split = 'demo'
    with open(f'grail_{split}_entities.json','r',encoding='utf8') as f:
        json_arr = json.load(f)

    with open(f'grail_{split}_entities_indented.json','w',encoding='utf8') as f:
        json.dump(json_arr,f,indent=2)

if __name__=='__main__':
    redump_entityLinking('demo')
