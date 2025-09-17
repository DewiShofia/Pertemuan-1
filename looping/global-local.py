print("Belajar global dan local variabel")
x = 10 # ini adalah global variabel

def contoh():
    x = 5  # ini adalah local variabel
    print("Print x dari local variabel", x)

# walaupun variabel sama tapi scope berbeda

contoh()
print("Print x dari global variabel", x)



