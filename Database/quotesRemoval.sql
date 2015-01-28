/**---------------------------------------------------------------------*/
/**			Unnecesary quotes removal script							*/
/**---------------------------------------------------------------------*/
/**--	To be applyed on the DB in case of rebuilding because of	 ---*/
/**-- 				inconsistencies in the test data                 ---*/
/**---------------------------------------------------------------------*/
/**--						   USAGE: 								 ---*/
/**--   UPDATE Client SET firstName = REPLACE(firstName, "'", "")    ---*/
/**--    ^             ^                 ^         ^     ^				*/
/**-- Table name   attrib name      attrib name   what   what to replace with
/**--											  to 					*/
/**--											replace 				*/
/**---------------------------------------------------------------------*/

/* BEGIN */
UPDATE Client SET firstName = REPLACE(firstName, "'", "")
UPDATE Client SET lastName = REPLACE(lastName, "'", "")
UPDATE Client SET email = REPLACE(email, "'", "")
UPDATE address SET city = REPLACE(city, "'", "")
UPDATE address SET country = REPLACE(country, "'", "")
UPDATE address SET street = REPLACE(street, "'", "")
UPDATE address SET label = REPLACE(label, "'", "")
UPDATE subvenue SET label = REPLACE(label, "'", "")
UPDATE subvenue SET capacity = REPLACE(capacity, "'", "")
;
/* END */