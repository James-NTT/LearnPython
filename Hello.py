# Bài tập: Viết một đoạn chương trình hỏi tên người dùng, tuổi, rồi in ra một lời chào như sau: Xin chào A! Bạn sinh năm 2004 đúng không?  
def Great_user():
    name = input ("Tên của bạn là gì? ")
    age = int(input ("Bạn bao nhiêu tuổi?")) //dùng int sẽ không phải ép kiểu
    #ép kiểu dữ liệu tuổi sang int để tính toán
    # age = int (age)
    birth_year = 2025 - age
    print (f"Xin chào {name}! Bạn sinh năm {birth_year} đúng không?")
Great_user()

