from fastapi import APIRouter, HTTPException
from app.models.employee import Employee, SalaryUpdate
from app.db.database import get_connection

router = APIRouter()


@router.get("/employees")
def get_employees():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT EMP_ID, EMP_NAME
        FROM EMPLOYEES
        ORDER BY EMP_ID
    """)

    rows = cursor.fetchall()

    result = []

    for row in rows:
        result.append({
            "emp_id": row[0],
            "emp_name": row[1]
        })

    cursor.close()
    conn.close()

    return result


@router.post("/employees")
def create_employee(employee: Employee):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO EMPLOYEES
    (EMP_ID, EMP_NAME, DEPARTMENT, SALARY, HIRE_DATE)
    VALUES (:1, :2, :3, :4, SYSDATE)
    """

    cursor.execute(
        query,
        (
            employee.emp_id,
            employee.emp_name,
            employee.department,
            employee.salary
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Employee inserted successfully"}



@router.get("/employees/{emp_id}")
def get_employee(emp_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT EMP_ID,
               EMP_NAME,
               DEPARTMENT,
               SALARY
        FROM EMPLOYEES
        WHERE EMP_ID = :1
    """, (emp_id,))

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "emp_id": row[0],
        "emp_name": row[1],
        "department": row[2],
        "salary": row[3]
    }
    
    
    
@router.put("/employees/{emp_id}")
def update_salary(
        emp_id: int,
        salary_data: SalaryUpdate):

    if salary_data.salary <= 0:
        raise HTTPException(
            status_code=400,
            detail="Salary must be positive"
        )

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE EMPLOYEES
        SET SALARY = :1
        WHERE EMP_ID = :2
    """, (salary_data.salary, emp_id))

    conn.commit()

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    cursor.execute("""
        SELECT EMP_ID,
               EMP_NAME,
               SALARY
        FROM EMPLOYEES
        WHERE EMP_ID = :1
    """, (emp_id,))

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    return {
        "emp_id": row[0],
        "emp_name": row[1],
        "salary": row[2]
    }
    

    