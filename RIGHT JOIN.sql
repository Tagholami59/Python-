SELECT Production.Product. ProductID,Production.ProductDocument.ProductID
FROM Production.Product 
RIGHT JOIN Production.ProductDocument
ON Production.Product.ProductID = Production.ProductDocument.ProductID;