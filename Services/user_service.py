from Repositories.sql_server.user_repository import AccountRepository

class UserService:
    def __init__(self):
        self.account_repo = AccountRepository()

    def login(self, username, password):
        # Có thể thêm các logic khác như ghi log, kiểm tra trạng thái tài khoản
        return self.account_repo.authenticate(username, password)

    def register_account(self, username, password, role, requirement_role):
        # Logic nghiệp vụ có thể kiểm tra role hợp lệ, phân quyền
        print(f"Checking register_account with username={username}, requirement_role={requirement_role}")

        if requirement_role != 'owner':
            # chỉ owner mới được tạo tài khoản
            print("Permission denied: only owner can create accounts")

            return False
        if self.account_repo.is_used(username):
            print(f"Username {username} already used")

            return False
        return self.account_repo.create_account(username, password, role, requirement_role)

    def check_if_admin(self, username):
        return self.account_repo.is_admin(username)

    def check_if_owner(self, username):
        return self.account_repo.is_owner(username)

    def get_users_without_slot(self):
        return self.account_repo.account_has_no_slot()

    def reset_status(self, username):
        return self.account_repo.reset_user_status(username)

    def close(self):
        self.account_repo.close()
