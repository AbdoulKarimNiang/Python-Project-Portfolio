# Create Database


  
  
# Create Tables



# Solving the problem

USE globant_db;

WITH cte AS (
    SELECT 
        e.id,
        e.name,
        j.job,
        e.date,
        e.year,
        d.product_management as department,
        CASE 
            WHEN MONTH(e.date) BETWEEN 1 AND 3 THEN 'Q1'
            WHEN MONTH(e.date) BETWEEN 4 AND 6 THEN 'Q2'
            WHEN MONTH(e.date) BETWEEN 7 AND 9 THEN 'Q3'
            WHEN MONTH(e.date) BETWEEN 10 AND 12 THEN 'Q4'
        END AS quarter
    FROM 
        globant_db.employee e
    INNER JOIN 
        globant_db.job j ON e.job_id = j.id
    INNER JOIN 
        globant_db.department d ON e.department_id = d.id
    WHERE 
        e.year = '2021'
)
SELECT
	department,
    job,
    COUNT(CASE WHEN quarter = 'Q1' THEN 1 END) AS Q1,
    COUNT(CASE WHEN quarter = 'Q2' THEN 1 END) AS Q2,
    COUNT(CASE WHEN quarter = 'Q3' THEN 1 END) AS Q3,
    COUNT(CASE WHEN quarter = 'Q4' THEN 1 END) AS Q4
FROM 
    cte
GROUP by DEPARTMENT, JOB
ORDER BY DEPARTMENT, JOB ASC;



______________________

