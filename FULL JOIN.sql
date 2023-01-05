SELECT Production.Product. ProductID,Production.ProductDocument.ProductID
FROM Production.Product 
FULL JOIN Production.ProductDocument
ON Production.Product.ProductID = Production.ProductDocument.ProductID;