import sqlite3
import os

class CursorAuthManager:
    """Cursor认证信息管理器"""

    def __init__(self):
        # 判断操作系统
        if os.name == 'nt':  # Windows
            self.db_path = os.path.join(os.getenv('APPDATA'), 'Cursor', 'User', 'globalStorage', 'state.vscdb')
        else:  # macOS
            self.db_path = os.path.expanduser('~/Library/Application Support/Cursor/User/globalStorage/state.vscdb')


    def update_auth(self, email=None, access_token=None, refresh_token=None):
        """
        更新Cursor的认证信息
        :param email: 新的邮箱地址
        :param access_token: 新的访问令牌
        :param refresh_token: 新的刷新令牌
        :return: bool 是否成功更新
        """
        updates = []
        if email is not None:
            updates.append(('cursorAuth/cachedEmail', email))
        if access_token is not None:
            updates.append(('cursorAuth/accessToken', access_token))
        if refresh_token is not None:
            updates.append(('cursorAuth/refreshToken', refresh_token))

        if not updates:
            print("没有提供任何要更新的值")
            return False

        conn = None
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            for key, value in updates:
                query = "UPDATE itemTable SET value = ? WHERE key = ?"
                cursor.execute(query, (value, key))

                if cursor.rowcount > 0:
                    print(f"成功更新 {key.split('/')[-1]}")
                else:
                    print(f"未找到 {key.split('/')[-1]} 或值未变化")

            conn.commit()
            return True

        except sqlite3.Error as e:
            print("数据库错误:", str(e))
            return False
        except Exception as e:
            print("发生错误:", str(e))
            return False
        finally:
            if conn:
                conn.close()
