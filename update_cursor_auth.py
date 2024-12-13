from cursor_auth_manager import CursorAuthManager

def update_cursor_auth(email=None, access_token=None, refresh_token=None):
    """
    更新Cursor的认证信息的便捷函数
    """
    auth_manager = CursorAuthManager()
    return auth_manager.update_auth(email, access_token, refresh_token)

def main():
    # 示例用法
    print("请选择要更新的项目：")
    print("1. 更新邮箱")
    print("2. 更新访问令牌")
    print("3. 更新刷新令牌")
    print("4. 更新多个值")
    print("0. 退出")
    
    choice = input("\n请输入选项数字: ")
    
    if choice == "1":
        email = input("请输入新的邮箱: ")
        update_cursor_auth(email=email)
    elif choice == "2":
        token = input("请输入新的访问令牌: ")
        update_cursor_auth(access_token=token)
    elif choice == "3":
        token = input("请输入新的刷新令牌: ")
        update_cursor_auth(refresh_token=token)
    elif choice == "4":
        email = input("请输入新的邮箱 (直接回车跳过): ")
        access_token = input("请输入新的访问令牌 (直接回车跳过): ")
        refresh_token = input("请输入新的刷新令牌 (直接回车跳过): ")
        
        update_cursor_auth(
            email=email if email else None,
            access_token=access_token if access_token else None,
            refresh_token=refresh_token if refresh_token else None
        )
    elif choice == "0":
        print("退出程序")
    else:
        print("无效的选项")

if __name__ == "__main__":
    main() 