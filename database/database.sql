CREATE DATABASE Hospital_app

USE Hospital_app


CREATE TABLE Hospital_app.hospital (
                id INT auto_increment NOT NULL,
                name varchar(100) NOT NULL,
                phone INT NOT NULL,
                address varchar(500) NOT NULL,
                description varchar(1000) NULL,
                CONSTRAINT hospital_pk PRIMARY KEY (id)
                )
            
CREATE TABLE Hospital_app.doctor (
                id INT auto_increment NOT NULL,
                name varchar(100) NOT NULL,
                phone INT NOT NULL,
                email varchar(100) NOT NULL,
                address varchar(100) NOT NULL,
                hospital_id INT NOT NULL,
                CONSTRAINT doctor_pk PRIMARY KEY (id),
                CONSTRAINT doctor_FK FOREIGN KEY (hospital_id) REFERENCES hospital.hospital(id) ON UPDATE CASCADE
                )
        

CREATE TABLE Hospital_app.patient (
                id INT auto_increment NOT NULL,
                name varchar(100) NOT NULL,
                phone INT NOT NULL,
                email varchar(100) NOT NULL,
                address varchar(100) NOT NULL,
                hospital_id INT NOT NULL,
                CONSTRAINT patient_pk PRIMARY KEY (id),
                CONSTRAINT patient_FK FOREIGN KEY (hospital_id) REFERENCES hospital.hospital(id) ON UPDATE CASCADE
                )
               

CREATE TABLE Hospital_app.schedule (
                id INT auto_increment NOT NULL,
                name varchar(100) NOT NULL,
                `date` DATE NOT NULL,
                doctor_id INT NOT NULL,
                patient_id INT NOT NULL,
                `result` varchar(100),
                CONSTRAINT schedule_pk PRIMARY KEY (id),
                CONSTRAINT schedule_FK FOREIGN KEY (doctor_id) REFERENCES hospital.doctor(id) ON UPDATE CASCADE,
                CONSTRAINT schedule_FK_1 FOREIGN KEY (patient_id) REFERENCES hospital.patient(id) ON UPDATE CASCADE
                )
               