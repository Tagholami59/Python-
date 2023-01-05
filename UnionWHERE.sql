SELECT name FROM Production.Product
WHERE name='chains'
UNION
SELECT name FROM Production.ProductSubcategory
WHERE name='chains'
ORDER BY name;
