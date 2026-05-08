def grade_calculate(grade):
    if grade >= 80:
        return "A"
    if grade >= 70:
        return "B"
    if grade >= 60:
        return "C"
    if grade >= 50:
        return "D"
    return "F"

calculate=grade_calculate(50)
print(calculate)

def validate_file(filename):
    allowed_extensions = [".jpg",".png",".pdf"]
    for extension in allowed_extensions:
        if filename.endswith(extension):
            return "valid file"
    return "Invalid"        

print(validate_file("photo.jpg"))