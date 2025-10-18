
import pandas as pd
from src.utils import read_csv, write_csv, generate_id
from config.settings import config


class MemberManager:
    """
    Handles library member management operations such as registration,
    suspension, activation, and listing of members.
    """

    def __init__(self):
        """Initialize the member manager and ensure file consistency."""
        try:
            self.file_path = config.MEMBER_FILE
            self.fields = config.MEMBER_FIELDS
            self.df = read_csv(self.file_path)

            # Load member data
            # if not os.path.exists(self.file_path):
            #     self.df = pd.DataFrame(columns=self.fields)
            #     write_csv(self.file_path, self.df, self.fields)
            # else:
            #     self.df = read_csv(self.file_path)

            # Ensure DataFrame consistency
            if self.df.empty:
                self.df = pd.DataFrame(columns=self.fields)

        except Exception as e:
            print(f"[INIT ERROR] Failed to initialize MemberManager: {e}")

    
    def register_member(self, name: str) -> None:
        """
        Register a new library member.

        Args:
            name (str): Member's full name.
        """
        try:
            new_member = {
                "member_id": generate_id("MB"),
                "name": name.strip(),
                "status": "active"
            }

            self.df = pd.concat([self.df, pd.DataFrame([new_member])], ignore_index=True)
            write_csv(self.file_path, self.df, self.fields)

            print(f" Member '{name}' registered successfully.")
        except Exception as e:
            print(f" Error while registering member: {e}")


    def suspend_member(self, member_id: str) -> None:
        """
        Suspend a member's account.

        Args:
            member_id (str): ID of the member to suspend.
        """
        try:
            # if self.df.empty or member_id not in self.df["member_id"].values:
            # if self.df.empty or member_id not in self.df['member_id'].values:
            #     print(" Member not found.")
            #     return

            # self.df.loc[self.df["member_id"] == member_id, "status"] = "suspended"
            # member_id = str(member_id).strip()  # ensure it's a clean string
            

            if self.df.empty or member_id not in self.df["member_id"].astype(str).str.strip().values:
                
                print(" Member not found.")
                return

            # Update status safely
            self.df.loc[self.df["member_id"].astype(str).str.strip() == member_id, "status"] = "suspended"

            write_csv(self.file_path, self.df, self.fields)

            print(f" Member '{member_id}' suspended successfully.")
        except Exception as e:
            print(f" Error while suspending member: {e}")

    

    def activate_member(self, member_id: str) -> None:
        """
        Reactivate a suspended member.

        Args:
            member_id (str): ID of the member to activate.
        """
        try:
            if self.df.empty or member_id not in self.df["member_id"].values:
                print(" Member not found.")
                return

            self.df.loc[self.df["member_id"] == member_id, "status"] = "active"
            write_csv(self.file_path, self.df, self.fields)

            print(f" Member '{member_id}' reactivated successfully.")
        except Exception as e:
            print(f" Error while activating member: {e}")

    

    def list_members(self, status_filter: str | None = None) -> None:
        """
        List all registered members (optionally filtered by status).

        Args:
            status_filter (str, optional): Filter by 'active' or 'suspended'.
        """
        try:
            if self.df.empty:
                print(" No members registered.")
                return

            df = self.df
            if status_filter:
                df = df[df["status"].str.lower() == status_filter.lower()]

            if df.empty:
                print(f" No members found with status '{status_filter}'.")
                return

            print("\n👥 Registered Members:\n")
            for _, row in df.iterrows():
                print(f"{row['member_id']}: {row['name']} ({row['status'].capitalize()})")
        except Exception as e:
            print(f" Error while listing members: {e}")

    

    def delete_member(self, member_id: str) -> None:
        """
        Delete a member record from the system.

        Args:
            member_id (str): ID of the member to delete.
        """
        try:
            if self.df.empty or member_id not in self.df["member_id"].values:
                print(" Member not found.")
                return

            self.df = self.df[self.df["member_id"] != member_id]
            write_csv(self.file_path, self.df, self.fields)
            print(f" Member '{member_id}' deleted successfully.")
        except Exception as e:
            print(f" Error while deleting member: {e}")

