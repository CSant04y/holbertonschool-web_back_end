-- This SQL script creates idx_name_first_score 
-- on table names and score

CREATE INDEX idx_name_first_score
ON names(name(1), score);