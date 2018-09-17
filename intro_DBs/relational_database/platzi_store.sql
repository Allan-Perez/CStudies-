/* start off with these drops 
  to avoid any kind of possible 
  incensistency with the database */
drop table if exists customer;
drop table if exists item;
drop table if exists cart;
drop table if exists mPayment;
drop table if exists mShipment;
drop table if exists supplier;
drop table if exists cartItemWeak;
drop table if exists itemSupplierWeak;
/* BE CAREFUL. THIS IS DEVELOPMENT, NOT PRODUCTION
 THIS(^) MUST NEVER BE DONE IN PRODUCTION */


/*==============================================*/
/*	TABLE: CUSTOMER */ 
/*==============================================*/
CREATE TABLE customer(
	CST_ID 			int not null auto_increment,
	CST_Name 		varchar(10) not null,
	CST_LastName 	varchar(15) not null,
	CST_Email 		varchar(50) not null,
	CST_Address		varchar(40) not null, 
	CST_City 		varchar(40) not null, 
	CST_State		varchar(40) not null,
	CST_Country 	varchar(40) not null, 
	CST_BirthDay 	datetime not null, 
	CST_RegisDay 	datetime not null, 
	CST_Currency 	varchar(3) not null,
	CST_Picture 	varchar(80) not null,
	PAY_ID			int, 
	SHP_ID			int, 

	PRIMARY KEY (CST_ID)	
);

/*==============================================*/
/*	TABLE: mPayment */ 
/*==============================================*/
CREATE TABLE mPayment(
	PAY_ID 			int not null auto_increment,
	PAY_Name 		varchar(30) not null, 
	PAY_CCNum 		varchar(30) not null, 
	PAY_CVC 		varchar(3) not null, 
	PAY_Expir		datetime not null, #
	PAY_HolderName 	varchar(10) not null,
	PAY_HolderLast 	varchar(15) not null,
	PAY_Date 		datetime not null, 
	PAY_GatewCode 	decimal(12,0) not null,

	PRIMARY KEY (PAY_ID)
);




/*==============================================*/
/*	TABLE: mShipment */ 
/*==============================================*/
CREATE TABLE mShipment(
	SHP_ID 			int not null auto_increment,
	SHP_Type 		varchar(10) not null,
	SHP_Comp 		varchar(10) not null,
	SHP_Price 		decimal(2,2) not null, 

	PRIMARY KEY (SHP_ID)
);


/*==============================================*/
/*	TABLE: supplier */ 
/*==============================================*/
CREATE TABLE supplier(
	SPL_ID 				int not null auto_increment,
	SPL_Name			varchar(40) not null,
	SPL_HQAddr			varchar(30) not null,
	SPL_City			varchar(30) not null,
	SPL_Country			varchar(20) not null,
	SPL_ChamberComCode 	varchar(30) not null comment 'The chamber commerce code for a supplier', 
	SPL_FirstDay 		datetime not null,
	SPL_Currency		varchar(3) not null,

	PRIMARY KEY (SPL_ID)

);



/*==============================================*/
/*	TABLE: ITEM */ 
/*==============================================*/
CREATE TABLE item(
	ITM_ID 			int not null auto_increment,
	ITM_Name 		varchar(50) not null, 
	ITM_Category 	varchar(30) not null,
	ITM_Picture 	varchar(80) not null, 
	ITM_WeightKG 	decimal(3,2) not null,
	SPL_ID 			int,

	PRIMARY KEY (ITM_ID), #
	FOREIGN KEY (SPL_ID) REFERENCES supplier (SPL_ID)
);


/*==============================================*/
/*	TABLE: CART */ 
/*==============================================*/
CREATE TABLE cart(
	CRT_ID 			int not null auto_increment,
	CRT_Size 		int not null,
	CRT_Price 		decimal(5,2) not null, 
	CRT_nItems 		decimal(3,0) not null, 
	CST_ID  		int, #

	PRIMARY KEY (CRT_ID), 
	FOREIGN KEY (CST_ID) REFERENCES customer (CST_ID)
);



/*==============================================*/
/*	TABLE: cartItemWeak */ 
/*==============================================*/
CREATE TABLE cartItemWeak(
	ITM_ID 				int ,
	CRT_ID 				int , 
	CNI_Quantity		int not null,
	CNI_UnitCost 		decimal(5,2) not null,
	CNI_PromotionCode  	varchar(10),

	FOREIGN KEY (ITM_ID) 
		REFERENCES item (ITM_ID), #
	FOREIGN KEY (CRT_ID) 
		REFERENCES cart (CRT_ID)
);




/*==============================================*/
/*	TABLE: itemSupplierWeak */ 
/*==============================================*/
CREATE TABLE itemSupplierWeak(
	ITM_ID			int ,
	SPL_ID			int ,
	SNI_Lot 		int not null,
	SNI_Cost		decimal(6,2) not null,
	SNI_Date		datetime not null,
	SNI_ItemName 	varchar(30) not null, #

	FOREIGN KEY (ITM_ID) REFERENCES item (ITM_ID), # not because in mysql i have to create the table first
	FOREIGN KEY (SPL_ID) REFERENCES supplier (SPL_ID)

);


ALTER TABLE customer ADD CONSTRAINT FK_SHP_ID FOREIGN KEY (SHP_ID) REFERENCES mShipment (SHP_ID) on delete restrict on update restrict;
ALTER TABLE customer ADD CONSTRAINT FK_PAY_ID FOREIGN KEY (PAY_ID) REFERENCES mPayment (PAY_ID) on delete restrict on update restrict;

	
