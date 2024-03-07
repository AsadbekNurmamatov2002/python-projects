x=int(input("x="))
y=int(input("y="))

if x and y:
    print(f"x va y mavjud bo\'lsa shar bajariladi!!! x={x} va y={y}")
elif x or y:
    print(f"x yoke y mavjud bo\'lsa shar bajariladi!!! x={x} or y={y}")
else:
    print("ikki shar bajarilmadi")
    