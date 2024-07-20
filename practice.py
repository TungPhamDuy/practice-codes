book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
book_count = {}
for i in book_title:
    if i not in book_count:
        book_count[i]=1
    else:
        book_count[i]+=1
print(book_count)