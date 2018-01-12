# dailyfresh
利用python的django框架实现中小型电商项目(B2C)

    
1.需求分析
1.1 用户模块
1)注册页
注册时校验用户名是否已被注册。
完成用户信息的注册。
给用户的注册邮箱发送邮件，用户点击邮件中的激活链接完成用户账户的激活。
2)登录页
实现用户的登录功能。
3)用户中心
用户中心信息页：显示登录用户的信息，包括用户名、电话和地址，同时页面下方显示出用户最近浏览的商品信息。
用户中心地址页：显示登录用户的默认收件地址，页面下方的表单可以新增用户的收货地址。
用户中心订单页：显示登录用户的订单信息。
4)其他
如果用户已经登录，页面顶部显示登录用户的信息。
1.2 商品相关
1)首页
动态指定首页轮播商品信息。
动态指定首页活动信息。
动态获取商品的种类信息并显示。
动态指定首页显示的每个种类的商品(包括图片商品和文字商品)。
点击某一个商品时跳转到商品的详情页面。
2)商品详情页
显示出某个商品的详情信息。
页面的左下方显示出该种类商品的2个新品信息。
3）商品列表页
显示出某一个种类商品的列表数据，分页显示并支持按照默认、价格、和人气进行排序。
页面的左下方显示出该种类商品的2个新品信息。
4）其他
通过页面搜索框搜索商品信息。
1.3 购物车相关
列表页和详情页将商品添加到购物车。
用户登录后，首页，详情页，列表页显示登录用户购物车中商品的数目。
购物车页面：对用户购物车中商品的操作。如选择某件商品，增加或减少购物车中商品的数目。
1.4 订单相关
提交订单页面：显示用户准备购买的商品信息。
点击提交订单完成订单的创建。
用户中心订单页显示用户的订单信息。
点击支付完成订单的支付。

第一天进度:
    主要工作:数据库搭建
    
    1.明确分类,将数据库抽象到四个应用中.
        1)用户类
            (1.1) 用户信息表(这里我们使用django中以实现的抽象用户类(AbstractUser))
            (1.2) 用户收货地址表(一个用户对应可多个收货地址)
        2)商品类
            (2.1) 商品分类表
            (2.2) 商品的spu表
            (2.3) 商品的sku表
            (2.4) 商品图片表
            (2.5) 首页促销活动表
            (2.6) 首页商品轮播表
            (2.7) 首页商品分类及个别商品展示表
        3)订单类
            (3.1) 订单信息表
            (3.2) 订单商品信息表
        4)购物车
            购物车目前准备不熟于redis中


        

