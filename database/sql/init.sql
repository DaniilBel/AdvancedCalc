CREATE DATABASE IF NOT EXISTS advanced_calc;
USE advanced_calc;

CREATE TABLE calc_history 
(
	line VARCHAR(512) PRIMARY KEY,
    answer BIGINT
);
