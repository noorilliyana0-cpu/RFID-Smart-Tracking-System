from datetime import datetime

# Registered RFID cards
rfid_cards = {
    "RFID001": "Liyana",
    "RFID002": "pavi",
    "RFID003": "saran"
}

# Tracking records
tracking_records = []


def scan_rfid():
    print("\n----------------------------------------")
    print("           RFID SMART TRACKING")
    print("----------------------------------------")

    card_id = input("Enter RFID Card ID: ").strip().upper()

    if card_id in rfid_cards:
        name = rfid_cards[card_id]
        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        record = {
            "card_id": card_id,
            "name": name,
            "time": current_time
        }

        tracking_records.append(record)

        print("\n✓ RFID Card Detected")
        print("Name       :", name)
        print("Card ID    :", card_id)
        print("Date & Time:", current_time)
        print("Status     : ACCESS GRANTED")

    else:
        print("\n✗ Unknown RFID Card")
        print("Card ID :", card_id)
        print("Status  : ACCESS DENIED")


def show_records():
    print("\n========================================")
    print("          TRACKING RECORDS")
    print("========================================")

    if not tracking_records:
        print("No tracking records found.")
        return

    for number, record in enumerate(tracking_records, start=1):
        print(f"\nRecord {number}")
        print("Name       :", record["name"])
        print("Card ID    :", record["card_id"])
        print("Date & Time:", record["time"])


def register_card():
    print("\n----------------------------------------")
    print("          REGISTER RFID CARD")
    print("----------------------------------------")

    card_id = input("Enter new Card ID: ").strip().upper()

    if card_id in rfid_cards:
        print("This RFID card is already registered.")
        return

    name = input("Enter person's name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    rfid_cards[card_id] = name

    print("\n✓ RFID Card registered successfully!")
    print("Card ID:", card_id)
    print("Name   :", name)


def show_registered_cards():
    print("\n========================================")
    print("         REGISTERED RFID CARDS")
    print("========================================")

    if not rfid_cards:
        print("No RFID cards registered yet.")
        return

    for number, (card_id, name) in enumerate(rfid_cards.items(), start=1):
        print(f"{number}. {card_id} - {name}")


def delete_card():
    print("\n----------------------------------------")
    print("          DELETE RFID CARD")
    print("----------------------------------------")

    if not rfid_cards:
        print("No RFID cards registered to delete.")
        return

    card_id = input("Enter Card ID to delete: ").strip().upper()

    if card_id not in rfid_cards:
        print("\n✗ Card ID not found in the registry.")
        return

    name = rfid_cards.pop(card_id)
    print("\n✓ RFID Card deleted successfully!")
    print("Card ID:", card_id)
    print("Name   :", name)


def main():
    while True:
        print("\n")
        print("========================================")
        print("       RFID SMART TRACKING SYSTEM")
        print("========================================")
        print("1. Scan RFID Card")
        print("2. View Tracking Records")
        print("3. Register New RFID Card")
        print("4. View Registered Cards")
        print("5. Delete RFID Card")
        print("6. Exit")
        print("========================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            scan_rfid()

        elif choice == "2":
            show_records()

        elif choice == "3":
            register_card()

        elif choice == "4":
            show_registered_cards()

        elif choice == "5":
            delete_card()

        elif choice == "6":
            print("\nThank you for using RFID Smart Tracking System!")
            break

        else:
            print("\nInvalid choice. Please enter 1, 2, 3, 4, 5, or 6.")


if __name__ == "__main__":
    main()