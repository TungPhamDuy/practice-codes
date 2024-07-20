book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
book_count = {}
for i in book_title:
    book_count[i] = book_count.get(i,0)+1
print(book_count)
