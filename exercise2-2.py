from utilities import get_engine, get_result

engine = get_engine()

base_query = "SELECT {fields} FROM emp WHERE {condition} {order_by};"

queries = [
    {
        "fields": "ename, sal",
        "condition": "sal > 2850",
        "order_by": "",
    },
    {
        "fields": "ename, deptno",
        "condition": "empno = 7566",
        "order_by": "",
    },
    {
        "fields": "ename, sal",
        "condition": "NOT(sal BETWEEN 1500 AND 2850)",
        "order_by": "",
    },
    {
        "fields": "ename, job, hiredate",
        "condition": "hiredate BETWEEN '2011-02-20' AND '2011-05-01'",
        "order_by": " ORDER BY hiredate ASC",
    },
    {
        "fields": "ename, deptno",
        "condition": "deptno IN (10, 30)",
        "order_by": " ORDER BY ename ASC",
    },
    {
        "fields": "ename AS Employee, sal AS 'Monthly Salary'",
        "condition": "sal > 1500 AND deptno IN (10, 30)",
        "order_by": "",
    },
    {
        "fields": "ename, job, hiredate",
        "condition": "hiredate BETWEEN '2012-01-01' AND '2012-12-31'",
        "order_by": "",
    },
]

commands = [
    base_query.format(fields=q["fields"], condition=q["condition"], order_by=q["order_by"])
    for q in queries
]

try:
    with engine.connect() as conn:
        print("✅ 成功連線到 MySQL！\n")
        for command in commands:
            get_result(command, conn)

except Exception as e:
    print("❌ 連線失敗：", e)