CREATE TABLE Passanger (
PSG_ID int not null auto_increment,
PSG_Name varchar(30) not null,
PSG_LastN varchar(15) not null,
PSG_BirthD datetime not null, 
PSG_Nation varchar(20) not null,
PSG_NationalID varchar(15) not null,
PSG_Contact varchar(12) not null,
primary key (PSG_ID)
);

CREATE TABLE Airline(
ALN_ID int not null auto_increment,
ALN_Name varchar(20) not null,
ALN_Chief varchar(15) not null,
primary key (ALN_ID)
);

CREATE TABLE Airline_Passanger(
PSG_ID int not null,
ALN_ID int not null,
PSG_frequent numeric(12,0),
primary key (PSG_ID, ALN_ID),
foreign key (PSG_ID) references Passanger(PSG_ID),
foreign key (ALN_ID) references Airline(ALN_ID)
);

# Necessary because of inconsistency error
# due to our order of creation of tables
# alter table Airline_Passanger
# add constraint FK_Airline_Passanger
# foreign key (PSG_ID) 
# references Passanger (PSG_ID);
