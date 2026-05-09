def greet_user(name):
    return f"Welcome {name}"

print(greet_user("Ali"))


def calculate_area(length, width):
    return length*width
result = calculate_area(3,4)
print(f"The area of the rectangle is: {result}")

def gen(yob):
    if yob < 1981:
        return "Gen X"
    if yob < 1997:
        return "Millenials" 
    if yob < 2013:
        return "Gen Z"
    return "Gen Alpha"
print(gen(2000))


def check_temperature(temp):
    if temp > 30:
        return "Hot"
    if temp < 20:
        return " Cold"
    return "Normal"
status = check_temperature(40)
print(f"This temperature is: {status}.")

def validate_email(email):
    return "Valid email" if "@" in email else "Invalid email"
print(validate_email("abcgmail.com"))

def validate_phone(phone):
    return "Valid phone number" if len(phone) == 10 else "Invalid phone number"
print(validate_phone("024264489"))

def login(username,password):
    return "login successfully" if username == "admin" and password == "12345" 