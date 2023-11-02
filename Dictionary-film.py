# Dictionary data film
from functools import reduce
movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title": "Spider-Man: No Way Home", "year": 2021, "rating": 7.6, "genre": "Action"},
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title": "No Time to Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]

# Fungsi higher order untuk menghitung jumlah film berdasarkan genre menggunakan reduce
def genre(movies):
    genre_count = reduce(lambda count, movie: {**count, movie["genre"]: count.get(movie["genre"], 0) + 1}, movies, {})
    return genre_count

# Fungsi higher order untuk menghitung rata-rata rating film berdasarkan tahun rilis menggunakan map dan reduce
def rating_by_year(movies):
    year_ratings = reduce(
        lambda acc, movie: {**acc, movie["year"]: {"total_rating": acc.get(movie["year"],
        {"total_rating": 0})["total_rating"] + movie["rating"], "count": acc.get(movie["year"], {"count": 0})["count"] + 1}},
        movies, {})
    return {year: data["total_rating"] / data["count"] for year, data in year_ratings.items()}

# Fungsi higher order untuk menemukan film dengan rating tertinggi menggunakan max
def high_rated_movie(movies):
    high_rated_movie = max(movies, key=lambda x: x["rating"])
    return high_rated_movie

# Fungsi higher order untuk menemukan film dengan rating terendah menggunakan min
def low_rated_movie(movies):
    low_rated_movie = min(movies, key=lambda x: x["rating"])
    return low_rated_movie

# Fungsi higher order dan filter untuk mencari judul film dan menampilkan informasi rating, tahun rilis, dan genre
def movie_by_title(movies, title):
    found_movies = list(filter(lambda x: x["title"] == title, movies))
    if found_movies:
        return found_movies[0]
    else:
        return None

# Menu
while True:
    print("\nPilih tugas yang ingin dilakukan:")
    print("1. Menghitung jumlah film berdasarkan genre")
    print("2. Menghitung rata-rata rating film berdasarkan tahun rilis")
    print("3. Menemukan film dengan rating tertinggi")
    print("4. Menemukan film dengan rating terendah")
    print("5. Cari judul film untuk menampilkan informasi rating, tahun rilis, dan genre")
    print("0. Selesai")

    choice = input("Masukkan nomor tugas (1/2/3/4/5/0): ")
    print("\n")

    if choice == "1":
        genre_count = genre(movies)
        print("Jumlah Film Berdasarkan Genre:", genre_count)

    elif choice == "2":
        average_ratings = rating_by_year(movies)
        print("Rata-rata Rating Film Berdasarkan Tahun Rilis:", average_ratings)

    elif choice == "3":
        high_rated_movie = high_rated_movie(movies)
        print("Film dengan Rating Tertinggi:")
        print("Informasi Film:", high_rated_movie["title"])
        print("Rating:", high_rated_movie["rating"])
        print("Tahun Rilis:", high_rated_movie["year"])
        print("Genre:", high_rated_movie["genre"])
        
    elif choice == "4":
        low_rated_movie = low_rated_movie(movies)
        print("Film dengan Rating Terendah:")
        print("Informasi Film:", low_rated_movie["title"])
        print("Rating:", low_rated_movie["rating"])
        print("Tahun Rilis:", low_rated_movie["year"])
        print("Genre:", low_rated_movie["genre"])

    elif choice == "5":
        title = input("Masukkan judul film yang ingin dicari: ")
        movie = movie_by_title(movies, title)
        if movie:
            print("Informasi Film:", movie["title"])
            print("Rating:", movie["rating"])
            print("Tahun Rilis:", movie["year"])
            print("Genre:", movie["genre"])
        else:
            print("Film dengan judul tersebut tidak ditemukan.")

    elif choice == "0":
        break