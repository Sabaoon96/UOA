/* Q1 */   SELECT * FROM Employee;
/* Q2 */   SELECT firstName, lastName, gender FROM Customer;
/* Q3 */   SELECT * FROM Product;
/* Q4 */   SELECT prodNo, prodName, prodPrice, prodPrice+2 FROM Product;
/* Q5 */   SELECT prodNo, prodName, prodPrice, prodPrice+2, prodPrice/1.15 FROM Product;
/* Q6 */   SELECT prodNo 'Product number', prodName 'Product name', prodPrice 'Product price', prodPrice+2 'New product price', prodPrice/1.15 'Product price excl GST' 
			   FROM Product;
/* Q7 */   SELECT empID, empFirstName, empLastName, roleID FROM Employee 
			   WHERE LOWER(empFirstName) = 'amanda' AND LOWER(empLastName) = 'corry';
/* Q8 */   SELECT empID, empFirstName || ' ' || empLastName 'Full name', roleID FROM Employee 
			   WHERE LOWER('Full name') = 'amanda corry';
/* Q9 */   SELECT 'The price for an ' ||prodName|| ' is $' ||prodPrice
			   FROM Product
			   WHERE prodName = "Agilo";
/* Q10 */ SELECT DISTINCT suburb FROM Address;
/* Q11 */ SELECT * FROM Customer WHERE gender = 'M';
/* Q12 */ SELECT ingrNo, ingrName FROM Ingredient LIMIT 3;
/* Q13 */ SELECT ingrNo, ingrName FROM Ingredient LIMIT 3 OFFSET 6; 
/* Q14 */ SELECT * FROM Customer WHERE contactNumber IS NULL;
/* Q15 */ SELECT * FROM Customer WHERE contactNumber IS NOT NULL;
/* Q16 */ SELECT * FROM Review WHERE reviewStar BETWEEN 1 AND 3;
/* Q17 */ SELECT * FROM ProductSpecial WHERE startDateTime < '2015-05-02';
/* Q18 */ SELECT orderNumber FROM CustOrder WHERE empID = 4 AND orderDateTime < '2015-07-09';
/* Q19 */ SELECT * FROM Review WHERE reviewStar IN (1,3,5);
/* Q20 */ SELECT customerID, firstName FROM Customer 
			   WHERE firstName LIKE '%a%';
/* Q21 */ SELECT customerID, firstName FROM Customer WHERE firstName LIKE '_o%';
/* Q22 */ SELECT * FROM Product WHERE prodPrice < 18 OR prodDesc LIKE '%mozzarella%';
/* Q23 */ SELECT * FROM Review ORDER BY reviewStar ASC;
/* Q23 */ SELECT lastName, firstName FROM Customer ORDER BY lastName ASC;

/* ---------------------------------------------------------------------------------------------------------------------------------------- */

/* Q1 */   SELECT LOWER(firstName), UPPER(lastName) FROM Customer;
/* Q2 */   SELECT firstName ||' '|| lastName ||"'s customer ID is "|| customerID ||' and their phone number is: '|| contactNumber
			   FROM Customer;
/* Q3 */   SELECT empFirstName, empLastName, IFNULL(endDate, 'Unconfirmed')  FROM Employee;
/* Q4 */   SELECT c.customerID, firstName, lastName, orderNo FROM Customer c, CustOrder o;
/* Q5 */   SELECT c.customerID, firstName, lastName, orderNo FROM Customer c
			   INNER JOIN CustOrder o
			   ON c.customerID = o .customerID;
/* Q6 */   SELECT reviewNo, reviewTypeDesc, reviewStar, reviewDesc FROM Review r
			   INNER JOIN ReviewType t
			   ON r.reviewTypeID = t.reviewTypeID;
/* Q7 */   SELECT 

			   