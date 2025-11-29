def words_counter(book_as_strings:str):
    count_num=len(book_as_strings.split())
    print(f"Found {count_num} total words")

def count_chars(book_as_strings:str):
    dict_each_word={}
    for num in book_as_strings:
        if num==" ":
            continue
        else:
            lwr=num.lower()
            if lwr in dict_each_word:
                dict_each_word[lwr]+=1
            else:
                dict_each_word[lwr]=1
    return dict_each_word

def sorted_dict_list(dict_words:dict):

    def sort_value_dict(dict1:dict):
        return dict1["num"]
    
    new_list=[]
    for letter,count in dict_words.items():
        new_dict={}
        if letter.isalpha():
            new_dict["char"]=letter
            new_dict["num"]=count
            new_list.append(new_dict)
    new_list.sort(reverse=True,key=sort_value_dict)
    for index in new_list:
        character=index["char"]
        num_count=index["num"]
        print(f"{character}: {num_count}")

# def format_report(path_to_file,total_words,total_characters):
#     print(f"============ BOOKBOT ============\nAnalyzing book found at {path_to_file}...")
#     print(f"----------- Word Count ----------\nFound {total_words} total words")
#     print("--------- Character Count -------")
#     total_characters()