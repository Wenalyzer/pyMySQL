SET SQL_SAFE_UPDATES=0;
DROP TABLE IF EXISTS my_emp;

CREATE TABLE my_emp (
  ID int NOT NULL,
  LAST_NAME varchar(25) DEFAULT NULL,
  FIRST_NAME varchar(25) DEFAULT NULL,
  USERID varchar(8) DEFAULT NULL,
  SALARY decimal(9,2) DEFAULT NULL
) ENGINE InnoDB; 

-- 1. 將下列的資料新增至MY_EMP 資料表中,不要列舉欄位。
INSERT INTO my_emp
	VALUES(1, 'Patel', 'Ralph', 'rpatel', 795);
SELECT *
FROM my_emp;

-- 2. 使用列舉欄位方式,將下列的資料新增至 MY_EMP資料表中。
INSERT INTO my_emp(ID, LAST_NAME, FIRST_NAME, USERID, SALARY)
	VALUES(2, 'Dancs', 'Betty', 'bdancs', 860);
SELECT *
FROM my_emp;

-- 3. 將下列的資料新增至 MY_EMP資料表中。
INSERT INTO my_emp
	VALUES(3, 'Biri', 'Ben', 'bbiri', 1100),
		  (4, 'Newman', 'Chad', 'cnewman', 750);
SELECT *
FROM my_emp;

-- 4. 將員工編號為3的名字(last name)更改為 Drexler 。
UPDATE my_emp
SET LAST_NAME = 'Drexler'
WHERE ID = 3;
SELECT *
FROM my_emp;

-- 5. 將薪資低於900元的所有員工薪資調整為1000元。
UPDATE my_emp
SET SALARY = 1000
WHERE SALARY < 900;
SELECT *
FROM my_emp;

-- 6. 刪除 Betty Dancs 的資料。
DELETE FROM my_emp
WHERE ID = 2;
SELECT *
FROM my_emp;

-- 7. 啟動一個資料庫交易
-- 將所有員工的薪資調升10%
-- 設定一個交易儲存點
-- 刪除所有MY_EMP資料表中的資料
-- 確認資料已被你刪光了
-- 放棄刪除資料的動作
-- 確認交易

START TRANSACTION;
UPDATE my_emp
SET SALARY = SALARY*1.1;
SAVEPOINT TX1;
DELETE FROM my_emp;
SELECT *
FROM my_emp;
ROLLBACK TO TX1;
COMMIT;
