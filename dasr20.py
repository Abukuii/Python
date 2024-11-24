# Mehmonxona dasturi
def add_client(clients, name, number, status):
    """Mehmonxonaga mehmon qo'shish funksiyasi"""
    clients.append({"name": name, "number": number, "status": status})
    print(f'{name} qabul qilindi!...')

def delete_client(clients, name):
    """Mehmonxonadan mehmonni chiqarish funksiyasi"""
    for client in clients:
        if client["name"] == name:
            clients.remove(client)
            print(f"{name} Mehmonxonadan chiqarildi!")
            return
    print(f"{name} ismli mehmon topilmadi!")

def display_clients(clients):
    """Mehmonlarni ko'rsatish funksiyasi"""
    if clients:
        print("*" * 44)
        print("*     Mehmonlar ro'yxati:                  *")
        print(f"*    {'Name':<15}{'Number':<10}{'Status':<10}   *")
        print("-" * 44)
        for client in clients:
            print(f"*    {client['name']:<15}{client['number']:<10}{client['status']:<10}   * \n")
        print("*" * 44)
    else:
        print("Mehmonxona bo'sh.")

def main():
    clients = [
        {"name": "John", "number": 12, "status": "lyuks"},
        {"name": "Anna", "number": 23, "status": "standart"},
    ]
    while True:
        print("Assalomu alekum Mehmonxonamizga xush kelibsiz!")
        print("\n1 - Mehmon qo'shish")
        print("2 - Mehmonni chiqarish")
        print("3 - Mehmonni ko'rsatish")
        print("\n0 - Chiqish\n")

        try:
            choice = int(input("Sonni kiriting >>> "))
        except ValueError:
            print("Faqat son kiriting!")
            continue

        if choice == 0:
            print("Tizimdan chiqildi!")
            break
        elif choice == 1:
            name = input("Ismni kiriting >>> ")
            try:
                number = int(input("Xona raqamini kiriting >>> "))
            except ValueError:
                print("Xona raqami son bo‘lishi kerak!")
                continue
            if any(client["number"] == number for client in clients):
                print("Bu xona band boshqa xona tanlang!")
                continue
            status = input("Xona turini kiriting (Lyuks/Standart) >>> ").lower()
            add_client(clients, name, number, status)
        elif choice == 2:
            name = input("O'chiriladigan mehmon ismi >>> ")
            delete_client(clients, name)
        elif choice == 3:
            display_clients(clients)
        else:
            print("Xato! Noto'g'ri son kiritildi!")

main()

