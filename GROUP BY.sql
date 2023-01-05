SELECT COUNT(750), ComponentID
from Production.BillOfMaterials
GROUP BY ComponentID;

SELECT COUNT(750), ComponentID
FROM Production.BillOfMaterials
GROUP BY ComponentID
ORDER BY COUNT(ComponentID) DESC;
