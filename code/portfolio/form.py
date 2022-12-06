from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class CreateUserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()


class PictureForm(forms.Form):
    # label01 = '1. When faced with a major financial decision, are you more concerned about the possible losses or the possible gains?'
    label01 = "1. 當面臨一個重大的財務決定時，你更加關心的是可能損失還是可能收益？"
    # label02 = '2. Investments can go up and down in value, and experts often say you should be prepared to weather a downturn. By how much could the total value of all your investments go down before you would begin to feel uncomfortable?'
    label02 = "2. 投資的市值有高有低，專家們經常說，你應該對經濟下滑做好準備。當你的所有投資的總價值下降多少時，你會開始感到不舒服？"
    # label03 = '3. In addition to whatever you own, you have been given $1,000. You are now asked to choose between:'
    label03 = "3. 你在意外時獲得1000元，請你在以下問題做出選擇"
    # label04 = '4. In addition to whatever you own, you have been given $2,000. You are now asked to choose between:'
    label04 = "4. 你在意外時獲得2000元，請你在以下問題做出選擇"
    # label05 = '5. After the stock market declines significantly, what do you typically do?'
    label05 = "5. 在股市大幅下跌後，你通常會怎麽做？"
    # label06 = '6. Suppose you have saved $500,000 for retirement in a diversified stock portfolio. By what percentage could the total value of your retirement assets drop before you would begin to think about selling your investments and going to cash?'
    label06 = "6. 假設你為了退休基金，在一個多元化的股票投資組合中儲蓄了50萬元。在你的退休資產總價值下降多少比例時，你會開始考慮出售你的投資並轉為現金？"
    # label07 = '7. What degree of risk have you taken with your financial decisions in the past?'
    label07 = "7. 你曾經冒了多大程度的風險在財務決策上？"
    # label08 = '8. What degree of risk are you currently prepared to take with your financial decisions?'
    label08 = "8. 你現在冒了多大程度的風險在財務決策上？"
    # label09 = '9. What degree of risk have you assumed on your investments in the past?'
    label09 = "9. 你過去在投資當中承擔了多大程度的風險？"
    # label10 = '10. How do you usually feel about your major financial decisions after you make them?'
    label10 = "10. 在你做出重大的財務決策後，你對這些決策有什麽想法？"
    # label11 = '11. If you had to invest $500,000 for retirement, which of the following'
    label11 = "11. 如果你必須為退休基金投資50萬元，你會選擇以下哪項投資？"
    # label12 = '12. Compared to others, how would you rate your willingness to take financial risks?'
    label12 = "12. 與其他人相比，你如何評估本身承擔風險之意願？"

    CHOICES01 = [
        (0, "總是會考慮損失的可能性"),
        (0.33, "通常會考慮損失的可能性"),
        (0.66, "通常會考慮收益的可能性"),
        (1, "總是會考慮收益的可能性"),
    ]

    CHOICES02 = [
        (0, "任何形式的投資總值下降都將使我感到不舒服"),
        (0.2, "10%"),
        (0.4, "20%"),
        (0.6, "33%"),
        (0.8, "50%"),
        (1, "超過50%"),
    ]

    CHOICES03 = [
        (0, "保證獲得500元"),
        (1, "有50%的概率獲得1000元，但有50%的概率啥都沒有"),
    ]

    CHOICES04 = [
        (0, "保證獲得500元"),
        (1, "有50%的概率獲得1000元，但有50%的概率啥都沒有"),
    ]

    CHOICES05 = [
        (0, "我通常會買低風險的投資標的"),
        (0.33, "我總是會買低風險的投資標的"),
        (0.66, "我總是會買高風險的投資標的"),
        (1, "我通常會買高風險的投資標的"),
    ]

    CHOICES06 = [
        (0, "當退休總資產價值下降10%時"),
        (0.25, "當退休總資產價值下降20%時"),
        (0.5, "當退休總資產價值下降30%時"),
        (0.75, "當退休總資產價值下降40%時"),
        (1, "當退休總資產價值下降50%時"),
    ]

    CHOICES07 = [
        (0, "非常小"),
        (0.25, "小的"),
        (0.5, "普通"),
        (0.75, "大的"),
        (1, "非常大"),
    ]

    CHOICES08 = [
        (0, "非常小"),
        (0.25, "小的"),
        (0.5, "普通"),
        (0.75, "大的"),
        (1, "非常大"),
    ]

    CHOICES09 = [
        (0, "非常小"),
        (0.25, "小的"),
        (0.5, "普通"),
        (0.75, "大的"),
        (1, "非常大"),
    ]

    CHOICES10 = [
        (0, "我對於我所做的決策感到非常悲觀"),
        (0.33, "我對於我所做的決策感到部分悲觀"),
        (0.66, "我對於我所做的決策感到部分樂觀"),
        (1, "我對於我所做的決策感到非常樂觀"),
    ]

    CHOICES11 = [
        (0, "70%低風險、30%中風險以及0%高風險投資"),
        (0.33, "50%低風險、20%中風險以及30%高風險投資"),
        (0.66, "30%低風險、20%中風險以及50%高風險投資"),
        (1, "0%低風險、30%中風險以及70%高風險投資"),
    ]

    CHOICES12 = [
        (0, "我屬於極度低風險承擔人"),
        (0.1666, "我屬於非常低風險承擔人"),
        (0.3332, "我屬於低風險承擔人"),
        (0.4998, "我屬於普遍風險承擔人"),
        (0.6664, "我屬於高風險承擔人"),
        (0.833, "我屬於非常高風險承擔人"),
        (0.9996, "我屬於極度高風險承擔人"),
    ]

    question01 = forms.ChoiceField(
        choices=CHOICES01, widget=forms.RadioSelect, label=label01
    )
    question02 = forms.ChoiceField(
        choices=CHOICES02, widget=forms.RadioSelect, label=label02
    )
    question03 = forms.ChoiceField(
        choices=CHOICES03, widget=forms.RadioSelect, label=label03
    )
    question04 = forms.ChoiceField(
        choices=CHOICES04, widget=forms.RadioSelect, label=label04
    )
    question05 = forms.ChoiceField(
        choices=CHOICES05, widget=forms.RadioSelect, label=label05
    )
    question06 = forms.ChoiceField(
        choices=CHOICES06, widget=forms.RadioSelect, label=label06
    )
    question07 = forms.ChoiceField(
        choices=CHOICES07, widget=forms.RadioSelect, label=label07
    )
    question08 = forms.ChoiceField(
        choices=CHOICES08, widget=forms.RadioSelect, label=label08
    )
    question09 = forms.ChoiceField(
        choices=CHOICES09, widget=forms.RadioSelect, label=label09
    )
    question10 = forms.ChoiceField(
        choices=CHOICES10, widget=forms.RadioSelect, label=label10
    )
    question11 = forms.ChoiceField(
        choices=CHOICES11, widget=forms.RadioSelect, label=label11
    )
    question12 = forms.ChoiceField(
        choices=CHOICES12, widget=forms.RadioSelect, label=label12
    )
    amount = forms.FloatField(min_value=0.0, label="請輸入您想投資的金額")


class CalculationForm(forms.Form):
    CHOICES = [
        (1, "Mean-Variance model: 均異模型"),
        (2, "Conditional Value at Risk model: 條件風險值模型"),
        (3, "Omega ratio model: Omega比率模型"),
    ]
    label = "請選擇您所偏好之投資組合最佳化模型"
    model = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label=label)
    amount = forms.FloatField(min_value=0.0, label="請輸入您想投資的金額")
