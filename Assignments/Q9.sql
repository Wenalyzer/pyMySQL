-- 1. 使用EMP資料表中的員工編號(empno),姓名(ename)及部門編號(deptno)來建立一個EMP_VU view，並將姓名(ename)欄位名稱改成EMPLOYEE。
CREATE VIEW emp_vu
AS
SELECT 
    empno, 
    ename AS employee, 
    deptno
FROM emp;
DESC emp_vu;

-- 2. 使用EMP_VU view來顯示所有員工之姓名及部門編號。
SELECT 
    employee, deptno
FROM emp_vu;

-- 3. 新建一個名為DEPT20的view，包含在部門20的所有員工之員工編號，員工姓名，及部門編號。將View中的資料項目命名為EMPLOYEE_ID, EMPLOYEE, and DEPARTMENT_NO。並設定不允許使用者透過DEPT20來更改員工所屬的部門編號。
CREATE VIEW dept20
AS
SELECT 
	  empno AS employee_id,
  	ename AS employee,
  	deptno AS department_no
FROM emp
WHERE deptno = 20
WITH CHECK OPTION;
DESC dept20;

-- 4. 使用DEPT20 view 顯示其所有資料內容。
SELECT *
FROM dept20;

-- 5. 試試看利用DEPT20 view將 Smith 轉調到部門30。
UPDATE dept20
SET department_no = 30
WHERE employee = "Smith";

-- 6. 新建一個名為SALARY_VU的view，包含所有員工之姓名，部門名稱，薪資和薪資等級。將View中的資料項目分別命名為Employee, Department, Salary, Grade。
CREATE VIEW salary_vu
AS
SELECT 
	  e.ename AS Employee,
    d.dname AS Department,
    e.sal AS Salary,
    s.grade AS Grade
FROM emp AS e
JOIN dept AS d
  ON e.deptno = d.deptno
JOIN salgrade AS s
  ON (e.sal BETWEEN s.losal AND s.hisal);
SELECT * FROM salary_vu;

-- 7. 在EMP資料表中利用ename欄位建立一個non-unique index 命名為idx_emp_ename。
CREATE INDEX index_emp_ename
   ON emp(ename);
SHOW INDEXES FROM emp;