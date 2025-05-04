from utilities import get_engine, get_select_query, get_result

engine = get_engine()

queries = [
    {
        "fields": "CURRENT_DATE() AS '系統日期'",
    },
    {
        "fields": "empno, ename, sal, ROUND(sal*1.15) AS 'New Salary'",
        "table": "emp",
    },
    {
        "fields": "empno, ename, sal, ROUND(sal*1.15) AS 'New Salary', ROUND(sal*1.15-sal) AS Increase",
        "table": "emp",
    },
    {
        "fields": """ename, hiredate, DATE_FORMAT(
                    ADDDATE(ADDDATE(hiredate, INTERVAL 6 MONTH), 
                    INTERVAL (7 - WEEKDAY(ADDDATE(hiredate, INTERVAL 6 MONTH))) % 7 DAY), 
                    '%W, the %D of %M') AS REVIEW""",
        "table": "emp",
    },
    {
        "fields": "ename, TIMESTAMPDIFF(MONTH, hiredate, NOW()) AS MONTHS_WORKED",
        "table": "emp",
    },
    {
        "fields": "CONCAT(ename, ' earns ', sal, ' monthly but wants ', sal*3, '.') AS 'Dream Salaries'",
        "table": "emp",
    }
]

commands = [get_select_query(q) for q in queries]

try:
    with engine.connect() as conn:
        print("✅ 成功連線到 MySQL！\n")
        for command in commands:
            get_result(command, conn)

except Exception as e:
    print("❌ 連線失敗：", e)