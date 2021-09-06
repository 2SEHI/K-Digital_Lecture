-- 1 데이터베이스 구축
-- => 실제 업무에서 테이블 생성은 직접 SQL을 사용하는 것보다는 
--    Modeling Tool을 이용해서 데이터베이스 모델링을 하고 필요한 데이트베이스에 연결해서 자동으로 생성하는 형태를 많이 사용
--    password는 하나의 자료형일 수도 있으므로 주의해야 합니다.

CREATE TABLE USER_INFO( 
	ID CHAR(18) PRIMARY KEY,
	NAME CHAR(18), 
	PASSWORD CHAR(18), 
	EMAIL CHAR(30),
);

-- 외래키를 설정할 때는 특별한 경우가 아니면 삭제 옵션을 추가
-- 삭제 옵션을 추가하지 않으면 BOARD에서 삽입된 데이터는 USER_INFO 테이블에서 삭제할 수 없습니다.
-- 하나의 테이블에 속해야할 것 같은 요소이지만 특정 항목의 값이 여러개(배열)이면 별도의 테이블로 추출
CREATE TABLE BOARD( 
	ARTICLE_ID NUMBER PRIMARY KEY,
	USER_ID CHAR(18), 
	ARTICLE_TITLE CHAR(50), 
	ARTICLE_DETAIL VARCHAR2(1000), 
	ARTICLE_HITS NUMBER, 
	ARTICLE_RECOMMEND NUMBER, 
	FOREIGN KEY(USER_ID) REFERENCES USER_INFO(ID)
);

CREATE TABLE FILES(
    FILE_ID CHAR(18) PRIMARY KEY,
    FILE_NAMe CHAR(18),
    FILE_SIZE CHAR(18),
    ARTICLE_ID NUMBER,
    FOREIGN KEY(ARTICLE_ID) REFERENCES BOARD(ARTICLE_ID)
);

CREATE TABLE FILES(
    FILE_ID CHAR(18) PRIMARY KEY,
    FILE_NAMe CHAR(18),
    FILE_SIZE CHAR(18),
    ARTICLE_ID NUMBER,
	-- 제약조건을 쓸때 한꺼번에 몰아놓는것도 좋은 방법입니다
    CONSTRAINT PK_FILES PRIMARY KEY(FILE_ID),
	CONSTRAINT FK_BOARD FOREIGN KEY(ARTICLE_ID) REFERENCES BOARD(ARTICLE_ID)
);



-- 2.데이터베이스 활용

--DEPT 부서 테이블, DEPTNO가 부서 번호, DNAME이 부서명, LOC가 지역
CREATE TABLE DEPT
       (DEPTNO NUMBER(2) CONSTRAINT PK_DEPT PRIMARY KEY,
	DNAME VARCHAR2(14) ,
	LOC VARCHAR2(13) ) ;


CREATE TABLE EMP
   (EMPNO NUMBER(4) CONSTRAINT PK_EMP PRIMARY KEY,
	ENAME VARCHAR2(10),
	JOB VARCHAR2(9),
	MGR NUMBER(4),
	HIREDATE DATE,
	SAL NUMBER(7,2),
	COMM NUMBER(7,2),
	DEPTNO NUMBER(2) CONSTRAINT FK_DEPTNO REFERENCES DEPT);
);

INSERT INTO DEPT VALUES(10,'ACCOUNTING','NEW YORK');
INSERT INTO DEPT VALUES (20,'RESEARCH','DALLAS');
INSERT INTO DEPT VALUES(30,'SALES','CHICAGO');
INSERT INTO DEPT VALUES(40,'OPERATIONS','BOSTON');

INSERT INTO EMP VALUES
(7369,'SMITH','CLERK',7902,to_date('17-12-1980','dd-mm-yyyy'),800,NULL,20);
INSERT INTO EMP VALUES
(7499,'ALLEN','SALESMAN',7698,to_date('20-2-1981','dd-mm-yyyy'),1600,300,30);
INSERT INTO EMP VALUES
(7521,'WARD','SALESMAN',7698,to_date('22-2-1981','dd-mm-yyyy'),1250,500,30);
INSERT INTO EMP VALUES
(7566,'JONES','MANAGER',7839,to_date('2-4-1981','dd-mm-yyyy'),2975,NULL,20);
INSERT INTO EMP VALUES
(7654,'MARTIN','SALESMAN',7698,to_date('28-9-1981','dd-mm-yyyy'),1250,1400,30);
INSERT INTO EMP VALUES
(7698,'BLAKE','MANAGER',7839,to_date('1-5-1981','dd-mm-yyyy'),2850,NULL,30);
INSERT INTO EMP VALUES
(7782,'CLARK','MANAGER',7839,to_date('9-6-1981','dd-mm-yyyy'),2450,NULL,10);
INSERT INTO EMP VALUES
(7788,'SCOTT','ANALYST',7566,to_date('13-7-1987','dd-mm-yyyy')-85,3000,NULL,20);
INSERT INTO EMP VALUES
(7839,'KING','PRESIDENT',NULL,to_date('17-11-1981','dd-mm-yyyy'),5000,NULL,10);
INSERT INTO EMP VALUES
(7844,'TURNER','SALESMAN',7698,to_date('8-9-1981','dd-mm-yyyy'),1500,0,30);
INSERT INTO EMP VALUES
(7876,'ADAMS','CLERK',7788,to_date('13-7-1987','dd-mm-yyyy'),1100,NULL,20);
INSERT INTO EMP VALUES
(7900,'JAMES','CLERK',7698,to_date('3-12-1981','dd-mm-yyyy'),950,NULL,30);
INSERT INTO EMP VALUES
(7902,'FORD','ANALYST',7566,to_date('3-12-1981','dd-mm-yyyy'),3000,NULL,20);
INSERT INTO EMP VALUES
(7934,'MILLER','CLERK',7782,to_date('23-1-1982','dd-mm-yyyy'),1300,NULL,10);

-- 2-1 : EMP 테이블에서 SAL이 3000이상인 사원의 EMPNO, ENAME, JOB, SAL을 조회하는 SELECT 문장을 작성
SELECT EMPNO, ENAME, JOB, SAL
FROM EMP
WHERE SAL >= 3000;

-- 2-2 : EMP 테이블에서 EMPNO가 7788인 사원의 ENAME과 DEPTNO를 조회하는 SELECT 문장을 작성
SELECT ENAME, DEPTNO
FROM EMP
WHERE EMPNO = 7788;



-- 2-3 : EMP 테이블에서 (ENAME에 L이 두 자 이상이 포함되어 있고 DEPTNO가 30)이거나 MGR이 7782인 사원의 모든 정보를 조회하는 SELECT 문을 작성
SELECT *
FROM EMP
WHERE ENAME LIKE '%L%L%' 
AND (DEPTNO = 30 OR MGR = 7782)

-- 실제론 데이터가 너무 많아 제대로 처리했는지 데이터만 보고 알 수 없습니다
-- 실제 구현되는 구문이라면 OR와 AND의 순서를 변경하는 것도 고민해야 합니다.
-- FOR를 이용해서 데이터를 찾을 것이냐 DICT를 만들고 DICT를 이용할 것이냐
SELECT *
FROM EMP
WHERE ENAME LIKE '%L%L' 
AND DEPTNO = 30 OR MGR = 7782;



-- 2-4 : EMP 테이블에서 각 업무별(job)로 최대 급여(sal), 최소 급여, 급여의 합을 출력하는 SELECT 문장을 작성
select job as "업무", max(sal) as "최대 급여", min(sal) as "최소 급여", sum(sal)  as "급여의 합"
from emp 
group by job

SELECT MAX(SAL) MAXSAL, MIN(SAL) MINSAL, SUM(SAL) SUMSAL
FROM EMP
GROUP BY JOB


-- 2-5 : EMP 테이블에서 모든 사원에 대한 이름(ename), 부서번호(deptno) DEPT 테이블에서 부서명(dname)을
-- 가져와서 출력하는 SELECT 문장을 작성 – 2개의 테이블에는 DEPTNO 가 같이 존재
select emp.ename, emp.deptno, dept.dname
from emp, dept

-- 여러 개의 테이블을 사용할 때는 별도의 이름을 만들어 쓰는경우가 많은데 
-- 그 이유는 공통된 컬럼의 이름을 사용할 때 테이블이름.컬럼이름으로 작성해야 해서 SQL이 길어지기 때문입니다.
SELECT ENAME, EMP.DEPTNO, DNAME
FROM EMP E, DEPT D
WHERE E.DEPTNO = D.DEPTNO



-- 2-6 
select emp.empno as "사원번호", emp.hiredate as "관리자 입사일", mng.empno as "관리자 사원번호", mng.hiredate as "관리자 입사일"
from emp, 
-- 관리자의 사원번호와 입사일
(select empno, hiredate
from emp
where JOB='MANAGER')  mng
-- 사원의 관리자 번호와 관리자 사원번호가 같으면서
-- 사원의 입사일이 관리자의 입사일보다 빠른 경우
where emp.mgr = mng.empno and 
emp.hiredate < mng.hiredate

-- SELF JOIN을 이용
SELECT E.NAMEM, E.HIREDATE, M.ENAME, M.HIREDATE
FROM EMP E, EMP M
WHERE E.MGR = M.EMPNO AND E.HIREDATE < M.HIREDATE



--2-7 : EMP 테이블에서 DEPT 테이블의 LOC 가 DALLAS인 종업원에 대해 이름(ENAME),업무(job),급여(SAL)를
-- 출력하는 SELECT문을 작성
select ename, job, sal
from emp
where DEPTNO = (select DEPTNO from dept where loc = 'DALLAS')

-- NATURAL JOIN 의 경우 
SELECT ENAME, JOB, SAL
FROM EMP E JOIN DEPT D
ON E.DEPTNO = D.DEPTNO
WHERE LOC = (select LOC from DEPT where loc = 'DALLAS')



--2-8 : DEPT 테이블에 DEPTNO 가 50 DNAME 이 영업 LOC가 서울인 데이터를 삽입하시오
insert into dept (DEPTNO, DNAME, LOC) values (50, 'SALES', 'SEOUL')



--2-9 : DEPT 테이블을 삭제하는 SQL 문을 작성하시오
drop table DEPT



--2-10
-- 1)데이터베이스에서 제공하는 하나 이상의 테이블로부터 유도된 가상의 테이블은? view
-- 데이터베이스에서는 가상 테이블을 VIEW라고 합니다
-- ARCHITECTURE에서는 일반적으로 입출력 화면을 VIEW라고 하는데 DJANGO에서 VIEW가 CONTROLLER의 역할을 수행합니다.
-- 프로그래밍에서는 링크를 복사한 것(원본의 참조를 복사)을 VIEW라고 하기도 합니다.

-- 2)테이블의 데이터를 빠르게 찾을 수 있도록 설정하는 포인터는?index
-- =>프로그래밍에서 인덱스는 배열이나 LIST 에서 데이터의 순번을 의미하며 순번 대신에 이름을 사용하면 이 경우는 INDEXER(KEY) 라고 합니다.