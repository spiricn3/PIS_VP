-- Brisanje postojeće baze podataka (ako postoji):
DROP DATABASE IF EXISTS voznipark;

-- Kreiranje nove baze podataka:
CREATE DATABASE voznipark;

-- Kreiranje novog korisnika:
CREATE USER 'vozac'@'%' IDENTIFIED BY 'vozilo';

-- Dodeljivanje privilegija korisniku na bazi:
GRANT ALL PRIVILEGES ON voznipark.* TO 'vozac'@'%';

-- Primena promena privilegija:
FLUSH PRIVILEGES;