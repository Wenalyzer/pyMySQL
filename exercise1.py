from sqlalchemy import create_engine, text

# 建立連線字串
connection_str = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"

# 建立 engine
engine = create_engine(connection_str)
# print(engine)
# input()

# 測試連線
try:
    with engine.connect() as conn:
        # print("✅ 成功連線到 MySQL！")

        result = conn.execute(text("SELECT * FROM dept"))
        # print(type(result))
        for row in result:
            print(row)
        print()

        result = conn.execute(text("SELECT empno, ename, job, hiredate FROM emp"))
        for row in result:
            print(row)
        print()

        result = conn.execute(text("SELECT DISTINCT job FROM emp"))
        for row in result:
            print(row)
        print()

        result = conn.execute(text("SELECT empno AS \"Emp#\", ename AS Employee, job AS Job, hiredate AS \"Hire Date\" FROM emp"))
        for row in result:
            print(row)
        print()

        result = conn.execute(text("SELECT CONCAT(ename, \", \", job) AS \"Employee and Title\" FROM emp"))
        for row in result:
            print(row)
        print()

except Exception as e:
    print("❌ 連線失敗：", e)