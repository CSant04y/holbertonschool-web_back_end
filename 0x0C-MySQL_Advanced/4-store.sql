-- This is a mysql trigger that decreases quantity of item
-- Through a trigger that inserts after insert.
CREATE TRIGGER buy_item AFTER INSERT ON orders
FOR EACH ROW UPDATE items
SET
quantity = quantity - NEW.number
WHERE name = NEW.item_name;