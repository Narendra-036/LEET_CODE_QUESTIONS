# Write your MySQL query statement below
select employee_id,
(case
when employee_id % 2 = 0 then salary=0
when name like 'M%' then salary=0
else salary
end ) 'bonus'
from employees
order by employee_id
