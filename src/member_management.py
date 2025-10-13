from src.utils import read_csv, write_csv, generate_id

MEMBER_FILE = "members.csv"
MEMBER_FIELDS = ["member_id", "name", "status"]

def register_member(name):
    members = read_csv(MEMBER_FILE)
    new_member = {
        "member_id": generate_id("MB"),
        "name": name,
        "status": "active"
    }
    members.append(new_member)
    write_csv(MEMBER_FILE, members, MEMBER_FIELDS)
    print(f"Member '{name}' registered successfully.")

def suspend_member(member_id):
    members = read_csv(MEMBER_FILE)
    for m in members:
        if m["member_id"] == member_id:
            m["status"] = "suspended"
            write_csv(MEMBER_FILE, members, MEMBER_FIELDS)
            print("Member suspended.")
            return
    print("Member not found.")
