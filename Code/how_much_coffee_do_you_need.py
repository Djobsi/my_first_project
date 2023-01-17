total_coffees = 0

while True:
    event = input()
    if event == "END":
        print(f"{total_coffees}")
        break

    coding = "CODING"
    dog = "DOG"
    cat = "CAT"
    movie = "MOVIE"
    coding_1 = "coding"
    dog_1 = "dog"
    cat_1 = "cat"
    movie_1 = "movie"

    if event != dog and event != dog_1 and event != cat and event != cat_1 and event != movie and event != movie_1 and event != coding and event != coding_1:
        continue

    if event == coding or event == dog or event == cat or event == movie:
        total_coffees += 2

    if event == coding_1 or event == dog_1 or event == cat_1 or event == movie_1:
        total_coffees += 1

    if total_coffees > 5:
        print("You need extra sleep")
        break
    print()