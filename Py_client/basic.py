import requests
import urllib.request
from bs4 import BeautifulSoup
from newspaper import Article


endpoint = 'http://127.0.0.1:8000/user/register/'

bodyFormData = {
    'username': 'duongvan',
    'password': '123456789',
    'last_name': 'duong',
    'first_name': 'thi van',
    'email': 'email@gmail.com',
}

page = requests.post(endpoint, data=bodyFormData)
# page = requests.post(endpoint, data=bodyFormData, headers={
#     'Content-Type': 'multipart/form-data;',
# })
# page = requests.get(endpoint)


print(page.text)
# print(page.json())


# # url = 'https://vnexpress.net/12-000-nguoi-do-ve-cua-lo-4092705.html'
# article = Article(endpoint)
# article.download()
# article.parse()
# # Xong rồi đấy, giờ lấy data thôi
# print(article.body)


# data = []

# # get trang web về
# page = urllib.request.urlopen(endpoint)

# soup = BeautifulSoup(page, 'html.parser')
# # print(': ', soup)
# # print('soup---: ', soup.find_all('div', attrs={"class": "product"}))
# for tag in soup.find_all('div', attrs={"class": "product"}):
#     if tag.a:

#         pageChildren = urllib.request.urlopen(
#             'https://gaubongvip.com/' + tag.a['href'])
#         soupChildren = BeautifulSoup(pageChildren, 'html.parser')
#         for tagchildren in soupChildren.find_all('div', attrs={"class": "ghichungan tab-content"}):
#             discription = tagchildren.string.strip()
#     else:
#         discription = 'no discription'

#     data.append(
#         {
#             'name':  tag.h3.a.string if tag.h3.a else 'no name',
#             'image': 'https://gaubongvip.com/' + tag.img['src'] if tag.img else 'no image',
#             'discription': discription,
#             'type': 'no type',
#             'color': 'no color',
#             'size': 'no size',
#             'material': 'no material',
#             'amount_sold': 82,
#             'price': 'LIÊN HỆ',

#         }
#     )
# print(
#     {
#         'name':  tag.h3.a.string if tag.h3.a else 'no name',
#         'image': 'https://gaubongvip.com/' + tag.img['src'] if tag.img else 'no image',
#         'discription': discription,
#         'type': 'no type',
#         'color': 'no color',
#         'size': 'no size',
#         'material': 'no material',
#         'amount_sold': 82,
#         'price': 'LIÊN HỆ',

#     }
# )
# if tag.img:
#     print(
#         {
#             'name': tag.h3.a.string,
#             'image': tag.img['src']
#         }
#     )
#     # print(tag.img['alt'], tag.img['src'], tag.h3.a.string)
# else:
#     print("----- no:", tag.getText())


# endpoint = 'http://127.0.0.1:8000/danh-muc/movies/?genre=tam-ly'

# get_movieCountry = requests.get(endpoint)

# print(get_movieCountry.text)
# print(get_movieCountry.json())


# {
#         id: 1,
#         name: 'HEO ĐEO TIM NGỒI',
#         discription:
#             'Dáng lợn ngồi, béo, mặt ngộ nghĩnh. Bên ngoài là chất nhung siêu mềm mịn, đàn hồi và mát tay. Bên trong là 100% bông trắng loại 1, mềm êm làm cho người ôm cảm giác rất thích thú. Kích thước tính từ đầu đến hết mông.',
#         icon: images.heoDeoTimNgoi,
#         link: '/',
#         rating: 255,
#         price: 'LIÊN HỆ',
#     },

# a = [

#     {
#         'name': 'Gối ôm thú mềm',
#         'image': 'https://scontent.fhan3-5.fna.fbcdn.net/v/t39.30808-6/306562938_3269762353293969_5061079386813182437_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=VGy_j7yTXbEAX9pIfwT&_nc_ht=scontent.fhan3-5.fna&oh=00_AT_YEmXIDaxhvzim8CKJNgoWpOAZQyJrZILwnKUaoPIHXg&oe=634EEA63',
#         'discription': 'Gối ôm hình thú với kiểu dáng thuôn dài, chất nhung bên ngoài siêu mềm mịn kết hợp với chất bông đàn hồi cực kì an toàn là sự lựa chọn lí tưởng cho giấc ngủ của bạn. Đặc biệt gối ôm có nhiều hình, kiểu dáng, màu sắc đa dạng cho bạn thỏa sức lựa chọn',
#         'type': 'no type',
#         'color': 'no color',
#         'size': 'no size',
#         'material': 'no material',
#         'amount_sold': 82,
#         'price': 'LIÊN HỆ'
#     },
#     {
#         'name': 'Trâu nằm',
#         'image': 'https://gaubongvip.com/data/Product/gau-bong-trau-nam_1615105404.jpg',
#         'discription': 'Dáng thuôn dài, dễ ôm. Có thể sử dụng để làm gối ôm, gối đầu, gác chân. Bên ngoài là chất nhung mềm mịn, bên trong là 100% bông trắng đàn hồi',
#         'type': 'no type',
#         'color': 'no color',
#         'size': 'no size',
#         'material': 'no material',
#         'amount_sold': 82,
#         'price': 'LIÊN HỆ'
#     },
#     {
#         'name': 'Lợn đeo tim ngồi',
#         'image': 'https://scontent.fhan3-4.fna.fbcdn.net/v/t39.30808-6/311828958_3294784657458405_7525564996645306649_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=0qXZSdNqHOcAX8GFrMz&_nc_ht=scontent.fhan3-4.fna&oh=00_AT-7VvuDCPyig6ecrR_7xAAOoFkBc6NPVWBYmJBXfndf6Q&oe=6350942B',
#         'discription': 'Dáng lợn ngồi, béo, mặt ngộ nghĩnh. Bên ngoài là chất nhung siêu mềm mịn, đàn hồi và mát tay. Bên trong là 100% bông trắng loại 1, mềm êm làm cho người ôm cảm giác rất thích thú. Kích thước tính từ đầu đến hết mông.',
#         'type': 'no type',
#         'color': 'no color',
#         'size': 'no size',
#         'material': 'no material',
#         'amount_sold': 82,
#         'price': 'LIÊN HỆ'
#     },
#     {
#         'name': 'Lợn mắt hồng bông mềm',
#         'image': 'https://scontent.fhan3-2.fna.fbcdn.net/v/t39.30808-6/310433321_3286723981597806_2569179693551752498_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=LTd8gCGQGYoAX9nu67w&_nc_oc=AQkABN0Bhazi6-uG8wEqHntJBOMysNL5esQPdL1KMs06DG4JVoVtDP2k-vvKwmyrU73muDTxqFMM2zjD4YJNNJGo&_nc_ht=scontent.fhan3-2.fna&oh=00_AT9UEz-vYessTc2s0m5YWU5XUQe5Z29lIZnd7QjSah4ueA&oe=634FA705',
#         'discription': 'Chất nhung mềm mịn, không xù, không rụng, đặc biệt rất an toàn và thích hợp cho mọi lứa tuổi.',
#         'type': 'no type',
#         'color': 'no color',
#         'size': 'no size',
#         'material': 'no material',
#         'amount_sold': 82,
#         'price': 'LIÊN HỆ'
#     },
#     {
#         'name': 'Lợn nằm mềm',
#         'image': 'https://scontent.fhan4-2.fna.fbcdn.net/v/t39.30808-6/311784680_3294784170791787_2828136563224666755_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=AdFmf6_0VJUAX-GrTqR&tn=6CPhYCWUAXTxwr8S&_nc_ht=scontent.fhan4-2.fna&oh=00_AT9TdcyMHJjzRlqz_Y399ksSKTQ7I6gajRPpPhM93GI8JQ&oe=635099B6',
#         'discription': 'Thiết kế thuôn dài. Có thể sử dụng làm gối ôm, gác chân, tựa lưng, gối đầu đều rất tuyệt vời với chất nhung mềm mịn, mát tay và 100% bông trắng cao cấp',
#         'type': 'no type',
#         'color': 'no color',
#         'size': 'no size',
#         'material': 'no material',
#         'amount_sold': 82,
#         'price': 'LIÊN HỆ'
#     },
#     {
#         'name': 'Gấu Teddy thêu Love',
#         'image': 'https://scontent.fhan4-3.fna.fbcdn.net/v/t1.6435-9/109520282_2789852171301718_1893586834733365853_n.jpg?stp=dst-jpg_s960x960&_nc_cat=100&ccb=1-7&_nc_sid=0debeb&_nc_ohc=V6bJAMw3DoYAX-RxcL7&_nc_ht=scontent.fhan4-3.fna&oh=00_AT_yRE769xpsmX9lataNVWP3GA8rKqXPMOcU0y38aiSBVg&oe=63724473',
#         'discription': 'Lông ngắn siêu mềm mượt, dày và không rụng nên ôm cực thích. Hàng nhập khẩu cao cấp nên gấu rất cân đối, cái miệng cười xinh và đôi má ửng hồng. Trông gấu rất có hồn khác hẳn với gấu hàng chợ. Chiếc áo len dày dặn có thể dễ dàng cởi để giặt. Kích thước gấu là chiều cao từ đầu đến chân khi gấu đứng (ko phải kích thước khổ vải)',
#         'type': 'no type',
#         'color': 'no color',
#         'size': 'no size',
#         'material': 'no material',
#         'amount_sold': 82,
#         'price': 'LIÊN HỆ'
#     },

#     {
#         'name': 'Gối cổ chữ U hình thú',
#         'image': 'https://scontent.fhan3-5.fna.fbcdn.net/v/t39.30808-6/300585281_3253091798294358_4613431842630728764_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=9ebGCs6AgAUAX-g13Lp&tn=6CPhYCWUAXTxwr8S&_nc_ht=scontent.fhan3-5.fna&oh=00_AT_DkYLfzcoQf2uMo6Dv0L4oQDEJ41lADCjvT_mRkMY3fA&oe=634EE4C3',
#         'discription': 'Hàng cao cấp. Bên ngoài là lớp nhung siêu mềm mịn. Bên trong là 100% cao su non nên đàn hồi cực tốt, không lo bị xẹp. Đặc biệt là không bị nóng khi dùng. Gối được trang bị khoá kéo tiện dụng, dễ dàng kéo khoá ra để thay giặt vỏ. Đặc biệt là có tặng kèm bịt mắt hình thú xinh xắn',
#         'type': 'no type',
#         'color': 'no color',
#         'size': 'no size',
#         'material': 'no material',
#         'amount_sold': 82,
#         'price': 'LIÊN HỆ'
#     },

#     {
#         'name': 'Mèo Doremon',
#         'image': 'https://scontent.fhan4-3.fna.fbcdn.net/v/t1.6435-9/108005845_2789850787968523_744321982350208420_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=0debeb&_nc_ohc=XPSJ_o25uFYAX-_J62A&tn=6CPhYCWUAXTxwr8S&_nc_ht=scontent.fhan4-3.fna&oh=00_AT9P-AIwCulzdNwIL-SmeWM4seY-f4oQherv6nVKPD6FNQ&oe=636FD990',
#         'discription': 'Doremon dáng ngồi, kích thước trên tính cả chân (ko tính chân giảm 10-20cm)',
#         'type': 'no type',
#         'color': 'no color',
#         'size': 'no size',
#         'material': 'no material',
#         'amount_sold': 82,
#         'price': 'LIÊN HỆ'
#     },
#     {
#         'name': 'Thỏ hồng ôm bình sữa',
#         'image': 'https://scontent.fhan4-2.fna.fbcdn.net/v/t39.30808-6/310350201_3286723141597890_9030491314550871911_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=v4Pq_cDWnaUAX9I0ewx&tn=6CPhYCWUAXTxwr8S&_nc_ht=scontent.fhan4-2.fna&oh=00_AT8Ll3poeRWE9yTg1ZO4JdZu368Uo_8DFL2TFdqFKh9gNg&oe=63504D1C',
#         'discription': 'Chất nhung mềm mịn, mắt nhắm dạng thêu (ko sợ bé cắn), váy ren liền thân xinh xắn',
#         'type': 'no type',
#         'color': 'no color',
#         'size': 'no size',
#         'material': 'no material',
#         'amount_sold': 82,
#         'price': 'LIÊN HỆ'
#     },

#     {
#         'name': 'Khủng long nằm',
#         'image': 'https://scontent.fhan3-1.fna.fbcdn.net/v/t39.30808-6/305083416_3267890793481125_1067960947164314841_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=m4FOlYIHFLoAX__1vZx&_nc_ht=scontent.fhan3-1.fna&oh=00_AT_wPR6DoLJOsH1RCtAR3YtxpguTWexLBoRiHK-2cMXnrw&oe=634FD71B',
#         'discription': 'Khủng long thêu love với thiết kế thuôn dài và cái bụng bự rất thích hợp để ôm, gác chân. Giấc ngủ của bạn sẽ ngon hơn khi có một em ý bên cạnh. Gaubongvip có đầy đủ các size cho cả người lớn và trẻ em',
#         'type': 'no type',
#         'color': 'no color',
#         'size': 'no size',
#         'material': 'no material',
#         'amount_sold': 82,
#         'price': 'LIÊN HỆ'
#     },
#     {
#         'name': 'Gấu trúc',
#         'image': 'https://scontent.fhan3-5.fna.fbcdn.net/v/t39.30808-6/299861729_3249049082031963_1478892410190319438_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=gObPAuwxskgAX9VoeAI&_nc_ht=scontent.fhan3-5.fna&oh=00_AT-_kKC6LJVSf5pAdYiBhpddBU601iVy7jMMqwH_b1zQlQ&oe=634F7A96',
#         'discription': 'Dáng gấu nằm. Có thể sử dụng để ôm, gồi đầu, gác chân hay tựa lưng đều rất tuyệt vời. Bên ngoài là chất vải nhung siêu mềm mịn, bên trong là 100% bông trắng đàn hồi',
#         'type': 'no type',
#         'color': 'no color',
#         'size': 'no size',
#         'material': 'no material',
#         'amount_sold': 82,
#         'price': 'LIÊN HỆ'
#     },
#     {
#         'name': 'Cá  heo mềm',
#         'image': 'https://scontent.fhan3-5.fna.fbcdn.net/v/t39.30808-6/300373607_3253091921627679_5637667204062679600_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=7oi7J_UhGy8AX-RVjoS&_nc_ht=scontent.fhan3-5.fna&oh=00_AT_2ixhM13vHmgDhwrRRQ9cThUGimTDDDE1FW0aTV8m7mQ&oe=634EF175',
#         'discription': 'Nhung mịn sờ siêu thích, thiết kế đẹp mắt như chú cá heo thật',
#         'type': 'no type',
#         'color': 'no color',
#         'size': 'no size',
#         'material': 'no material',
#         'amount_sold': 82,
#         'price': 'LIÊN HỆ'
#     },

#     {
#         'name': 'Gấu Teddy logo',
#         'image': 'https://scontent.fhan4-1.fna.fbcdn.net/v/t1.6435-9/107831940_2789850941301841_853276185246424735_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=0debeb&_nc_ohc=OjGFID6aSjgAX9CnM5O&_nc_ht=scontent.fhan4-1.fna&oh=00_AT8yBN3eiev_9ftCPJFE2ho0b2XbrzVYZDEhq61B4UBFlw&oe=6371CC58',
#         'discription': 'Lông xoắn hoa hồng, chất lông dày đẹp. Màu kem sang và sáng rất hợp với những cô gái thích màu nhẹ nhàng. Gấu béo căng tròn nên ôm rất phê',
#         'type': 'no type',
#         'color': 'no color',
#         'size': 'no size',
#         'material': 'no material',
#         'amount_sold': 82,
#         'price': 'LIÊN HỆ'
#     },

#     {
#         'name': 'Gấu trúc ngồi',
#         'image': 'https://scontent.fhan3-5.fna.fbcdn.net/v/t39.30808-6/311779046_3294782017458669_4203703603442235244_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=p1FT8XQB_2IAX-gUxoA&tn=6CPhYCWUAXTxwr8S&_nc_ht=scontent.fhan3-5.fna&oh=00_AT_U2UFZrE50dLeGRXoJvS1vI2yc8f6vNaBztAMfT3dYdg&oe=634FCF66',
#         'discription': 'Dáng gấu ngồi. Chất nhung siêu mềm mịn, mát tay. Bên trong là 100% bông trắng đàn hồi, an toàn',
#         'type': 'no type',
#         'color': 'no color',
#         'size': 'no size',
#         'material': 'no material',
#         'amount_sold': 82,
#         'price': 'LIÊN HỆ'
#     },


#     {
#         'name': 'Gấu Teddy ôm tim hoa',
#         'image': 'https://gaubongvip.com/data/Product/gau-om-tim-hoa13_1536892395.jpg',
#         'discription': '',
#         'type': 'no type',
#         'color': 'no color',
#         'size': 'no size',
#         'material': 'no material',
#         'amount_sold': 82,
#         'price': 'LIÊN HỆ'
#     },
#     {
#         'name': 'Chó Shiba nằm mềm',
#         'image': 'https://scontent.fhan3-4.fna.fbcdn.net/v/t39.30808-6/310269352_3286722321597972_2846889348927833612_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=N74ajKrgHcgAX9UJT1d&_nc_ht=scontent.fhan3-4.fna&oh=00_AT8bXitnrQAntvxbK8m4nR4fTVJZ8ehM37yYiFgubZjGMQ&oe=634F2FE9',
#         'discription': 'Chó Shiba nằm mềm nhồi bông - phiên bản vô cùng hot hit dành cho những ai muốn sở hữu những em thú bông xinh xắn, cá tính kiểu dài dài, dễ ôm',
#         'type': 'no type',
#         'color': 'no color',
#         'size': 'no size',
#         'material': 'no material',
#         'amount_sold': 82,
#         'price': 'LIÊN HỆ'
#     },

#     {
#         'name': 'Chó Mặt nhăn',
#         'image': 'https://scontent.fhan4-3.fna.fbcdn.net/v/t39.30808-6/311574597_3294788667458004_5816324441010805765_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=dxrfypAcOX0AX9aeF_L&tn=6CPhYCWUAXTxwr8S&_nc_ht=scontent.fhan4-3.fna&oh=00_AT-fi3Ho9d0CKo_RTyMVDM6W4VGuD5i0W11OJ2iQtFASHQ&oe=634FAE0B',
#         'discription': 'Chó Mặt nhăn 100% nguyên liệu cao cấp, được sản xuất từ những xưởng uy tín, an toàn tuyệt đối',
#         'type': 'no type',
#         'color': 'no color',
#         'size': 'no size',
#         'material': 'no material',
#         'amount_sold': 82,
#         'price': 'LIÊN HỆ'
#     },

#     {
#         'name': 'Gối ôm chó xương',
#         'image': 'https://gaubongvip.com/data/Product/goi-om-cho-xuong-sieu-mem-2_1638022102.jpg',
#         'discription': 'Thiết kế thuôn dài rất dễ ôm. Có thể sử dụng để ôm đi ngủ, gối đầu, tựa lưng, gác chân đều rất thích. Bên ngoài là chất nhung mềm mịn, bên trong là 100% bông trắng đàn hồi siêu sạch, an toàn cho mọi người',
#         'type': 'no type',
#         'color': 'no color',
#         'size': 'no size',
#         'material': 'no material',
#         'amount_sold': 82,
#         'price': 'LIÊN HỆ'
#     },
#     {
#         'name': 'Heo bình sữa',
#         'image': 'https://scontent.fhan3-3.fna.fbcdn.net/v/t39.30808-6/309587080_3286723488264522_4581016009421712988_n.jpg?stp=cp6_dst-jpg&_nc_cat=101&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=not2296YkiYAX-lwyZR&_nc_ht=scontent.fhan3-3.fna&oh=00_AT8yziQSdM0R3E6RSWq4ZbI4Cvrm7NicdoCJ3L0EcuSuGw&oe=634F82F6',
#         'discription': 'Heo Bình Sữa được thiết kế là dáng chó ngồi với khuôn mặt béo phúng phính cực kỳ dễ thương. Bên ngoài là chất nhung mềm mịn, mát tay. Bên trong l�� 100% bông trắng đàn hồi sạch và an toàn',
#         'type': 'no type',
#         'color': 'no color',
#         'size': 'no size',
#         'material': 'no material',
#         'amount_sold': 82,
#         'price': 'LIÊN HỆ'
#     },


#     {
#         'name': 'Ngựa bông Pony',
#         'image': 'https://scontent.fhan3-5.fna.fbcdn.net/v/t39.30808-6/310673956_3286723144931223_8449603733958160284_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=XAECNMgR5lcAX-eU3zQ&tn=6CPhYCWUAXTxwr8S&_nc_ht=scontent.fhan3-5.fna&oh=00_AT9GHTOHVdrJdeYmLIdBZPTbru-YIGDwlY440ii-rbW6AA&oe=634F84D8',
#         'discription': 'Chất nhung mềm mịn, an toàn tuyệt đối cho bé',
#         'type': 'no type',
#         'color': 'no color',
#         'size': 'no size',
#         'material': 'no material',
#         'amount_sold': 82,
#         'price': 'LIÊN HỆ'
#     },
#     {
#         'name': 'Khủng long má hồng mềm',
#         'image': 'https://scontent.fhan3-5.fna.fbcdn.net/v/t39.30808-6/310086321_3286723371597867_4152918527285824124_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=lo9TfUMnOeUAX9dYZGM&_nc_ht=scontent.fhan3-5.fna&oh=00_AT84CJBUsVrNJgxsliH28xcUbP_B5v-cPGW7j7yxOgyfTQ&oe=634F851A',
#         'discription': 'Chất nhung nước siêu mềm mịn, mát tay. Bên trong là 100% bông trắng đàn hồi sạch, an toàn cho bé. Có màu xanh, hồng phù hợp cho cả bé trai và bé gái. Có 2 size cho bé lựa chọn',
#         'type': 'no type',
#         'color': 'no color',
#         'size': 'no size',
#         'material': 'no material',
#         'amount_sold': 82,
#         'price': 'LIÊN HỆ'
#     },


#     {
#         'name': 'Lợn ong nằm',
#         'image': 'https://scontent.fhan4-1.fna.fbcdn.net/v/t39.30808-6/308062778_3286721674931370_6577845416421210971_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=zmiyQjUnve4AX9paG_w&tn=6CPhYCWUAXTxwr8S&_nc_ht=scontent.fhan4-1.fna&oh=00_AT_Ji0dGHGim4LuuOcD0E6r1iTDEJo5dQlbSjj2goMfWdA&oe=634F076A',
#         'discription': 'Thiết kế thuôn dài mình tròn rất dễ ôm và gác chân. Bên ngoài là chất nhung mềm mịn và mát tay; bên trong là bông trắng đàn hồi cao cấp nên lợn ong nằm này rất căng mềm và không lo bị xẹp',
#         'type': 'no type',
#         'color': 'no color',
#         'size': 'no size',
#         'material': 'no material',
#         'amount_sold': 82,
#         'price': 'LIÊN HỆ'
#     },

#     {
#         'name': 'Mèo hoàng thượng ngồi',
#         'image': 'https://scontent.fhan4-1.fna.fbcdn.net/v/t39.30808-6/305266731_3274697412800463_2059609459288610361_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=-SfWoJKqGkEAX-5mCT2&_nc_oc=AQnljIg9lHf2WrnbWiFkdm_zIjc1i2L6bpYmhk_UKfv8x4gGlhv96srSD5E_XtehM0zJ1rQL7JQyXtY6-yf0TLCF&_nc_ht=scontent.fhan4-1.fna&oh=00_AT-kq40ElQpROXFpB2pjwAk3CU0CwJDgXkBNkcwZhCmEJA&oe=634F8A8C',
#         'discription': 'Dáng gấu nằm dài. Mặt vô cùng xinh xắn. Bên ngoài là chất nhung siêu mềm mịn. Bên trong là 100% bông trắng đàn hồi nên rất căng mềm, ôm cực thích',
#         'type': 'no type',
#         'color': 'no color',
#         'size': 'no size',
#         'material': 'no material',
#         'amount_sold': 82,
#         'price': 'LIÊN HỆ'
#     },

#     {
#         'name': 'Búp bê mũ',
#         'image': 'https://gaubongvip.com/data/Product/gau-bong-bup-be-mu-7_1515245656.jpg',
#         'discription': 'Chất nhung mềm mịn, an toàn cho bé',
#         'type': 'no type',
#         'color': 'no color',
#         'size': 'no size',
#         'material': 'no material',
#         'amount_sold': 82,
#         'price': 'LIÊN HỆ'
#     },
#     {
#         'name': 'Búp bê mũ nhung',
#         'image': 'https://scontent.fhan3-3.fna.fbcdn.net/v/t1.6435-9/110163356_2789851477968454_4796020141662869875_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=0debeb&_nc_ohc=n9LoYlH2Bq4AX-WaS_V&tn=6CPhYCWUAXTxwr8S&_nc_ht=scontent.fhan3-3.fna&oh=00_AT8ABuC_2DrCQ4Mi9DrgVZV4KyCkCioM7H5-u5dG2VPV8Q&oe=6370F70A',
#         'discription': 'Búp bê mũ nhung váy thêu hoa cúc nhồi bông cực dễ thương bé nào cũng thích mẫu này nha các mẹ ah',
#         'type': 'no type',
#         'color': 'no color',
#         'size': 'no size',
#         'material': 'no material',
#         'amount_sold': 82,
#         'price': 'LIÊN HỆ'
#     },

# ]
