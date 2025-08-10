# Viết chương trình:
# 1. Hỏi tên người dùng
#     Chỉ được chứa chữ cái và khoảng trắng.
#     Độ dài từ 2 → 30 ký tự.
#     Nếu sai → thông báo lỗi và yêu cầu nhập lại.
# 2. Hỏi tuổi
#     Phải là số nguyên.
#     Nằm trong khoảng 1 → 120.
#     Nếu sai → thông báo lỗi và yêu cầu nhập lại.
# 3. Hỏi email
#     Phải chứa ký tự @ và dấu chấm ..
#     Không chứa khoảng trắng.
#     Nếu sai → yêu cầu nhập lại.
def get_valid_name(): # Hàm để lấy tên hợp lệ từ người dùng
    while True:  # Vòng lặp vô hạn để liên tục yêu cầu nhập tên cho đến khi hợp lệ
        name = input("Tên của bạn là gì? ").strip()  # Loại bỏ khoảng trắng đầu và cuối
        if all(part.isalpha() for part in name.split()) and 2 <= len(name) <= 30:  # Kiểm tra tên chỉ chứa chữ cái và khoảng trắng, độ dài từ 2 đến 30 ký tự
            return name.title()  # Chuyển đổi tên thành chữ hoa đầu mỗi từ
        else:
            print("❌Tên không hợp lệ, vui lòng chỉ nhập chữ cái, không có số hay kí tự đặc biệt.\n") 
def get_valid_age():  # Hàm để lấy tuổi hợp lệ từ người dùng
    while True:
        age_input = input("Bạn bao nhiêu tuổi? ").strip()  # Loại bỏ khoảng trắng đầu và cuối
        if not age_input.isdigit():  # Kiểm tra xem chuỗi có phải là số nguyên dương không
            print("❌Tuổi không hợp lệ, vui lòng chỉ nhập số nguyên dương.\n")
            continue
        age = int(age_input)  # Chuyển đổi chuỗi nhập vào thành số nguyên
        if 1 <= age <= 120:  # Kiểm tra tuổi trong khoảng hợp lệ
            return age  # Trả về tuổi hợp lệ
        else:
            print("❌Tuổi không hợp lệ, vui lòng nhập tuổi trong khoảng từ 1 đến 120.\n")
def get_valid_email():  # Hàm để lấy email hợp lệ từ người dùng
    while True:
        email = input("Email của bạn là gì? ").strip()  # Loại bỏ khoảng trắng đầu và cuối
        if "@" in email and "." in email and " " not in email:  # Kiểm tra email có chứa ký tự @ và dấu chấm ., không chứa khoảng trắng
            return email  # Trả về email hợp lệ
        else:   
            print("❌Email không hợp lệ, vui lòng nhập email chứa ký tự @ và dấu chấm ., không có khoảng trắng.\n")
def greet_user():  # Hàm để chào người dùng
    name = get_valid_name()  # Lấy tên hợp lệ
    age = get_valid_age()  # Lấy tuổi hợp lệ
    email = get_valid_email()  # Lấy email hợp lệ   
    birth_year = 2025 - age  # Tính năm sinh dựa trên tuổi
    print(f"Xin chào {name}! Bạn sinh năm {birth_year} đúng không?")  # In lời chào và năm sinh
    print(f"Email của bạn là: {email}")  # In email của người dùng  
greet_user()  # Gọi hàm để thực hiện chương trình  