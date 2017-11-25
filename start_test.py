from start import create_app

if __name__ == '__main__':
    app = create_app()
    from init_db import init_db
    # 初始化数据库的表
    init_db()
    app.run()