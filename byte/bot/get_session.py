from pyrogram import Client

def main():
    app = Client('name', api_id=28104091, api_hash='eedf962b5b2e6c1b124c01b9d6b044fe')

    with app:
        print("Session created!")
        me = app.get_me()
        print(f"You entered like: {me.first_name} (ID: {me.id})")

if __name__ == "__main__":
    main()
