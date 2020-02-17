"""
对于每个录入的分数
判定其等级
"""

score = float(input("请录入学生的分数:"))
if score >= 90:
    grade = "A"
elif score > 80 and score <= 90:
    grade = "B"
elif score > 70 and score <= 80:
    grade = "C"
elif score > 60 and score <= 70:
    grade = "D"
elif score > 0 and score <= 60:
    grade = "E"
else:
    grade = "您输入的分数需要在0-100之间"
print("该学生的等级是: %s"%(grade))