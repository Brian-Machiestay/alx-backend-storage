-- create a trigger on update
delimiter |
CREATE TRIGGER setValidEmail BEFORE UPDATE
ON users
FOR EACH ROW
BEGIN
SET NEW.valid_email = CASE
    WHEN OLD.valid_email = 0 AND  NEW.email != OLD.email THEN 1
    WHEN OLD.valid_email = 1 AND  NEW.email != OLD.email THEN 0
    ELSE NEW.valid_email
END;
END;
|
delimiter ;
