from utilities import get_engine, get_result

engine = get_engine()

commands = [
    "SELECT ename, sal FROM emp WHERE sal > 2850;",
    "SELECT ename, deptno FROM emp WHERE empno = 7566;",
    "SELECT ename, sal FROM emp WHERE NOT(sal BETWEEN 1500 AND 2850);",
    "SELECT ename, job, hiredate FROM emp WHERE hiredate BETWEEN '2011-02-20' AND '2011-05-01' ORDER BY hiredate ASC;",
    "SELECT ename, deptno FROM emp WHERE deptno IN (10, 30) ORDER BY ename ASC;",
    "SELECT ename AS Employee, sal AS 'Monthly Salary' FROM emp WHERE sal > 1500 AND deptno IN (10, 30);",
    "SELECT ename, job, hiredate FROM emp WHERE hiredate BETWEEN '2012-01-01' AND '2012-12-31';"
]

try:
    with engine.connect() as conn:
        print("✅ 成功連線到 MySQL！\n")
        for command in commands:
            get_result(command, conn)

except Exception as e:
    print("❌ 連線失敗：", e)