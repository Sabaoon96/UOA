/*******************************************************************************
   Drop Tables
********************************************************************************/
DROP TABLE IF EXISTS [Customer];
DROP TABLE IF EXISTS [AddressType];
DROP TABLE IF EXISTS [Address];
DROP TABLE IF EXISTS [Role];
DROP TABLE IF EXISTS [Employee];
DROP TABLE IF EXISTS [OrderStatus];
DROP TABLE IF EXISTS [CustOrder];
DROP TABLE IF EXISTS [Product];
DROP TABLE IF EXISTS [OrderProduct];
DROP TABLE IF EXISTS [Ingredient];
DROP TABLE IF EXISTS [Recipe];
DROP TABLE IF EXISTS [ProductSpecial];
DROP TABLE IF EXISTS [ReviewType];
DROP TABLE IF EXISTS [Review];

/*******************************************************************************
   Create Tables
********************************************************************************/
CREATE TABLE [Customer]
(
  [customerID] INTEGER NOT NULL,
	[email] VARCHAR(100)  NOT NULL,
	[firstName] VARCHAR(25)  NOT NULL,
	[lastName] VARCHAR(25)  NOT NULL,
  [gender] VARCHAR(1)  NOT NULL,
  [birthDate] DATE,
	[contactNumber] VARCHAR(20)  NOT NULL,
	[password] VARCHAR(20)  NOT NULL,
	CONSTRAINT Customer_pk PRIMARY KEY([customerID]),
	CONSTRAINT gender_ch CHECK(gender IN ('M','F'))
);

CREATE TABLE [AddressType]
(
  [addressTypeID] INTEGER NOT NULL,
  [addressTypeDesc] VARCHAR(20),
	CONSTRAINT AddressType_pk PRIMARY KEY([addressTypeID])
);

CREATE TABLE [Address]
(
  [addressID] INTEGER NOT NULL,
  [street] VARCHAR(60) NOT NULL,
  [suburb] VARCHAR(40) NOT NULL,
  [city] VARCHAR(40) NOT NULL,
  [postalCode] VARCHAR(10) NOT NULL,
  [addressTypeID] INTEGER NOT NULL,
  [customerID] INTEGER,
  CONSTRAINT Address_pk PRIMARY KEY([addressID]),
	CONSTRAINT Address_fk1 FOREIGN KEY([addressTypeID]) REFERENCES AddressType([addressTypeID]),
	CONSTRAINT Address_fk2 FOREIGN KEY([customerID]) REFERENCES Customer([customerID])
);

CREATE TABLE [Role]
(
  [roleID] VARCHAR(10) NOT NULL,
  [roleName] VARCHAR(20) NOT NULL,
	CONSTRAINT Role_pk PRIMARY KEY([roleID])
);

CREATE TABLE [Employee]
(
  [empID] INTEGER NOT NULL,
  [empFirstName] VARCHAR(30) NOT NULL,
	[empLastName] VARCHAR(30) NOT NULL,
	[roleID] VARCHAR(10) NOT NULL,
	[startDate] DATE NOT NULL,
	[endDate] DATE,
	CONSTRAINT Employee_pk PRIMARY KEY([empID]),
	CONSTRAINT Employee_fk FOREIGN KEY([roleID]) REFERENCES Role([roleID])
);

CREATE TABLE [OrderStatus]
(
  [orderStatusCode] INTEGER NOT NULL,
  [orderStatusDesc] VARCHAR(20) NOT NULL,
	CONSTRAINT OrderStatus_pk PRIMARY KEY([orderStatusCode])
);

CREATE TABLE [CustOrder]
(
  [orderNo] INTEGER NOT NULL,
  [orderDateTime] DATE NOT NULL,
  [deliveryName] VARCHAR(50) NOT NULL,
  [deliveryMobile] VARCHAR(20) NOT NULL,
  [orderStatusCode] INTEGER NOT NULL,
  [deliveryAddressID] INTEGER NOT NULL,
  [billingAddressID] INTEGER NOT NULL,
  [customerID] INTEGER NOT NULL,
  [empID] INTEGER NOT NULL,
	CONSTRAINT CustOrder_pk PRIMARY KEY([orderNo]),
	CONSTRAINT CustOrder_fk1 FOREIGN KEY([orderStatusCode]) REFERENCES OrderStatus([orderStatusCode]),
	CONSTRAINT CustOrder_fk2 FOREIGN KEY([deliveryAddressID]) REFERENCES Address([addressID]),
	CONSTRAINT CustOrder_fk3 FOREIGN KEY([billingAddressID]) REFERENCES Address([addressID]),
	CONSTRAINT CustOrder_fk4 FOREIGN KEY([customerID]) REFERENCES Customer([customerID]),
	CONSTRAINT CustOrder_fk5 FOREIGN KEY([empID]) REFERENCES Employee([empID])
);

CREATE TABLE [Product]
(
  [prodNo] INTEGER NOT NULL,
  [prodName] VARCHAR(50) NOT NULL,
	[prodDesc] VARCHAR(100) NOT NULL,
	[prodPrice] NUMERIC(10,2),
	[prodParentNo] INTEGER,
	CONSTRAINT Product_pk PRIMARY KEY([prodNo]),
	CONSTRAINT Product_fk1 FOREIGN KEY([prodParentNo]) REFERENCES Product([prodNo])
);

CREATE TABLE [OrderProduct]
(
  [orderNo] INTEGER NOT NULL,
  [prodNo] INTEGER NOT NULL,
	[quantity] INTEGER NOT NULL,
	CONSTRAINT OrderProduct_pk PRIMARY KEY([orderNo], [prodNo]),
	CONSTRAINT OrderProduct_fk1 FOREIGN KEY([orderNo]) REFERENCES CustOrder([orderNo]),
	CONSTRAINT OrderProduct_fk2 FOREIGN KEY([prodNo]) REFERENCES Product([prodNo])
);

CREATE TABLE [Ingredient]
(
  [ingrNo] INTEGER NOT NULL,
  [ingrName] VARCHAR(50) NOT NULL,
	[ingrUnit] VARCHAR(20) NOT NULL,
	CONSTRAINT Ingredient_pk PRIMARY KEY([ingrNo])
);

CREATE TABLE [Recipe]
(
  [prodNo] INTEGER NOT NULL,
  [ingrNo] INTEGER NOT NULL,
	[unitRequired] NUMERIC(10, 2) NOT NULL,
	CONSTRAINT Recipe_pk PRIMARY KEY([prodNo], [ingrNo]),
	CONSTRAINT Recipe_fk1 FOREIGN KEY([prodNo]) REFERENCES Product([prodNo]),
	CONSTRAINT Recipe_fk2 FOREIGN KEY([ingrNo]) REFERENCES Ingredient([ingrNo])
);

CREATE TABLE [ProductSpecial]
(
  [prodNo] INTEGER NOT NULL,
  [startDateTime] DATE NOT NULL,
	[endDateTime] DATE,
	[discount] NUMERIC(5,2) NOT NULL,
	CONSTRAINT ProductSpecial_pk PRIMARY KEY([prodNo], [startDateTime]),
	CONSTRAINT ProductSpecial_fk FOREIGN KEY([prodNo]) REFERENCES Product([prodNo])
);

CREATE TABLE [ReviewType]
(
  [reviewTypeID] INTEGER NOT NULL,
  [reviewTypeDesc] VARCHAR(30) NOT NULL,
	CONSTRAINT ReviewType_pk PRIMARY KEY([reviewTypeID])
);

CREATE TABLE [Review]
(
  [reviewNo] INTEGER NOT NULL,
  [reviewDate] DATE NOT NULL,
	[reviewDesc] TEXT NOT NULL,
	[reviewStar] INTEGER NOT NULL,
	[reviewPublished] VARCHAR(1) NOT NULL,
	[customerID] INTEGER,
	[prodNo] INTEGER,
	[reviewTypeID] INTEGER NOT NULL,
	CONSTRAINT Review_pk PRIMARY KEY([reviewNo]),
	CONSTRAINT Review_fk1 FOREIGN KEY([customerID]) REFERENCES Customer([customerID]),
	CONSTRAINT Review_fk2 FOREIGN KEY([prodNo]) REFERENCES Product([prodNo]),
	CONSTRAINT Review_fk3 FOREIGN KEY([reviewTypeID]) REFERENCES ReviewType([reviewTypeID]),
	CONSTRAINT reviewStar_ch CHECK(reviewStar BETWEEN 1 AND 5),
	CONSTRAINT reviewPublished_ch CHECK(reviewPublished IN ('Y', 'N'))
);

/*******************************************************************************
   Populate Tables
********************************************************************************/

INSERT INTO [Customer] ([customerID], [email], [firstName], [lastName], [gender], [birthDate], [contactNumber],	[password]) VALUES (1, 'lowellandanna.dacanay77@yahoo.com', 'Lowell', 'Dacanay', 'M', '1987-05-25 00:00:00', '0210146549', 'T28cX47N');
INSERT INTO [Customer] ([customerID], [email], [firstName], [lastName], [gender], [birthDate], [contactNumber],	[password]) VALUES (2, 's.sharif79@gmail.com', 'Shonna', 'Sharif', 'F', '1979-04-30 00:00:00', '0218640344', 'gFcEK8WW');
INSERT INTO [Customer] ([customerID], [email], [firstName], [lastName], [gender], [birthDate], [contactNumber],	[password]) VALUES (3, 'donetta111@gmail.com', 'Donetta', 'Figgs', 'F', '1981-10-19 00:00:00', '095314623', 'TAnfXr4V');
INSERT INTO [Customer] ([customerID], [email], [firstName], [lastName], [gender], [birthDate], [contactNumber],	[password]) VALUES (4, 'mrhuggable82@live.com', 'Tyler', 'Hug', 'M', '1982-03-15 00:00:00', '0213082533', 'pXnWgsLe');
INSERT INTO [Customer] ([customerID], [email], [firstName], [lastName], [gender], [birthDate], [contactNumber],	[password]) VALUES (5, 'whitney.t1982@yahoo.com', 'Whitney', 'Toy', 'M', '1982-05-31 00:00:00', '0276691473', 'GzFe23ue');
INSERT INTO [Customer] ([customerID], [email], [firstName], [lastName], [gender], [birthDate], [contactNumber],	[password]) VALUES (6, 'deborah.schlatter@yahoo.com', 'Deborah', 'Schlatter', 'F', '1984-03-22 00:00:00', '0218755468', 'HPZsNqRB');
INSERT INTO [Customer] ([customerID], [email], [firstName], [lastName], [gender], [birthDate], [contactNumber],	[password]) VALUES (7, 'frederic.setzer@hotmail.com', 'Frederic', 'Setzer', 'M', '1985-12-04 00:00:00', '0223882353', 'uSdXThCC');
INSERT INTO [Customer] ([customerID], [email], [firstName], [lastName], [gender], [birthDate], [contactNumber],	[password]) VALUES (8, 'dania-marie.pilon94@gmail.com', 'Dania', 'Pilon', 'F', '1993-03-29 00:00:00', '0217593751', 'Y6Mc87Fe');
INSERT INTO [Customer] ([customerID], [email], [firstName], [lastName], [gender], [birthDate], [contactNumber],	[password]) VALUES (9, 'jo94.pisani@gmail.com', 'Joanna', 'Pisani', 'F', '1994-06-18 00:00:00', '0271195909', 'sd34tVCe');
INSERT INTO [Customer] ([customerID], [email], [firstName], [lastName], [gender], [birthDate], [contactNumber],	[password]) VALUES (10, 'cassi.demaris@gmail.com', 'Cassi', 'Demaris', 'F', '1990-09-03 00:00:00', '0275485863', 'Ya3FeSyp');

INSERT INTO [AddressType] ([addressTypeID], [addressTypeDesc]) VALUES (1, 'Residential');
INSERT INTO [AddressType] ([addressTypeID], [addressTypeDesc]) VALUES (2, 'Commercial');

INSERT INTO [Address] ([addressID], [street], [suburb], [city], [postalCode], [addressTypeID], [customerID]) VALUES (1001, '705 Durham Court', 'East Tamaki', 'Auckland', '2016', 1, 1);
INSERT INTO [Address] ([addressID], [street], [suburb], [city], [postalCode], [addressTypeID], [customerID]) VALUES (1002, '276 Front Street', 'Epsom', 'Auckland', '1023', 1, 2);
INSERT INTO [Address] ([addressID], [street], [suburb], [city], [postalCode], [addressTypeID], [customerID]) VALUES (1003, '26 Farm Street', 'Remuera', 'Auckland', '1050', 1, 3);
INSERT INTO [Address] ([addressID], [street], [suburb], [city], [postalCode], [addressTypeID], [customerID]) VALUES (1004, '689 Magnolia Avenue', 'Remuera', 'Auckland', '1050', 1, 4);
INSERT INTO [Address] ([addressID], [street], [suburb], [city], [postalCode], [addressTypeID], [customerID]) VALUES (1005, '675 Elizabeth Street', 'Howick', 'Auckland', '2014', 2, 5);
INSERT INTO [Address] ([addressID], [street], [suburb], [city], [postalCode], [addressTypeID], [customerID]) VALUES (1006, '371 Snake Street', 'Epsom', 'Auckland', '1023', 2, 6);
INSERT INTO [Address] ([addressID], [street], [suburb], [city], [postalCode], [addressTypeID], [customerID]) VALUES (1007, '875 Wood Street', 'Avondale', 'Auckland', '0600', 1, 7);
INSERT INTO [Address] ([addressID], [street], [suburb], [city], [postalCode], [addressTypeID], [customerID]) VALUES (1008, '649 Cobblestone Court', 'Botany Downs', 'Auckland', '2010', 1, 8);
INSERT INTO [Address] ([addressID], [street], [suburb], [city], [postalCode], [addressTypeID], [customerID]) VALUES (1009, '596 Tongalo Crescent', 'East Tamaki', 'Auckland', '2016', 1, 9);
INSERT INTO [Address] ([addressID], [street], [suburb], [city], [postalCode], [addressTypeID], [customerID]) VALUES (1010, '51 York Road', 'Ranui', 'Auckland',	'0612',	2, 10);

INSERT INTO [Role] ([roleID], [roleName]) VALUES ('man01', 'Manager');
INSERT INTO [Role] ([roleID], [roleName]) VALUES ('che02', 'Chef');
INSERT INTO [Role] ([roleID], [roleName]) VALUES ('cas03', 'Cashier');
INSERT INTO [Role] ([roleID], [roleName]) VALUES ('del04', 'Delivery');

INSERT INTO [Employee] ([empID], [empFirstName], [empLastName], [roleID], [startDate], [endDate]) VALUES (1, 'Classie', 'Filkins', 'man01', '2015-06-01 00:00:00', null);
INSERT INTO [Employee] ([empID], [empFirstName], [empLastName], [roleID], [startDate], [endDate]) VALUES (2, 'Miesha', 'Rozek', 'che02', '2015-06-02 00:00:00', null);
INSERT INTO [Employee] ([empID], [empFirstName], [empLastName], [roleID], [startDate], [endDate]) VALUES (3, 'Amanda', 'Corry', 'cas03', '2015-06-29 00:00:00', '2015-12-29 00:00:00');
INSERT INTO [Employee] ([empID], [empFirstName], [empLastName], [roleID], [startDate], [endDate]) VALUES (4, 'Owen', 'Willcutt', 'cas03', '2015-06-29 00:00:00', null);
INSERT INTO [Employee] ([empID], [empFirstName], [empLastName], [roleID], [startDate], [endDate]) VALUES (5, 'Gary', 'Zeledon', 'del04', '2015-06-29 00:00:00', null);

INSERT INTO [OrderStatus] ([orderStatusCode], [orderStatusDesc]) VALUES (1, 'Making Order');
INSERT INTO [OrderStatus] ([orderStatusCode], [orderStatusDesc]) VALUES (2, 'Ready in Store');
INSERT INTO [OrderStatus] ([orderStatusCode], [orderStatusDesc]) VALUES (3, 'Delivering');
INSERT INTO [OrderStatus] ([orderStatusCode], [orderStatusDesc]) VALUES (4, 'Order Complete');

INSERT INTO [CustOrder] ([orderNo], [orderDateTime], [deliveryName], [deliveryMobile], [orderStatusCode], [deliveryAddressID], [billingAddressID], [customerID], [empID]) VALUES (1, '2015-07-07 00:00:00', 'Lowell Dacanay', '0210146549', 4, 1001, 1001, 1, 3);
INSERT INTO [CustOrder] ([orderNo], [orderDateTime], [deliveryName], [deliveryMobile], [orderStatusCode], [deliveryAddressID], [billingAddressID], [customerID], [empID]) VALUES (2, '2015-07-07 00:00:00', 'Shonna Sharif', '0218640344', 4, 1002, 1002, 2, 3);
INSERT INTO [CustOrder] ([orderNo], [orderDateTime], [deliveryName], [deliveryMobile], [orderStatusCode], [deliveryAddressID], [billingAddressID], [customerID], [empID]) VALUES (3, '2015-07-08 00:00:00', 'Tyler Hug',	'0213082533', 4, 1004, 1004, 4, 4);
INSERT INTO [CustOrder] ([orderNo], [orderDateTime], [deliveryName], [deliveryMobile], [orderStatusCode], [deliveryAddressID], [billingAddressID], [customerID], [empID]) VALUES (4, '2015-07-08 00:00:00', 'Whitney Toy', '0276691473', 4, 1005, 1005, 5, 4);
INSERT INTO [CustOrder] ([orderNo], [orderDateTime], [deliveryName], [deliveryMobile], [orderStatusCode], [deliveryAddressID], [billingAddressID], [customerID], [empID]) VALUES (5, '2015-07-09 00:00:00', 'Frederic Setzer', '0223882353', 4, 1007, 1007, 7, 4);
INSERT INTO [CustOrder] ([orderNo], [orderDateTime], [deliveryName], [deliveryMobile], [orderStatusCode], [deliveryAddressID], [billingAddressID], [customerID], [empID]) VALUES (6, '2015-07-09 00:00:00', 'Dania Pilon', '0217593751', 4, 1008, 1008, 8, 4);
INSERT INTO [CustOrder] ([orderNo], [orderDateTime], [deliveryName], [deliveryMobile], [orderStatusCode], [deliveryAddressID], [billingAddressID], [customerID], [empID]) VALUES (7, '2015-07-09 00:00:00', 'Joanna Pisani', '0271195909', 4, 1009, 1009, 9, 4);
INSERT INTO [CustOrder] ([orderNo], [orderDateTime], [deliveryName], [deliveryMobile], [orderStatusCode], [deliveryAddressID], [billingAddressID], [customerID], [empID]) VALUES (8, '2015-07-09 00:00:00', 'Shonna Sharif', '0218640344', 4, 1002, 1006, 2, 4);
INSERT INTO [CustOrder] ([orderNo], [orderDateTime], [deliveryName], [deliveryMobile], [orderStatusCode], [deliveryAddressID], [billingAddressID], [customerID], [empID]) VALUES (9, '2015-07-10 00:00:00', 'Cassi Demaris', '0275485863', 4, 1010, 1010, 10, 3);
INSERT INTO [CustOrder] ([orderNo], [orderDateTime], [deliveryName], [deliveryMobile], [orderStatusCode], [deliveryAddressID], [billingAddressID], [customerID], [empID]) VALUES (10, '2015-07-10 00:00:00', 'Whitney Toy', '0276691473', 4, 1005, 1005, 5, 3);

INSERT INTO [Product] ([prodNo], [prodName], [prodDesc], [prodPrice], [prodParentNo]) VALUES (1001, 'Marinara D.O.C', 'Tomatoes, E.V.O.O, oregano, garlic (no cheese)', 20.00, null);
INSERT INTO [Product] ([prodNo], [prodName], [prodDesc], [prodPrice], [prodParentNo]) VALUES (1002, 'Regina Margherita D.O.C', 'Tomato, E.V.O.O, fresh mozzarella di bufala, fresh basil', 24.00, null);
INSERT INTO [Product] ([prodNo], [prodName], [prodDesc], [prodPrice], [prodParentNo]) VALUES (1003, 'La Bella Italia D.O.C', 'Tomato, E.V.O.O, fresh mozzarella di bufala, fresh tomatoes, crached black pepper, rocket', 24.00, null);
INSERT INTO [Product] ([prodNo], [prodName], [prodDesc], [prodPrice], [prodParentNo]) VALUES (1004, 'Con Prosciutto', 'Tomato, mozzarella, Italian cured ham, rocket, parmigiano',	24.00, null);
INSERT INTO [Product] ([prodNo], [prodName], [prodDesc], [prodPrice], [prodParentNo]) VALUES (1005, 'Chorizo Reale', 'Tomato, mozzarella, chorizo', 24.00, null);
INSERT INTO [Product] ([prodNo], [prodName], [prodDesc], [prodPrice], [prodParentNo]) VALUES (1006, 'Agilo', 'E.V.O.O, fresh garlic, rosemary, sea salt', 15.00, null);
INSERT INTO [Product] ([prodNo], [prodName], [prodDesc], [prodPrice], [prodParentNo]) VALUES (2002, 'Regina Margherita D.O.C (v)', 'Tomato, E.V.O.O, fresh vegetarian rennet, fresh basil', 24.00, 1002);
INSERT INTO [Product] ([prodNo], [prodName], [prodDesc], [prodPrice], [prodParentNo]) VALUES (2003, 'La Bella Italia D.O.C (v)', 'Tomato, E.V.O.O, fresh vegetarian rennet, fresh tomatoes, crached black pepper, rocket', 24.00, 1003);

INSERT INTO [OrderProduct] ([orderNo], [prodNo], [quantity]) VALUES (1, 1005, 1);
INSERT INTO [OrderProduct] ([orderNo], [prodNo], [quantity]) VALUES (1, 1006, 1);
INSERT INTO [OrderProduct] ([orderNo], [prodNo], [quantity]) VALUES (2, 2002, 2);
INSERT INTO [OrderProduct] ([orderNo], [prodNo], [quantity]) VALUES (3, 1005, 1);
INSERT INTO [OrderProduct] ([orderNo], [prodNo], [quantity]) VALUES (4, 1001, 2);
INSERT INTO [OrderProduct] ([orderNo], [prodNo], [quantity]) VALUES (4, 1002, 2);
INSERT INTO [OrderProduct] ([orderNo], [prodNo], [quantity]) VALUES (4, 1003, 1);
INSERT INTO [OrderProduct] ([orderNo], [prodNo], [quantity]) VALUES (4, 1004, 1);
INSERT INTO [OrderProduct] ([orderNo], [prodNo], [quantity]) VALUES (5, 1001, 1);
INSERT INTO [OrderProduct] ([orderNo], [prodNo], [quantity]) VALUES (6, 1005, 3);
INSERT INTO [OrderProduct] ([orderNo], [prodNo], [quantity]) VALUES (7, 1002, 1);
INSERT INTO [OrderProduct] ([orderNo], [prodNo], [quantity]) VALUES (8, 1002, 1);
INSERT INTO [OrderProduct] ([orderNo], [prodNo], [quantity]) VALUES (8, 1004, 2);
INSERT INTO [OrderProduct] ([orderNo], [prodNo], [quantity]) VALUES (9, 1003, 2);
INSERT INTO [OrderProduct] ([orderNo], [prodNo], [quantity]) VALUES (9, 1005, 1);
INSERT INTO [OrderProduct] ([orderNo], [prodNo], [quantity]) VALUES (10, 1005, 1);

INSERT INTO [Ingredient] ([ingrNo], [ingrName], [ingrUnit]) VALUES (1, 'Tomato', 'whole');
INSERT INTO [Ingredient] ([ingrNo], [ingrName], [ingrUnit]) VALUES (2, 'Garlic', 'cloves');
INSERT INTO [Ingredient] ([ingrNo], [ingrName], [ingrUnit]) VALUES (3, 'Olive oil', 'millilitres');
INSERT INTO [Ingredient] ([ingrNo], [ingrName], [ingrUnit]) VALUES (4, 'Mozzarella', 'grams');
INSERT INTO [Ingredient] ([ingrNo], [ingrName], [ingrUnit]) VALUES (5, 'Parmesan', 'grams');
INSERT INTO [Ingredient] ([ingrNo], [ingrName], [ingrUnit]) VALUES (6, 'Vegetarian rennet', 'grams');
INSERT INTO [Ingredient] ([ingrNo], [ingrName], [ingrUnit]) VALUES (7, 'Oregano', 'tablespoons');
INSERT INTO [Ingredient] ([ingrNo], [ingrName], [ingrUnit]) VALUES (8, 'Basil', 'tablespoons');
INSERT INTO [Ingredient] ([ingrNo], [ingrName], [ingrUnit]) VALUES (9, 'Rocket', 'tablespoons');
INSERT INTO [Ingredient] ([ingrNo], [ingrName], [ingrUnit]) VALUES (10, 'Ham', 'grams');
INSERT INTO [Ingredient] ([ingrNo], [ingrName], [ingrUnit]) VALUES (11, 'Chorizo', 'grams');

INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (1001, 1, 2.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (1001, 3, 60.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (1001, 7, 2.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (1001, 2, 1.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (1002, 1, 2.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (1002, 3, 60.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (1002, 4, 50.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (1002, 8, 2.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (1003, 1, 2.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (1003, 3, 60.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (1003, 4, 50.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (1003, 9, 1.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (1004, 1, 1.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (1004, 4, 50.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (1004, 10, 200.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (1004, 9, 2.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (1004, 5, 30.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (1005, 1, 2.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (1005, 4, 50.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (1005, 11, 200.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (1006, 3, 60.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (1006, 2, 2.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (2002, 1, 2.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (2002, 3, 60.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (2002, 6, 50.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (2002, 8, 2.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (2003, 1, 2.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (2003, 3, 60.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (2003, 6, 50.00);
INSERT INTO [Recipe] ([prodNo], [ingrNo], [unitRequired]) VALUES (2003, 9, 1.00);

INSERT INTO [ProductSpecial] ([prodNo], [startDateTime], [endDateTime], [discount]) VALUES (1002, '2015-05-01 00:00:00', '2015-05-31 00:00:00', 0.20);
INSERT INTO [ProductSpecial] ([prodNo], [startDateTime], [endDateTime], [discount]) VALUES (1003, '2015-05-01 00:00:00', '2015-06-30 00:00:00', 0.20);
INSERT INTO [ProductSpecial] ([prodNo], [startDateTime], [endDateTime], [discount]) VALUES (1001, '2015-07-01 00:00:00', '2015-07-03 00:00:00', 0.50);

INSERT INTO [ReviewType] ([reviewTypeID], [reviewTypeDesc]) VALUES (1, 'Product');
INSERT INTO [ReviewType] ([reviewTypeID], [reviewTypeDesc]) VALUES (2, 'Company');
INSERT INTO [ReviewType] ([reviewTypeID], [reviewTypeDesc]) VALUES (3, 'Product and company');

INSERT INTO [Review] ([reviewNo], [reviewDate], [reviewDesc], [reviewStar], [reviewPublished], [customerID], [prodNo], [reviewTypeID]) VALUES (1, '2015-07-07 00:00:00', 'Great vegetarian pizza!', 5, 'Y', 2, 2002, 1);
INSERT INTO [Review] ([reviewNo], [reviewDate], [reviewDesc], [reviewStar], [reviewPublished], [customerID], [prodNo], [reviewTypeID]) VALUES (2, '2015-07-08 00:00:00', 'Not bad, but it had a little too much garlic.', 3, 'Y', 5, 1001, 1);
INSERT INTO [Review] ([reviewNo], [reviewDate], [reviewDesc], [reviewStar], [reviewPublished], [customerID], [prodNo], [reviewTypeID]) VALUES (3, '2015-07-08 00:00:00', 'Great pizza.', 5, 'Y', 5, 1002, 1);
INSERT INTO [Review] ([reviewNo], [reviewDate], [reviewDesc], [reviewStar], [reviewPublished], [customerID], [prodNo], [reviewTypeID]) VALUES (4, '2015-07-09 00:00:00', 'This was definitely my favourite!', 5, 'Y', 5, 1003, 1);
INSERT INTO [Review] ([reviewNo], [reviewDate], [reviewDesc], [reviewStar], [reviewPublished], [customerID], [prodNo], [reviewTypeID]) VALUES (5, '2015-07-09 00:00:00', 'Great blend of the different types of cheese.', 4, 'Y', 5, 1004, 1);
INSERT INTO [Review] ([reviewNo], [reviewDate], [reviewDesc], [reviewStar], [reviewPublished], [customerID], [prodNo], [reviewTypeID]) VALUES (6, '2015-07-10 00:00:00', 'Had too much cheese.', 2, 'Y', 7, 1001, 1);
INSERT INTO [Review] ([reviewNo], [reviewDate], [reviewDesc], [reviewStar], [reviewPublished], [customerID], [prodNo], [reviewTypeID]) VALUES (7, '2015-07-10 00:00:00', 'The pizzas were delivered very quickly, and everyone at the party loved it!',	5, 'Y', 8, 1005, 3);
INSERT INTO [Review] ([reviewNo], [reviewDate], [reviewDesc], [reviewStar], [reviewPublished], [customerID], [prodNo], [reviewTypeID]) VALUES (8, '2015-07-11 00:00:00', 'Bought this flavour a second time, and it still tastes just as great as the first one.', 5, 'N', 2, 1002, 1);
INSERT INTO [Review] ([reviewNo], [reviewDate], [reviewDesc], [reviewStar], [reviewPublished], [customerID], [prodNo], [reviewTypeID]) VALUES (9, '2015-07-13 00:00:00', "This pizza was quite nice, but the base was too thin so it wasn't very filling", 3, 'Y', 5, 1005, 1);
