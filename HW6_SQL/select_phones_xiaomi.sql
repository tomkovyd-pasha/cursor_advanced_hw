-- Write select and save it to file to get phones where company_id=XIAOMI COMPANY ID.
USE my_items;

SELECT * FROM phones p WHERE p.company_id = 1;

SELECT * FROM phones p WHERE p.company_id = (SELECT c.id FROM phone_companies c WHERE c.name = 'xiaomi');