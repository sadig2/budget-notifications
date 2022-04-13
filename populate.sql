select * from notification_t_shop;

INSERT INTO notification_t_shop
    (id,  name,             online)
VALUES
    (1,     'Steve McQueen',    True),
    (2,     'Fashion Quasar',   False),
    (3,     'As Seen On Sale',  True),
    (4,     'H&R',              False),
    (5,     'Meow Meow',        True),
    (6,     'Dole & Cabbage',   False),
    (7,     'George Manly',     True),
    (8,     'Harrison Ford',    False);
	
	
	
	INSERT INTO notification_t_budget
    (shop_id_id, month, budget_amount, amount_spent)
VALUES
    (1, '2020-06-01', 930.00, 725.67),
    (2, '2020-06-01', 990.00, 886.63),
    (3, '2020-06-01', 650.00, 685.91),
    (4, '2020-06-01', 740.00, 746.92),
    (5, '2020-06-01', 630.00, 507.64),
    (6, '2020-06-01', 640.00, 946.32),
    (7, '2020-06-01', 980.00, 640.16),
    (8, '2020-06-01', 790.00, 965.64),
    (1, '2020-07-01', 960.00, 803.67),
    (2, '2020-07-01', 670.00, 715.64),
    (3, '2020-07-01', 890.00, 580.81),
    (4, '2020-07-01', 590.00, 754.93),
    (5, '2020-07-01', 870.00, 505.12),
    (6, '2020-07-01', 700.00, 912.30),
    (7, '2020-07-01', 990.00, 805.15),
    (8, '2020-07-01', 720.00, 504.25);