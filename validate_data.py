def validate(data: dict):
    # return False, "Υπάρχουν τα παρακάτω λάθη:\nΑΦΜ 232424 λάθος"
    errors = []

    if data["aa"] == "":
        errors.append("Το παραστατικό δεν έχει τιμή")

    if data["lines"] == []:
        errors.append("Χρειαζόμαστε τουλάχιστον μια γραμμή")

    return errors
