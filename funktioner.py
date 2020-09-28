# import libraries
import datetime


def movie_start_worth(cd_price, cd_year, health_grade):
    # kalla funktion och använd detta värda som argument ! assgin:ar värde till purchase_year för tydlighetens skull.
    item_age = berakna_ars_differens(cd_year)

    # kalla funktion och använd detta värda som argument !
    inital_item_value = alders_avdrag(cd_price, item_age)

    health_grade = float(float(health_grade) / 10)
    inital_item_value = round(inital_item_value * float(health_grade))

    return inital_item_value


def book_appreciation_value(years_past_50, initial_value_recieved):
    book_treasure_value = initial_value_recieved * (1.08 ** years_past_50)
    book_treasure_value = str(round(book_treasure_value, 2))
    return book_treasure_value


def alders_avdrag(item_price, item_age):

    # return item_value, which is calculated by items value decreased by each year.
    if item_age > 50:
        item_age = 50
    initial_item_value = float(item_price * 0.9**item_age)
    return initial_item_value


def berakna_ars_differens(purchase_year):
    current_year = datetime.datetime.now().year
    age_of_item = current_year - purchase_year
    return age_of_item


def get_book_value(book_year, book_price):
    # kalla funktion och använd detta värda som argument ! assgin:ar värde till purchase_year för tydlighetens skull.
    item_age = berakna_ars_differens(book_year)

    # kalla funktion och använd detta värda som argument !
    inital_item_value = alders_avdrag(book_price, item_age)

    # call function only for book, the 8% yearly increase of value (a condition must be met in beforehand !)
    if item_age > 50:
        treasure_age = item_age - 50
        book_value = book_appreciation_value(treasure_age, inital_item_value)
        # then set new value. The value is the returnen value from the book_appreciation_value function
        return book_value
    else:
        inital_item_value = round(inital_item_value, 2)
        return inital_item_value
