

def get_num_words(txt):
    words=txt.split()
    return len(words)

def get_num_chara(txt):
    low_txt=txt.lower()
    low_txt=low_txt.replace("\n", " ")

    num_chara ={}
    for char in low_txt:
        if char != " " :
            if char in num_chara:
                num_chara[char] += 1
            else:
                num_chara[char]=1

    return num_chara

def sort_items (lista):
    nuevo_dic=[]
    for v,k in lista.items():
        nuevo_dic.append({"name": k, "num": v})
    nuevo_dic.sort(reverse=True, key=lambda x: x["name"])
    return nuevo_dic