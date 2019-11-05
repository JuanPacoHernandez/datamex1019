INSERT INTO cars (ID,VIN,Manufacturer,Model,Año,Color) 
VALUES (0,3K096I98581DHSNUP,Volkswagen,Tiguan,2019,Blue);
INSERT INTO cars (ID,VIN,Manufacturer,Model,Año,Color) 
VALUES (1,ZM8G7BEUQZ97IH46V,Peugeot,Rifter,2019,Red);
INSERT INTO cars (ID,VIN,Manufacturer,Model,Año,Color) 
VALUES (2,RKXVNNIHLVVZOUB4M,Ford,Fusion,2018,White);
INSERT INTO cars (ID,VIN,Manufacturer,Model,Año,Color) 
VALUES (3,HKNDGS7CU31E9Z7JW,Toyota,RAV4,2018,Silver);
INSERT INTO cars (ID,VIN,Manufacturer,Model,Año,Color) 
VALUES (4,DAM41UDN3CHU2WVF6,Volvo,V60,2019,Gray);
INSERT INTO cars (ID,VIN,Manufacturer,Model,Año,Color) 
VALUES (5,DAM41UDN3CHU2WVF6,Volvo,V60 Cross Country,2019,Gray);
INSERT INTO customers (ID,Customer_ID,Nombre,Phone,Email,Address,City,State/Province,Country,Postal) 
VALUES (0,10001,Pablo Picasso,+34 636 17 63 82,-,Paseo de la Chopera 14,Madrid,Spain,28045);
INSERT INTO customers (ID,Customer_ID,Nombre,Phone,Email,Address,City,State/Province,Country,Postal) 
VALUES (1,20001,Abraham Lincoln,+1 305 907 7086,-,120 SW 8th St,),Miami,Florida, United States,33130);
INSERT INTO customers (ID,Customer_ID,Nombre,Phone,Email,Address,City,State/Province,Country,Postal) 
VALUES (2,30001,Napoleon Bonaparte,+33 1 79 75 40 00,,-,40 Rue du Colisée,Paris,Île-de-France,France,75008);
INSERT INTO salesperson (ID,Staff_ID,Nombre,Store) 
VALUES (0,0001,Peter Cruiser,Madrid);
INSERT INTO salesperson (ID,Staff_ID,Nombre,Store) 
VALUES (1,0002,Anna Sthesia,Barcelona);
INSERT INTO salesperson (ID,Staff_ID,Nombre,Store) 
VALUES (2,0003,Paul Molive,Berlin);
INSERT INTO salesperson (ID,Staff_ID,Nombre,Store) 
VALUES (3,0004,Gail Forcewind,Paris);
INSERT INTO salesperson (ID,Staff_ID,Nombre,Store) 
VALUES (4,0005,Paige Turner,Mimia);
INSERT INTO salesperson (ID,Staff_ID,Nombre,Store) 
VALUES (5,0006,Bob Frapples,Mexico);
INSERT INTO salesperson (ID,Staff_ID,Nombre,Store) 
VALUES (6,0007,Walter Melon,Amsterdam);
INSERT INTO salesperson (ID,Staff_ID,Nombre,Store) 
VALUES (7,0008,Shonda Leer,São Paulo);
INSERT INTO invoices (ID,invoice_number,date,car,customer,salesperson) 
VALUES (0,852399038,'2018/08/22',0,1,3);
INSERT INTO invoices (ID,invoice_number,date,car,customer,salesperson) 
VALUES (1,731166526,'2018/01/31',3,0,5);
INSERT INTO invoices (ID,invoice_number,date,car,customer,salesperson) 
VALUES (0,271135104,'2019/01/22',2,2,7);

