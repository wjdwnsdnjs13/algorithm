-- 코드를 입력하세요
# 자종이 SUV인 차들의 평균 일일 대여 요금을 출력.
# 평균 일일 대여 요금은 소수 첫 번째 자리에서 반올림, 컬럼명은 AVERAGE_FEE
SELECT
    round(avg(DAILY_FEE)) as AVERAGE_FEE
FROM
    CAR_RENTAL_COMPANY_CAR
WHERE
    CAR_TYPE = "SUV"