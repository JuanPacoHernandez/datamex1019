CREATE DATABASE cars_sales_inc;
USE cars_sales_inc;
CREATE TABLE cars (ID INT(5), VIN VARCHAR(20), Manufacturer VARCHAR(20), Model VARCHAR(20), Año INT(5), Color VARCHAR(20));
CREATE TABLE customers (ID INT(5), Customer_ID ID INT(5), Nombre VARCHAR(20), Phone VARCHAR(20), Email VARCHAR(20), Address VARCHAR(20), City VARCHAR(10), State/Province VARCHAR(20), Country VARCHAR(20), Postal INT(10));
CREATE TABLE salesperson (ID INT(5), Staff_ID INT(10), Nombre VARCHAR(20), Store VARCHAR(20));
CREATE TABLE invoices (ID INT(5), Invoice Number INT(15), Date DATE, Car INT(10), Customer INT(5), Sales Person INT(5));
