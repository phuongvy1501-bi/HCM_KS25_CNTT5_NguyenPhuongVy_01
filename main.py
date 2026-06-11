staff = [
    {"id": "NV001", "name": "Nguyen Van A", "salary" : "400000", "working_day": "25", "allowance": "1500000", "total_income": "11500000", "income_classification": "Khá"}
]
def display_all(data_list):
    if not data_list:
        print("\n[Thông báo]: Danh sách hiện tại đang rỗng!")
        return
    print("\n" + "=" * 75)
    print(f"{'ID':<10} | {'Tên đối tượng':<20} | {'Giá trị':<10} | {'Phân loại':<12} | {'Trạng thái':<15}")
    print("-" * 75)
    for item in data_list:
        v_status = format_status(item.get('status'))
        print(f"{item.get('id').upper():<10} | {item.get('name'):<20} | {item.get('value'):<10} | {item.get('rank'):<12} | {v_status:<15}")
    print("=" * 75)

def add_item(data_list):
    print("\n--- TIẾP NHẬN ĐỐI TƯỢNG MỚI ---")
    while True:
        search_id = validate_input("Nhập mã ID định danh: ")
        for item in data_list:
            if search_id.lower() == item.get("id").lower():
                print("[Lỗi]: Mã ID này đã tồn tại! Vui lòng nhập lại.")
                break
        else:
            name = validate_input("Nhập tên đối tượng: ")
            value = validate_input("Nhập số liệu tính toán: ", "int")
            status = "0"
            rank = classify_item(value)
            
            new_record = {
                "id": search_id,
                "name": name,
                "value": value,
                "rank": rank,
                "status": status
            }
            data_list.append(new_record)
            print("[Thành công]: Đã thêm đối tượng mới vào hệ thống!")
            break

def update_item(data_list):
    print("\n--- CẬP NHẬT TRẠNG THÁI ---")
    if not data_list:
        print("[Thông báo]: Danh sách rỗng!")
        return
    search_id = validate_input("Nhập mã ID cần chỉnh sửa: ")
    for item in data_list:
        if search_id.lower() == item.get("id").lower():
            print(f"Tìm thấy đối tượng: {item.get('name')} | Trạng thái cũ: {format_status(item.get('status'))}")
            item["status"] = "1"
            print("[Thành công]: Đã cập nhật trạng thái sang ĐÃ XỬ LÝ!")
            break
    else:
        print("[Lỗi]: Không tìm thấy mã ID yêu cầu!")










def main():
    database = [
        {"id": "ID01", "name": "Doi tuong Mau A", "value": 45, "rank": "Loại A", "status": "1"},
        {"id": "ID02", "name": "Doi tuong Mau B", "value": 10, "rank": "Loại C", "status": "0"}
    ]
    while True:
        print("\n====== HỆ THỐNG QUẢN LÝ ======")
        print("1. Hiển thị toàn bộ danh sách")
        print("2. Thêm đối tượng mới")
        print("3. Cập nhật trạng thái")
        print("4. Xóa đối tượng")
        print("5. Tìm kiếm (Theo ID hoặc Tên)")
        print("6. Thống kê số lượng phân loại")
        print("7. Thoát chương trình")
        print("========================================")
        choice = input("Vui lòng nhập lựa chọn của bạn: ").strip()
        match choice:
            case "1": display_all(staff)
            case "2": add_item(staff)
            case "3": update_item(staff)
            case "4": remove_item(staff)
            case "5": search_item(staff)
            case "6": chart_item(staff)
            case "7":
                print("Chương trình kết thúc! Hẹn gặp lại.")
                break
            case _:
                print("[Lỗi]: Lựa chọn không hợp lệ! Vui lòng nhập lại.")

if __name__ == "__main__":
    main()