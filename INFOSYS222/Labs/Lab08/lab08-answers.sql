/*Q1*/
SELECT LENGTH(suburb) FROM Address;

/*Q2*/
SELECT restID, SUBSTR(UPPER(restName),1, 4) From Restaurant;

/*Q3*/
SELECT INSTR(restName, 'a') FROM Restaurant;

/*Q4*/
SELECT SUBSTR(email, INSTR(email, '@')) AS 'Email Provider', COUNT('Email Provider') AS 'No. of Customers using' FROM Customer
GROUP BY SUBSTR(email, INSTR(email, '@'));

/*Q5*/
SELECT AVG(prodPrice) FROM Product;

/*Q6*/
SELECT AVG(prodPrice), MIN(prodPrice), MAX(prodPrice) FROM Product;

/*Q7*/
SELECT prodName, AVG(reviewStar) FROM Review r
INNER JOIN Product p
ON r.prodNo = p.prodNo
GROUP BY prodName;

/*Q8*/
SELECT TOTAL(quantity) FROM OrderProduct
GROUP BY orderNo;

/*Q9*/
SELECT orderNo, TOTAL(quantity) AS 'Products Ordered' FROM OrderProduct
WHERE 'Products Ordered' > 3
GROUP BY orderNo;

/*Q10*/
SELECT p.prodNo, prodName, prodPrice, prodPrice*(1 - discount) AS 'Discounted Price' FROM Product p
INNER JOIN ProductSpecial s
ON p.prodNo = s.prodNo;

/*Q11*/
SELECT COUNT(*) FROM Review;

/*Q12*/
SELECT TOTAL(prodPrice) FROM 

/*Q13*/
SELECT  

/*Q14*/
SELECT prodNo, prodName, prodPrice,
CASE 
	WHEN (INSTR(prodDesc, 'ham') <> 0) THEN (prodPrice + 2)
	WHEN (INSTR(prodDesc, 'garlic') <> 0) THEN (prodPrice - 1)
	ELSE 'No change'
END AS 'Revised Price'
FROM Product;
	


