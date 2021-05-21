INSERT INTO category values ('Leisure');
INSERT INTO category values ('Things');
INSERT INTO category values ('Items');

INSERT INTO super_category values ('Leisure');
INSERT INTO super_category values ('Things');
INSERT INTO super_category values ('Items');
INSERT INTO super_category values ('Technology');
INSERT INTO super_category values ('Cuisine');

INSERT INTO simple_category values ('Movies');
INSERT INTO simple_category values ('Board Games');
INSERT INTO simple_category values ('Things at the Beach');
INSERT INTO simple_category values ('Things with Pockets');
INSERT INTO simple_category values ('Things with Wheels');
INSERT INTO simple_category values ('Bathroom Items');
INSERT INTO simple_category values ('Bedroom Items');
INSERT INTO simple_category values ('Television');
INSERT INTO simple_category values ('Electronic Goods');
INSERT INTO simple_category values ('Condiments');
INSERT INTO simple_category values ('Types of Breakfast');

INSERT INTO consists_of values ('Leisure', 'Movies');
INSERT INTO consists_of values ('Leisure','Board Games');
INSERT INTO consists_of values ('Things','Things at the Beach');
INSERT INTO consists_of values ('Things','Things with Pockets');
INSERT INTO consists_of values ('Things','Things with Wheels');
INSERT INTO consists_of values ('Items','Bathroom Items');
INSERT INTO consists_of values ('Items','Bedroom Items');
INSERT INTO consists_of values ('Technology','Television');
INSERT INTO consists_of values ('Technology','Electronic Goods');
INSERT INTO consists_of values ('Cuisine','Condiments');
INSERT INTO consists_of values ('Cuisine','Types of Breakfast');

