CREATE DATABASE advanced_calc;

USE advanced_calc;

CREATE TABLE calc_history 
(
	line VARCHAR(512), 
	answer FLOAT,
	date VARCHAR(50) PRIMARY KEY
);
