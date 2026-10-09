"""
Student Manager — DevOps Lab 5
Module: Main Application
"""

def main():
    """Hàm chính của ứng dụng."""
    print("=" * 50)
    print("STUDENT MANAGER — DevOps Lab 5")
    print("=" * 50)

    # Tạo danh sách sinh viên mẫu
    students = [
        {"id": "SV001", "name": "Nguyen Van A", "age": 20, "grade": "K20"},
        {"id": "SV002", "name": "Tran Thi B", "age": 21, "grade": "K20"},
        {"id": "SV003", "name": "Le Van C", "age": 19, "grade": "K21"},
    ]

    # Hiển thị danh sách
    for student in students:
        print(f"  Student(id={student['id']}, name='{student['name']}', age={student['age']}, grade='{student['grade']}')")

    print(f"\nTotal: {len(students)} students")


if __name__ == "__main__":
    main()
    print("\n--- Tìm kiếm ---")
    search_student(students, "Van")

def search_student(students: list, keyword: str) -> list:
    """Tìm kiếm sinh viên theo tên hoặc mã."""
    results = []
    keyword_lower = keyword.lower()

    for s in students:
        if keyword_lower in s['name'].lower() or keyword_lower in s['id'].lower():
            results.append(s)

    if results:
        print(f"\n🔍 Tìm thấy {len(results)} sinh viên với từ khóa '{keyword}':")
        for s in results:
            print(f"  Student(id={s['id']}, name='{s['name']}', age={s['age']}, grade='{s['grade']}')")
    else:
        print(f"\n❌ Không tìm thấy sinh viên nào với từ khóa '{keyword}'")

    return results