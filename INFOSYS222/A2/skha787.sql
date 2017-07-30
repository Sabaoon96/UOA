/* Q1 */
SELECT "Sabaoon Raza" AS "First Name", "Khan" AS "Last Name", "983957824" AS "ID", "BSc. Computer Science Major" AS "Description";


/* Q2 */
SELECT * FROM Artist WHERE Name LIKE 'F%';


/* Q3 */
SELECT FirstName || ' ' || LastName AS 'Employee Name' FROM Employee
ORDER BY LENGTH(FirstName || ' ' || LastName) DESC;


/* Q4 */
UPDATE Employee SET Fax = '+' || Fax WHERE NOT INSTR(Fax, '+');


/* Q5 */
CREATE TABLE Country(
   CountryID	INTEGER   PRIMARY KEY     NOT NULL	UNIQUE,
   Name			TEXT		NOT NULL,
   'Desc'			TEXT		DEFAULT 'A Happy Place',
   Code			TEXT        CHECK (LENGTH(Code) <= 7)
);


/* Q6 */
SELECT Name FROM Track
WHERE Name LIKE 'RIGHT %' OR Name LIKE '% RIGHT'
OR Name LIKE '% RIGHT %' OR Name LIKE 'RIGHT';


/* Q7 */
SELECT a.Title 'Album', COUNT(t.AlbumID) 'Tracks', t.UnitPrice*COUNT(t.AlbumID) 'Price'
FROM Album a
INNER JOIN Track t
	ON a.AlbumID = t.AlbumID
GROUP BY t.AlbumID
HAVING (t.UnitPrice*COUNT(t.AlbumID) >= 30)
ORDER BY t.UnitPrice*COUNT(t.AlbumID) DESC;


/* Q8 */
SELECT FirstName AS 'Name', 
MIN(CAST(strftime('%Y.%m%d', 'now') - strftime('%Y.%m%d', BirthDate) as INT)) AS 'Age'
FROM Employee
WHERE (Title LIKE 'Manager %' OR Title LIKE '% Manager'
OR Title LIKE '% Manager %' OR Title LIKE 'Manager');


/* Q9 */
INSERT INTO Playlist (Name) VALUES ('Quick Music');

INSERT INTO PlaylistTrack 
SELECT p.PlaylistID, T.TrackID
FROM Playlist p, Track t
WHERE p.Name = 'Quick Music'
ORDER BY Millisecond ASC LIMIT 10;


/* Q10 */
SELECT 
CASE 
	WHEN m.Name LIKE '%AAC%' THEN 'AAC'
	WHEN m.Name NOT LIKE '%AAC%' THEN 'non-AAC'
END AS 'Media',
COUNT(t.TrackID) AS 'Tracks'
FROM MediaType m
INNER JOIN Track t
	ON m.MediaTypeID = t.MediaTypeID
GROUP BY Media;


/* Q11 */
SELECT a.Title 'Album', GROUP_CONCAT(DISTINCT g.Name) 'Genre'
FROM Track t, Genre g, Album a
WHERE t.GenreID = g.GenreID AND a.AlbumID = t.AlbumID
GROUP BY a.Title
HAVING COUNT(DISTINCT g.Name) > 1;


/* Q12 */				
SELECT UPPER(SUBSTR(SUBSTR(Email, INSTR(Email, '@') +1), 1, INSTR(SUBSTR(Email, INSTR(Email, '@') +1), SUBSTR(SUBSTR(Email, INSTR(Email, '@') +1), INSTR(SUBSTR(Email, INSTR(Email, '@') +1), '.') - 1)))) AS 'Provider', 
			ROUND((COUNT('Provider')*1.00/
			(SELECT COUNT(CustomerID) FROM Customer)
			)*100, 2) AS 'Percentage' 
FROM Customer
GROUP BY Provider
ORDER BY Percentage DESC,
				Provider ASC;	
			
			
/* Q13 */
CREATE VIEW CustomerView AS
SELECT Country, 
(COUNT(FirstName) - COUNT(Company)) AS 'Individual', 
COUNT(Company) AS 'Company'
FROM Customer
GROUP BY Country
ORDER BY Country ASC;


/* Q14 */			
CREATE TRIGGER UndeleteLostTrack AFTER DELETE ON Track
WHEN old.TrackID =
	(SELECT old.TrackID
	FROM Track t, Album a
	WHERE a.AlbumID = old.AlbumID AND a.Title LIKE '%LOST%'
	LIMIT 1)
BEGIN
	INSERT INTO Track 
	VALUES (old.TrackID, old.Name, old.AlbumID, old.MediaTypeID, old.GenreID, old.Composer, old.Millisecond, old.Byte, old.UnitPrice);
END;