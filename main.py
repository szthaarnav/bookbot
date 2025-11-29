from stats import words_counter,count_chars,sorted_dict_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents=f.read()
        return(file_contents)

def main():
    import sys
    if len(sys.argv)==2:
        path1=sys.argv[1]
        print(f"Analyzing book found at {path1}...")
        book1_string=get_book_text(path1)
        words_counter(book1_string)
        sorted_dict_list(count_chars(book1_string))
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()