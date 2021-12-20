
file_path = '/data/xxhu/rng-kbqa/GrailQA/entity_linker/data/entity_list_file_freebase_complete_all_mention'
# file_path = '/data/xxhu/rng-kbqa/GrailQA/entity_linker/data/surface_map_file_freebase_complete_all_mention'

with open(file_path,'r', encoding='utf8') as f:
    idx = 0
    for line in f:
        print(line)
        idx+=1
        if idx==20:
            break

