# from sqlalchemy import create_engine, text

from utilities import get_engine, get_result

engine = get_engine()
# print(engine)

# 測試連線
try:
    with engine.connect() as conn:
        print("✅ 成功連線到 MySQL！\n")
        
        command = """SELECT ename, sal
            FROM emp
            WHERE sal > 2850;"""
        result = get_result(command, conn)

        command = """SELECT ename, deptno
            FROM emp
            WHERE empno = 7566;"""
        result = get_result(command, conn)

        command = """SELECT ename, sal
            FROM emp
            WHERE NOT(sal BETWEEN 1500 AND 2850);"""
        result = get_result(command, conn)

        command = """SELECT ename, job, hiredate
            FROM emp
            WHERE hiredate BETWEEN '2011-02-20' AND '2011-05-01'
            ORDER BY hiredate ASC;"""
        result = get_result(command, conn)

        command = """SELECT ename, deptno
            FROM emp
            WHERE deptno IN (10, 30)
            ORDER BY ename ASC;"""
        result = get_result(command, conn)

except Exception as e:
    print("❌ 連線失敗：", e)