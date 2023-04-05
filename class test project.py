class Book:
    def __init__(self, adi, yazar, sayfa_sayisi, yayinevi):
        self.adi = adi
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.yayinevi = yayinevi

class lib:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Kitap eklendi")

    def del_book(self, adi):
        for book in self.books:
            if book.adi == adi:
                self.books.remove(book)
                print("Kitap silindi")
                break
        else:
            print("Kitap bulunamadı.")

    def look_books(self):
        print("Kütüphanedeki kitaplar:")
        for book in self.books:
            print(f"{book.adi} - {book.yazar}")

    def search_book(self, adi):
        for book in self.books:
            if book.adi == adi:
                print(f"{book.adi} - {book.yazar}")
                break
        else:
            print("Kitap bulunamadı.")


print("Kütüphanemize hoşgeldiniz\n")

library = lib()


while True:
    print("1-Kitap ekleme\n2-Kitap silme\n3-Kitaplara bakma\n4-Kitap arama\n5-Programdan çıkma\n")
    secim = input("Yapmak istediğiniz işlemi seçiniz: ")

    if secim == "1":
        adi = input("Kitap adını giriniz: ")
        yazar = input("Yazarın adını giriniz: ")
        sayfa_sayisi = input("Sayfa sayısını giriniz: ")
        yayinevi = input("Yayınevi adını giriniz: ")
        book = Book(adi, yazar, sayfa_sayisi, yayinevi)
        library.add_book(book)

    elif secim == "2":
        adi = input("Silmek istediğiniz kitabın adını giriniz: ")
        library.del_book(adi)

    elif secim == "3":
        library.look_books()

    elif secim == "4":
        adi = input("Aramak istediğiniz kitabın adını giriniz: ")
        library.search_book(adi)

    elif secim == "5":
        print("Program sonlandırılıyor...")
        break

    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
