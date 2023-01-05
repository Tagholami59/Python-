SELECT Name FROM Production.Product
UNION 
SELECT Name FROM Production.ProductSubcategory
ORDER BY Name;
