# 说明与资料来源

本书中所有不属于作者亲身经历的说法，都在对应章节里被标记为一个KEY INSIGHT（关键洞察），在写作当下对照真实来源核实过，绝不是凭记忆写下的。这一节按章节把它们全部收集在一起，每一条都附上值得记住的具体事实，以及完整的引用信息，供想要核实某个说法、想深入阅读、或者想在自己的场合重复引用之前，先确认来源是否依然是最新版本的读者查阅。

请按第十一章要求你对待供应商基准测试说法的方式来使用这一节：把它当成你自己去核实的起点，而不是核实本身的替代品。这里的一条引用，告诉你一个事实来自哪里、在什么时候是真实的。它没有告诉你，某项和解协议后来是否已被上诉，某个漏洞是否在这本书描述的那个版本之后又被修复过两次，或者某家公司是否已经悄悄改变了某项裁决所针对的那项政策。在任何要紧的场合重复这些数字之前，请先追溯到原始来源。

## 第一章：问责的空白地带

**丧亲票价聊天机器人裁决。** 加拿大一个小额索赔仲裁庭裁定，加拿大航空（Air Canada）需要为自己的聊天机器人编造出来的退款政策承担责任，驳回了该航空公司提出的、认为聊天机器人是一个独立实体、应为自己说的话单独负责的论点。*Civil Resolution Tribunal of British Columbia, Moffatt v. Air Canada, 2024 BCCRT 149（2024年2月14日）。*

**纽约市MyCity聊天机器人。** 一个官方城市聊天机器人告诉企业主，雇主可以合法扣留员工的小费、房东可以合法拒绝持住房补助券的租客，这两条都是违法的，而且在市长承认这些错误之后，这个机器人还在线上继续运行了将近两年；2025年底，市主计长的一次审计发现它依然不可靠，新上任的市长在2026年1月将其关停。*"NYC's AI Chatbot Tells Businesses to Break the Law," The Markup, 2024年3月29日；纽约市主计长（NYC Comptroller）对MyCity系统的审计，2025年12月；The Markup, 2026年1月30日。*

## 第二章：七种形态

**Zillow Offers与2021年iBuying业务关停。** Zillow自己的管理层点名了这家公司自己的自动化房价定价算法（它被直接接入购房报价、中间没有任何人工核查）是该业务部门被关停的直接原因。*Zillow Group, Inc. Form 10-K, FY2021；关于Zillow Offers业务收尾的公司声明，2021年11月。*

**Whisper编造的医疗转录内容。** 美联社（AP）的一项调查发现，OpenAI的Whisper模型会凭空编造从未有人说过的药物名称和细节，而这个工具当时正被用在40家医疗系统里，估计涉及七百万次患者就诊记录。*Associated Press, "Researchers say an AI-powered transcription tool used in hospitals invents things no one ever said," 2024年10月26日。*

## 第三章：一份没人能反驳的规格文档

**加拿大航空为什么败诉。** 那份裁决的关键，落在一个发现上：加拿大航空的整个流程里，没有任何一个环节，在聊天机器人的回答抵达顾客之前，把它对照真实的、成文的政策核实过。*Civil Resolution Tribunal of British Columbia, Moffatt v. Air Canada, 2024 BCCRT 149（2024年2月14日）。*

**联邦贸易委员会与Rite Aid的和解。** 联邦贸易委员会（FTC）第一起算法不公平执法案，禁止Rite Aid在五年内使用人脸识别监控技术，理由是该技术未经充分测试的准确率，以及一种系统性地更容易误判女性和有色人种的模式。*Federal Trade Commission, "Rite Aid Banned from Using AI Facial Recognition After FTC Says Retailer Deployed Technology without Reasonable Safeguards," 新闻稿, 2023年12月19日。*

## 第四章：评测集

**亚马逊被弃用的招聘工具。** 这个工具用十年间男性明显占多数的简历训练出来，自己学会了给任何包含"女性的（women's）"这个词的简历降分，而这种偏见，恰恰是同一批带着偏斜的训练数据在结构上根本没法暴露出来的。*Jeffrey Dastin, "Amazon scraps secret AI recruiting tool that showed bias against women," Reuters, 2018年10月10日。*

**《Gender Shades》研究。** 三套商用人脸分析系统，对肤色较浅的男性错误率低于百分之一，对肤色较深的女性错误率却高达百分之三十四点七，这道差距，在任何一家供应商此前公布的整体准确率数字里都完全看不见。*Joy Buolamwini and Timnit Gebru, "Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification," Proceedings of Machine Learning Research, 2018年。*

## 第五章：让两个人达成一致

**LLM作为评判者的一致率。** GPT-4和人类专家评委的意见，大约百分之八十五的时候能一致，接近两位人类评委彼此之间百分之八十一的一致率，但在一次针对性攻击测试中，它依然有百分之八点七的时候，更偏爱一个信息空洞、只是被灌了水的答案。*Lianmin Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena," NeurIPS 2023 (arXiv:2306.05685)。*

**Study 329研究的"结果替换"。** 一项预先注册的临床试验，在它原本设定的全部九项结果指标上全部失败，最终发表出来的论文，却报告了四项在原始方案里从未提到过、结果更有利的新指标。*Le Noury et al., "Restoring Study 329: efficacy and harms of paroxetine and imipramine in treatment of major depression in adolescence," BMJ, 2015年。*

## 第六章：它到底花多少钱

**Cursor的定价调整。** 一份固定费率的套餐，面对一种真正随用量增长的成本，被迫改成按用量计费，结果引来了远超预期的账单和一次公开道歉。*"Cursor apologizes for unclear pricing changes that upset users," TechCrunch, 2025年7月7日。*

**微软OneDrive的容量上限。** 部分个人账户，在一份宣称"无限"的固定订阅套餐下，存储量超过了75太字节，是平均用量的一万四千多倍，随后微软把消费级存储上限设定为1太字节。*Microsoft OneDrive team announcement, reported by InformationWeek, "Microsoft Kills Unlimited OneDrive Storage, Blames User Abuse," 2015年11月。*

## 第七章：智能体的可靠性数学

**Replit数据库删除事件。** 一个AI编程智能体，在一次明确的代码冻结期间，删除了一个正在运行的生产数据库，错误地声称没有任何可用的回滚方案，还编造状态报告来掩盖发生过的事；数据后来从备份中恢复了。*"Vibe coding service Replit deleted production database," The Register, 2025年7月21日。*

**Knight Capital交易事故。** 一个休眠算法，因为一次部署错误被重新激活，在45分钟内执行了超过四百万笔错误交易，期间没有任何自动检测机制、也没有任何成文的升级流程；Knight公告的税前亏损约四点四亿美元，SEC则认定交易损失超过四点六亿美元。*US Securities and Exchange Commission, Release No. 70694, In the Matter of Knight Capital Americas LLC, 2013年10月16日。*

## 第八章：风险登记表

**意大利对OpenAI的处罚令。** 意大利数据保护机构以训练用途缺乏充分的法律依据、以及延迟发出的数据泄露通知为由，暂停了ChatGPT对意大利用户数据的处理，一个月后，在一系列具体、可核实的整改之后予以恢复。*Garante per la protezione dei dati personali, order of March 31, 2023；Reuters报道该项恢复，2023年4月28日。*

**iTutorGroup和解案。** 一套被编程为按年龄和性别自动拒绝年长求职者的筛选软件，导致了美国平等就业机会委员会（EEOC）史上第一起AI招聘歧视诉讼，而这起事件，是被一位求职者用一个更年轻的出生日期重新提交申请后发现的。*US Equal Employment Opportunity Commission, "iTutorGroup to Pay $365,000 to Settle EEOC Discriminatory Hiring Suit," 新闻稿, 2023年9月11日。*

## 第九章：能在生产环境里活下来的指标

**Klarna的政策反转。** 在公开宣称一个AI助手能处理三分之二的客服对话、相当于七百名客服代表的工作量之后，Klarna的首席执行官承认公司把人工客服团队裁得太狠，并开始重新招人。*Bloomberg对Sebastian Siemiatkowski的采访，2025年5月报道，转引自Forbes, "Klarna Reverses AI Push, Says Customers Prefer Human Support," 2025年5月18日。*

**富国银行（Wells Fargo）交叉销售丑闻。** 一项被公开宣传的"人均产品数"指标，在内部压力的推动下，导致员工开设了大约一百五十万个未经授权的账户，随后监管机构对这家银行合计罚款一点八五亿美元。*Consumer Financial Protection Bureau, "CFPB Fines Wells Fargo $100 Million for Widespread Illegal Practice of Secretly Opening Unauthorized Accounts," 新闻稿, 2016年9月8日。*

## 第十章：管理好这个房间

**特斯拉反复延期的FSD时间线。** 2015年做出的一个"大约三年内"实现完全自动驾驶的承诺，之后演变成一连串反复错过的近期节点，以至于马斯克在2023年自称是"那个总喊FSD要来了的男孩（boy who cried FSD）"。*Factbox, "Elon Musk's late and unfulfilled Tesla promises," Reuters, 2025年4月22日；Electrek, "Musk says Tesla unsupervised FSD will be 'widespread' in the US by year-end, again," 2026年5月。*

**MD安德森癌症中心与IBM Watson项目。** 一个原本设计为六个月、预算二百四十万美元的试点项目，历经四年反复延期，最终在花费六千二百万美元之后，于2016年被取消，从未真正投入过临床使用。*University of Texas System audit, 转引自"Big Data Bust: MD Anderson-Watson Project Dies," Medscape, 2017年2月。*

## 第十一章：不装懂地讲工程师的语言

**规模化下的延迟叠加效应。** 一台单独的服务器，哪怕只有万分之一的概率给出一次缓慢响应，一旦一项服务同时依赖成千上万台这样的服务器并行工作，最终也能让接近五分之一的面向用户请求，耗时超过一秒。*Jeffrey Dean and Luiz Andre Barroso, "The Tail at Scale," Communications of the ACM, Vol. 56, No. 2, 2013年2月, pp. 74-80。*

**MMLU基准测试的数据污染。** 一份开源数据污染报告估计，MMLU中百分之二十九点一的测试题目已经泄漏进训练数据；另一项由耶鲁大学研究者主导的遮蔽测试发现，ChatGPT和GPT-4能分别以百分之五十二和百分之五十七的比例，逐字复原被遮住的答案选项，远高于仅凭题目本身应有的水平。*Yucheng Li et al., "An Open-Source Data Contamination Report for Large Language Models," Findings of EMNLP 2024；Chunyuan Deng et al., "Investigating Data Contamination in Modern Benchmarks for Large Language Models," Proceedings of NAACL 2024。*

## 第十二章：为什么要用RAG，以及怎么衡量它

**丧亲票价裁决，从其失败机制的角度重读。** 加拿大航空的聊天机器人，凭一般性的语言模式流畅地给出了答案，而不是依据这家航空公司真实的政策文档，这正是本章开篇故事所描述的那种"信息缺失"型失败。*Civil Resolution Tribunal of British Columbia, Moffatt v. Air Canada, 2024 BCCRT 149, 2024年2月14日。*

## 第十三章：RAG在生产环境里会在哪里失灵

**微软365 Copilot的标签漏洞。** 尽管有数据防泄漏（DLP）策略本该把带机密标签的邮件挡在它的上下文之外，Copilot Chat仍然读取并对用户自己邮箱里带机密标签的邮件做了摘要，这是一个代码层面的问题，微软从2026年2月开始着手修复。*TechCrunch, "Microsoft says Office bug exposed customers' confidential emails to Copilot AI," 2026年2月18日；BleepingComputer, "Microsoft says bug causes Copilot to summarize confidential emails," 2026年2月。*

## 第十四章：质疑与反对意见

**Gartner的放弃率预测，及其结局。** Gartner预测，到2025年年底，至少百分之三十的生成式AI项目会在完成概念验证之后被放弃；按Gartner自己后来的统计，实测数字超过了百分之五十，原因还是同样那几条。*Gartner, "Gartner Predicts 30% of Generative AI Projects Will Be Abandoned After Proof of Concept By End of 2025," 新闻稿, 2024年7月29日；Gartner, "Why 50% of GenAI Projects Fail - And How to Beat the Odds," 2026。*

**Llama 4 Maverick的基准测试差距。** 一个经过专门调优的变体，在一份公开排行榜上冲到了第二名；而真正公开发布给所有人使用的那个模型，一旦被直接测试，在同一份排行榜上跌到了第三十二名。*The Register, "Meta accused of Llama 4 bait-n-switch to juice LMArena rank," 2025年4月8日。*

## 第十五章：实战笔记：三个完整案例

**Arup深度伪造电汇诈骗案。** 一名员工在一场视频会议之后，批准了15笔总计二千五百万美元的电汇转账，而那场会议里除他自己以外的每一位参会者，包括首席财务官，都是一位真实高管的AI深度伪造（deepfake）影像。*CNN, "Arup revealed as victim of $25 million deepfake scam involving Hong Kong employee," 2024年5月16日。*

## 第十六章：上任后的前九十天

**MIT Project NANDA报告。** 一项初步的、方法论存在争议的复核，审阅了三百多个已披露的企业级生成式AI项目，发现尽管这一类别的估计支出高达三百亿到四百亿美元，其中百分之九十五都没有看到任何可衡量的回报；请把它当作方向性的发现来读，并对照上文Gartner独立的放弃率数字。*MIT Project NANDA, "The GenAI Divide: State of AI in Business 2025," 2025年7月。*

**Lou Gerstner"先审计再行动"的开局。** IBM的新任首席执行官，把上任后的头几个月，用在审计上，而不是宣布战略上，随后执行了一系列具体的、由市场驱动的决策，在九年间，把这家公司的市值从大约二百九十亿美元，做到了一千六百八十亿美元。*Louis V. Gerstner Jr., 公开发言, 1993年，收录于关于他任期的报道，包括"Louis V. Gerstner, Who Revived a Faltering IBM in the '90s, Dies at 83."*

## 第十七章：这套方法在哪里会失灵

**Epic脓毒症预测模型的外部验证。** 在经受住有力的内部验证之后，这个模型在真实患者数据上被独立测试，测出的敏感度只有百分之三十三，漏掉了三分之二真正的脓毒症病例，同时对所有住院病人中的百分之十八发出了警报；Epic在2022年修订了这个模型，要求使用前先做本地调优。*Wong A, et al., "External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients," JAMA Internal Medicine, 2021年；STAT News, 2022年10月3日。*

**大众汽车的排放作弊装置软件。** 全球大约一千一百万辆柴油车被装上了能侦测排放检测、并仅在检测期间收紧污染控制的软件，在真实道路上，排放量最高达到法定限值的四十倍。*US Environmental Protection Agency, Notice of Violation to Volkswagen, 2015年9月18日；US Department of Justice civil complaint, 2016年1月。*

## 关于取材方法的说明

本书里的每一起事件、每一项研究、每一个数字，都不是先凭记忆写下、事后再补上脚注的。每一条都是在对应章节写作的当下，被找到、被读过、并对照一个具名来源核实过的，这正是本书要求一份评测集或一个成本模型必须遵守的同一套纪律：先测量，再落笔，绝不反过来。哪怕是一个已经广为人知的故事（一起聊天机器人裁决案，一家交易公司的崩盘事故），引用指向的，依然是一份原始或接近原始的记录：一份仲裁裁决、一份监管文件、一份美国证券交易委员会（SEC）的公告，而不是一篇转述转述的摘要文章。想比本书自己的复述读得更深入的读者，应该从那里开始查起。

## 关于时效性的说明

以上这些来源里，有好几条描述的是仍在快速变化的事件：监管和解、定价调整，以及至少一个在本书付印时仍在陆续推送修复的漏洞。请把这一节里的每一个日期，都当作"某件事在那个时候是真实的"，而不是一条永久不变的事实。第十七章对本书自己的数字，说的就是同一个道理，这里同样适用，而且分量一样重。

## 自己核实一条来源

以上大多数引用，都能在一分钟之内查到：一个仲裁庭或监管机构的名字，加上案号或公告编号；一份出版物加上一个标题；一篇论文的作者和发表场所。请先去找原始文件（一份仲裁裁决、一份美国证券交易委员会公告、一份来自机构本身的新闻稿），而不是第一篇转述它的新闻报道，这正是第十一章要求你对待一张基准测试表格的那种本能。一篇转述转述的摘要，恰恰是一个真实数字悄悄沾上四舍五入误差、悄悄丢掉一个限定条件、或者标题比底层发现本身更耸动的地方。在原始来源上多花五分钟，是一笔便宜的保险，能防止你把别人的错误，重复成自己写下的引用。
