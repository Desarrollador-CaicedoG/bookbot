from stats import get_num_words
from stats import get_num_chara
from stats import sort_items
import sys



def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()



def main():
    a=1
    if len(sys.argv) == 1:
        
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:
            
        book=sys.argv[1]
        print (book)
        txt=get_book_text(book)
        n = get_num_words(txt)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}...")
        print("----------- Word Count ----------")
        print(f"Found {n} total words")
        #print(get_num_chara(txt))
        listado=get_num_chara(txt)
        otro_listado= sort_items(listado) 
    
        print ("--------- Character Count -------")
        for item in otro_listado:
            print(f"{item['num']}: {item['name']}")


main()