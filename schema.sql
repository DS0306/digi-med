CREATE DATABASE IF NOT EXISTS project;
USE project;

--Doctor Details
CREATE TABLE doctordetails (
    doctorid INT PRIMARY KEY,
    doctorname VARCHAR(50),
    specialisation VARCHAR(50),
    fees INT,
    degree VARCHAR(50),
    timings VARCHAR(50),
    hospitalname VARCHAR(100),
    gender VARCHAR(10),
    password VARCHAR(50),
    phonenumber BIGINT,
    emailid VARCHAR(100)
);

--Patient Details
CREATE TABLE patientdetails (
    patientid INT PRIMARY KEY,
    password VARCHAR(50),
    patientname VARCHAR(50),
    age INT,
    gender VARCHAR(10),
    contactno BIGINT,
    emailid VARCHAR(100)
);

--Appointments
CREATE TABLE appointment (
    appointmentid INT PRIMARY KEY,
    doctorname VARCHAR(50),
    department VARCHAR(50),
    hospital VARCHAR(100),
    date VARCHAR(20),
    timings VARCHAR(50),
    patientname VARCHAR(50),
    age INT,
    gender VARCHAR(10),
    contactno BIGINT,
    doctorid INT
);