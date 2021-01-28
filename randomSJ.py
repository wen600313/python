#! python3
# randomSJ.py
# random order,along with the answer key.

import random

# 键是省名称，值是省会
shenghui ={'北京市':'北京','上海市':'上海','天津市':'天津',\
'重庆市':'重庆','黑龙江省':'哈尔滨','吉林省':'长春','辽宁省':'沈阳',\
'内蒙古':'呼和浩特','河北省':'石家庄','新疆':'乌鲁木齐',\
'甘肃省':'兰州','青海省':'西宁','陕西省':'西安','宁夏':'银川',\
'河南省':'郑州','山东省':'济南','山西省':'太原','安徽省':'合肥',\
'湖北省':'武汉','湖南省':'长沙','江苏省':'南京','四川省':'成都',\
'贵州省':'贵阳','云南省':'昆明','广西省':'南宁','西藏':'拉萨',\
'浙江省':'杭州','江西省':'南昌','广东省':'广州','福建省':'福州',\
'台湾省':'台北','海南省':'海口','香港':'香港','澳门':'澳门'}

#随机安排35个问题和答案的次序

for quizNum in range(35):
	#创建测验和答案文件
	quizFile = open('shijuan%s.txt' % (quizNum + 1),'w',encoding='UTF-8')
	answerKeyFile = open('shijuan_answer%s.txt' % (quizNum + 1),'w',encoding='UTF-8')
	
	#写出测验的标题
	quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quizFile.write((' ' * 20) + '省会测验 (From %s)' % (quizNum + 1))
	quizFile.write('\n\n')
	
	#把各省的顺序打乱
	shengMing = list(shenghui.keys())
	random.shuffle(shengMing)
	
	#遍历47个省份，给每个人提一个问题
	for questionNum in range(34):
		#得到正确和错误的答案
		correctAnswer = shenghui[shengMing[questionNum]]
		wrongAnswers = list(shenghui.values())
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		wrongAnswers = random.sample(wrongAnswers,3)
		answerOptions = wrongAnswers + [correctAnswer]
		random.shuffle(answerOptions)
		
		#把问题和答案选项写进测验文件
		quizFile.write('%s.%s的省会在哪里?\n' % (questionNum + 1,\
		shengMing[questionNum]))
		for i in range(4):
			quizFile.write(' %s. %s\n' % ('ABCD'[i],answerOptions[i]))
		quizFile.write('\n')
		
		#在文件中写入答案的键
		answerKeyFile.write('%s. %s\n' % (questionNum + 1,'ABCD'[\
		answerOptions.index(correctAnswer)]))
	quizFile.close()
	answerKeyFile.close()
