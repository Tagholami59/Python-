SELECT Production.Product. ProductID,Production.ProductDocument.ProductID
FROM Production.Product 
INNER JOIN Production.ProductDocument
ON Production.Product.ProductID = Production.ProductDocument.ProductID;