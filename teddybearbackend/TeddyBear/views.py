from rest_framework import viewsets
from rest_framework import viewsets, status, permissions, generics
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializes import *


datas = [

    {
        'name': 'Gối ôm thú mềm',
        'image': 'https://scontent.fhan3-5.fna.fbcdn.net/v/t39.30808-6/306562938_3269762353293969_5061079386813182437_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=VGy_j7yTXbEAX9pIfwT&_nc_ht=scontent.fhan3-5.fna&oh=00_AT_YEmXIDaxhvzim8CKJNgoWpOAZQyJrZILwnKUaoPIHXg&oe=634EEA63',
        'discription': 'Gối ôm hình thú với kiểu dáng thuôn dài, chất nhung bên ngoài siêu mềm mịn kết hợp với chất bông đàn hồi cực kì an toàn là sự lựa chọn lí tưởng cho giấc ngủ của bạn. Đặc biệt gối ôm có nhiều hình, kiểu dáng, màu sắc đa dạng cho bạn thỏa sức lựa chọn',
        'type': 'thu bong',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Trâu nằm',
        'image': 'https://gaubongvip.com/data/Product/gau-bong-trau-nam_1615105404.jpg',
        'discription': 'Dáng thuôn dài, dễ ôm. Có thể sử dụng để làm gối ôm, gối đầu, gác chân. Bên ngoài là chất nhung mềm mịn, bên trong là 100% bông trắng đàn hồi',
        'type': 'thu bong',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Lợn đeo tim ngồi',
        'image': 'https://scontent.fhan3-4.fna.fbcdn.net/v/t39.30808-6/311828958_3294784657458405_7525564996645306649_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=0qXZSdNqHOcAX8GFrMz&_nc_ht=scontent.fhan3-4.fna&oh=00_AT-7VvuDCPyig6ecrR_7xAAOoFkBc6NPVWBYmJBXfndf6Q&oe=6350942B',
        'discription': 'Dáng lợn ngồi, béo, mặt ngộ nghĩnh. Bên ngoài là chất nhung siêu mềm mịn, đàn hồi và mát tay. Bên trong là 100% bông trắng loại 1, mềm êm làm cho người ôm cảm giác rất thích thú. Kích thước tính từ đầu đến hết mông.',
        'type': 'thu bong',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Lợn mắt hồng bông mềm',
        'image': 'https://scontent.fhan3-2.fna.fbcdn.net/v/t39.30808-6/310433321_3286723981597806_2569179693551752498_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=LTd8gCGQGYoAX9nu67w&_nc_oc=AQkABN0Bhazi6-uG8wEqHntJBOMysNL5esQPdL1KMs06DG4JVoVtDP2k-vvKwmyrU73muDTxqFMM2zjD4YJNNJGo&_nc_ht=scontent.fhan3-2.fna&oh=00_AT9UEz-vYessTc2s0m5YWU5XUQe5Z29lIZnd7QjSah4ueA&oe=634FA705',
        'discription': 'Chất nhung mềm mịn, không xù, không rụng, đặc biệt rất an toàn và thích hợp cho mọi lứa tuổi.',
        'type': 'thu bong',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Lợn nằm mềm',
        'image': 'https://scontent.fhan4-2.fna.fbcdn.net/v/t39.30808-6/311784680_3294784170791787_2828136563224666755_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=AdFmf6_0VJUAX-GrTqR&tn=6CPhYCWUAXTxwr8S&_nc_ht=scontent.fhan4-2.fna&oh=00_AT9TdcyMHJjzRlqz_Y399ksSKTQ7I6gajRPpPhM93GI8JQ&oe=635099B6',
        'discription': 'Thiết kế thuôn dài. Có thể sử dụng làm gối ôm, gác chân, tựa lưng, gối đầu đều rất tuyệt vời với chất nhung mềm mịn, mát tay và 100% bông trắng cao cấp',
        'type': 'thu bong',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Gấu Teddy thêu Love',
        'image': 'https://scontent.fhan4-3.fna.fbcdn.net/v/t1.6435-9/109520282_2789852171301718_1893586834733365853_n.jpg?stp=dst-jpg_s960x960&_nc_cat=100&ccb=1-7&_nc_sid=0debeb&_nc_ohc=V6bJAMw3DoYAX-RxcL7&_nc_ht=scontent.fhan4-3.fna&oh=00_AT_yRE769xpsmX9lataNVWP3GA8rKqXPMOcU0y38aiSBVg&oe=63724473',
        'discription': 'Lông ngắn siêu mềm mượt, dày và không rụng nên ôm cực thích. Hàng nhập khẩu cao cấp nên gấu rất cân đối, cái miệng cười xinh và đôi má ửng hồng. Trông gấu rất có hồn khác hẳn với gấu hàng chợ. Chiếc áo len dày dặn có thể dễ dàng cởi để giặt. Kích thước gấu là chiều cao từ đầu đến chân khi gấu đứng (ko phải kích thước khổ vải)',
        'type': 'gau bong',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Gấu Teddy lông đỏ',
        'image': 'https://scontent.fhan3-3.fna.fbcdn.net/v/t39.30808-6/305996146_3269765009960370_2074144184040000518_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=GC_mIHgc8sUAX_x4pnM&_nc_oc=AQlrrpL69QQ-ccT3R3x-NaC1iihj43YN-3grsBQ6awSz4QhLFOPE7PY-4ort_7zqPJVQ_g4O0ffCMtn-GVzWVPHd&tn=6CPhYCWUAXTxwr8S&_nc_ht=scontent.fhan3-3.fna&oh=00_AT8SG0EEUF79zuujEhf6dnUUCVnFfdDrcJI6eF7tbvhnKg&oe=6350CA23',
        'discription': 'Lông ngắn siêu mềm mượt, dày và không rụng nên ôm cực thích. Hàng nhập khẩu cao cấp nên gấu rất cân đối, cái miệng cười xinh và đôi má ửng hồng. Trông gấu rất có hồn khác hẳn với gấu hàng chợ. Chiếc áo len dày dặn có thể dễ dàng cởi để giặt. Kích thước gấu là chiều cao từ đầu đến chân khi gấu đứng (ko phải kích thước khổ vải)',
        'type': 'gau bong',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },

    {
        'name': 'Gối cổ chữ U hình thú',
        'image': 'https://scontent.fhan3-5.fna.fbcdn.net/v/t39.30808-6/300585281_3253091798294358_4613431842630728764_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=9ebGCs6AgAUAX-g13Lp&tn=6CPhYCWUAXTxwr8S&_nc_ht=scontent.fhan3-5.fna&oh=00_AT_DkYLfzcoQf2uMo6Dv0L4oQDEJ41lADCjvT_mRkMY3fA&oe=634EE4C3',
        'discription': 'Hàng cao cấp. Bên ngoài là lớp nhung siêu mềm mịn. Bên trong là 100% cao su non nên đàn hồi cực tốt, không lo bị xẹp. Đặc biệt là không bị nóng khi dùng. Gối được trang bị khoá kéo tiện dụng, dễ dàng kéo khoá ra để thay giặt vỏ. Đặc biệt là có tặng kèm bịt mắt hình thú xinh xắn',
        'type': 'phu kien',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },

    {
        'name': 'Mèo Doremon',
        'image': 'https://scontent.fhan4-3.fna.fbcdn.net/v/t1.6435-9/108005845_2789850787968523_744321982350208420_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=0debeb&_nc_ohc=XPSJ_o25uFYAX-_J62A&tn=6CPhYCWUAXTxwr8S&_nc_ht=scontent.fhan4-3.fna&oh=00_AT9P-AIwCulzdNwIL-SmeWM4seY-f4oQherv6nVKPD6FNQ&oe=636FD990',
        'discription': 'Doremon dáng ngồi, kích thước trên tính cả chân (ko tính chân giảm 10-20cm)',
        'type': 'hoat hinh',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Thỏ hồng ôm bình sữa',
        'image': 'https://scontent.fhan4-2.fna.fbcdn.net/v/t39.30808-6/310350201_3286723141597890_9030491314550871911_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=v4Pq_cDWnaUAX9I0ewx&tn=6CPhYCWUAXTxwr8S&_nc_ht=scontent.fhan4-2.fna&oh=00_AT8Ll3poeRWE9yTg1ZO4JdZu368Uo_8DFL2TFdqFKh9gNg&oe=63504D1C',
        'discription': 'Chất nhung mềm mịn, mắt nhắm dạng thêu (ko sợ bé cắn), váy ren liền thân xinh xắn',
        'type': 'thu bong',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Hổ vàng ôm bình sữa',
        'image': 'https://scontent.fhan3-4.fna.fbcdn.net/v/t39.30808-6/305206363_3269763279960543_2349559708535004976_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=AWjdfzvPaqMAX8W-lNd&_nc_ht=scontent.fhan3-4.fna&oh=00_AT8LTx0TNAC8YXJx0C6ITVduCc1xnkTWJSB2SDfaTYZudA&oe=6350F25B',
        'discription': 'Chất nhung mềm mịn, mắt nhắm dạng thêu (ko sợ bé cắn), váy ren liền thân xinh xắn',
        'type': 'thu bong',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },

    {
        'name': 'Khủng long nằm',
        'image': 'https://scontent.fhan3-1.fna.fbcdn.net/v/t39.30808-6/305083416_3267890793481125_1067960947164314841_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=m4FOlYIHFLoAX__1vZx&_nc_ht=scontent.fhan3-1.fna&oh=00_AT_wPR6DoLJOsH1RCtAR3YtxpguTWexLBoRiHK-2cMXnrw&oe=634FD71B',
        'discription': 'Khủng long thêu love với thiết kế thuôn dài và cái bụng bự rất thích hợp để ôm, gác chân. Giấc ngủ của bạn sẽ ngon hơn khi có một em ý bên cạnh. Gaubongvip có đầy đủ các size cho cả người lớn và trẻ em',
        'type': 'thu bong',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Gấu trúc',
        'image': 'https://scontent.fhan3-5.fna.fbcdn.net/v/t39.30808-6/299861729_3249049082031963_1478892410190319438_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=gObPAuwxskgAX9VoeAI&_nc_ht=scontent.fhan3-5.fna&oh=00_AT-_kKC6LJVSf5pAdYiBhpddBU601iVy7jMMqwH_b1zQlQ&oe=634F7A96',
        'discription': 'Dáng gấu nằm. Có thể sử dụng để ôm, gồi đầu, gác chân hay tựa lưng đều rất tuyệt vời. Bên ngoài là chất vải nhung siêu mềm mịn, bên trong là 100% bông trắng đàn hồi',
        'type': 'thu bong',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Cá  heo mềm',
        'image': 'https://scontent.fhan3-5.fna.fbcdn.net/v/t39.30808-6/300373607_3253091921627679_5637667204062679600_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=7oi7J_UhGy8AX-RVjoS&_nc_ht=scontent.fhan3-5.fna&oh=00_AT_2ixhM13vHmgDhwrRRQ9cThUGimTDDDE1FW0aTV8m7mQ&oe=634EF175',
        'discription': 'Nhung mịn sờ siêu thích, thiết kế đẹp mắt như chú cá heo thật',
        'type': 'thu bong',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },

    {
        'name': 'Gấu Teddy logo',
        'image': 'https://scontent.fhan4-1.fna.fbcdn.net/v/t1.6435-9/107831940_2789850941301841_853276185246424735_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=0debeb&_nc_ohc=OjGFID6aSjgAX9CnM5O&_nc_ht=scontent.fhan4-1.fna&oh=00_AT8yBN3eiev_9ftCPJFE2ho0b2XbrzVYZDEhq61B4UBFlw&oe=6371CC58',
        'discription': 'Lông xoắn hoa hồng, chất lông dày đẹp. Màu kem sang và sáng rất hợp với những cô gái thích màu nhẹ nhàng. Gấu béo căng tròn nên ôm rất phê',
        'type': 'gau bong',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },

    {
        'name': 'Gấu trúc ngồi',
        'image': 'https://scontent.fhan3-5.fna.fbcdn.net/v/t39.30808-6/311779046_3294782017458669_4203703603442235244_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=p1FT8XQB_2IAX-gUxoA&tn=6CPhYCWUAXTxwr8S&_nc_ht=scontent.fhan3-5.fna&oh=00_AT_U2UFZrE50dLeGRXoJvS1vI2yc8f6vNaBztAMfT3dYdg&oe=634FCF66',
        'discription': 'Dáng gấu ngồi. Chất nhung siêu mềm mịn, mát tay. Bên trong là 100% bông trắng đàn hồi, an toàn',
        'type': 'gau bong',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },


    {
        'name': 'Gấu Teddy ôm tim hoa',
        'image': 'https://gaubongvip.com/data/Product/gau-om-tim-hoa13_1536892395.jpg',
        'discription': '',
        'type': 'gau bong',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Chó Shiba nằm mềm',
        'image': 'https://scontent.fhan3-4.fna.fbcdn.net/v/t39.30808-6/310269352_3286722321597972_2846889348927833612_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=N74ajKrgHcgAX9UJT1d&_nc_ht=scontent.fhan3-4.fna&oh=00_AT8bXitnrQAntvxbK8m4nR4fTVJZ8ehM37yYiFgubZjGMQ&oe=634F2FE9',
        'discription': 'Chó Shiba nằm mềm nhồi bông - phiên bản vô cùng hot hit dành cho những ai muốn sở hữu những em thú bông xinh xắn, cá tính kiểu dài dài, dễ ôm',
        'type': 'thu bong',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },

    {
        'name': 'Chó Mặt nhăn',
        'image': 'https://scontent.fhan4-3.fna.fbcdn.net/v/t39.30808-6/311574597_3294788667458004_5816324441010805765_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=dxrfypAcOX0AX9aeF_L&tn=6CPhYCWUAXTxwr8S&_nc_ht=scontent.fhan4-3.fna&oh=00_AT-fi3Ho9d0CKo_RTyMVDM6W4VGuD5i0W11OJ2iQtFASHQ&oe=634FAE0B',
        'discription': 'Chó Mặt nhăn 100% nguyên liệu cao cấp, được sản xuất từ những xưởng uy tín, an toàn tuyệt đối',
        'type': 'thu bong',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },

    {
        'name': 'Gối ôm chó xương',
        'image': 'https://gaubongvip.com/data/Product/goi-om-cho-xuong-sieu-mem-2_1638022102.jpg',
        'discription': 'Thiết kế thuôn dài rất dễ ôm. Có thể sử dụng để ôm đi ngủ, gối đầu, tựa lưng, gác chân đều rất thích. Bên ngoài là chất nhung mềm mịn, bên trong là 100% bông trắng đàn hồi siêu sạch, an toàn cho mọi người',
        'type': 'goi om',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Heo bình sữa',
        'image': 'https://scontent.fhan3-3.fna.fbcdn.net/v/t39.30808-6/309587080_3286723488264522_4581016009421712988_n.jpg?stp=cp6_dst-jpg&_nc_cat=101&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=not2296YkiYAX-lwyZR&_nc_ht=scontent.fhan3-3.fna&oh=00_AT8yziQSdM0R3E6RSWq4ZbI4Cvrm7NicdoCJ3L0EcuSuGw&oe=634F82F6',
        'discription': 'Heo Bình Sữa được thiết kế là dáng chó ngồi với khuôn mặt béo phúng phính cực kỳ dễ thương. Bên ngoài là chất nhung mềm mịn, mát tay. Bên trong l�� 100% bông trắng đàn hồi sạch và an toàn',
        'type': 'thu bong',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },


    {
        'name': 'Ngựa bông Pony',
        'image': 'https://scontent.fhan3-5.fna.fbcdn.net/v/t39.30808-6/310673956_3286723144931223_8449603733958160284_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=XAECNMgR5lcAX-eU3zQ&tn=6CPhYCWUAXTxwr8S&_nc_ht=scontent.fhan3-5.fna&oh=00_AT9GHTOHVdrJdeYmLIdBZPTbru-YIGDwlY440ii-rbW6AA&oe=634F84D8',
        'discription': 'Chất nhung mềm mịn, an toàn tuyệt đối cho bé',
        'type': 'thu bong',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Khủng long má hồng mềm',
        'image': 'https://scontent.fhan3-5.fna.fbcdn.net/v/t39.30808-6/310086321_3286723371597867_4152918527285824124_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=lo9TfUMnOeUAX9dYZGM&_nc_ht=scontent.fhan3-5.fna&oh=00_AT84CJBUsVrNJgxsliH28xcUbP_B5v-cPGW7j7yxOgyfTQ&oe=634F851A',
        'discription': 'Chất nhung nước siêu mềm mịn, mát tay. Bên trong là 100% bông trắng đàn hồi sạch, an toàn cho bé. Có màu xanh, hồng phù hợp cho cả bé trai và bé gái. Có 2 size cho bé lựa chọn',
        'type': 'thu bong',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },


    {
        'name': 'Lợn ong nằm',
        'image': 'https://scontent.fhan4-1.fna.fbcdn.net/v/t39.30808-6/308062778_3286721674931370_6577845416421210971_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=zmiyQjUnve4AX9paG_w&tn=6CPhYCWUAXTxwr8S&_nc_ht=scontent.fhan4-1.fna&oh=00_AT_Ji0dGHGim4LuuOcD0E6r1iTDEJo5dQlbSjj2goMfWdA&oe=634F076A',
        'discription': 'Thiết kế thuôn dài mình tròn rất dễ ôm và gác chân. Bên ngoài là chất nhung mềm mịn và mát tay; bên trong là bông trắng đàn hồi cao cấp nên lợn ong nằm này rất căng mềm và không lo bị xẹp',
        'type': 'thu bong',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },

    {
        'name': 'Mèo hoàng thượng ngồi',
        'image': 'https://scontent.fhan4-1.fna.fbcdn.net/v/t39.30808-6/305266731_3274697412800463_2059609459288610361_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=-SfWoJKqGkEAX-5mCT2&_nc_oc=AQnljIg9lHf2WrnbWiFkdm_zIjc1i2L6bpYmhk_UKfv8x4gGlhv96srSD5E_XtehM0zJ1rQL7JQyXtY6-yf0TLCF&_nc_ht=scontent.fhan4-1.fna&oh=00_AT-kq40ElQpROXFpB2pjwAk3CU0CwJDgXkBNkcwZhCmEJA&oe=634F8A8C',
        'discription': 'Dáng gấu nằm dài. Mặt vô cùng xinh xắn. Bên ngoài là chất nhung siêu mềm mịn. Bên trong là 100% bông trắng đàn hồi nên rất căng mềm, ôm cực thích',
        'type': 'thu bong',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Gối ôm Mèo hoàng thượng',
        'image': 'https://scontent.fhan3-5.fna.fbcdn.net/v/t39.30808-6/305077034_3264629690473902_3578217439783016202_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=YSuMQX9OJdMAX-nmBup&_nc_ht=scontent.fhan3-5.fna&oh=00_AT_P5gsXcmxqTJKk5eHh5YFMm9jZt0J9PAk5sPcKr-4G5Q&oe=635001AA',
        'discription': 'Dáng gấu nằm dài. Mặt vô cùng xinh xắn. Bên ngoài là chất nhung siêu mềm mịn. Bên trong là 100% bông trắng đàn hồi nên rất căng mềm, ôm cực thích',
        'type': 'goi om',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Gối ôm Bò sữa',
        'image': 'https://scontent.fhan4-3.fna.fbcdn.net/v/t39.30808-6/305302000_3269763499960521_5524475521647370581_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=PNC2LYtBDI8AX_xOxJa&_nc_ht=scontent.fhan4-3.fna&oh=00_AT-iGCOsKkC_-7D63HL7eS9ZH44KUQC3vUZzkUdjEIf0Kg&oe=63503140',
        'discription': 'Dáng gấu nằm dài. Mặt vô cùng xinh xắn. Bên ngoài là chất nhung siêu mềm mịn. Bên trong là 100% bông trắng đàn hồi nên rất căng mềm, ôm cực thích',
        'type': 'goi om',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },

    {
        'name': 'Búp bê mũ',
        'image': 'https://gaubongvip.com/data/Product/gau-bong-bup-be-mu-7_1515245656.jpg',
        'discription': 'Chất nhung mềm mịn, an toàn cho bé',
        'type': 'bup be',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Búp bê mũ nhung',
        'image': 'https://scontent.fhan3-3.fna.fbcdn.net/v/t1.6435-9/110163356_2789851477968454_4796020141662869875_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=0debeb&_nc_ohc=n9LoYlH2Bq4AX-WaS_V&tn=6CPhYCWUAXTxwr8S&_nc_ht=scontent.fhan3-3.fna&oh=00_AT8ABuC_2DrCQ4Mi9DrgVZV4KyCkCioM7H5-u5dG2VPV8Q&oe=6370F70A',
        'discription': 'Búp bê mũ nhung váy thêu hoa cúc nhồi bông cực dễ thương bé nào cũng thích mẫu này nha các mẹ ah',
        'type': 'bup be',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Hoa Hồng Sáp - Mẫu 01',
        'image': 'https://scontent.fhan4-3.fna.fbcdn.net/v/t39.30808-6/309661016_3295989774004560_8437938023435769582_n.jpg?stp=cp6_dst-jpg&_nc_cat=103&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=IId51OOwAhgAX-ZX2bX&tn=6CPhYCWUAXTxwr8S&_nc_ht=scontent.fhan4-3.fna&oh=00_AT-HXO28Ztclz4Du2Q8xDI6eE1h_SsjMsGev8-uClybSSQ&oe=6350A8AE',
        'discription': 'Bó Hoa hồng Sáp, số lượng 1 bông, với hồng sáp chất lượng cao , lưu hương thơm lâu...',
        'type': 'hoa',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Hoa Hồng Sáp - Mẫu 02',
        'image': 'https://scontent.fhan3-3.fna.fbcdn.net/v/t39.30808-6/310062700_3294788684124669_1835695960781147753_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=c4U-PLTSpf0AX8vVFkf&_nc_ht=scontent.fhan3-3.fna&oh=00_AT_hyIMz__CnfG2rs5F5BN8RIdOI76tUiPwc0YFXHHf3Pw&oe=6350C01B',
        'discription': 'Bó Hoa hồng Sáp, với hồng sáp chất lượng cao , lưu hương thơm lâu...',
        'type': 'hoa',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Hoa Hồng Sáp - Mẫu 03',
        'image': 'https://scontent.fhan3-2.fna.fbcdn.net/v/t39.30808-6/309269243_3294785467458324_5004876672448171089_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=mprS20hZxskAX9hzRUY&tn=6CPhYCWUAXTxwr8S&_nc_ht=scontent.fhan3-2.fna&oh=00_AT8N8mOeSocYaiWrKLtdLy2kfWYJFSEazleOPMsMb9F8CQ&oe=6350DFCA',
        'discription': 'Bó Hoa hồng Sáp, với hồng sáp chất lượng cao , lưu hương thơm lâu...',
        'type': 'hoa',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Hoa Hồng Sáp - Mẫu 04',
        'image': 'https://scontent.fhan3-4.fna.fbcdn.net/v/t39.30808-6/311571839_3294781954125342_6612178875307413241_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=jucrQNRERJsAX-cECwq&tn=6CPhYCWUAXTxwr8S&_nc_ht=scontent.fhan3-4.fna&oh=00_AT8fKDOvTSWWPo1cptoeQmP55kL5bPi_dujoLwwp1m8x6g&oe=634F7418',
        'discription': 'Bó Hoa hồng Sáp, với hồng sáp chất lượng cao , lưu hương thơm lâu...',
        'type': 'hoa',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Hoa Hồng Sáp - Mẫu 05',
        'image': 'https://scontent.fhan3-2.fna.fbcdn.net/v/t39.30808-6/310563340_3294785524124985_4589787759549220295_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=wM8X1xgGnc8AX8Qv3I4&_nc_ht=scontent.fhan3-2.fna&oh=00_AT895qPRv0RGHvXkUj3eNi6dXrQ89y5d5n9teUabr5Z5Gg&oe=634F9031',
        'discription': 'Bó Hoa hồng Sáp, với hồng sáp chất lượng cao , lưu hương thơm lâu...',
        'type': 'hoa',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Hoa Hồng Sáp - Mẫu 06',
        'image': 'https://scontent.fhan3-4.fna.fbcdn.net/v/t39.30808-6/311331647_3294779400792264_4856180605462842026_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=xGzNELm3uwcAX_pbFHP&_nc_ht=scontent.fhan3-4.fna&oh=00_AT9BvXFPfFqyca8AcVBLHWdz-YOjbEtBGc_fKjy3zWNO1g&oe=6350C8EA',
        'discription': 'Bó Hoa hồng Sáp, với hồng sáp chất lượng cao , lưu hương thơm lâu...',
        'type': 'hoa',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Hoa Hồng Sáp - Mẫu 07',
        'image': 'https://scontent.fhan3-5.fna.fbcdn.net/v/t39.30808-6/311783183_3294779337458937_64130021722187766_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=fptxgjt1MW8AX_u1Bbw&_nc_ht=scontent.fhan3-5.fna&oh=00_AT_lvIH6Jlft5eaQy94GVi_qnXGb2HezQjrr0cn18X05vg&oe=635132EF',
        'discription': 'Bó Hoa hồng Sáp, với hồng sáp chất lượng cao , lưu hương thơm lâu...',
        'type': 'hoa',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Hoa Hồng Sáp - Mẫu 08',
        'image': 'https://scontent.fhan3-2.fna.fbcdn.net/v/t39.30808-6/311836909_3294779327458938_974965823998065754_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=MafjLeU0n-YAX85KmAZ&_nc_ht=scontent.fhan3-2.fna&oh=00_AT9iuXzGoCfunZESujiQdE0QSM69DT7M4NnbAFzyVge2Jw&oe=634F62A3',
        'discription': 'Bó Hoa hồng Sáp, với hồng sáp chất lượng cao , lưu hương thơm lâu...',
        'type': 'hoa',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Hoa Hồng Sáp - Mẫu 09',
        'image': 'https://scontent.fhan3-1.fna.fbcdn.net/v/t39.30808-6/309629112_3293987767538094_8877556291930346420_n.jpg?stp=cp6_dst-jpg&_nc_cat=102&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=bQBRYZpZc0UAX_8gOBX&_nc_ht=scontent.fhan3-1.fna&oh=00_AT9MqA7Xtvo3Rjl8N7zDhy-Yx5gjrfEfgUXPUpGnLNlOgg&oe=6350B9BC',
        'discription': 'Bó Hoa hồng Sáp, với hồng sáp chất lượng cao , lưu hương thơm lâu...',
        'type': 'hoa',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Hoa Hồng Sáp - Mẫu 10',
        'image': 'https://scontent.fhan3-2.fna.fbcdn.net/v/t39.30808-6/310055762_3286724041597800_4196645727697580784_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=Bq8JL3yzUmYAX-H_RTA&_nc_ht=scontent.fhan3-2.fna&oh=00_AT9edAcUkhaTU2-sfaZh7frtbbtnrhNvdnZQU_p9MAEB0Q&oe=634FE476',
        'discription': 'Bó Hoa hồng Sáp, có kết hợp với đèn nháy tạo điểm nhấn, với hồng sáp chất lượng cao , lưu hương thơm lâu...',
        'type': 'hoa',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Hoa Hồng Sáp + Hoa tiền - Mẫu 11',
        'image': 'https://scontent.fhan3-3.fna.fbcdn.net/v/t39.30808-6/309990549_3294785547458316_3938868023304381927_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=TFO6wV9TKEYAX-XkGSz&tn=6CPhYCWUAXTxwr8S&_nc_ht=scontent.fhan3-3.fna&oh=00_AT9mFCqpLMMqtz7NrzLFvMRg8CF4PuliGrP6Gmz3e7FvTw&oe=6350B3D3',
        'discription': 'Bó Hoa hồng Sáp, với hồng sáp chất lượng cao , lưu hương thơm lâu...',
        'type': 'hoa',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Hoa tiền - Mẫu 01',
        'image': 'https://scontent.fhan3-4.fna.fbcdn.net/v/t39.30808-6/311589557_3294788764124661_1529201832491416299_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=t9zSQ9T0lG8AX_NsX9u&_nc_ht=scontent.fhan3-4.fna&oh=00_AT80PdoLMXKB_Sj6EBOo8vGyxbPFiRv6GY4k0cuzP3osvw&oe=634FDC38',
        'discription': 'Bó hoa được kết hợp từ những đồng tiền có mệnh giá theo yêu cầu, là kết hợp của sự lãng mạng và sự khẳng định đẳng cấp',
        'type': 'hoa',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Hoa tiền - Mẫu 02',
        'image': 'https://scontent.fhan4-1.fna.fbcdn.net/v/t39.30808-6/311787058_3294782447458626_7586662479947345746_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=FIa_oCJHuTYAX9aXduW&_nc_ht=scontent.fhan4-1.fna&oh=00_AT_rheRWwS2u32JuQs9SByNHNFJyHW02VCTFjjiByASvdA&oe=634FC5A1',
        'discription': 'Bó hoa được kết hợp từ những đồng tiền có mệnh giá theo yêu cầu, là kết hợp của sự lãng mạng và sự khẳng định đẳng cấp',
        'type': 'hoa',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Hoa tiền + Hồng sáp - Mẫu 03',
        'image': 'https://scontent.fhan3-1.fna.fbcdn.net/v/t39.30808-6/311696968_3294781774125360_7112578379977047903_n.jpg?stp=cp6_dst-jpg&_nc_cat=102&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=YjBk71iroCcAX9-KW9H&_nc_ht=scontent.fhan3-1.fna&oh=00_AT-x1ktTZwQx3s-BHMVaxjXlab2oADd5qAms94MdQcY0fg&oe=635103E8',
        'discription': 'Bó hoa được kết hợp từ những đồng tiền có mệnh giá theo yêu cầu, là kết hợp của sự lãng mạng và sự khẳng định đẳng cấp',
        'type': 'hoa',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },
    {
        'name': 'Hoa tiền - Mẫu 04',
        'image': 'https://scontent.fhan3-3.fna.fbcdn.net/v/t39.30808-6/310012489_3292451077691763_4592956106873852491_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=P7a_RBqF5y0AX8NN0UE&_nc_ht=scontent.fhan3-3.fna&oh=00_AT8Y5waIRFWz5s5o4DzjdLkXVkOs59Y74gC0nnk8Vj5mXw&oe=63505704',
        'discription': 'Bó hoa được kết hợp từ những đồng tiền có mệnh giá theo yêu cầu, là kết hợp của sự lãng mạng và sự khẳng định đẳng cấp',
        'type': 'hoa',
        'color': 'no color',
        'size': 'no size',
        'material': 'no material',
        'amount_sold': 82,
        'price': 'LIÊN HỆ'
    },



]

# phan trang


class PageSize24Pagiration(PageNumberPagination):
    page_size = 24


class PageSize10Pagiration(PageNumberPagination):
    page_size = 10


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Products.objects.filter(active=True)
    serializer_class = ProductSerialize


class NewProductViewSet(viewsets.ModelViewSet):

    queryset = Products.objects.filter(active=True)
    queryset = queryset.order_by('-create_date')
    serializer_class = ProductSerialize
    pagination_class = PageSize10Pagiration


class GauBongViewSet(viewsets.ModelViewSet):

    queryset = Products.objects.filter(active=True, category=1)
    serializer_class = ProductSerialize
    pagination_class = PageSize24Pagiration


class ThuBongViewSet(viewsets.ModelViewSet):

    queryset = Products.objects.filter(active=True, category=2)
    serializer_class = ProductSerialize
    pagination_class = PageSize24Pagiration


class GoiBongViewSet(viewsets.ModelViewSet):

    queryset = Products.objects.filter(active=True, category=3)
    serializer_class = ProductSerialize
    pagination_class = PageSize24Pagiration


class GauBongHoatHinhViewSet(viewsets.ModelViewSet):

    queryset = Products.objects.filter(active=True, category=4)
    serializer_class = ProductSerialize
    pagination_class = PageSize24Pagiration


class BupBeViewSet(viewsets.ModelViewSet):

    queryset = Products.objects.filter(active=True, category=5)
    serializer_class = ProductSerialize
    pagination_class = PageSize24Pagiration


class HoaViewSet(viewsets.ModelViewSet):

    queryset = Products.objects.filter(active=True, category=6)
    serializer_class = ProductSerialize
    pagination_class = PageSize24Pagiration


class PhuKienViewSet(viewsets.ModelViewSet):

    queryset = Products.objects.filter(active=True, category=7)
    serializer_class = ProductSerialize
    pagination_class = PageSize24Pagiration


class HopQuaViewSet(viewsets.ModelViewSet):

    queryset = Products.objects.filter(active=True, category=8)
    serializer_class = ProductSerialize
    pagination_class = PageSize24Pagiration


class TeddyBearHotViewSet(viewsets.ModelViewSet):

    queryset = Products.objects.filter(active=True, category='1')
    queryset = queryset.order_by('-amount_sold')
    serializer_class = ProductSerialize
    pagination_class = PageSize10Pagiration


class BouquetHotViewSet(viewsets.ModelViewSet):

    queryset = Products.objects.filter(active=True, type='hoa')
    queryset = queryset.order_by('-amount_sold')
    serializer_class = ProductSerialize
    pagination_class = PageSize10Pagiration


class GiftBoxHotViewSet(viewsets.ModelViewSet):

    queryset = Products.objects.filter(active=True, type='hop qua')
    queryset = queryset.order_by('-amount_sold')
    serializer_class = ProductSerialize
    pagination_class = PageSize10Pagiration

    # def index(request):
    #     for data in datas:
    #         if data['type'] == 'gau bong':
    #             c = Category.objects.get(name='Gấu Bông')
    #         elif data['type'] == 'thu bong':
    #             c = Category.objects.get(name='Thú Bông')
    #         elif data['type'] == 'hoat hinh':
    #             c = Category.objects.get(name='Gấu Bông Hoạt Hình')
    #         elif data['type'] == 'goi om':
    #             c = Category.objects.get(name='Gối Bông')
    #         elif data['type'] == 'bup be':
    #             c = Category.objects.get(name='Búp Bê')
    #         elif data['type'] == 'hoa':
    #             c = Category.objects.get(name='Hoa')
    #         elif data['type'] == 'phu kien':
    #             c = Category.objects.get(name='Phụ Kiện')
    #         else:
    #             c = ''

    #         Products.objects.get_or_create(name=data['name'], image=data['image'], discription=data['discription'],
    #                                        type=data['type'], price=data['price'], amount_sold=data['amount_sold'], category=c)
    #     return render(request, template_name='index.html', context={
    #         'name': 'tạo database xong'
    #     })


def index(request):
    for data in datas:
        pass
    return render(request, template_name='index.html', context={
        'name': datas
    })

# Create your views here.
