-- This script creates an index idx_name_first_score
-- on the tables names

CREATE INDEX idx_name_first_score
ON names (name(1));