-- Creates Table "users" with id, email, name, country
-- gets unique
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email varchar(255) NOT NULL UNIQUE,
    name varchar(255),
    country ENUM('US', 'CO', 'TN') NOT NULL
); 
