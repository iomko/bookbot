def sort_on(items):
    return items["num"]

def convert_dic_to_dic_list(dic):
    char_list_key_value = [{"char": k, "num": v} for k, v in dic.items()]
    char_list_key_value.sort(reverse=True,key=sort_on)
    return char_list_key_value

def count_characters(book_str):
    dic = {}

    for cha in book_str:
        lowered_char = cha.lower()
        if lowered_char not in dic:
            dic[lowered_char] = 1
        else:
            dic[lowered_char] += 1
    
    return dic

def count_words(book):
    split_text = book.split()
    return len(split_text)

def get_book_text(filepath):
    
    file_contents = None
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

