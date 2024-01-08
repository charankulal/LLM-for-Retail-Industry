few_shots=[
    {
        'Question':'How many t-shirts do we have left for Nike in XS size and white colour?',
        'SQLQuery':"select sum(stock_quantity) from t_shirts where brand='Nike' and color='White' and size='XS'",
        'SQLResult': "Result of the SQL Query",
        'Answer':100
    },
    {
        'Question':"How much is the price of the inventory for all small size t-shirts?",
        'SQLQuery':"SELECT SUM(price*stock_quantity) FROM t_shirts WHERE size = 'S'",
        'SQLResult': "Result of the SQL Query",
        'Answer':19432
    },
    {
        'Question':"If we have to sell all the Levi's T-shirts today with discounts applied. How much revenue our store will generate (post discounts)?",
        'SQLQuery':"select sum(a.total_amount*((100-COALESCE(discounts.pct_discount,0))/100)) as total revenue from (select sum(price*stock_quantity) as total_amount, t_shirt_id fro, t_shirts where brand='Levi' group by t_shirt_id) a left join discounts on a.t_shirts_id=discounts.t_shirt_id",
        'SQLResult': "Result of the SQL Query",
        'Answer':28201.0
    },
    {
        'Question':"If we have to sell all th eLevi's T-shirts today. How much revenue our store will gain?",
        'SQLQuery':"select sum(price*stock_quantity) from t_shirts where brand='Levi'",
        'SQLResult': "Result of the SQL Query",
        'Answer':28381
    },
    {
        'Question':"How many white color Levi's t shirts we have?",
        'SQLQuery':"SELECT sum(stock_quantity) FROM t_shirts WHERE brand = 'Levi' AND color = 'White';",
        'SQLResult': "Result of the SQL Query",
        'Answer':144
    },
    
]