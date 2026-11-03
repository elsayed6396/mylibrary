library = []
wishlist = []

Book = input ("Enter the name of a book you own: ")
library. append(Book)

Book = input ("Enter the name of anther book you own (or press 'Enter' to skip): ")
if Book:
    library. append(Book)

print("\nYour library: ", library)

Book = input ("\nEnter the of a book you wish to have in the future: ")
wishlist.append(Book)

Book = input ("\nEnter the name of another book you wish to have (or press 'Enter' to skip): ")
if Book:
    wishlist. append(Book)

    print("\nYour wishlist: ", wishlist)
 
acquired_book = input ("\nEnter the name of a book from your wishlist that you ve acquired (or press 'Enter' to skip):")
if acquired_book in wishlist:
   library. append(acquired_book)
   wishlist. remove(acquired_book)

   print("\nUpdated library: ", library)
   print("\nUpdated wishlist: ", wishlist)

donated_book = input ("\nEnter the name of a book from your library you wish to don ate z(or press 'Enter' to skip):").lower()

if donated_book in library:
    library.remove(donated_book) 
print("\nfinal library after Dontinos: ", library) 


