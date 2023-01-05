SELECT Production.Product. ProductID,Production.ProductDocument.ProductID
FROM Production.Product 
LEFT JOIN Production.ProductDocument
ON Production.Product.ProductID = Production.ProductDocument.ProductID;