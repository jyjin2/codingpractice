-- 코드를 입력하세요
SELECT ANIMAL_ID, name
from ANIMAL_INS
where NAME like '%el%' and ANIMAL_TYPE = 'Dog'
order by name