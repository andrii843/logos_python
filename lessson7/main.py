class Shop():
	name = None
	manager = None
	address = None
	contacts = None
	goods_list = []
	def __init__(self, **kwargs):
		self.name = kwargs['name']
		self.manager = kwargs['manager']
		self.address = kwargs['address']
		self.contacts = kwargs['contacts']

	def add_goods(self, goods):
		self.goods_list.append(goods)

	def get_goods_in_stock(self):
		res = []
		for g in self.goods_list:
			if g.in_stock:
				res.append(g)
		return res

	def set_manager(self, name, contacts):
		self.manager = name
		self.contacts = contacts

	def get_manager(self):
		return {
			'manager': self.manager,
			'contacts': self.contacts
		}


class Goods():
	name = None
	price = 0
	in_stock = False
	count_in_stock = 0
	def __init__(self, **kwargs):
		self.name = kwargs['name']
		self.price = kwargs['price']
		if 'count_in_stock' in kwargs.keys():
			self.count_in_stock = kwargs['count_in_stock']
		if self.count_in_stock:
			self.in_stock = True

	def discount(self, percent):
		self.price = (1 - percent / 100) * self.price

class Smartphone(Goods):
	os = None
	battery = None
	proccesor = None
	raw = None
	if_fronal_camera = True
	count_sim = 1
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.os = kwargs['os']
		self.battery = kwargs['battery']
		self.processor = kwargs['processor']
		self.raw = kwargs['raw']
		if 'if_fronal_camera' in kwargs.keys():
			self.if_fronal_camera = kwargs['if_fronal_camera']
		if 'count_sim' in kwargs.keys():
			self.count_sim = kwargs['count_sim']

class Laptop(Goods):
	processor = None
	raw = None
	os = None
	video_card = None
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.processor = kwargs['processor']
		self.raw = kwargs['raw']
		self.os = kwargs['os']
		self.video_card = kwargs['video_card']

class TV(Goods):
	screen_size = None
	if_smart = True
	frequency = None
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.screen_size = kwargs['screen_size']
		self.frequency = kwargs['frequency']
		if 'if_smart' in kwargs.keys():
			self.if_smart = kwargs['if_smart']

xiaomi = Laptop(processor=3.3, raw=8, video_card='nVidia', os='Windows', name='Xiaomi pro', price=1000, count_in_stock=10)
iphone = Smartphone(os='ios', battery=3000, processor=2.2, raw=3, name='Iphone', price=800, count_in_stock=15)
lg = TV(screen_size=44, frequency=50, name='LG', price=1999)

shop = Shop(name='Tech Shop', manager='Admin', address='Lviv', contacts='123456789')
shop.add_goods(xiaomi)
shop.add_goods(iphone)
shop.add_goods(lg)

xiaomi.discount(15)

goods = shop.get_goods_in_stock()

manager_1 = shop.get_manager()
shop.set_manager('Max', '333555')
manager_2 = shop.get_manager()