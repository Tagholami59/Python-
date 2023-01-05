SELECT Name FROM Production.Product
UNION All
SELECT Name FROM Production.ProductSubcategory
ORDER BY Name;