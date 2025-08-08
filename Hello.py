# Bài tập: Viết một đoạn chương trình hỏi tên người dùng, tuổi, rồi in ra một lời chào như sau: Xin chào A! Bạn sinh năm 2004 đúng không? 
# Nâng cao, kiểm tra điều kiện nhập vào, nếu sai thông báo lỗi và nhập lại
# TH1
# def Great_user():
#     name = input ("Tên của bạn là gì? ")
#     age = int(input ("Bạn bao nhiêu tuổi?")) 
#     #ép kiểu dữ liệu tuổi sang int để tính toán
#     # age = int (age)
#     birth_year = 2025 - age
#     print (f"Xin chào {name}! Bạn sinh năm {birth_year} đúng không?")
# Great_user()
# TH2
def get_valid_name():
    while True:
        name =input("Tên của bạn là gì? ").strip()
        if all(part.isalpha() for part in name.split()) and 2 <= len(name) <= 30: # Kiểm tra tên chỉ chứa chữ cái và khoảng trắng, độ dài từ 2 đến 30 ký tự
            return name.title() # Chuyển đổi tên thành chữ hoa đầu mỗi từ
        else:
            print("❌Tên không hợp lệ, vui lòng chỉ nhập chữ cái, không có số hay kí tự đặc biệt.\n")
def get_valid_age():
    while True:
        age_input = input("Bạn bao nhiêu tuổi? ").strip() # Loại bỏ khoảng trắng đầu và cuối
        if not age_input.isdigit(): # Kiểm tra xem chuỗi có phải là số nguyên dương không
            print("❌Tuổi không hợp lệ, vui lòng chỉ nhập số nguyên dương.\n")
            continue
        age = int(age_input) # Chuyển đổi chuỗi nhập vào thành số nguyên
        if 1 <= age <= 120: # Kiểm tra tuổi trong khoảng hợp lệ
            return age # Trả về tuổi hợp lệ
        else:
            print("❌Tuổi không hợp lệ, vui lòng nhập tuổi trong khoảng từ 1 đến 120.\n")
def greet_user():
    name = get_valid_name()  # Lấy tên hợp lệ
    age = get_valid_age()  # Lấy tuổi hợp lệ
    birth_year = 2025 - age  # Tính năm sinh dựa trên tuổi
    print(f"Xin chào {name}! Bạn sinh năm {birth_year} đúng không?")  # In lời chào và năm sinh
greet_user()  # Gọi hàm để thực hiện chương trình
# Lưu ý: Hàm `title()` sẽ chuyển đổi chữ cái đầu tiên của mỗi từ thành chữ hoa, giúp tên người dùng trông đẹp hơn.