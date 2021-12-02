-- SQL script to create trigger that resets attr valid_email only when email has been changed
DELIMITER $$
CREATE TRIGGER email_check BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$

DELIMITER ;
