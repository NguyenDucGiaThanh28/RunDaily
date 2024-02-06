def main():
    # Đọc số lần đã chạy từ file
    try:
        with open("helloworld.txt", "r") as file:
            content = file.read()
            if content.strip() == "":
                count = 0
            else:
                count = int(content.split()[-1])  # Lấy số cuối cùng từ nội dung file
    except FileNotFoundError:
        count = 0

    # Tăng số lần chạy lên 1
    count += 1

    # Ghi "Hello n" vào file HelloWorld.txt
    with open("helloworld.txt", "a") as file:
        file.write("Hello " + str(count) + "\n")

if __name__ == "__main__":
    print("Script is running")
    main()
