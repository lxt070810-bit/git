from pathlib import Path

DATA_FILE = Path(__file__).with_name("address_book.txt")
contacts = {}


def add_contacts():
    name = input("please write your name:")
    phone_number = input("please write your number:")
    contacts[name] = phone_number
    save_contacts()
    print(f"{name} 已保存。")


def search_contacts():
    name = input("please write the name you need to search:")
    if name in contacts:
        print("The contact number is:" + contacts[name])
    else:
        print("Contact not found.")


def delete_contacts():
    name = input("please write the name:")
    if name in contacts:
        del contacts[name]
        save_contacts()
        print(f"{name} 已删除。")
    else:
        print("contact not found.")


def load_contacts():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    name, phone_number = line.split(",", 1)
                except ValueError:
                    print(f"跳过格式错误的行：{line}")
                    continue
                contacts[name] = phone_number
    except FileNotFoundError:
        print("Contact not found, will create a new Contacts!")


def save_contacts():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for name, phone_number in contacts.items():
            f.write(name + "," + phone_number + "\n")


def main():
    print("欢迎来到通讯录！")
    load_contacts()

    while True:
        print("1.添加联系人")
        print("2.查询联系人")
        print("3.删除联系人")
        print("4.显示所有联系人")
        print("0.退出")

        choice = input("你的选择是：")

        if choice == "1":
            add_contacts()
        elif choice == "2":
            search_contacts()
        elif choice == "3":
            delete_contacts()
        elif choice == "4":
            for name, phone_number in contacts.items():
                print(f"name:{name},number:{phone_number}\n")
        elif choice == "0":
            save_contacts()
            print("contacts has saved!")
            break
        else:
            print("输入错误！")


if __name__ == "__main__":
    main()
