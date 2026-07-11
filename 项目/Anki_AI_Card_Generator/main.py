import genanki
import openai


# 配置OpenAI API密钥
openai.api_key = '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'


# 创建英语单词牌组模型
english_word_model = genanki.Model(
    model_id=1234567891,
    name='英语单词学习模型',
    fields=[
        {'name': 'Front'},
        {'name': 'Back'},
        {'name': 'Tags'},
        {'name': 'Related'},
        {'name': 'Example'},
        {'name': 'Notes'},
        {'name': 'Type'},
        {'name': 'Source'}
    ],
    templates=[
        {
            'name': '单词卡片',
            'qfmt': '{{Front}}',
            'afmt': '{{FrontSide}}<hr id="answer">'
                    '{{Back}}<br>'
                    'Tags: {{Tags}}<br>'
                    'Related: {{Related}}<br>'
                    'Example: {{Example}}<br>'
                    'Notes: {{Notes}}<br>'
                    'Type: {{Type}}<br>'
                    'Source: {{Source}}'
        }
    ]
)


# 创建英语单词牌组
english_word_deck = genanki.Deck(
    deck_id=2345678910,
    name='英语单词综合牌组'
)


# 借助AI生成浙江英语专升本单词
def generate_zju_words(num):
    prompt = f"请生成{num}个浙江英语专升本相关的英语单词及信息，以列表形式输出，每个元素格式为：" \
             f"['单词', '释义', '标签', '相关知识', '例句', '备注', '类型', '来源']"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    words = eval(response['choices'][0]['message']['content'])
    return words


# 借助AI生成四级单词
def generate_cet4_words(num):
    prompt = f"请生成{num}个四级英语相关的英语单词及信息，以列表形式输出，每个元素格式为：" \
             f"['单词', '释义', '标签', '相关知识', '例句', '备注', '类型', '来源']"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    words = eval(response['choices'][0]['message']['content'])
    return words


# 借助AI生成六级单词
def generate_cet6_words(num):
    prompt = f"请生成{num}个六级英语相关的英语单词及信息，以列表形式输出，每个元素格式为：" \
             f"['单词', '释义', '标签', '相关知识', '例句', '备注', '类型', '来源']"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    words = eval(response['choices'][0]['message']['content'])
    return words


# 借助AI生成AI相关单词
def generate_ai_words(num):
    prompt = f"请生成{num}个AI相关的英语单词及信息，以列表形式输出，每个元素格式为：" \
             f"['单词', '释义', '标签', '相关知识', '例句', '备注', '类型', '来源']"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    words = eval(response['choices'][0]['message']['content'])
    return words


# 决定每个板块的单词数量
zju_num = 5
cet4_num = 5
cet6_num = 5
ai_num = 5

# 生成并添加单词到牌组
zju_words = generate_zju_words(zju_num)
for word_info in zju_words:
    note = genanki.Note(
        model=english_word_model,
        fields=word_info
    )
    english_word_deck.add_note(note)

cet4_words = generate_cet4_words(cet4_num)
for word_info in cet4_words:
    note = genanki.Note(
        model=english_word_model,
        fields=word_info
    )
    english_word_deck.add_note(note)

cet6_words = generate_cet6_words(cet6_num)
for word_info in cet6_words:
    note = genanki.Note(
        model=english_word_model,
        fields=word_info
    )
    english_word_deck.add_note(note)

ai_words = generate_ai_words(ai_num)
for word_info in ai_words:
    note = genanki.Note(
        model=english_word_model,
        fields=word_info
    )
    english_word_deck.add_note(note)


# 生成APKG文件
genanki.Package(english_word_deck).write_to_file('english_words.apkg')
