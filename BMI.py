# 體重（公斤）身高（公尺）
height= input ('請輸入身高(m): ')
height= float (height)
weight= input ('請輸入體重(kg)：')
weight= float (weight)
bmi= weight / (height * 2)
bmi= float (bmi)
if bmi <= 18.5: 
    print ('您的BMI值為：', bmi, '屬體重過輕')
elif bmi >= 18.5 and bmi < 24:
	print ('您的BMI值為：', bmi, '屬正常範圍')
elif bmi >= 24 and bmi < 27:
	print ('您的BMI值為：', bmi, '屬體重過重')
elif bmi >= 27 and bmi < 30:
	print('您的BMI值為：', bmi, '屬輕度肥胖')
elif bmi >= 30 and bmi <  35:
	print ('您的BMI值為：', bmi, '屬中度肥胖')
else:
	print('您的BMI值為：', bmi, '屬重度肥胖')