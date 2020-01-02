import FASPell

sentence = ['相关附件真实、淮确、合法有效','因此产生的法律后果由中方全权承担',
            '昌方如需向乙方申请','乙方有权根所法律法规及相关监管规定政策等的变化',
            '乙方仅是甲方与受让方之问的信息传递媒介','由甲方与相关爱让方通过签订相'
                                  '关债权资产转让协议等文件完成债权资产的转让',
            '在乙方宫网展示债权转让信息页面时乙方有权要求甲方向投资者明示投资风险',
            '乙方不子王涉亦不承担任何责任','甲方不得利用乙方提供的债权资产服务做任何误导性和/或虚俱性的描述',
            '床对投资者进行适当性管理']

result = FASPell.correct(sentence)

for i, s in enumerate(result):
    print(f'【{i}】{s}')