text = '''Những làn sương mờ ảo vẫn còn phảng phất, bình minh vừa hé. Đột ngột tiếng gà gáy vang, phá tan sự yên tĩnh, mọi vật bừng tỉnh giấc. Đó là tiếng gáy của bạn gà trống nòi nhà em.
Con gà trống tía nhà em khoảng ba ký. Nhìn nó thật oai vệ. Cả thân hình trùm lên một bộ lông màu đot tía xen kẽ với màu xanh đen bóng mượt. Om sát đầu có mào đỏ thắm như trông thấy chú càng khỏe hơn. Hai con mắt tròn xoe nhìn qua nhìn lại trông chú rất lanh lợi. Cái mỏ chú nhỏ nhưng rất cứng. Cái đuôi nhỏ nhưng những lông đuôi dài và cong về phía sau, làm tôn thêm vẻ oai phong của chú. Mỗi lần chú đứng gáy, cổ chú vươn ra làm cho lớp da ở cổ căng ra đỏ như máu, đôi cánh xòe ra vỗ phành phạch “ ò ó o…”. Hai cái chân như hai thanh thép,được bọc bằng lớp sừng màu vàng đồng óng xếp lại.
Cách từ bàn chân lên phía trên là hai cái cựa chòi ra như hai mũi dao. Cũng chính nhờ cái cựa này mà chú đã chiến thắng đối phương rất nhiều trận.
Em rất quý bạn gà trống. Chú là chiếc đồng hồ báo thức chính xác nhất vào buổi sáng sớm đi làm của mọi người và đánh thức mình thức dậy để đi học đúng giờ.'''

dictionary= {}

for word in text_list:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1
print(dictionary['chú'])